#!/usr/bin/env python
import os
import unittest
from cardano_explorer import blockfrost_api

# Check if the Blockfrost API Key is configured in a environmental variable 
assert (os.getenv('BLOCKFROST_API_KEY') is not None), '[ERROR] Your blockfrost api key is not configured in your environement path.'

# Random pool_id, address, stake_address find in the cardano network
pool_id= "pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288ys5kumqce5"
address= 'addr1q8z24xgrlj3m2qjh2vxyqg2fh33y3tegufkll5c4lu8u35gkhpw3h4yhn93ve2whllg0wjazjs5jj8332mgqe332f3uq8m7m6h'
stake_address= 'stake1u8uzevd539lxn40jt60g72a649zdphe9e8hrye4nf5jv0js9uzhzg'
policy_id='ceb5dedd6cda3f0b4a98919b5d3827e15e324771642b57e0e6aabd57'
asset_name='476f6c64486f736b696e736f6e3431'

cardano_mainnet = blockfrost_api.Auth()

class Test(unittest.TestCase):
    
    def test_pool(self):
        print("****************************")
        print('[INFO] POOL Functions tests.')
        print("****************************")
        self.assertFalse(cardano_mainnet.registered_polls(nb_of_results=100, pandas=True).empty)
        self.assertTrue(isinstance(cardano_mainnet.pool_informations(pool_id), dict))
        self.assertFalse(cardano_mainnet.stake_pool_history(pool_id, nb_of_results=100, pandas=True).empty)
        
    def test_nb_results_to_return(self):
        print("***************************************************")
        print("[INFO] Test of the function 'nb_results_to_return'.")
        print("***************************************************")
        self.assertEqual(blockfrost_api.nb_results_to_return(100), (1, False))
        self.assertEqual(blockfrost_api.nb_results_to_return(None), (0, True))
        self.assertRaises(AssertionError, blockfrost_api.nb_results_to_return, 5)
        self.assertRaises(AssertionError, blockfrost_api.nb_results_to_return, 0)
        
    def test_set_query_string_parameter(self): 
        print("*****************************************************")
        print("[INFO] Test of the function 'query_string_parameter'.")
        print("*****************************************************")
        self.assertEqual(blockfrost_api.set_query_string_parameter(1, 'desc'), '?page=1&order=desc')
        self.assertEqual(blockfrost_api.set_query_string_parameter(1), '?page=1&')
        
    def test_epoch(self):
        print("*****************************")
        print("[INFO] EPOCH Functions tests.")
        print("*****************************")
        self.assertTrue(isinstance(cardano_mainnet.latest_epoch()['epoch'], int))
        self.assertTrue(isinstance(cardano_mainnet.latest_epoch_protocol_parameters()['epoch'], int))
        self.assertTrue(isinstance(cardano_mainnet.specific_epoch(287)['epoch'], int))
        self.assertRaises(AssertionError, cardano_mainnet.specific_epoch, -1)
        self.assertFalse(cardano_mainnet.epochs_history([270, 271], pandas=True).empty)
        self.assertRaises(AssertionError, cardano_mainnet.epochs_history, [-1])
        self.assertRaises(AssertionError, cardano_mainnet.epochs_history, 200)
        self.assertRaises(AssertionError, cardano_mainnet.epochs_history, (cardano_mainnet.latest_epoch()['epoch'] + 1))
        
    def test_network_info(self):
        print("*******************************************")
        print("[INFO] Test of the function 'network_info'.")
        print("*******************************************")
        self.assertTrue(isinstance(cardano_mainnet.network_info()['supply']['max'], str))
    
    def test_address(self):
        self.assertTrue(isinstance(cardano_mainnet.address_utxo(address)[0]['tx_hash'], str))
        self.assertTrue(isinstance(cardano_mainnet.address_details(address)['tx_count'], int))
        self.assertTrue(isinstance(cardano_mainnet.address_info(address)['type'], str))
        
    def test_stake(self):
        print("*****************************")
        print("[INFO] Stake Functions tests.")
        print("*****************************")
        self.assertTrue(isinstance(cardano_mainnet.stake_informations(stake_address)['active_epoch'], int))
        self.assertFalse(cardano_mainnet.stake_reward_history(stake_address, nb_of_results=100, pandas=True).empty)
        self.assertFalse(cardano_mainnet.stake_amount_history(stake_address, nb_of_results=100, pandas=True).empty)
        self.assertFalse(cardano_mainnet.stake_delegation(stake_address, nb_of_results=100,  pandas=True).empty)
        self.assertFalse(cardano_mainnet.stake_registration_deregistrations(stake_address, nb_of_results=100, pandas=True).empty)
        self.assertTrue(cardano_mainnet.stake_mir_history(stake_address, nb_of_results=100,  pandas=True).empty)
        self.assertFalse(cardano_mainnet.stake_associated_addresses(stake_address, nb_of_results=100, pandas=True).empty)
        self.assertEqual(cardano_mainnet.stake_assets_associated_addresses(stake_address), {})
        self.assertFalse(cardano_mainnet.stake_withdrawal_history(stake_address, pandas=True).empty)
        
    def test_rewards_history_analysis(self):
        print("*******************************************************")
        print("[INFO] Test of the function 'rewards_history_analysis'.")
        print("*******************************************************")
        self.assertFalse(cardano_mainnet.rewards_history_analysis(stake_address, pandas=True).empty)

    def test_asset(self):
        print("***************************")
        print("[INFO] ASSET Function test.")
        print("***************************")
        self.assertFalse(cardano_mainnet.assets(policy_id+asset_name, pandas=True).empty)
        self.assertTrue(cardano_mainnet.specific_asset(policy_id+asset_name)['asset'] == policy_id+asset_name)
        self.assertFalse(cardano_mainnet.asset_history(policy_id+asset_name, pandas=True).empty)
        self.assertFalse(cardano_mainnet.asset_transactions(policy_id+asset_name, pandas=True).empty)
        self.assertFalse(cardano_mainnet.asset_addresses(policy_id+asset_name, pandas=True).empty)  
        self.assertFalse(cardano_mainnet.assets_policy(policy_id, pandas=True).empty)      
        
if __name__ == '__main__':
    unittest.main()