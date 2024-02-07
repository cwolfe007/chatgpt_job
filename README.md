# ChatGPT Resume Generator

Welcome to the chatgpt_job Resume Generator repository! This project leverages the power of OpenAI's ChatGPT to help users enhance their resumes for specific job applications quickly and effectively. By using ChatGPT, our tool customizes your resume based on your experiences and the job description you provide, aiming to increase the quality of your applications and speed up the application process.

## Overview

This tool reads files from Google Drive, including a base resume, a job description, and a prompt. It then instructs ChatGPT to generate tailored resumes. Here’s how it works:

1. **Prompt**: Guides ChatGPT on the resume generation process.
2. **Base Resume/List of Experiences**: Your existing resume or a list of experiences from which ChatGPT will craft a new resume.
3. **Job Description**: The specific job description you're targeting with your application.

ChatGPT uses this information to produce a single customized resume.

## Setup Instructions

to get started with chatgpt_job, you will need to install dependencies, setup a Google Cloud Project, and create an account with OpenAI.  

### Prerequisites

- **Python 3.10 or higher**: Ensure Python 3.10+ is installed on your machine.
- **Poetry**: This project uses the Poetry CLI to manage dependencies.

### Installing Poetry and Project Dependencies

1. **Install Poetry**:

   Poetry is a tool for dependency management and packaging in Python.

   - **Option 1**: Install Poetry using `curl`:

     ```bash
     curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
     ```

   - **Option 2**: Install Poetry using Homebrew:

     ```bash
     brew install poetry
     ```

   For other installation methods, refer to the [Poetry documentation](https://python-poetry.org/docs/).

2. **Install Dependencies**:

   Navigate to the project directory and run:

   ```bash
    brew install pyenv pyenv-virtualenv              
    pyenv install 3.10.13     
    pyenv virtualenv 3.10.13 chatgpt_job
    pyenv activate chatgpt_job
    poetry install 
   ```

   These commands installs all necessary dependencies for the project.

### Google Cloud Platform (GCP) Setup

1. **Create a GCP Project**:

   Visit the [Google Cloud Console](https://console.cloud.google.com/) to create a new project for this application.

2. **Enable APIs**:

   Enable the following scopes by searching for and enabling each API in the "APIs & Services" dashboard:

   - `https://www.googleapis.com/auth/drive.metadata.readonly`
   - `https://www.googleapis.com/auth/drive.readonly`
   - `https://www.googleapis.com/auth/drive.file`
   - `https://www.googleapis.com/auth/documents`

3. **Authentication**:

   Create credentials for your application to access Google Drive and Google Docs. Download the `credentials.json` file and place it in your project directory.

### OpenAI Account Setup

1. **Create an OpenAI Account**:

   Sign up at [OpenAI](https://openai.com/) and create an API key for using ChatGPT.

2. **Configure API Key**:

   Add your OpenAI API key to the `env.yaml` file as `OPENAI_API_KEY: "your_api_key_here"`.

### Environment Variables

All necessary environment variables are listed in the `env.example.yaml` file. Copy this file to `env.yaml` and fill in the values as per your setup. The script imports these as environment variables.

### Running the Script

To run the script, ensure your `env.yaml` is configured correctly, then execute:

```bash
poetry run python main.py
```

## Contributing

Feel free to contribute to the project by submitting pull requests or opening issues for any bugs or feature requests.


