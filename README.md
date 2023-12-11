# chatgpt_job
Repo for looking up jobs via OpenAIs chat gpt

# How this works at a high level

This code is meant to read files from google drive to prompt chatgpt to produce resumes tailored to a give job description. So to get this to work you will need 
  1. A prompt
  2. A base resume/list experiences that chatgpt will use to generate a resume from
  3. A job description to feed chatgpt. 

The program will take the above and give it to chatgpt to get it functioning. In order to have the code function you will need the prerequisites below.

  1. A google app that you will use to access google drive TODO: add instructions link
    - With the app you will download the `credentials.json` and put it in this directory
    - DO NOT SHARE THE  `credentials.json` file
  2. An open ai api key
  3. The following environment variables set, the folder/file ids can be found in the google drive url 

    ```
    export OPENAI_API_KEY="<>"
    export GOOGLE_DRIVE_BASE_RESUME_FILE_ID=<google_drive_id>
    export GOOGLE_DRIVE_JOB_DESC_FILE_ID=<google_drive_id>
    export GOOGLE_DRIVE_FOLDER_ID=<google_drive_id>
    export GOOGLE_DRIVE_PROMPT_FILE_ID=<google_drive_id>
    ```
