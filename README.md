# Python Cardano Explorer
Python wrapper for accessing and processing information stored on the  Cardano blockchain using [Blockfrost API](https://blockfrost.io/).

## Install

pip3 install cardano_explorer

## Usage


```python
from cardano_explorer import blockfrost_api
```

## Api Key
If you have an API key, you can either set it as environment variable **BLOCKFROST_API_KEY** or set it manually.


```python
cardano_mainnet = blockfrost_api.Auth()
#or
cardano_mainnet = blockfrost_api.Auth(api_key=api_key)
```

## Using Proxy authentication


```python
proxies = {
 "http": "http://@:port",
 "https": "https://@:port8",
}

cardano_mainnet = blockfrost_api.Auth(proxies=proxies)
```

## Network (mainnet, tesnet, local)
You can specify the cardano network with the class parameter **network** (mainnet by default).


```python
cardano_mainnet = blockfrost_api.Auth()
#or
cardano_mainnet = blockfrost_api.Auth(network='mainnet')
```

## Network

### Network information
Return detailed network information.


```python
cardano_mainnet.network_info()
```

    {'supply': {'max': '45000000000000000',
      'total': '33095610707522483',
      'circulating': '32815060450967318'},
     'stake': {'live': '23309647932671648', 'active': '23136223153988390'}}



## Stake

### Stake informations
Obtain information about a specific stake account.


```python
cardano_mainnet.stake_informations(stake_address)
```

    {'stake_address': 'stake1uyttshgm6jtejckv48tll58hfw3fg2ffrcc4d5qvcc4yc7q9jsalf',
     'active': True,
     'active_epoch': 271,
     'controlled_amount': '2868511950',
     'rewards_sum': '18946556',
     'withdrawals_sum': '0',
     'reserves_sum': '97317',
     'treasury_sum': '0',
     'withdrawable_amount': '19043873',
     'pool_id': 'pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288ys5kumqce5'}



### Stake reward history 
Obtain information about the reward history of a specific account.


```python
cardano_mainnet.stake_reward_history(stake_address) 
#or      
cardano_mainnet.stake_reward_history(stake_address, 
                                     data_order='asc', # Optional: Data order (default: Ascending)
                                     nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                     pandas=True).head() # Optional: Return a pandas dataframe
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>epoch</th>
      <th>amount</th>
      <th>pool_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>273</td>
      <td>587159</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>274</td>
      <td>715853</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>275</td>
      <td>902199</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>276</td>
      <td>824733</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>277</td>
      <td>1056705</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
  </tbody>
</table>
</div>



### Stake amount history 
Obtain information about the history of a specific account.


```python
cardano_mainnet.stake_amount_history(stake_address)
#or                        
cardano_mainnet.stake_amount_history(stake_address, 
                                     data_order='asc', # Optional: Data order (default: Ascending)
                                     nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                     pandas=True) # Optional: Return a pandas dataframe
```

    [INFO] Function stake_amount_history, 1 API calls.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>active_epoch</th>
      <th>amount</th>
      <th>pool_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>273</td>
      <td>998824863</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>274</td>
      <td>998824863</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>275</td>
      <td>1618824863</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>276</td>
      <td>1619412022</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>277</td>
      <td>1620127875</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
  </tbody>
</table>
</div>



### Stake delegation history
Obtain information about the delegation of a specific account.


```python
cardano_mainnet.stake_delegation(stake_address)
#or
cardano_mainnet.stake_delegation(stake_address, 
                                 data_order='asc', # Optional: Data order (default: Ascending)
                                 nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                 pandas=True) # Optional: Return a pandas dataframe
```

    [INFO] Function stake_delegation, 1 API calls.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>active_epoch</th>
      <th>tx_hash</th>
      <th>amount</th>
      <th>pool_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>273</td>
      <td>97a774aa60a2926c9949bfe1edf1dcc2f2297d36633e14...</td>
      <td>497824863</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
  </tbody>
</table>
</div>



### Stake registrations and deregistrations history
Obtain information about the registrations and deregistrations of a specific account.


```python
cardano_mainnet.stake_registration_deregistrations(stake_address)
#or
cardano_mainnet.stake_registration_deregistrations(stake_address, 
                                                   data_order='asc', # Optional: Data order (default: Ascending)
                                                   nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                                   pandas=True) # Optional: Return a pandas dataframe
```

    [INFO] Function stake_registration_deregistrations, 1 API calls.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tx_hash</th>
      <th>action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>97a774aa60a2926c9949bfe1edf1dcc2f2297d36633e14...</td>
      <td>registered</td>
    </tr>
  </tbody>
</table>
</div>



### Stake withdrawal history
Obtain information about the withdrawals of a specific account.


```python
cardano_mainnet.stake_withdrawal_history(stake_address)
#or
cardano_mainnet.stake_withdrawal_history(stake_address, 
                                         data_order='asc', # Optional: Data order (default: Ascending)
                                         nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                         pandas=True) # Optional: Return a pandas dataframe
```

### Stake MIR history
Obtain information about the MIRs of a specific account.


```python
cardano_mainnet.stake_mir_history(stake_address)
#or
cardano_mainnet.stake_mir_history(stake_address, 
                                  data_order='asc', # Optional: Data order (default: Ascending)
                                  nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                  pandas=True) # Optional: Return a pandas dataframe
```

    [INFO] Function stake_mir_history, 1 API calls.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tx_hash</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>c041e475d161444a6a8ca9005ef3deb36ebd579c347d90...</td>
      <td>74456</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9ede69b0ebd0903b1cc6a914a79fabd9a5d6dd94e8c110...</td>
      <td>22861</td>
    </tr>
  </tbody>
</table>
</div>



### Stake associated addresses
Obtain information about the MIRs of a specific account.


```python
cardano_mainnet.stake_associated_addresses(stake_address)
#or
cardano_mainnet.stake_associated_addresses(stake_address, 
                                           data_order='asc', # Optional: Data order (default: Ascending)
                                           nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                           pandas=True) # Optional: Return a pandas dataframe 
```

    [INFO] Function stake_associated_addresses, 1 API calls.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>address</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>addr1qx96yn08e5u7hthawh63ss6269dkzxekq85elrthw...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>addr1q9u0kfvd57parl03j8v9fz52xqz8yjkcu47lcy8hw...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>addr1q8m6tn3edl333c8yzms8dzrkkckm0vn0dkvq436au...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>addr1q9py3k58fmyu896charn6mey8c5f22uq830m4udsy...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>addr1q8mk7kft30hwmj2yttltm8j5f4ccuguxr9z3werwm...</td>
    </tr>
  </tbody>
</table>
</div>



### Stake assets associated addresses
Obtain information about assets associated with addresses of a specific account.</blockquote>


```python
cardano_mainnet.stake_associated_addresses(stake_address)
#or
cardano_mainnet.stake_assets_associated_addresses(stake_address, 
                                                  data_order='asc', # Optional: Data order (default: Ascending)
                                                  nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                                  pandas=True) # Optional: Return a pandas dataframe 
```

    [INFO] No data available.
    [INFO] Function stake_assets_associated_addresses, 1 API calls.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>



# Addresse Informations

### Addresses
Obtain information about a specific address.


```python
cardano_mainnet.address_info(address)
```




    {'address': 'addr1q8z24xgrlj3m2qjh2vxyqg2fh33y3tegufkll5c4lu8u35gkhpw3h4yhn93ve2whllg0wjazjs5jj8332mgqe332f3uq8m7m6h',
     'amount': [{'unit': 'lovelace', 'quantity': '350000000'}],
     'stake_address': 'stake1uyttshgm6jtejckv48tll58hfw3fg2ffrcc4d5qvcc4yc7q9jsalf',
     'type': 'shelley'}



### Address details
Obtain details about an address.


```python
cardano_mainnet.address_details(address)
```




    {'address': 'addr1q8z24xgrlj3m2qjh2vxyqg2fh33y3tegufkll5c4lu8u35gkhpw3h4yhn93ve2whllg0wjazjs5jj8332mgqe332f3uq8m7m6h',
     'received_sum': [{'unit': 'lovelace', 'quantity': '350000000'}],
     'sent_sum': [{'unit': 'lovelace', 'quantity': '0'}],
     'tx_count': 1}



### Address UTXOs
UTXOs of the address.


```python
cardano_mainnet.address_utxo(address)
```




    [{'tx_hash': '996ff0a57282ef943ecdbc263cf9c41c178d65587d70d9d9dcbe98e520f8e406',
      'tx_index': 4,
      'output_index': 4,
      'amount': [{'unit': 'lovelace', 'quantity': '350000000'}],
      'block': '73768f4ca2a0c96611a1fbd7f53a3b1b573fb0371012e54a943cf58926eb9cea'}]



### Address transactions
Transactions on the address.


```python
cardano_mainnet.address_transaction(address)
```




    [{'tx_hash': '996ff0a57282ef943ecdbc263cf9c41c178d65587d70d9d9dcbe98e520f8e406',
      'tx_index': 45,
      'block_height': 6095572}]



## Epochs

### Latest epoch
Obtain the information about the latest epoch.


```python
cardano_mainnet.latest_epoch()
```




    {'epoch': 288,
     'start_time': 1630619091,
     'end_time': 1631051091,
     'first_block_time': 1630619101,
     'last_block_time': 1630695809,
     'block_count': 3867,
     'tx_count': 77200,
     'output': '41529702474109934',
     'fees': '16021622015',
     'active_stake': '23136223153988390'}



### Latest epoch protocol parameters
Return the protocol parameters for the latest epoch.


```python
cardano_mainnet.latest_epoch_protocol_parameters()
```




    {'epoch': 288,
     'min_fee_a': 44,
     'min_fee_b': 155381,
     'max_block_size': 65536,
     'max_tx_size': 16384,
     'max_block_header_size': 1100,
     'key_deposit': '2000000',
     'pool_deposit': '500000000',
     'e_max': 18,
     'n_opt': 500,
     'a0': 0.3,
     'rho': 0.003,
     'tau': 0.2,
     'decentralisation_param': 0,
     'extra_entropy': None,
     'protocol_major_ver': 4,
     'protocol_minor_ver': 0,
     'min_utxo': '1000000',
     'min_pool_cost': '340000000',
     'nonce': 'bf3b52ab86e152b392cbf095c1d0f07aaeda956eecfdb44b09bcb85a0ecae36a'}



### Specific epoch
Obtain informations about a specific epoch.


```python
cardano_mainnet.specific_epoch(287)
```




    {'epoch': 287,
     'start_time': 1630187091,
     'end_time': 1630619091,
     'first_block_time': 1630187230,
     'last_block_time': 1630619085,
     'block_count': 21065,
     'tx_count': 401343,
     'output': '74754307451589173',
     'fees': '86536781869',
     'active_stake': '23041097075076811'}



### Epochs history
Obtain informations about sevrals epochs.


```python
cardano_mainnet.epochs_history([270, 271, 272],
                               pandas=True) # Optional: Return a pandas dataframe 
```

    [INFO] Function epochs_history, 4 API calls.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>epoch</th>
      <th>start_time</th>
      <th>end_time</th>
      <th>first_block_time</th>
      <th>last_block_time</th>
      <th>block_count</th>
      <th>tx_count</th>
      <th>output</th>
      <th>fees</th>
      <th>active_stake</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>270</td>
      <td>1622843091</td>
      <td>1623275091</td>
      <td>1622843183</td>
      <td>1623275038</td>
      <td>21395</td>
      <td>174334</td>
      <td>12213404538685056</td>
      <td>36489177917</td>
      <td>22893778548073522</td>
    </tr>
    <tr>
      <th>1</th>
      <td>271</td>
      <td>1623275091</td>
      <td>1623707091</td>
      <td>1623275098</td>
      <td>1623707059</td>
      <td>21410</td>
      <td>145244</td>
      <td>12686700012872148</td>
      <td>30802442909</td>
      <td>22970909569111347</td>
    </tr>
    <tr>
      <th>2</th>
      <td>272</td>
      <td>1623707091</td>
      <td>1624139091</td>
      <td>1623707123</td>
      <td>1624139087</td>
      <td>21499</td>
      <td>135373</td>
      <td>10640794327820158</td>
      <td>29593210504</td>
      <td>23020000415780615</td>
    </tr>
  </tbody>
</table>
</div>



# Pools

### List of stake pools
List of registered stake pools.


```python
cardano_mainnet.registered_polls()
#or
cardano_mainnet.registered_polls(nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                 pandas=True) # Optional: Return a pandas dataframe 
```

    [INFO] Function registered_polls, 1 API calls.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>registered_polls_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>pool1z5uqdk7dzdxaae5633fqfcu2eqzy3a3rgtuvy087f...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0na...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pool1c8k78ny3xvsfgenhf4yzvpzwgzxmz0t0um0h2xnn2...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>pool1q80jjs53w0fx836n8g38gtdwr8ck5zre3da90peux...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pool1ddskftmsscw92d7vnj89pldwx5feegkgcmamgt5t0...</td>
    </tr>
  </tbody>
</table>
</div>



### Specific stake pool informations
Pool informations.


```python
cardano_mainnet.pool_informations(pool_id)
```




    {'pool_id': 'pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288ys5kumqce5',
     'hex': 'cdae4a1a08974113e77ea332cb1da97d9e3fca5cf797f9394739214b',
     'vrf_key': '5517fbeb4c6a5a613835808de183345eaf85ab0e251210e493e088afa41d9ab0',
     'blocks_minted': 3073,
     'live_stake': '55648149168432',
     'live_size': 0.0023887520907477904,
     'live_saturation': 0.8479059445396915,
     'live_delegators': 1443,
     'active_stake': '55449417952886',
     'active_size': 0.002396649512923082,
     'declared_pledge': '200000000000',
     'live_pledge': '203180990314',
     'margin_cost': 0.01,
     'fixed_cost': '340000000',
     'reward_account': 'stake1u8uzevd539lxn40jt60g72a649zdphe9e8hrye4nf5jv0js9uzhzg',
     'owners': ['stake1u9qsgte62jau0qu6kjy8zch8aynt55gql6jsxe05464n99gsqd7ra',
      'stake1u8uzevd539lxn40jt60g72a649zdphe9e8hrye4nf5jv0js9uzhzg'],
     'registration': ['b1bfffc26b6210ced9cc679781922e8b1ac70a2f7719523528639da4ab7f2d88',
      'be5b798897f5b83e5bf562df6fc68a94d5528acc80ab8e999ce866aa63a4d06a',
      '0f4781efd649f91e37847cb2699a8a41632ee94df1465e255577772f362339bf',
      '630c7195fdc1c5c14bb12c460059c5adb11b3cd6d3e576628aee0a8338f1b6ad',
      '119fe23a35e0ddcbb5778f17ad2371228a53b5ced037c12083a0c77b5711e1d4',
      'f1fe58c30ec7f5193476694fafc46dcdb11c3408e114e8fa2a95425243907ed4',
      '09c2c3d34de116365c9cf9a6e75f45856013388d962dbd5584c27b7d0bb36eed'],
     'retirement': []}



### Stake pool history

History of stake pool parameters over epochs.


```python
cardano_mainnet.stake_pool_history(pool_id)
#or
cardano_mainnet.stake_pool_history(pool_id,
                                   pandas=True) # Optional: Return a pandas dataframe 
```

    [INFO] Function param_stake_pool_history, 1 API calls.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>epoch</th>
      <th>blocks</th>
      <th>active_stake</th>
      <th>active_size</th>
      <th>delegators_count</th>
      <th>rewards</th>
      <th>fees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>210</td>
      <td>0</td>
      <td>37220609681471</td>
      <td>0.006144</td>
      <td>66</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>211</td>
      <td>10</td>
      <td>54335156396766</td>
      <td>0.005339</td>
      <td>81</td>
      <td>41930800644</td>
      <td>795508006</td>
    </tr>
    <tr>
      <th>2</th>
      <td>212</td>
      <td>19</td>
      <td>57680429746242</td>
      <td>0.004764</td>
      <td>100</td>
      <td>44444415813</td>
      <td>820644158</td>
    </tr>
    <tr>
      <th>3</th>
      <td>213</td>
      <td>17</td>
      <td>39988128646167</td>
      <td>0.003134</td>
      <td>113</td>
      <td>35108072495</td>
      <td>687680724</td>
    </tr>
    <tr>
      <th>4</th>
      <td>214</td>
      <td>16</td>
      <td>37882297876063</td>
      <td>0.002831</td>
      <td>114</td>
      <td>31712032983</td>
      <td>653720329</td>
    </tr>
  </tbody>
</table>
</div>



## Analysis

### Rewards history analysis
Data table to analyze the stake rewards.


```python
cardano_mainnet.rewards_history_analysis(stake_address)
#or
cardano_mainnet.rewards_history_analysis(stake_address,
                                         pandas=True). # Optional: Return a pandas dataframe 
```

    [INFO] Function stake_reward_history, 1 API calls.
    [INFO] Function stake_amount_history, 1 API calls.
    [INFO] Function param_stake_pool_history, 1 API calls.
    [INFO] Function epochs_history, 15 API calls.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>epoch</th>
      <th>rewards_amount</th>
      <th>stake_amount</th>
      <th>pool_id</th>
      <th>epoch_start_time</th>
      <th>epoch_end_time</th>
      <th>epoch_first_block_time</th>
      <th>epoch_last_block_time</th>
      <th>epoch_block_count</th>
      <th>epoch_tx_count</th>
      <th>epoch_output</th>
      <th>epoch_fees</th>
      <th>epoch_active_stake</th>
      <th>stake_pool_blocks</th>
      <th>stake_pool_active_stake</th>
      <th>stake_pool_active_size</th>
      <th>stake_pool_delegators_count</th>
      <th>stake_pool_rewards</th>
      <th>stake_pool_fees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>273</td>
      <td>587159</td>
      <td>998824863</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
      <td>1624139091</td>
      <td>1624571091</td>
      <td>1624139124</td>
      <td>1624571089</td>
      <td>21464</td>
      <td>150752</td>
      <td>15740586909359854</td>
      <td>32570360903</td>
      <td>23075664958746578</td>
      <td>39</td>
      <td>47829822938326</td>
      <td>0.002073</td>
      <td>1120</td>
      <td>28740378749</td>
      <td>624003787</td>
    </tr>
    <tr>
      <th>1</th>
      <td>274</td>
      <td>715853</td>
      <td>998824863</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
      <td>1624571091</td>
      <td>1625003091</td>
      <td>1624571155</td>
      <td>1625003071</td>
      <td>21521</td>
      <td>133041</td>
      <td>11764235372205745</td>
      <td>28650900551</td>
      <td>23094302016775953</td>
      <td>50</td>
      <td>50332107694676</td>
      <td>0.002179</td>
      <td>1174</td>
      <td>36776812909</td>
      <td>704368129</td>
    </tr>
    <tr>
      <th>2</th>
      <td>275</td>
      <td>902199</td>
      <td>1618824863</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
      <td>1625003091</td>
      <td>1625435091</td>
      <td>1625003255</td>
      <td>1625435086</td>
      <td>21505</td>
      <td>136339</td>
      <td>13402253806474700</td>
      <td>29088470734</td>
      <td>23006172979540278</td>
      <td>37</td>
      <td>47430899220515</td>
      <td>0.002062</td>
      <td>1190</td>
      <td>27005861046</td>
      <td>606658610</td>
    </tr>
    <tr>
      <th>3</th>
      <td>276</td>
      <td>824733</td>
      <td>1619412022</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
      <td>1625435091</td>
      <td>1625867091</td>
      <td>1625435146</td>
      <td>1625867083</td>
      <td>21298</td>
      <td>144737</td>
      <td>12581437590766031</td>
      <td>30139500685</td>
      <td>23092420021153886</td>
      <td>33</td>
      <td>46277458382635</td>
      <td>0.002004</td>
      <td>1204</td>
      <td>24108337832</td>
      <td>577683378</td>
    </tr>
    <tr>
      <th>4</th>
      <td>277</td>
      <td>1056705</td>
      <td>1620127875</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
      <td>1625867091</td>
      <td>1626299091</td>
      <td>1625867167</td>
      <td>1626299088</td>
      <td>21323</td>
      <td>135191</td>
      <td>9892737538002395</td>
      <td>28508156761</td>
      <td>23196615273348567</td>
      <td>41</td>
      <td>45104996094565</td>
      <td>0.001944</td>
      <td>1221</td>
      <td>30007226603</td>
      <td>636672266</td>
    </tr>
  </tbody>
</table>
</div>
