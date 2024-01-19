import google_drive as drive
import chatgpt as chatbot
import os
import logging
import time

logging.basicConfig(
    filename="chatgpt-main.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
)
# model = "gpt-3.5-turbo"


def main():
    params_dict_list = [
        {
            "param_profile": "standard",
            # Randomness in the response
            "temperature": 1.5,
            # Number of tokens to generate
            "tokens": 4096,
            # Sample selction of words
            "top_p": 0.5,
            # Penalty for repeating words
            "frequency_penalty": 1.0,
            # Penalty for repeating tokens
            "presence_penalty": 0.6,
        },
        {
            "param_profile": "strict",
            # Randomness in the response
            "temperature": 1.75,
            # Number of tokens to generate
            "tokens": 4096,
            # Sample selction of words
            "top_p": 0.5,
            # Penalty for repeating words
            "frequency_penalty": 1.0,
            # Penalty for repeating tokens
            "presence_penalty": 0.6,
        },
        {
            "param_profile": "flexible",
            # Randomness in the response
            "temperature": 2.0,
            # Number of tokens to generate
            "tokens": 4096,
            # Sample selction of words
            "top_p": 0.5,
            # Penalty for repeating words
            "frequency_penalty": 1.0,
            # Penalty for repeating tokens
            "presence_penalty": 0.6,
        },
        # {
        #
        #     "param_profile": "flexible-maxed",
        #     # Randomness in the response
        #     "temperature": 2.0,
        #     # Number of tokens to generate
        #     "tokens": 4096,
        #     # Sample selction of words
        #     "top_p": 1.0,
        #     # Penalty for repeating words
        #     "frequency_penalty": 1.0,
        #     # Penalty for repeating tokens
        #     "presence_penalty": 1.0,
        # }
    ]

    # Get prompt from google drive
    logging.info("Get Job Description, Resume, and Prompt from Google Drive")
    b_file_id = os.environ["GOOGLE_DRIVE_BASE_RESUME_FILE_ID"]
    base_resume = drive.get_file(b_file_id).decode("utf-8")
    logging.debug(f"base_resume: {base_resume}")
    p_file_id = os.environ["GOOGLE_DRIVE_PROMPT_FILE_ID"]
    prompt = drive.get_file(p_file_id).decode("utf-8")
    logging.debug(f"prompt: {prompt}")
    jd_file_id = os.environ["GOOGLE_DRIVE_JOB_DESC_FILE_ID"]
    job_desc = drive.get_file(jd_file_id).decode("utf-8")
    logging.debug(f"job_desc: {job_desc}")

    logging.info("Build Propmt")
    base_resume_list = base_resume.strip().split("\n")
    prompt_desc_list = prompt.strip().split("\n")
    prompt = "\n".join(prompt_desc_list + base_resume_list)
    logging.debug(prompt)
    logging.info("Build Propmt")
    prompt_file_name = f"prompt-{str(hash(prompt))}"
    prompt_file_path = f"{prompt_file_name}.txt"
    with open(prompt_file_path, "w") as f:
        f.write(prompt)
    file_id = drive.upload_to_drive(prompt_file_name, prompt_file_path)
    logging.info(f"uploaded prompt: {file_id}")
    logging.info("start gerneating response")
    # Print prompt to file for local review
    with open(f"prompt-{str(hash(prompt))}.txt", "w") as f:
        f.write(prompt)

    for model in ["gpt-4"]:
        # for model in ["gpt-3.5-turbo", "gpt-4"]:
        prompt_num_tokens = chatbot.get_tokenized_count(prompt, model)
        logging.debug(f"tokens from prompt: {prompt_num_tokens}")
        job_num_tokens = chatbot.get_tokenized_count(job_desc, model)
        logging.debug(f"tokens from job_desc: {job_num_tokens}")
        total_tokens = prompt_num_tokens + job_num_tokens
        logging.debug(f"total tokens: {total_tokens}")
        for params_dict in params_dict_list:
            logging.info(f"params_dict: {params_dict}")
            logging.info(f"total_tokens: {total_tokens}")
            params_dict["tokens"] = total_tokens
            logging.info(f"params_dict: {params_dict}")
            params_dict["tokens"] = total_tokens
            completion = chatbot.get_chatbot_response(
                prompt,
                job_desc,
                params_dict,
                gpt_model=model,
            )
            # API only allows 10000 tokens per request per minute
            if model == "gpt-4":
                time.sleep(60)
            message = completion.choices[0].message.content
            logging.debug(completion)
            logging.info(message)
            file_name = (
                f"resume-message-{params_dict['param_profile']}-settings-{model}"
            )
            file_path = f"{file_name}.txt"
            with open(file_path, "w") as f:
                f.write(message)
            file_id = drive.upload_to_drive(file_name, file_path)
            logging.info(f"uploaded {file_id}")
            print(message)
            print(f"uploaded {file_id}")


if __name__ == "__main__":
    main()
