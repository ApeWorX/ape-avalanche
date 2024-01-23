def test_use_provider(accounts, eth_tester_provider):
    _ = eth_tester_provider
    account = accounts.test_accounts[0]
    receipt = account.transfer(account, 100)

    assert not receipt.failed
    assert receipt.value == 100
