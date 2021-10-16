#!/usr/bin/env python


import json
import base64
import requests
import pandas as pd
from .cnft.urls import repo_url

def verified_policies(pandas: bool=False) -> list:
    """
    Get the list of the policies verifed by cnft.io.
    
    :param pandas: True for return a dataframe
    :return the list of the verified cnft projects
    """

    url = repo_url
    req = requests.get(url)
    
    if req.status_code == requests.codes.ok:
        req = req.json() 
    else:
        raise requests.ConnectionError('[ERROR {}] Request failed. {}'.format(req.status_code, req.text))
        
    return pd.DataFrame.from_dict(req).sort_values(by='name') if pandas else req 


def project_exist(project_name: str) -> bool:
    """
    Check if the project have been verified by cnft.io.

    :param project_name: Name of the project
    """
    project_names = verified_policies(pandas=True)['name'].tolist()

    return True if project_name in project_names else False


def check_policy_id(policy_id: str, project_name: str) -> bool:
    """
    Check if a policy id is verified.
    
    :param polict_id: True for return a dataframe
    :param polict_name: Name of the project
    :return True if verified
    """

    # Check if the project name have been verified by cnft.io
    if not project_exist(project_name):
        raise ValueError('This project ({}) has not been verified by cnft.io or the project name is incorect.'.format(project_name))
    
    url = repo_url + project_name 
    
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()  # the response is a JSON
        content = json.loads(base64.b64decode(req['content']))
    else:
        raise requests.ConnectionError('[ERROR {}] Request failed. {}'.format(req.status_code, req.text))
        
        
    return True if policy_id in content['policies'] else False


def get_policy_id(project_name: str) -> str:
    """
    Obtain the verified policy id of a project.
    
    :param polict_name: Name of the project
    :return the policy id of the project
    """
    
    # Check if the project name have been verified by cnft.io
    if not project_exist(project_name):
        raise ValueError('This project ({}) has not been verified by cnft.io or the project name is incorect.'.format(project_name))
    
    url = repo_url + project_name
    req = requests.get(url)

    if req.status_code == requests.codes.ok:
        req = req.json()
        content = json.loads(base64.b64decode(req['content']))
    else:
        raise requests.ConnectionError('[ERROR {}] Request failed. {}'.format(req.status_code, req.text))
            
    return content['policies']


def get_project_info(project_name: str) -> dict:
    """
    Obtain informations about the cnft project.

    :param project_name: Name of the project
    """
    
    # Check if the project name have been verified by cnft.io
    if not project_exist(project_name):
        raise ValueError('This project ({}) has not been verified by cnft.io or the project name is incorect.'.format(project_name))

    url = repo_url + project_name
    req = requests.get(url)

    if req.status_code == requests.codes.ok:
        req = req.json()
        decode_content = json.loads(base64.b64decode(req['content']))
        req['content'] = decode_content
    else:
        raise requests.ConnectionError('[ERROR {}] Request failed. {}'.format(req.status_code, req.text))

    return req


