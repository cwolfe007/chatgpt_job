# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
import tiktoken
import logging
import google_drive as drive




def get_tokenized_count(prompt, gpt_model):
    encoding = tiktoken.encoding_for_model(gpt_model)
    num_tokens = len(encoding.encode(prompt))
    return num_tokens


def get_chatbot_response(prompt, job_desc, params_dict, gpt_model="gpt-4"):
    client = OpenAI()
    if gpt_model == "gpt-4":
        total_tokens = 8192
    elif gpt_model == "gpt-3.5-turbo":
        total_tokens = 4097
    response = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": job_desc,
            },
        ],
        temperature=params_dict["temperature"],
        max_tokens=total_tokens - (params_dict["tokens"] + 11),
        top_p=params_dict["top_p"],
        frequency_penalty=params_dict["frequency_penalty"],
        presence_penalty=params_dict["presence_penalty"],
    )
    return response


if __name__ == "__main__":
    import os
    import google_drive as drive
    
    params_dict = {
        "temperature": 0.9,
        "tokens": 4096,
        "top_p": 0.5,
        "frequency_penalty": 1.0,
        "presence_penalty": 0.6,
    }
    model = "gpt-3.5-turbo"
    # model = "gpt-4"
    with open("test_job_desc.txt", "r") as f:
        job_desc = f.read()
    with open("chatgpt_prompt.txt", "r") as f:
        file_id = os.environ["GOOGLE_DRIVE_FILE_ID"]
        base_resume = drive.get_base_resume(file_id).decode("utf-8")
        prompt_desc = f.read()
        base_resume_list = base_resume.strip().split("\n")
        prompt_desc_list = prompt_desc.strip().split("\n")
        prompt = "\n".join(prompt_desc_list + base_resume_list)
        # prompt = "You are a story teller, create a story from the given topic."

        logging.debug(prompt)

        with open(f"prompt-{str(hash(prompt))}.txt", "w") as f:
            f.write(prompt)

        prompt_num_tokens = get_tokenized_count(prompt, model)
        logging.debug(f"tokens from prompt: {prompt_num_tokens}")
        job_num_tokens = get_tokenized_count(job_desc, model)
        logging.debug(f"tokens from job_desc: {job_num_tokens}")
        params_dict["tokens"] = prompt_num_tokens + job_num_tokens  + 11
        logging.debug(f"total tokens: {params_dict['tokens']}")
        completion = get_chatbot_response(
            prompt,
            job_desc,
            gpt_model=model,
            num_tokens=prompt_num_tokens + job_num_tokens,
        )
        message = completion.choices[0].message.content
        logging.debug(completion)
        logging.info(message)
        file_name = f"chatgpt-{str(hash(prompt))}-message"
        file_path = f"{file_name}.txt"
        with open(file_path, "w") as f:
            f.write(message)
        file_id = drive.upload_to_drive(file_path, file_name)
        logging.info(f"uploaded {file_id}")
        print(message)
        print(f"uploaded {file_id}")
