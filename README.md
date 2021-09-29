# Python Cardano Explorer

Python wrapper for accessing and processing information stored on the Cardano blockchain using [Blockfrost API](https://blockfrost.io/).

<br />

**Table of contents**
- [Install](#Install)
- [Usage](#Usage)
- [Api Key](#Api-Key)
- [Using With Proxy](#Using-With-Proxy)
- [Network Info](#Network-Info)
  * [Network Informations](#Network-Informations)
- [Stake](#Stake)
  * [Stake Informations](#Stake-Informations)
  * [Stake Reward History](#Stake-Reward-History)
  * [Stake Amount History](#Stake-Amount-History)
  * [Stake Delegation History](#Stake-Delegation-History)
  * [Stake Registrations And Deregistrations History](#Stake-Registrations-And-Deregistrations-History)
  * [Stake Withdrawal History](#Stake-Withdrawal-History)
  * [Stake MIR History](#Stake-MIR-History)
  * [Stake Associated Addresses](#Stake-Associated-Addresses)
  * [Stake Assets Associated Addresses](#Stake-Assets-Associated-Addresses)
- [Address](#Address)
  * [Specific Address](#Specific-Address)
  * [Address Details](#Address-Details)
  * [Address UTXOs](#Address-UTXOs)
  * [Address Transactions](#Address-Transactions)
- [Epoch](#Epoch)
  * [Latest Epoch](#Latest-Epoch)
  * [Latest Epoch Protocol Parameters](#Latest-Epoch-Protocol-Parameters)
  * [Specific Epoch](#Specific-Epoch)
  * [Epochs History](#Epochs-History)
- [Pool](#Pool)
  * [List Of Stake Pools](#List-Of-Stake-Pools)
  * [Specific Stake Pool Informations](#Specific-Stake-Pool-Informations)
  * [Epochs History](#Epochs-History)
  * [Stake Pool History](#Stake-Pool-History)
- [Assets](#Assets)
  * [Assets List](#Assets-List)
  * [Specific Asset](#Specific-Asset)
  * [Asset History](#Asset-History)
  * [Assets Of A Apecific Policy](#Assets-Of-A-Apecific-Policy)
  * [Get Assets Informations](#Get-Assets-Informations)
- [Data Analysis](#Data-Analysis)
  * [Rewards History Analysis](#Rewards-History-Analysis)
- [Donation](#Donate)

<br />

## Install (Not available yet)
The library is not deployed yet, clone the project if you want testing the functions


```python
pip3 install cardano_explorer
```


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

## Using With Proxy


```python
proxies = {
 "http": "http://user:password@server:port",
 "https": "https://user:password@server:portt",
}

cardano_mainnet = blockfrost_api.Auth(proxies=proxies)
```

## Network
You can specify the cardano network with the class parameter **network**.


```python
cardano_mainnet = blockfrost_api.Auth() # mainnet by default
#or
cardano_mainnet = blockfrost_api.Auth(network='mainnet')
#or
cardano_mainnet = blockfrost_api.Auth(network='testnet')
```

## Network Informations

### Network Info
Return detailed about the network.


```python
cardano_mainnet.network_info()
```




    {'supply': {'max': '45000000000000000',
      'total': '33206309572085375',
<<<<<<< HEAD
      'circulating': '32854644466406483',
      'locked': '10756061545447'},
     'stake': {'live': '23378092915484642', 'active': '23395112387185878'}}
=======
      'circulating': '32854649043385098',
      'locked': '10734513504016'},
     'stake': {'live': '23379617482483942', 'active': '23395112387185878'}}
>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd



## Stake

### Stake Informations
Obtain information about a specific stake account.


```python
cardano_mainnet.stake_informations(stake_address)
```




    {'stake_address': 'stake1uyttshgm6jtejckv48tll58hfw3fg2ffrcc4d5qvcc4yc7q9jsalf',
     'active': True,
     'active_epoch': 271,
     'controlled_amount': '3002782240',
     'rewards_sum': '21216846',
     'withdrawals_sum': '0',
     'reserves_sum': '97317',
     'treasury_sum': '0',
     'withdrawable_amount': '21314163',
     'pool_id': 'pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288ys5kumqce5'}



### Stake Reward History
Obtain information about the reward history of a specific account.


```python
cardano_mainnet.stake_reward_history(stake_address)
#or      
cardano_mainnet.stake_reward_history(stake_address,
                                     data_order='asc', # Optional: Data order (default: Ascending)
                                     nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                     pandas=True) # Optional: Return a pandas dataframe
```

<<<<<<< HEAD
=======


>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd
<div>
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
      <th>14</th>
      <td>287</td>
      <td>2270290</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>288</td>
      <td>1768631</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>289</td>
      <td>2390373</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>290</td>
      <td>1878132</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>291</td>
      <td>2059700</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
  </tbody>
</table>
</div>



### Stake Amount History
Obtain information about the history of a specific account.


```python
cardano_mainnet.stake_amount_history(stake_address)
#or                        
cardano_mainnet.stake_amount_history(stake_address,
                                     data_order='asc', # Optional: Data order (default: Ascending)
                                     nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                     pandas=True) # Optional: Return a pandas dataframe
```
<<<<<<< HEAD


<div>
=======
>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd
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
      <td>242</td>
      <td>1424619058</td>
      <td>pool1u7mqtde27swkarngjsn5mmw3sy20zavlafgqkmg8q...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>243</td>
      <td>1424619058</td>
      <td>pool1u7mqtde27swkarngjsn5mmw3sy20zavlafgqkmg8q...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>244</td>
      <td>1424619058</td>
      <td>pool1u7mqtde27swkarngjsn5mmw3sy20zavlafgqkmg8q...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>245</td>
      <td>1425498425</td>
      <td>pool1u7mqtde27swkarngjsn5mmw3sy20zavlafgqkmg8q...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>246</td>
      <td>1426468544</td>
      <td>pool1u7mqtde27swkarngjsn5mmw3sy20zavlafgqkmg8q...</td>
    </tr>
  </tbody>
</table>
</div>



### Stake Delegation History
Obtain information about the delegation of a specific account.


```python
cardano_mainnet.stake_delegation(stake_address)
#or
cardano_mainnet.stake_delegation(stake_address,
                                 data_order='asc', # Optional: Data order (default: Ascending)
                                 nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                 pandas=True) # Optional: Return a pandas dataframe
```

<<<<<<< HEAD

<div>
=======
>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd
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
      <td>242</td>
      <td>b602262e1264dabd6c10747415558934d196834d7c7dea...</td>
      <td>747625479</td>
      <td>pool1u7mqtde27swkarngjsn5mmw3sy20zavlafgqkmg8q...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>248</td>
      <td>5822a3b2ebc0a45426aff524e5a0fd2bf7906f671e875a...</td>
      <td>747452454</td>
      <td>pool1m62sl6rauje9cknrkhwl39tc4hujudkd7gp478dpz...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>259</td>
      <td>2c0c3c2123b74b926d2b6969ea21f49ae92861acecf2b8...</td>
      <td>21263559</td>
      <td>pool1lurfk0k0wwx54hlg8a7zp3jtstu57u59aeq7aketl...</td>
    </tr>
  </tbody>
</table>
</div>



### Stake Registrations And Deregistrations History
Obtain information about the registrations and deregistrations of a specific account.


```python
cardano_mainnet.stake_registration_deregistrations(stake_address)
#or
cardano_mainnet.stake_registration_deregistrations(stake_address,
                                                   data_order='asc', # Optional: Data order (default: Ascending)
                                                   nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                                   pandas=True) # Optional: Return a pandas dataframe
```

<<<<<<< HEAD

<div>
=======
>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd
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
      <td>b602262e1264dabd6c10747415558934d196834d7c7dea...</td>
      <td>registered</td>
    </tr>
  </tbody>
</table>
</div>



### Stake Withdrawal History
Obtain information about the withdrawals of a specific account.


```python
cardano_mainnet.stake_withdrawal_history(stake_adress)
#or
cardano_mainnet.stake_withdrawal_history(stake_address,
                                         data_order='asc', # Optional: Data order (default: Ascending)
                                         nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                         pandas=True) # Optional: Return a pandas dataframe
```
<<<<<<< HEAD



<div>
=======
>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd
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
      <td>80b09b61d2da86f5847d0b9a5f72d32224fcd7e1aa1716...</td>
      <td>21239707</td>
    </tr>
  </tbody>
</table>
</div>



### Stake MIR History
Obtain information about the MIRs of a specific account.


```python
cardano_mainnet.stake_mir_history(stake_address)
#or
cardano_mainnet.stake_mir_history(stake_address,
                                  data_order='asc', # Optional: Data order (default: Ascending)
                                  nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                  pandas=True) # Optional: Return a pandas dataframe
```

<<<<<<< HEAD

<div>
=======
>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd
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
      <td>443b98009b9a705c7112b031d223f26a3399f8cf1e7f12...</td>
      <td>16922</td>
    </tr>
    <tr>
      <th>1</th>
      <td>f707cb4decf7f21991f506bba051a0184ca8ecbd402f79...</td>
      <td>5196</td>
    </tr>
  </tbody>
</table>
</div>



### Stake Associated Addresses
Obtain information about the MIRs of a specific account.


```python
cardano_mainnet.stake_associated_addresses(stake_address)
#or
cardano_mainnet.stake_associated_addresses(stake_address,
                                           data_order='asc', # Optional: Data order (default: Ascending)
                                           nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                           pandas=True) # Optional: Return a pandas dataframe
```

<<<<<<< HEAD
<div>
=======
>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd
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
      <td>addr1q9asyce9kg8x8srwjuehtj0sxzc206rn5nv8tzc66...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>addr1qyyzytknnnr3yy3hrxt7puzxy2zle6cfs3c839rdw...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>addr1q8qe2873c334m7s3j2g27fq4sjqkh03mr28z3nd3l...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>addr1q9226w0sg40mjhnzdt3myvnucrljqg7pyxgn9vypc...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>addr1q8amjln6cua3scnthlm8jd7vnz4w4j7hmpkj7l8vt...</td>
    </tr>
  </tbody>
</table>
</div>



### Stake Assets Associated Addresses
Obtain information about assets associated with addresses of a specific account.</blockquote>


```python
cardano_mainnet.stake_associated_addresses(stake_address)
#or
cardano_mainnet.stake_assets_associated_addresses(stake_address,
                                                  data_order='asc', # Optional: Data order (default: Ascending)
                                                  nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                                  pandas=True) # Optional: Return a pandas dataframe
```
<<<<<<< HEAD

<div>
=======
>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd
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



# Address

### Specific Address
Obtain information about a specific address.


```python
cardano_mainnet.address_info(address)
```




    {'address': 'addr1q8z24xgrlj3m2qjh2vxyqg2fh33y3tegufkll5c4lu8u35gkhpw3h4yhn93ve2whllg0wjazjs5jj8332mgqe332f3uq8m7m6h',
     'amount': [{'unit': 'lovelace', 'quantity': '350000000'}],
     'stake_address': 'stake1uyttshgm6jtejckv48tll58hfw3fg2ffrcc4d5qvcc4yc7q9jsalf',
     'type': 'shelley'}



### Address Details
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
#or
cardano_mainnet.address_utxo(address,
                             pandas=True) # Optional: Return a pandas dataframe
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tx_hash</th>
      <th>tx_index</th>
      <th>output_index</th>
      <th>amount</th>
      <th>block</th>
      <th>data_hash</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>996ff0a57282ef943ecdbc263cf9c41c178d65587d70d9...</td>
      <td>4</td>
      <td>4</td>
      <td>[{'unit': 'lovelace', 'quantity': '350000000'}]</td>
      <td>73768f4ca2a0c96611a1fbd7f53a3b1b573fb0371012e5...</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>



### Address Transactions
Transactions on the address.


```python
cardano_mainnet.address_transaction(address,
                                   pandas=True) # Optional: Return a pandas dataframe
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tx_hash</th>
      <th>tx_index</th>
      <th>block_height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>996ff0a57282ef943ecdbc263cf9c41c178d65587d70d9...</td>
      <td>45</td>
      <td>6095572</td>
    </tr>
  </tbody>
</table>
</div>



## Epoch

### Latest Epoch
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



### Latest Epoch Protocol Parameters
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



### Specific Epoch
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



### Epochs History
Obtain informations about sevrals epochs.


```python
cardano_mainnet.epochs_history([270, 271, 272],
                               pandas=True) # Optional: Return a pandas dataframe
```
<<<<<<< HEAD

<div>
=======
>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd
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



# Pool

### List Of Stake Pools
List of registered stake pools.


```python
cardano_mainnet.registered_polls()
#or
cardano_mainnet.registered_polls(nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                 pandas=True) # Optional: Return a pandas dataframe
```
<<<<<<< HEAD


<div>
=======
>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd
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



### Specific Stake Pool Informations
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



### Stake Pool History

History of stake pool over epochs.


```python
cardano_mainnet.stake_pool_history(pool_id)
#or
cardano_mainnet.stake_pool_history(pool_id,
                                   pandas=True) # Optional: Return a pandas dataframe
```
<<<<<<< HEAD


<div>
=======
>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd
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
      <th>79</th>
      <td>289</td>
      <td>66</td>
      <td>55724573270655</td>
      <td>0.002390</td>
      <td>1443</td>
      <td>47200199605</td>
      <td>808601996</td>
    </tr>
    <tr>
      <th>80</th>
      <td>290</td>
      <td>49</td>
      <td>54675837934319</td>
      <td>0.002351</td>
      <td>1440</td>
      <td>34877628423</td>
      <td>685376284</td>
    </tr>
    <tr>
      <th>81</th>
      <td>291</td>
      <td>54</td>
      <td>54806809508971</td>
      <td>0.002360</td>
      <td>1451</td>
      <td>38286415852</td>
      <td>719464158</td>
    </tr>
    <tr>
      <th>82</th>
      <td>292</td>
      <td>60</td>
      <td>57943587612745</td>
      <td>0.002484</td>
      <td>1451</td>
<<<<<<< HEAD
=======
      <td>0</td>
>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd
      <td>0</td>
    </tr>
    <tr>
      <th>83</th>
      <td>293</td>
      <td>22</td>
      <td>63400551099817</td>
      <td>0.002710</td>
      <td>1440</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



# Assets

### Assets List
List of assets.


```python
cardano_mainnet.assets()
#or
cardano_mainnet.assets(data_order='asc', # Optional: Data order (default: Ascending)
                       nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                       pandas=True) # Optional: Return a pandas dataframe
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>asset</th>
      <th>quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>00000002df633853f6a47465c9496721d2d5b1291b8398...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>83</th>
      <td>293</td>
      <td>15</td>
      <td>63400551099817</td>
      <td>0.002710</td>
      <td>1440</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



# Assets

### Assets List
List of assets.


```python
policy_id='40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c28262fab21728'
asset_name='436c61794e6174696f6e33393836' # (ASCII: ClayNation3986)
```


```python
cardano_mainnet.assets()
#or
cardano_mainnet.assets(data_order='asc', # Optional: Data order (default: Ascending)
                       nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                       pandas=True) # Optional: Return a pandas dataframe
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>asset</th>
      <th>quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>00000002df633853f6a47465c9496721d2d5b1291b8398...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3a9241cd79895e3a8d65261b40077d4437ce71e9d7c8c6...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>02f68378e37af4545d027d0a9fa5581ac682897a3fc1f6...</td>
      <td>1000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>e8e62d329e73190190c3e323fb5c9fb98ee55f0676332b...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ac3f4224723e2ed9d166478662f6e48bae9ddf0fc5ee58...</td>
      <td>10000000</td>
    </tr>
  </tbody>
</table>
</div>



### Specific Asset
Information about a specific asset.
<<<<<<< HEAD


```python
cardano_mainnet.specific_asset(policy_id+asset_name)
```




=======


```python
cardano_mainnet.specific_asset(policy_id+asset_name)
```




>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd
    {'asset': '40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c28262fab21728436c61794e6174696f6e33393836',
     'policy_id': '40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c28262fab21728',
     'asset_name': '436c61794e6174696f6e33393836',
     'fingerprint': 'asset1ay3atwzy3hrdnn74v05jusgsycl344nquyq9nq',
     'quantity': '1',
     'initial_mint_tx_hash': '117f97ccf6e98a16697e7cc205daf2d0bfe83d849a63df2f40d10bef235848e7',
     'mint_or_burn_count': 1,
     'onchain_metadata': {'name': 'Clay Nation #3986',
      'image': 'ipfs://QmYREMX1uTQAFScJD4Xv5tUPnWimKyLzBTBFLv1oCyzMj2',
      'body': 'Brown Clay',
      'eyes': 'Big Eyes',
      'brows': 'Normal Eyebrows',
      'mouth': 'Normal Mouth',
      'Project': 'Clay Nation by Clay Mates',
      'clothes': 'Tshirt Green',
      'background': 'Cyan',
      'accessories': 'Flower Necklace',
      'hats and hair': 'Fringe'},
     'metadata': None}



### Asset History
History of a specific asset.


```python
cardano_mainnet.asset_history(policy_id+asset_name)
#or
cardano_mainnet.asset_history(policy_id+asset_name,
                              data_order='asc', # Optional: Data order (default: Ascending)
                              nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                              pandas=True) # Optional: Return a pandas dataframe
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tx_hash</th>
      <th>action</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>117f97ccf6e98a16697e7cc205daf2d0bfe83d849a63df...</td>
      <td>minted</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Asset Transactions
List of a specific asset transactions.


```python
cardano_mainnet.asset_addresses(policy_id+asset_name)
#or
cardano_mainnet.asset_addresses(policy_id+asset_name,
                                data_order='asc', # Optional: Data order (default: Ascending)
                                nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                pandas=True) # Optional: Return a pandas dataframe
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>address</th>
      <th>quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>addr1qytstx6xt93ux775sg2k5f9l4xfpat8e06mpg8mm7...</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>

<<<<<<< HEAD

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tx_hash</th>
      <th>action</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>117f97ccf6e98a16697e7cc205daf2d0bfe83d849a63df...</td>
      <td>minted</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Asset Transactions
List of a specific asset transactions.
=======


### Assets Of A Specific Policy
>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd

List of asset minted under a specific policy

```python
cardano_mainnet.asset_addresses(policy_id+asset_name)
#or
cardano_mainnet.asset_addresses(policy_id+asset_name,
                                data_order='asc', # Optional: Data order (default: Ascending)
                                nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                pandas=True) # Optional: Return a pandas dataframe
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>address</th>
      <th>quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>addr1qytstx6xt93ux775sg2k5f9l4xfpat8e06mpg8mm7...</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Assets Of A Specific Policy

List of asset minted under a specific policy


```python
cardano_mainnet.assets_policy(policy_id)
#or
cardano_mainnet.assets_policy(policy_id,
                              data_order='asc', # Optional: Data order (default: Ascending)
                              nb_of_results=None, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                              pandas=True) # Optional: Return a pandas dataframe
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>asset</th>
      <th>quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Get Assets Informations
Get the information about the assests under a specific policy.


```python
assets_info, assets_not_found = cardano_mainnet.assets_policy_informations(policy_id, # Policy ID of the project
                                                                           nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                                                           pandas=True) # Optional: Return a pandas dataframe
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>asset</th>
      <th>policy_id</th>
      <th>asset_name</th>
      <th>fingerprint</th>
      <th>quantity</th>
      <th>initial_mint_tx_hash</th>
      <th>mint_or_burn_count</th>
      <th>name</th>
      <th>image</th>
      <th>body</th>
      <th>eyes</th>
      <th>brows</th>
      <th>mouth</th>
      <th>Project</th>
      <th>clothes</th>
      <th>background</th>
      <th>accessories</th>
      <th>hats and hair</th>
      <th>metadata</th>
      <th>wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>436c61794e6174696f6e37383939</td>
      <td>asset1xkngd3y2njd3dzhfg25rtfp66gyvke6skqftxc</td>
      <td>1</td>
      <td>d7e089dce7c170f1af519fab710f9ed5d4d8680978035d...</td>
      <td>1</td>
      <td>Clay Nation #7899</td>
      <td>ipfs://QmdXSPVnjRMsT2LuUMW5MMAKunwjpL34WDWjSy3...</td>
      <td>Tan Clay</td>
      <td>Trippy Eyes</td>
      <td>Blue Eyebrows</td>
      <td>Grin</td>
      <td>Clay Nation by Clay Mates</td>
      <td>Tracksuit</td>
      <td>Seafoam Green</td>
      <td>Silver Chain</td>
      <td>Clay Nation Hat &amp; Mullet</td>
      <td>None</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>436c61794e6174696f6e38343838</td>
      <td>asset14pm7d5k9xtgeu87g7skz8sqvxjkepwsysdmvcg</td>
      <td>1</td>
      <td>a5e9fb001c2a0838d380acccc90eb06f9c06c74ce94eee...</td>
      <td>1</td>
      <td>Clay Nation #8488</td>
      <td>ipfs://QmZfeNhctaLzmpNYAvkaoLcHR3yCvtBn44TNuUL...</td>
      <td>Tan Clay</td>
      <td>Big Eyes</td>
      <td>Normal Eyebrows</td>
      <td>Joint in Mouth</td>
      <td>Clay Nation by Clay Mates</td>
      <td>Tshirt Green</td>
      <td>Cyan</td>
      <td>No Accessories</td>
      <td>Top Hat</td>
      <td>None</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>436c61794e6174696f6e33323332</td>
      <td>asset1lge5ddeauys6emy6mzyduumsrlslm0t6kdm4fj</td>
      <td>1</td>
      <td>befa4ce55af8c4c7691262bb3ffd07eba5c3bdfe9165f2...</td>
      <td>1</td>
      <td>Clay Nation #3232</td>
      <td>ipfs://QmPG4UcamUUfjD5E92B3RMWp5gVe7hUN9ixmamc...</td>
      <td>White Clay</td>
      <td>Normal Eyes</td>
      <td>Pierced Eyebrows</td>
      <td>Pipe</td>
      <td>Clay Nation by Clay Mates</td>
      <td>Tshirt Green</td>
      <td>Salmon</td>
      <td>Silver Chain</td>
      <td>Pigtails</td>
      <td>None</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Data Analysis
___

### Rewards History Analysis
Stake rewards analysis.


```python
cardano_mainnet.rewards_history_analysis(stake_address)
#or
cardano_mainnet.rewards_history_analysis(stake_address,
                                         pandas=True) # Optional: Return a pandas dataframe
```


<<<<<<< HEAD
<div>
=======
```python
cardano_mainnet.assets_policy(policy_id)
#or
cardano_mainnet.assets_policy(policy_id,
                              data_order='asc', # Optional: Data order (default: Ascending)
                              nb_of_results=None, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                              pandas=True) # Optional: Return a pandas dataframe
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>asset</th>
      <th>quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Get Assets Informations
Get informations about the assests under a specific policy.


```python
assets_info, assets_not_found = cardano_mainnet.assets_policy_informations(policy_id, # Policy ID of the project
                                                                           nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                                                           pandas=True) # Optional: Return a pandas dataframe
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>asset</th>
      <th>policy_id</th>
      <th>asset_name</th>
      <th>fingerprint</th>
      <th>quantity</th>
      <th>initial_mint_tx_hash</th>
      <th>mint_or_burn_count</th>
      <th>name</th>
      <th>image</th>
      <th>body</th>
      <th>eyes</th>
      <th>brows</th>
      <th>mouth</th>
      <th>Project</th>
      <th>clothes</th>
      <th>background</th>
      <th>accessories</th>
      <th>hats and hair</th>
      <th>metadata</th>
      <th>wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>436c61794e6174696f6e37383939</td>
      <td>asset1xkngd3y2njd3dzhfg25rtfp66gyvke6skqftxc</td>
      <td>1</td>
      <td>d7e089dce7c170f1af519fab710f9ed5d4d8680978035d...</td>
      <td>1</td>
      <td>Clay Nation #7899</td>
      <td>ipfs://QmdXSPVnjRMsT2LuUMW5MMAKunwjpL34WDWjSy3...</td>
      <td>Tan Clay</td>
      <td>Trippy Eyes</td>
      <td>Blue Eyebrows</td>
      <td>Grin</td>
      <td>Clay Nation by Clay Mates</td>
      <td>Tracksuit</td>
      <td>Seafoam Green</td>
      <td>Silver Chain</td>
      <td>Clay Nation Hat &amp; Mullet</td>
      <td>None</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>436c61794e6174696f6e38343838</td>
      <td>asset14pm7d5k9xtgeu87g7skz8sqvxjkepwsysdmvcg</td>
      <td>1</td>
      <td>a5e9fb001c2a0838d380acccc90eb06f9c06c74ce94eee...</td>
      <td>1</td>
      <td>Clay Nation #8488</td>
      <td>ipfs://QmZfeNhctaLzmpNYAvkaoLcHR3yCvtBn44TNuUL...</td>
      <td>Tan Clay</td>
      <td>Big Eyes</td>
      <td>Normal Eyebrows</td>
      <td>Joint in Mouth</td>
      <td>Clay Nation by Clay Mates</td>
      <td>Tshirt Green</td>
      <td>Cyan</td>
      <td>No Accessories</td>
      <td>Top Hat</td>
      <td>None</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>436c61794e6174696f6e33323332</td>
      <td>asset1lge5ddeauys6emy6mzyduumsrlslm0t6kdm4fj</td>
      <td>1</td>
      <td>befa4ce55af8c4c7691262bb3ffd07eba5c3bdfe9165f2...</td>
      <td>1</td>
      <td>Clay Nation #3232</td>
      <td>ipfs://QmPG4UcamUUfjD5E92B3RMWp5gVe7hUN9ixmamc...</td>
      <td>White Clay</td>
      <td>Normal Eyes</td>
      <td>Pierced Eyebrows</td>
      <td>Pipe</td>
      <td>Clay Nation by Clay Mates</td>
      <td>Tshirt Green</td>
      <td>Salmon</td>
      <td>Silver Chain</td>
      <td>Pigtails</td>
      <td>None</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Data Analysis
___

### Rewards History Analysis
Stake rewards analysis.


```python
cardano_mainnet.rewards_history_analysis(stake_address)
#or
cardano_mainnet.rewards_history_analysis(stake_address,
                                         pandas=True) # Optional: Return a pandas dataframe
```
>>>>>>> f37f8d72c067194f71b7d7335f0d0f332a4f84dd
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
      <td>242</td>
      <td>879367</td>
      <td>1424619058</td>
      <td>pool1u7mqtde27swkarngjsn5mmw3sy20zavlafgqkmg8q...</td>
      <td>1610747091</td>
      <td>1611179091</td>
      <td>1610747091</td>
      <td>1611179076</td>
      <td>21418</td>
      <td>74057</td>
      <td>63148817438049616</td>
      <td>16905060417</td>
      <td>21755094259019945</td>
      <td>35</td>
      <td>60557688009496</td>
      <td>0.002784</td>
      <td>720</td>
      <td>37719841941</td>
      <td>340000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>243</td>
      <td>970119</td>
      <td>1424619058</td>
      <td>pool1u7mqtde27swkarngjsn5mmw3sy20zavlafgqkmg8q...</td>
      <td>1611179091</td>
      <td>1611611091</td>
      <td>1611179091</td>
      <td>1611611090</td>
      <td>21586</td>
      <td>58682</td>
      <td>44531349200446205</td>
      <td>13368193376</td>
      <td>21849089085260375</td>
      <td>40</td>
      <td>60943951290359</td>
      <td>0.002789</td>
      <td>757</td>
      <td>41840863127</td>
      <td>340000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>244</td>
      <td>1164610</td>
      <td>1424619058</td>
      <td>pool1u7mqtde27swkarngjsn5mmw3sy20zavlafgqkmg8q...</td>
      <td>1611611091</td>
      <td>1612043091</td>
      <td>1611611091</td>
      <td>1612043078</td>
      <td>21491</td>
      <td>59591</td>
      <td>29427703690683743</td>
      <td>13516792921</td>
      <td>21956206748623667</td>
      <td>50</td>
      <td>62177721021153</td>
      <td>0.002832</td>
      <td>767</td>
      <td>51169599395</td>
      <td>340000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>245</td>
      <td>1228869</td>
      <td>1425498425</td>
      <td>pool1u7mqtde27swkarngjsn5mmw3sy20zavlafgqkmg8q...</td>
      <td>1612043091</td>
      <td>1612475091</td>
      <td>1612043091</td>
      <td>1612475007</td>
      <td>21485</td>
      <td>88703</td>
      <td>52975770722098664</td>
      <td>20044918510</td>
      <td>22086904770458818</td>
      <td>55</td>
      <td>63400598572150</td>
      <td>0.002871</td>
      <td>784</td>
      <td>54946961660</td>
      <td>340000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>246</td>
      <td>857871</td>
      <td>1426468544</td>
      <td>pool1u7mqtde27swkarngjsn5mmw3sy20zavlafgqkmg8q...</td>
      <td>1612475091</td>
      <td>1612907091</td>
      <td>1612475091</td>
      <td>1612907067</td>
      <td>21327</td>
      <td>142367</td>
      <td>143252676044465523</td>
      <td>31528825577</td>
      <td>22190441040634090</td>
      <td>39</td>
      <td>62762389516418</td>
      <td>0.002828</td>
      <td>790</td>
      <td>38037964874</td>
      <td>340000000</td>
    </tr>
  </tbody>
</table>
</div>



# Developing
Tests run assuming you have set the API key in the environment variable ***BLOCKFROST_API_KEY***, otherwise they will error.


```python
python3 setup.py pytest
```

# Credit
- [Blockfrost API](https://blockfrost.io/).

# Donate

If the project has been useful to you, feel free to put a star or donate (ADA) at this address :blush:.

![Drag Racing](src/qr_donation_50x50.jpg)

Thank you.

# Disclaimer
The project is still under development, If you find bugs or want additional features, open an issue and/or create a pull request.
