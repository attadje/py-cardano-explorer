#!/usr/bin/env python

import os
import unittest
import pandas as pd
from cardano_explorer import blockfrost_api
from cardano_explorer.blockfrost import util
from cardano_explorer import cnft_io

# Check if the Blockfrost API Key is configured in a environmental variable 
# assert (os.getenv('BLOCKFROST_API_KEY') is not None), '[ERROR] Your blockfrost api key is not configured in your environement path.'

pool_id = "pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288ys5kumqce5"
address = 'addr1q8z24xgrlj3m2qjh2vxyqg2fh33y3tegufkll5c4lu8u35gkhpw3h4yhn93ve2whllg0wjazjs5jj8332mgqe332f3uq8m7m6h'
stake_address = 'stake1u8uzevd539lxn40jt60g72a649zdphe9e8hrye4nf5jv0js9uzhzg'
policy_id = '40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c28262fab21728'
asset_name = '436c61794e6174696f6e33393836'
tx_hash = '117f97ccf6e98a16697e7cc205daf2d0bfe83d849a63df2f40d10bef235848e7'
stake_tx_hash = '97a774aa60a2926c9949bfe1edf1dcc2f2297d36633e14a87ae449b4158a027f'
script_tx_hash_redeemers = '34dd0b7ae56b65f4cda029d99cda8322684ec6339ac1c195c16458c1e5e94b96'
stake_mir_tx_hash = 'c041e475d161444a6a8ca9005ef3deb36ebd579c347d90b5b53968d47d5193da'
stake_withdrawal_tx_hash = '80b09b61d2da86f5847d0b9a5f72d32224fcd7e1aa17161b9d24732339a26836'
script_redeemer_tx_hash = '34dd0b7ae56b65f4cda029d99cda8322684ec6339ac1c195c16458c1e5e94b96'
script_hash = 'cc7888851f0f5aa64c136e0c8fb251e9702f3f6c9efcf3a60a54f419'
stake_pool_registration_tx_hash = 'b1bfffc26b6210ced9cc679781922e8b1ac70a2f7719523528639da4ab7f2d88'

cardano_mainnet = blockfrost_api.Auth('iSXrfNxhpPChKCnts2KX9MJ1eQ7exYgb')

class TEST_BLOCKFROST_API(unittest.TestCase):
    
    def test_pool(self):
        self.assertTrue(isinstance(cardano_mainnet.registered_polls(), dict))
        self.assertTrue(isinstance(cardano_mainnet.registered_polls(pandas=True), pd.DataFrame))
        self.assertTrue(isinstance(cardano_mainnet.pool_informations(pool_id), dict))
        self.assertTrue(isinstance(cardano_mainnet.stake_pool_history(pool_id), dict))
        self.assertTrue(isinstance(cardano_mainnet.stake_pool_history(pool_id, pandas=True), pd.DataFrame))
        
    def test_nb_results_to_return(self):
        self.assertEqual(util.nb_results_to_return(100), (1, False))
        self.assertEqual(util.nb_results_to_return(None), (0, True))
        self.assertRaises(AssertionError, util.nb_results_to_return, 5)
        self.assertRaises(AssertionError, util.nb_results_to_return, 0)
        
    def test_set_query_string_parameter(self): 
        self.assertEqual(util.set_query_string_parameter(1, 'desc'), '?page=1&order=desc')
        self.assertEqual(util.set_query_string_parameter(1), '?page=1&')
        
    def test_epoch(self):
        self.assertTrue(isinstance(cardano_mainnet.latest_epoch(), dict))
        self.assertTrue(isinstance(cardano_mainnet.latest_epoch_protocol_parameters(), dict))
        self.assertTrue(isinstance(cardano_mainnet.specific_epoch(287), dict))
        self.assertTrue(isinstance(cardano_mainnet.epochs_history([270, 271]), list))
        self.assertTrue(isinstance(cardano_mainnet.epochs_history([270, 271], pandas=True), pd.DataFrame))
        self.assertRaises(AssertionError, cardano_mainnet.specific_epoch, -1)
        self.assertRaises(AssertionError, cardano_mainnet.epochs_history, [-1])
        self.assertRaises(AssertionError, cardano_mainnet.epochs_history, 200)
        self.assertRaises(AssertionError, cardano_mainnet.epochs_history, (cardano_mainnet.latest_epoch()['epoch'] + 1))
        
    def test_network_info(self):
        self.assertTrue(isinstance(cardano_mainnet.network_info(), dict))
    
    def test_address(self):
        self.assertTrue(isinstance(cardano_mainnet.address_utxo(address)[0], dict))
        self.assertTrue(isinstance(cardano_mainnet.address_details(address), dict))
        self.assertTrue(isinstance(cardano_mainnet.address_info(address), dict))
        
    def test_stake(self):
        self.assertTrue(isinstance(cardano_mainnet.stake_informations(stake_address), dict))
        self.assertTrue(isinstance(cardano_mainnet.stake_reward_history(stake_address), dict))
        self.assertTrue(isinstance(cardano_mainnet.stake_reward_history(stake_address, pandas=True), pd.DataFrame))
        self.assertTrue(isinstance(cardano_mainnet.stake_amount_history(stake_address), dict))
        self.assertTrue(isinstance(cardano_mainnet.stake_amount_history(stake_address, pandas=True), pd.DataFrame))
        self.assertTrue(isinstance(cardano_mainnet.stake_delegation(stake_address), dict))
        self.assertTrue(isinstance(cardano_mainnet.stake_delegation(stake_address, pandas=True), pd.DataFrame))
        self.assertTrue(isinstance(cardano_mainnet.stake_registration_deregistrations(stake_address), dict))
        self.assertTrue(isinstance(cardano_mainnet.stake_registration_deregistrations(stake_address, pandas=True), pd.DataFrame))
        self.assertTrue(isinstance(cardano_mainnet.stake_mir_history(stake_address), dict))
        self.assertTrue(isinstance(cardano_mainnet.stake_mir_history(stake_address, pandas=True), pd.DataFrame))
        self.assertTrue(isinstance(cardano_mainnet.stake_associated_addresses(stake_address), dict))
        self.assertTrue(isinstance(cardano_mainnet.stake_associated_addresses(stake_address, pandas=True), pd.DataFrame))
        self.assertTrue(isinstance(cardano_mainnet.stake_assets_associated_addresses(stake_address), dict))
        self.assertTrue(isinstance(cardano_mainnet.stake_assets_associated_addresses(stake_address, pandas=True), pd.DataFrame))
        self.assertTrue(isinstance(cardano_mainnet.stake_withdrawal_history(stake_address), dict))
        self.assertTrue(isinstance(cardano_mainnet.stake_withdrawal_history(stake_address, pandas=True), pd.DataFrame))
        self.assertTrue(isinstance(cardano_mainnet.stake_rewards_corr(stake_address), dict))
        self.assertTrue(isinstance(cardano_mainnet.stake_rewards_corr(stake_address, pandas=True), pd.DataFrame))

    def test_asset(self):
        self.assertTrue(isinstance(cardano_mainnet.assets(policy_id+asset_name), dict))
        self.assertTrue(isinstance(cardano_mainnet.assets(policy_id+asset_name, pandas=True), pd.DataFrame))
        self.assertTrue(isinstance(cardano_mainnet.specific_asset(policy_id+asset_name), dict))
        self.assertTrue(isinstance(cardano_mainnet.asset_history(policy_id+asset_name), dict))
        self.assertTrue(isinstance(cardano_mainnet.asset_history(policy_id+asset_name, pandas=True), pd.DataFrame))
        self.assertTrue(isinstance(cardano_mainnet.asset_transactions(policy_id+asset_name), dict))
        self.assertTrue(isinstance(cardano_mainnet.asset_transactions(policy_id+asset_name, pandas=True), pd.DataFrame))
        self.assertTrue(isinstance(cardano_mainnet.asset_addresses(policy_id+asset_name),  dict))
        self.assertTrue(isinstance(cardano_mainnet.asset_addresses(policy_id+asset_name, pandas=True), pd.DataFrame))
        self.assertTrue(isinstance(cardano_mainnet.assets_policy(policy_id), dict))
        self.assertTrue(isinstance(cardano_mainnet.assets_policy(policy_id, pandas=True), pd.DataFrame))
        self.assertTrue(isinstance(cardano_mainnet.assets_policy_info(policy_id, nb_of_results=100), list))

    def test_convert_hex_to_ascii(self):
         self.assertTrue(util.convert_hex_to_ascii('436c61794e6174696f6e33393836')=='ClayNation3986')

    def test_transaction(self):
         self.assertTrue(isinstance(cardano_mainnet.specific_tx(tx_hash), dict))
         self.assertTrue(isinstance(cardano_mainnet.tx_utxos(tx_hash), dict))
         self.assertTrue(isinstance(cardano_mainnet.tx_stake_address_cert(stake_tx_hash), list))
         self.assertTrue(isinstance(cardano_mainnet.tx_stake_address_cert(stake_tx_hash, pandas=True), pd.DataFrame))
         self.assertTrue(isinstance(cardano_mainnet.tx_delegation_cert(stake_tx_hash), list))
         self.assertTrue(isinstance(cardano_mainnet.tx_delegation_cert(stake_tx_hash, pandas=True), pd.DataFrame))
         self.assertTrue(isinstance(cardano_mainnet.tx_withdrawal_url(stake_withdrawal_tx_hash), list))
         self.assertTrue(isinstance(cardano_mainnet.tx_withdrawal_url(stake_withdrawal_tx_hash, pandas=True), pd.DataFrame))
         self.assertTrue(isinstance(cardano_mainnet.tx_transaction_mirs(stake_mir_tx_hash), list))
         self.assertTrue(isinstance(cardano_mainnet.tx_transaction_mirs(stake_mir_tx_hash, pandas=True), pd.DataFrame))
         self.assertTrue(isinstance(cardano_mainnet.tx_stake_pool_update(script_tx_hash_redeemers), list))
         self.assertTrue(isinstance(cardano_mainnet.tx_stake_pool_update(script_tx_hash_redeemers, pandas=True), pd.DataFrame))
         self.assertTrue(isinstance(cardano_mainnet.tx_stake_pool_retirement_cert(stake_tx_hash), list))
         self.assertTrue(isinstance(cardano_mainnet.tx_stake_pool_retirement_cert(stake_tx_hash, pandas=True), pd.DataFrame))
         self.assertTrue(isinstance(cardano_mainnet.tx_metadata(tx_hash), list))
         self.assertTrue(isinstance(cardano_mainnet.tx_metadata(tx_hash, pandas=True), pd.DataFrame))
         self.assertTrue(isinstance(cardano_mainnet.tx_stake_pool_update(script_tx_hash_redeemers), list))
         self.assertTrue(isinstance(cardano_mainnet.tx_stake_pool_update(script_tx_hash_redeemers, pandas=True), pd.DataFrame))
         self.assertTrue(isinstance(cardano_mainnet.tx_metadata(tx_hash), list))
         self.assertTrue(isinstance(cardano_mainnet.tx_metadata(tx_hash, pandas=True), pd.DataFrame))
         self.assertTrue(isinstance(cardano_mainnet.tx_cbor_metadata(tx_hash), list))
         self.assertTrue(isinstance(cardano_mainnet.tx_cbor_metadata(tx_hash, pandas=True), pd.DataFrame))
         self.assertTrue(isinstance(cardano_mainnet.tx_redeemers(script_redeemer_tx_hash), list))
         self.assertTrue(isinstance(cardano_mainnet.tx_redeemers(script_redeemer_tx_hash, pandas=True), pd.DataFrame))

    def test_script(self):
        self.assertTrue(isinstance(cardano_mainnet.scripts_list(), dict))
        self.assertTrue(isinstance(cardano_mainnet.specific_script(script_hash), dict))
        self.assertTrue(isinstance(cardano_mainnet.redeem_specific_script(script_hash), dict))

    
if __name__ == '__main__':
    unittest.main()

