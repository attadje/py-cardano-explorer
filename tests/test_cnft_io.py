#!/usr/bin/env python

import os
import unittest
import pandas as pd
from cardano_explorer import blockfrost_api
from cardano_explorer.blockfrost import util
from cardano_explorer import cnft_io

# Check if the Blockfrost API Key is configured in a environmental variable 
# assert (os.getenv('BLOCKFROST_API_KEY') is not None), '[ERROR] Your blockfrost api key is not configured in your environement path.'

policy_id = '40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c28262fab21728'
cardano_mainnet = blockfrost_api.Auth('iSXrfNxhpPChKCnts2KX9MJ1eQ7exYgb')

class TEST_CNFT_IO(unittest.TestCase):
    
    def test_policy(self):
        self.assertTrue(isinstance(cnft_io.verified_policies(), list))
        self.assertTrue(isinstance(cnft_io.get_policy_id('Clay Nation by Clay Mates'), list))
        self.assertTrue(cnft_io.check_policy_id(policy_id, 'Clay Nation by Clay Mates'), list)
        self.assertRaises(ValueError, cnft_io.check_policy_id, policy_id ,'hgvfv')
        self.assertTrue(isinstance(cnft_io.get_project_info('Clay Nation by Clay Mates'), dict))
        self.assertTrue(cnft_io.project_exist('Clay Nation by Clay Mates'), dict)
        self.assertFalse(cnft_io.project_exist('hgvgy'), dict)



if __name__ == '__main__':
    unittest.main()

