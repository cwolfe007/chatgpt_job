# chatgpt_job
Repo for looking up jobs via OpenAIs chat gpt

# How to set up

1. Set up google drive app
1. Set up Open ai acocunt
1. Create env file
   -   ```
    export OPENAI_API_KEY=<api_key_from_openai>
    export GOOGLE_ID="<google_oauth_key_id>"
    export GOOGLE_SECRET="<google_oauth_secret>"
    export GOOGLE_DRIVE_BASE_RESUME_FILE_ID=<google_drive_file_id>
    export GOOGLE_DRIVE_JOB_DESC_FILE_ID=<google_drive_file_id>
    export GOOGLE_DRIVE_PROMPT_FILE_ID=<google_drive_file_id>
    export GOOGLE_DRIVE_FOLDER_ID=<google_drive_folder_id>
   ```

# How to run

1. Find a linked in job, copy and paste descirption into google drive folder
1. Copy the folder id and use it to update the value of `export GOOGLE_DRIVE_JOB_DESC_FILE_ID=<google_drive_file_id>`
1. Similiarly, find the values of the base resume, job description, and prompt file ids
1. Export the google dirve environment vars  
1. Assuming all of the env vars above are set the script will generate 3 resumes with different chat gpt repsonse parameters. 
1. Open your folder in google drive and find your resumes for review

# NOTE

The prompt is meant to concatanated with a base resume, write the prompt accordingly