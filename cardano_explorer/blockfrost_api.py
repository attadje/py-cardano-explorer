import os
import requests
import pandas as pd
from time import sleep
from tqdm import tqdm
from typing import Union, Optional, List, Dict, Tuple

# API Header parameter
header_param_name = 'project_id'

# Blockfrost Network URL
bf_url_cardano_mainnet = 'https://cardano-mainnet.blockfrost.io/api/v0/'
bf_url_cardano_testnet = 'https://cardano-testnet.blockfrost.io/api/v0/'

# Blockfrost Stake URL
bf_stake_url = 'accounts/'
bf_stake_rewards_url = '/rewards'
bf_stake_amount_history_url = '/history'
bf_stake_delegation_url = '/delegations'
bf_stake_registration_url = '/registrations'
bf_stake_withdrawal_history_url = '/withdrawals'
bf_stake_mir_history_url = '/mirs'
bf_associated_addresses_url = '/addresses'
bf_assets_associated_addresses_url = '/addresses/assets'

# Blockfrost Addresse URL
bf_address_url = 'addresses/'
bf_address_details_url = '/total'
bf_address_utxo_url = '/utxos'
bf_address_transaction_url = '/transactions'

# Blockfrost Network Information URL
bf_network_informations_url = '/network'

# Blockfrost Epochs URL
bf_epoch_url = 'epochs/'
bf_latest_epoch_url = 'epochs/latest'
bf_latest_epoch_protocol_parameters_url = 'epochs/latest/parameters'

# Blockfrost Pools URL
bf_polls_url = 'pools/'
bf_param_stake_pool_history_url = '/history'

# Blockfrost Assets URL
bf_assets_url = 'assets/'
bf_asset_history_url = '/history'
bf_asset_transactions_url = '/transactions'
bf_asset_addresses_url = '/addresses'
bf_assets_policy_url = 'policy/'

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
    
    def stake_informations(self, stake_address: str) -> dict:
        """
        Obtain informations about a stake account.
        
        :param stake_address: The stake addresse
        :return: Dictionary with the informations about a specific stake account
        """
        
        url_stake_info = self.network + bf_stake_url + stake_address
        
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
        
        rewards_history_url = "{}{}{}".format(bf_stake_url,
                                              stake_address,
                                              bf_stake_rewards_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, rewards_history_url, self.proxies)
        
        #print('[INFO] Function stake_reward_history, {} API calls.'.format(count_api_calls))
        
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
        
        stake_amount_history_url = "{}{}{}".format(bf_stake_url,
                                                   stake_address,
                                                   bf_stake_amount_history_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, stake_amount_history_url, self.proxies)
        
        #print('[INFO] Function stake_amount_history, {} API calls.'.format(count_api_calls))
        
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
        
        stake_delegation_url = "{}{}{}".format(bf_stake_url,
                                               stake_address,
                                               bf_stake_delegation_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, stake_delegation_url, self.proxies)
        
        #('[INFO] Function stake_delegation, {} API calls.'.format(count_api_calls))
        
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
        
        stake_registration_url = "{}{}{}".format(bf_stake_url,
                                                 stake_address,
                                                 bf_stake_registration_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, stake_registration_url, self.proxies)
        
        #print('[INFO] Function stake_registration_deregistrations, {} API calls.'.format(count_api_calls))
        
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
        
        stake_withdrawal_history_url = "{}{}{}".format(bf_stake_url,
                                                       stake_address,
                                                       bf_stake_withdrawal_history_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, stake_withdrawal_history_url, self.proxies)
        
        #print('[INFO] Function stake_withdrawal_history, {} API calls.'.format(count_api_calls))
        
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
        
        stake_mir_history_url = "{}{}{}".format(bf_stake_url,
                                                stake_address,
                                                bf_stake_mir_history_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, stake_mir_history_url, self.proxies) 
        
        #print('[INFO] Function stake_mir_history, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    
    def stake_associated_addresses(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain information about the stake associated addresses.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake associated addresses or empty dictionary if the stake address have no stake ADA
        """
        
        stake_associated_addresses_url = "{}{}{}".format(bf_stake_url,
                                                         stake_address,
                                                         bf_associated_addresses_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, stake_associated_addresses_url, self.proxies)
        
        #print('[INFO] Function stake_associated_addresses, {} API calls.'.format(count_api_calls))
        
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
        
        stake_assets_associated_addresses_url = "{}{}{}".format(bf_stake_url,
                                                                stake_address,
                                                                bf_assets_associated_addresses_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, stake_assets_associated_addresses_url, self.proxies)
        
        #print('[INFO] Function stake_assets_associated_addresses, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    
    def address_info(self, address: str) -> dict:
        """
        Obtain informations about an address.
        
        :param stake_addresse: Address
        :return: Dictionary or DataFrame with the informations about the address
        
        """
        
        address_info_url = self.network + bf_address_url + address
        
        response = query_blockfrost(address_info_url, self.api_key, self.proxies)
        
        return response
    
    
    
    def address_details(self, address: str) -> dict:
        """
        Obtain details information about an address.
        
        :param stake_addresse: Address
        :return: Dictionary with the informations details about the address
        """
        
        address_details_url = self.network + bf_address_url + address + bf_address_details_url
        
        response = query_blockfrost(address_details_url, self.api_key, self.proxies)
        
        return response
    
    
    def address_utxo(self, address: str, pandas: bool=False) -> dict:
        """
        Obtain UTXO of the address.
        
        :param stake_addresse: Address
        :return: Dictionary with the informations details about the UTXO of an address
        """
        
        address_utxo_url = self.network + bf_address_url + address + bf_address_utxo_url
        
        response = query_blockfrost(address_utxo_url, self.api_key, self.proxies)
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    
    def address_transaction(self, address: str, pandas: bool=False) -> dict:
        """
        Transactions on the address.
        
        :param stake_addresse: Address
        :return: Dictionary with the informations details about the address transaction
        """
        
        address_transaction_url = self.network + bf_address_url + address + bf_address_transaction_url
        
        response = query_blockfrost(address_transaction_url, self.api_key, self.proxies)
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    
    def network_info(self) -> dict:
        """Return detailed network information."""
        
        network_info_url = self.network + bf_network_informations_url
        
        response = query_blockfrost(network_info_url, self.api_key, self.proxies)
        
        return response
    
    
    def latest_epoch(self) -> dict:
        """Return the information about the latest, therefore current, epoch."""
        
        latest_epoch_url = self.network + bf_latest_epoch_url
        
        response = query_blockfrost(latest_epoch_url, self.api_key, self.proxies)
        
        return response
    
    
    def specific_epoch(self, epoch: int) -> dict:
        """
        Obtain information about a specific epocht.
        
        :param epoch: The number of the epoch
        :return: Dictionary with information about a specific epoch
        """
        
        # Check if the epoch is greater than 0
        assert(int(epoch) >= 0), "[ERROR] The number of epoch can't be negatif."
        
        specific_epoch_url = self.network + bf_epoch_url + str(epoch)
        
        response = query_blockfrost(specific_epoch_url, self.api_key, self.proxies)
        
        return response
    
    
    def latest_epoch_protocol_parameters(self) -> dict:
        """Return the protocol parameters for the latest epoch."""
        
        address_info_url = self.network + bf_latest_epoch_protocol_parameters_url
        
        response = query_blockfrost(address_info_url, self.api_key, self.proxies)
        
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
               
        #print('[INFO] Function epochs_history, {} API calls.'.format(count_api_calls))
            
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
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, bf_polls_url, self.proxies)
        
        # Rename the column of the pool ID
        response['registered_polls_id'] = response.pop(0)
                  
        #print('[INFO] Function registered_polls, {} API calls.'.format(count_api_calls))
                        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    
    def pool_informations(self, pool_id: str) -> dict: 
        """
        Obtain Pool information.
        
        :param pool_id: The id of the pool
        :return: Dictionary with the informations about a pool
        """
        
        pool_informations_url = self.network + bf_polls_url + pool_id
        response = query_blockfrost(pool_informations_url, self.api_key, self.proxies)
        
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
        
        param_stake_pool_history_url = "{}{}{}".format(bf_polls_url,
                                                       pool_id,
                                                       bf_param_stake_pool_history_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, param_stake_pool_history_url, self.proxies)
        
        #print('[INFO] Function param_stake_pool_history, {} API calls.'.format(count_api_calls))
        
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

    def assets(self, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        List of assets.
        
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the assets
        """
        

        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, bf_assets_url, self.proxies)
        
        #print('[INFO] Function assets, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response


    def specific_asset(self, asset: str) -> dict: 
        """
        Obtain information about a specific asset.
        
        :param : :param assets: Assets (Concatenation of the policy_id and hex-encoded asset_name)
        :return: Dictionary with the info about the asset
        """
        
        specific_asset_url = self.network + bf_assets_url + asset

        response = query_blockfrost(specific_asset_url, self.api_key, self.proxies)
        
        return response

        
    def asset_history(self, asset: str, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain the history of a specific asset.
        
        :param assets: Assets (Concatenation of the policy_id and hex-encoded asset_name)
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the assets
        """
        
        assets_history_url = bf_assets_url + asset + bf_asset_history_url

        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, assets_history_url, self.proxies)
        
        #print('[INFO] Function asset_history, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response


    def asset_transactions(self, asset: str, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        List of a specific asset transactions.
        
        :param assets: Assets (Concatenation of the policy_id and hex-encoded asset_name)
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the assets
        """
        
        assets_transactions_url = bf_assets_url + asset + bf_asset_transactions_url

        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, assets_transactions_url, self.proxies)
        
        #print('[INFO] Function asset_transactions, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response

        
    def asset_addresses(self, asset: str, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        List of a addresses containing a specific asset.
        
        :param assets: Assets (Concatenation of the policy_id and hex-encoded asset_name)
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the assets
        """
        
        assets_addresses_url = bf_assets_url + asset + bf_asset_addresses_url
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, assets_addresses_url, self.proxies)
        
        #print('[INFO] Function asset_addresses, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response

    
    def assets_policy(self, policy_id: str, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        List of asset minted under a specific policy.
        
        :param policy_id: Policy ID of the asset
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the assets
        """
        
        assets_policy_url = bf_assets_url + bf_assets_policy_url + policy_id
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, assets_policy_url, self.proxies)
        
        #print('[INFO] Function assets_policy, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response


    def assets_policy_informations(self, policy_id: str, nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, list]:
        '''
        Obtain informations about the assets minted under a specific policy ID.

        :param policy_id: Policy ID
        :nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: None)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dict or DataFrame with the informations on each asset under the policy and the list ofbthe asset not found
        '''
        
        assets_data, assets_not_found  = [], []
        
        #print('[INFO] Get the asset names minted under the policy ID: {}'.format(policy_id))
        asset_minted_names = self.assets_policy(policy_id, pandas=True, nb_of_results=nb_of_results)['asset'].tolist()

        #print('[INFO] Get the information about the assets.'.format(policy_id))
        for asset in tqdm(asset_minted_names):
            try:
                response = self.specific_asset(asset)
            except Exception as e:
                # Save the asset name in a list if he is not found on the network
                if '404' in str(e):
                    assets_not_found.append(convert_hex_to_ascii(asset))
                    continue
                    
                raise Exception('[ERROR] {}'.format(e))

            # Add the asset data info to the list of assets
            assets_data.append(process_onchain_metadata(response))

        #print('[INFO] Function specific_asset, {} API calls.'.format(len(assets_data)))

        return (pd.DataFrame.from_dict(assets_data), assets_not_found)  if pandas else (assets_data, assets_not_found)

      
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
                #print("[INFO] No data available." )
                return {}, count_api_calls
            
            _dict = pd.concat(dataframes).reset_index(drop=True).to_dict()
            
            return _dict, count_api_calls

        # Create a dataframe with the data from each page and add them to the list of data
        dataframes.append(pd.DataFrame.from_dict(data))
    
    _dict = pd.concat(dataframes).reset_index(drop=True).to_dict()

    return _dict, count_api_calls


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

def convert_hex_to_ascii(hex_string: str) -> str:
    """Convert hex string to ascii format"""
    return bytearray.fromhex(hex_string).decode()