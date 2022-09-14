# Python Cardano Explorer ![PyPI - Python Version](https://img.shields.io/badge/python-%3E%3D3.8-blue) ![PyPI - Python Version](https://img.shields.io/badge/pypi%20package-v0.6--beta.0-green)

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
mainnet = blockfrost_api.Auth() # mainnet by default
#or
preprod = blockfrost_api.Auth(network='preprod')
#or
preview = blockfrost_api.Auth(network='preview')
#or
legacy = blockfrost_api.Auth(network='testnet')
```

## Quickstart

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

# Documentation

The official documentation is hosted on [GitHub](https://github.com/djessy-atta/py-cardano-explorer).

# Credit

- [Blockfrost API](https://blockfrost.io/).

# Disclaimer

The project is still under development, If you find bugs or want additional features, open an issue and/or create a pull request.
