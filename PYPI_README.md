# Python Cardano Explorer ![PyPI - Python Version](https://img.shields.io/badge/python-%3E%3D3.8-blue) ![PyPI - Python Version](https://img.shields.io/badge/pypi%20package-v0.1--beta.6-green) 

Python wrapper for accessing and processing information stored on the Cardano blockchain using [Blockfrost API](https://blockfrost.io/).


## Install 

```python
pip install cardano_explorer
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
      'circulating': '32854605043085013',
      'locked': '11030148142156',
      'treasury': '630037263793143',
      'reserves': '11793690427914625'},
     'stake': {'live': '23374530755001598', 'active': '23395112387185878'}}


# Credit
- [Blockfrost API](https://blockfrost.io/).

# Donate

If this wrapper has been useful to you, feel free to put a star or donate (ADA) at this address.

![wallet address](https://github.com/djessy-atta/py-cardano-explorer/raw/main/src/img/qr_donation_50x50.jpg)

Thank you.

# Disclaimer
The project is still under development, If you find bugs or want additional features, open an issue and/or create a pull request.
