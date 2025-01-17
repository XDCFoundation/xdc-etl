import os

from web3 import HTTPProvider

from xdcetl.providers.rpc import BatchHTTPProvider
from tests.xdcetl.job.mock_batch_web3_provider import MockBatchWeb3Provider
from tests.xdcetl.job.mock_web3_provider import MockWeb3Provider


def get_web3_provider(provider_type, read_resource_lambda=None, batch=False):
    if provider_type == 'mock':
        if read_resource_lambda is None:
            raise ValueError('read_resource_lambda must not be None for provider type mock'.format(provider_type))
        if batch:
            provider = MockBatchWeb3Provider(read_resource_lambda)
        else:
            provider = MockWeb3Provider(read_resource_lambda)
    elif provider_type == 'infura':
        provider_url = os.environ.get('PROVIDER_URL', 'https://mainnet.infura.io/v3/7aef3f0cd1f64408b163814b22cc643c')
        if batch:
            provider = BatchHTTPProvider(provider_url)
        else:
            provider = HTTPProvider(provider_url)
    elif provider_type == 'goerli':
        provider_url = os.environ.get('GOERLI_PROVIDER_URL', 'https://goerli.infura.io/v3/7aef3f0cd1f64408b163814b22cc643c')
        if batch:
            provider = BatchHTTPProvider(provider_url)
        else:
            provider = HTTPProvider(provider_url)
    else:
        raise ValueError('Provider type {} is unexpected'.format(provider_type))
    return provider
