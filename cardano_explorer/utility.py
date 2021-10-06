
#!/usr/bin/env python

from typing import Union, Optional, List, Dict, Tuple

def convert_hex_to_ascii(hex_string: str) -> str:
    """Convert hex string to ascii format"""
    return bytearray.fromhex(hex_string).decode()

def process_onchain_metadata(asset: dict) -> Dict:
    """
    Create a column for each onchain metadata item.
    
    :param assets_data: Asset data dictionary
    :return: Formated asset data dictionary
    """
    
    f_assets_data = {}
    
    for asset_item in asset:
        # If the asset have metadata
        if isinstance(asset[asset_item], dict):
            # Metadata dictionary
            metadata = asset[asset_item]
            # Browse the data, and add each item in the formated asset data dictionary
            for metadata_item in metadata:
                f_assets_data[metadata_item] = metadata[metadata_item]
            continue
        # If not, add the item and his unique value to the formated asset data dictionary 
        f_assets_data[asset_item] = asset[asset_item]
    
    return f_assets_data

def set_query_string_parameter(page: int, data_order: str="") -> str:
    """
    Create the query string to add at the end of the request url.
    
    :param page: Page number to extract the data
    :param data_order: Order of the data 
    :return: Query string parameter
    """
   
    # Data is returned in ascending (oldest first, newest last) order.
    # Use the ?order=desc query parameter to reverse this order
    order_parameter = lambda order: 'order=desc'if 'desc' in order else ''
    
    # By default, the api return 100 results at a time. You have to use ?page=2 to list through the results
    page_parameter = 'page={}'.format(page)
    
    query_string_parameter = '?' + page_parameter + '&' + order_parameter(data_order)
    
    return query_string_parameter

def nb_results_to_return(nb_of_results: int) -> Tuple[int, bool]:
    """
    Set the variables for determinated the number of data to return.
    If nb_of_results is None, nb_last_page is set to 0 for get all the data available.
    
    :param nb_of_results: Number of data to return, None for get all the data available
    :return: The number of the last page to get the data (or 0 for get all the data) and False (True for get all the data) or raise an error
    """

    # Check if the nb_of_results is not equal to 0 or is not a multiple of 100
    if nb_of_results != None:
        assert(nb_of_results!=0), "[ERROR] The function parameter 'nb_of_results' ({}), cant be zero, he should be 100 or a multiple of 100 or None for get all the data available.".format(nb_of_results)
        assert(nb_of_results%100 == 0), "[ERROR] The function parameter 'nb_of_results' ({}), should be 100 or a multiple of 100 or None for get all the data available.".format(nb_of_results)
   
    # Determine the number of the last page to get the data, O for request all the data available.
    nb_last_page = lambda number: 0 if not number else int(number / 100) 

    get_all_data = True
    
    if not nb_of_results:
        return nb_last_page(nb_of_results), get_all_data

    return nb_last_page(nb_of_results), False