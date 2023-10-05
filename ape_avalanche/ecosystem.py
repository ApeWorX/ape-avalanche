from typing import Optional, cast

from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.utils import DEFAULT_LOCAL_TRANSACTION_ACCEPTANCE_TIMEOUT
from ape_ethereum.ecosystem import Ethereum, NetworkConfig
from ape_ethereum.transactions import TransactionType

NETWORKS = {
    # chain_id, network_id
    "mainnet": (43114, 43114),
    "fuji": (43113, 43113),
}


def _create_network_config(
    required_confirmations: int = 1, block_time: int = 3, default_provider="geth", **kwargs
) -> NetworkConfig:
    return NetworkConfig(
        block_time=block_time,
        required_confirmations=required_confirmations,
        default_transaction_type=TransactionType.DYNAMIC,
        default_provider=default_provider,
        **kwargs,
    )


def _create_local_config(default_provider: Optional[str] = None, **kwargs) -> NetworkConfig:
    return _create_network_config(
        block_time=0,
        default_provider=default_provider,
        gas_limit="max",
        required_confirmations=0,
        transaction_acceptance_timeout=DEFAULT_LOCAL_TRANSACTION_ACCEPTANCE_TIMEOUT,
        **kwargs,
    )


class AvalancheConfig(PluginConfig):
    mainnet: NetworkConfig = _create_network_config()
    mainnet_fork: NetworkConfig = _create_local_config()
    fuji: NetworkConfig = _create_network_config()
    fuji_fork: NetworkConfig = _create_local_config()
    local: NetworkConfig = _create_local_config(default_provider="test")
    default_network: str = LOCAL_NETWORK_NAME


class Avalanche(Ethereum):
    @property
    def config(self) -> AvalancheConfig:  # type: ignore
        return cast(AvalancheConfig, self.config_manager.get_config("avalanche"))
