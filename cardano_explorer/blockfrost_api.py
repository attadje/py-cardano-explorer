import os
import requests
import pandas as pd
from typing import Union, Optional, List, Dict, Tuple

# API Header parameter
header_param_name = 'project_id'

# Blockfrost Network URL
bf_url_cardano_mainnet = 'https://cardano-mainnet.blockfrost.io/api/v0/'
bf_url_cardano_testnet = 'https://cardano-testnet.blockfrost.io/api/v0/'
bf_url_cardano_local = 'https://localhost:3000/'

# Blockfrost Stake URL
bf_url_stake = 'accounts/'
bf_url_stake_rewards = '/rewards'
bf_url_stake_amount_history = '/history'
bf_url_stake_delegation = '/delegations'
bf_url_stake_registration = '/registrations'
bf_url_stake_withdrawal_history = '/withdrawals'
bf_url_stake_mir_history = '/mirs'
bf_url_associated_addresses = '/addresses'
bf_url_assets_associated_addresses = '/addresses/assets'

# Blockfrost Addresse URL
bf_url_address = 'addresses/'
bf_url_address_details = '/total'
bf_url_address_utxo = '/utxos'
bf_url_address_transaction = '/transactions'

# Blockfrost Network Information URL
bf_url_network_informations = '/network'

# Blockfrost Epochs URL
bf_url_epoch = 'epochs/'
bf_url_latest_epoch = 'epochs/latest'
bf_url_latest_epoch_protocol_parameters = 'epochs/latest/parameters'

# Blockfrost Pools URL
bf_url_polls = 'pools/'
bf_url_param_stake_pool_history = '/history'

class Auth:
    def __init__(self, api_key: str=None, network: str="mainnet", proxies: dict=None):
        
        # Set proxies if needed
        self.proxies = proxies
        
        # Set the api key in the environement variable if the api_key variable is not defined
        if not api_key:
            # Check if the Blockfrost API Key is configured in a environmental variable 
            assert (os.getenv('BLOCKFROST_API_KEY') is not None), '[ERROR] Your blockfrost api key is not configured in your environement path.'
            self.api_key = os.getenv('BLOCKFROST_API_KEY')
        
        else:
            self.api_key = api_key
        
        # Set the network url
        if 'mainnet' in network:
            self.network = bf_url_cardano_mainnet
            
        elif 'testnet' in network:
            self.network = bf_url_cardano_testnet
            
        elif 'local' in network:
            self.network = bf_url_cardano_local
            
         
    def stake_informations(self, stake_address: str) -> dict:
        """
        Obtain informations about a stake account.
        
        :param stake_address: The stake addresse
        :return: Dictionary with the informations about a specific stake account
        """
        
        url_stake_info = self.network + bf_url_stake + stake_address
        
        response = query_blockfrost(url_stake_info, self.api_key, self.proxies)
        
        return response
            
            
    def stake_reward_history(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain the reward history.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the rewards history 
        """
        
        url_rewards_history = "{}{}{}".format(bf_url_stake,
                                              stake_address,
                                              bf_url_stake_rewards)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, url_rewards_history, self.proxies)
        
        print('[INFO] Function stake_reward_history, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
    

    def stake_amount_history(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain the stake amount history.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, the number of results wanted
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake amount history
        """
        
        url_stake_amount_history = "{}{}{}".format(bf_url_stake,
                                                   stake_address,
                                                   bf_url_stake_amount_history)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, url_stake_amount_history, self.proxies)
        
        print('[INFO] Function stake_amount_history, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
        
       

    
    def stake_delegation(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain information about the stake delegation.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake delegation history
        """
        
        url_stake_delegation = "{}{}{}".format(bf_url_stake,
                                               stake_address,
                                               bf_url_stake_delegation)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, url_stake_delegation, self.proxies)
        
        print('[INFO] Function stake_delegation, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    
    
    def stake_registration_deregistrations(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain information about the stake registration et deregistrations.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake registration and deregistrations history
        """
        
        url_stake_registration = "{}{}{}".format(bf_url_stake,
                                                 stake_address,
                                                 bf_url_stake_registration)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, url_stake_registration, self.proxies)
        
        print('[INFO] Function stake_registration_deregistrations, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    
    def stake_withdrawal_history(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain information about the stake withdrawal history.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake withdrawal history 
        """
        
        url_stake_withdrawal_history = "{}{}{}".format(bf_url_stake,
                                                       stake_address,
                                                       bf_url_stake_withdrawal_history)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, url_stake_withdrawal_history, self.proxies)
        
        print('[INFO] Function stake_withdrawal_history, {} API calls.'.format(count_api_calls))
        
        if pandas:
            return pd.DataFrame.from_dict(response)
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    
    def stake_mir_history(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain information about the stake mir history.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake mir history
        """
        
        url_stake_mir_history = "{}{}{}".format(bf_url_stake,
                                                stake_address,
                                                bf_url_stake_mir_history)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, url_stake_mir_history, self.proxies) 
        
        print('[INFO] Function stake_mir_history, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else reponse
    
    
    def stake_associated_addresses(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain information about the stake associated addresses.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake associated addresses or empty dictionary if the stake address have no stake ADA
        """
        
        url_stake_associated_addresses = "{}{}{}".format(bf_url_stake,
                                                         stake_address,
                                                         bf_url_associated_addresses)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, url_stake_associated_addresses, self.proxies)
        
        print('[INFO] Function stake_associated_addresses, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    
    def stake_assets_associated_addresses(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain information about the stake assets associated addresses.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake associated addresses or empty dictionary if the stake address have no stake ADA
        """
        
        url_stake_assets_associated_addresses = "{}{}{}".format(bf_url_stake,
                                                                stake_address,
                                                                bf_url_assets_associated_addresses)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, url_stake_assets_associated_addresses, self.proxies)
        
        print('[INFO] Function stake_assets_associated_addresses, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    
    def address_info(self, address: str) -> dict:
        """
        Obtain informations about an address.
        
        :param stake_addresse: Address
        :return: Dictionary or DataFrame with the informations about the address
        
        """
        
        url_address_info = self.network + bf_url_address + address
        
        response = query_blockfrost(url_address_info, self.api_key, self.proxies)
        
        return response
    
    
    
    def address_details(self, address: str) -> dict:
        """
        Obtain details information about an address.
        
        :param stake_addresse: Address
        :return: Dictionary with the informations details about the address
        """
        
        url_address_details = self.network + bf_url_address + address + bf_url_address_details
        
        response = query_blockfrost(url_address_details, self.api_key, self.proxies)
        
        return response
    
    
    def address_utxo(self, address: str) -> dict:
        """
        Obtain UTXO of the address.
        
        :param stake_addresse: Address
        :return: Dictionary with the informations details about the UTXO of an address
        """
        
        url_address_utxo = self.network + bf_url_address + address + bf_url_address_utxo
        
        response = query_blockfrost(url_address_utxo, self.api_key, self.proxies)
        
        return response
    
    
    def address_transaction(self, address: str) -> dict:
        """
        Transactions on the address.
        
        :param stake_addresse: Address
        :return: Dictionary with the informations details about the address transaction
        """
        
        url_address_transaction = self.network + bf_url_address + address + bf_url_address_transaction
        
        response = query_blockfrost(url_address_transaction, self.api_key, self.proxies)
        
        return response
    
    
    def network_info(self) -> dict:
        """Return detailed network information."""
        
        url_network_info = self.network + bf_url_network_informations
        
        response = query_blockfrost(url_network_info, self.api_key, self.proxies)
        
        return response
    
    
    def latest_epoch(self) -> dict:
        """Return the information about the latest, therefore current, epoch."""
        
        url_latest_epoch = self.network + bf_url_latest_epoch
        
        response = query_blockfrost(url_latest_epoch, self.api_key, self.proxies)
        
        return response
    
    
    def specific_epoch(self, epoch: int) -> dict:
        """
        Obtain information about a specific epocht.
        
        :param epoch: The number of the epoch
        :return: Dictionary with information about a specific epoch
        """
        
        # Check if the epoch is greater than 0
        assert(int(epoch) >= 0), "[ERROR] The number of epoch can't be negatif."
        
        url_specific_epoch = self.network + bf_url_epoch + str(epoch)
        
        response = query_blockfrost(url_specific_epoch, self.api_key, self.proxies)
        
        return response
    
    
    def latest_epoch_protocol_parameters(self) -> dict:
        """Return the protocol parameters for the latest epoch."""
        
        url_address_info = self.network + bf_url_latest_epoch_protocol_parameters
        
        response = query_blockfrost(url_address_info, self.api_key, self.proxies)
        
        return response
    
    
    def epochs_history(self, epochs: list, pandas: bool=False) -> Union[pd.DataFrame, dict]:            
        """
        Obtain history about the epochs.
        
        :param epochs: List of the epochs number
        :pandas: Optional, True for return a pandas dataframe
        :return: Dictionary or DataFrame of the epochs informations history
        """
        
        # Check if the parameter epochs is a list
        assert(isinstance(epochs, list)), "[ERROR] The parameter 'epochs' should be a list not ({})".format(type(epochs))
    
        epochs_history = []
        last_epoch = self.latest_epoch()['epoch']
        
        # Value to 1 because of the first call for get the last epoch
        count_api_calls = 1
   
        for epoch in epochs:
            
            # check if the epoch number is not inferior than O or greater than the last epoch.
            assert(epoch > 0), "[ERROR] The number of epoch ({}) can't be inferior than 0.".format(epoch)
            assert(epoch < last_epoch), "ERROR] The number of epoch can't be greater than the last epoch ({})".format(last_epoch)
        
            epochs_history.append(self.specific_epoch(epoch))
            count_api_calls += 1
               
        print('[INFO] Function epochs_history, {} API calls.'.format(count_api_calls))
            
        return pd.DataFrame.from_dict(epochs_history) if pandas else epochs_history
    
    
    def registered_polls(self, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain the list of registered stake pools.
        
        :param reward_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the registered stake pools
        """
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, bf_url_polls, self.proxies)
        
        # Rename the column of the pool ID
        response['registered_polls_id'] = response.pop(0)
                  
        print('[INFO] Function registered_polls, {} API calls.'.format(count_api_calls))
                        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    
    def pool_informations(self, pool_id: str) -> dict: 
        """
        Obtain Pool information.
        
        :param pool_id: The id of the pool
        :return: Dictionary with the informations about a pool
        """
        
        url_pool_informations = self.network + bf_url_polls + pool_id
        response = query_blockfrost(url_pool_informations, self.api_key, self.proxies)
        
        return response
    
    
    def stake_pool_history(self, pool_id: str, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain history of stake pool parameters over epochs
        
        :param pool_id: The id of the pool
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return dict: Dictionary or DataFrame of the history of stake pool parameters over epochs
        """
        
        url_param_stake_pool_history = "{}{}{}".format(bf_url_polls,
                                                       pool_id,
                                                       bf_url_param_stake_pool_history)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, url_param_stake_pool_history, self.proxies)
        
        print('[INFO] Function param_stake_pool_history, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response

    
    def rewards_history_analysis(self, stake_address: str, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Create a dataframe with explanatory variables of the stake rewards for each epochs.

        :param stake_address: Stake address
        :pandas: Optional, True for return a pandas dataframe
        :return: Dictionary or DataFrame about informations on the rewards history
        """

        # Get the rewards history
        df_rewards_hist = self.stake_reward_history(stake_address, pandas=True).rename({'amount': 'rewards_amount'}, axis=1)
        epoch_reward_list = df_rewards_hist['epoch'].tolist()
        pool_id = df_rewards_hist['pool_id'][0]

        # Get the stake amount history
        df_amount_hist = self.stake_amount_history(stake_address, pandas=True).rename({'amount': 'stake_amount'}, axis=1)

        # Get the pool informations
        df_stake_pool_hist = self.stake_pool_history(pool_id, pandas=True)
        # Replace the column names
        df_stake_pool_hist_col_name = {name:'stake_pool_{}'.format(name) for name in df_stake_pool_hist.columns.tolist()}
        df_stake_pool_hist = df_stake_pool_hist.rename(columns=df_stake_pool_hist_col_name)

        # Get the epochs information
        df_epochs_hist = self.epochs_history(epoch_reward_list, pandas=True)
        # Replace the column names
        df_epochs_hist_col_name = {name:'epoch_{}'.format(name) for name in df_epochs_hist.columns.tolist()}
        df_epochs_hist = df_epochs_hist.rename(columns=df_epochs_hist_col_name)

        # Concatenate the data into a unique dataframe
        df = df_rewards_hist[['epoch','rewards_amount']].join(df_amount_hist.set_index('active_epoch'), on='epoch')
        df = df.join(df_epochs_hist.set_index('epoch_epoch'), on='epoch')
        df = df.join(df_stake_pool_hist.set_index('stake_pool_epoch'), on='epoch')

        return df if pandas else df.to_dict()
      
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


def query_blockfrost(url: str, api_key: str, proxies: dict=None) -> dict:
    """
    Query blockfrost api.
    
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
                print("[INFO] No data available." )
                return {}, count_api_calls
            
            _dict = pd.concat(dataframes).reset_index(drop=True).to_dict()
            
            return _dict, count_api_calls

        # Create a dataframe with the data from each page and add them to the list of data
        dataframes.append(pd.DataFrame.from_dict(data))
    
    _dict = pd.concat(dataframes).reset_index(drop=True).to_dict()

    return _dict, count_api_calls