def test_gas_limit(networks):
    avalanche = networks.avalanche
    assert avalanche.config.local.gas_limit == "max"
