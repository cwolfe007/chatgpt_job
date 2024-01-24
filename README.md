# chatgpt_job
Repo for generating resumes with chatgpt. The goal of this repo is to provide all users of this code base with the opprotunity to put their best foot forward and increase the quality of their applications while filling out applications faster.

# How this works at a high level

This code is meant to read files from google drive to prompt chatgpt to produce resumes tailored to a give job description. So to get this to work you will need 
  1. A prompt
  2. A base resume/list experiences that chatgpt will use to generate a resume from
  3. A job description to feed chatgpt. 

The program will take the above and give it to chatgpt. Chatgpt then takes the prompt, your resume, and a given job description and will generate several resumes with different models of chatgpt. 

In order to have the code function you will need the prerequisites below.

  1. A google app that you will use to access google drive TODO: add instructions link
    - With the app you will download the `credentials.json` and put it in this directory
    - DO NOT SHARE THE  `credentials.json` file
  2. An OpenAI api key, will require payment for running models
  3. The following environment variables set, the folder/file ids can be found in the google drive url 

    ```
    export OPENAI_API_KEY="<>"
    export GOOGLE_DRIVE_BASE_RESUME_FILE_ID=<google_drive_id> # the file that contains the base resume
    export GOOGLE_DRIVE_JOB_DESC_FILE_ID=<google_drive_id> # file that stores the job description
    export GOOGLE_DRIVE_FOLDER_ID=<google_drive_id> #The folder where you want to store your generated resumes
    export GOOGLE_DRIVE_PROMPT_FILE_ID=<google_drive_id> # The file that stores the prompt to use for telling chatgpt what it should do
    ```
