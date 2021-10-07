
#!/usr/bin/env python

import requests
import pandas as pd
from .blockfrost_api_urls import header_param_name
from typing import Union, Optional, List, Dict, Tuple
from .utility import nb_results_to_return, set_query_string_parameter

def query_blockfrost(url: str, api_key: str, proxies: dict=None) -> dict:
    """
    Query Blockfrost API.
    
    :param url: The url
    :param api_key: Blockfrost api Key
    :return: Dictionary
    """
    try:
        if not proxies:
            response = requests.get(url, headers={header_param_name:api_key})
        else:
            response = requests.get(url, proxies=proxies, headers={header_param_name:api_key})  
    except Exception as e:
        raise Exception('[ERROR] {}'.format(e))
    
    if response.status_code == 200:
        return response.json()
    else:
        json = response.json()
        raise Exception("[ERROR {}] {} ({}). {}".format(json['status_code'],
                                                   json['error'],
                                                   url,
                                                   json['message']))

def query_on_several_pages(network: str, api_key: str, data_order: str, nb_of_results: int, query_url: str, proxies: dict) -> Tuple[dict, int]:
    """
    Get the data from several pages and the number of api calls.
    The blockfrost api return max 100 results at the time, this fonction allow to concatenate the data from each pages.
    
    :param network: The network (mainnet|testnet|local)
    :param api_key: Blockfrost api key
    :param data_order: The data order
    :param nb_of_results: The number of results wanted 
    :param query_url: Query url
    :return: Dictionary with the data and number of api calls
    """
            
    # List of dataframes, where each dataframe represent the data from each page
    dataframes = []
    
    # Set the param for determinated the number of data to return
    nb_last_page, get_all_data = nb_results_to_return(nb_of_results)
   
    nb_page = 0
    count_api_calls = 0

    # Retrieve the data of each page according to the desired number of data wanted or until the page is empty
    while (nb_page < nb_last_page) or (get_all_data==True):

        nb_page+=1
        count_api_calls =+1

        api_query_string_param = set_query_string_parameter(nb_page, data_order)

        url = network + query_url + api_query_string_param

        data = query_blockfrost(url, api_key, proxies)

        # Return the data as soon as a page is empty.
        if not data:
            # If no data have been found, return an empty dictionary
            if not dataframes:
                #print("[INFO] No data available." )
                return {}, count_api_calls
            
            _dict = pd.concat(dataframes).reset_index(drop=True).to_dict()
            
            return _dict, count_api_calls

        # Create a dataframe with the data from each page and add them to the list of data
        dataframes.append(pd.DataFrame.from_dict(data))
    
    _dict = pd.concat(dataframes).reset_index(drop=True).to_dict()

    return _dict, count_api_calls


    
