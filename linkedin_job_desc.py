import requests
import os


def get_job_desc():
    api_key = os.environ['PROXY_CURL']
    headers = {'Authorization': 'Bearer ' + api_key}

    api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/job'
    params = {
                'url': 'https://www.linkedin.com/jobs/view/3667167926/',
                }
    resp = requests.get(api_endpoint,
                            params=params,
                            headers=headers
                        )
    return resp.json()



