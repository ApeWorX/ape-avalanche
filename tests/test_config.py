from ape_ethereum.transactions import TransactionType

from ape_avalanche.ecosystem import AvalancheConfig


def test_gas_limit(avalanche):
    assert avalanche.config.local.gas_limit == "max"


def test_default_transaction_type(avalanche):
    assert avalanche.config.mainnet.default_transaction_type == TransactionType.DYNAMIC


def test_mainnet_fork_not_configured():
    obj = AvalancheConfig.model_validate({})
    assert obj.mainnet_fork.required_confirmations == 0


def test_mainnet_fork_configured():
    data = {"mainnet_fork": {"required_confirmations": 555}}
    obj = AvalancheConfig.model_validate(data)
    assert obj.mainnet_fork.required_confirmations == 555


def test_custom_network():
    data = {"apenet": {"required_confirmations": 333}}
    obj = AvalancheConfig.model_validate(data)
    assert obj.apenet.required_confirmations == 333
