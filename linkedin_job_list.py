import requests
import os

api_key = os.environ['PROXY_CURL']
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin/company/job'
params = {
            'job_type': 'anything',
            'experience_level': 'anything',
            'when': 'past-month',
            'flexibility': 'remote',
            'geo_id': '92000000',
             'keyword': 'DevOps'
                                }
resp = requests.get(api_endpoint,
                                                params=params,
                                                headers=headers)
print(resp.)



