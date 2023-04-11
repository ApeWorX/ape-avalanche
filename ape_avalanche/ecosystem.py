from typing import Optional

from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_ethereum.ecosystem import Ethereum, NetworkConfig

NETWORKS = {
    # chain_id, network_id
    "mainnet": (43114, 43114),
    "fuji": (43113, 43113),
}


def _create_network_config(
    required_confirmations: int = 1, block_time: int = 2, **kwargs
) -> NetworkConfig:
    return NetworkConfig(
        required_confirmations=required_confirmations, block_time=block_time, **kwargs
    )


def _create_local_config(default_provider: Optional[str] = None) -> NetworkConfig:
    return _create_network_config(
        required_confirmations=0, block_time=0, default_provider=default_provider
    )


class AvalancheConfig(PluginConfig):
    mainnet: NetworkConfig = _create_network_config()
    mainnet_fork: NetworkConfig = _create_local_config()
    fuji: NetworkConfig = _create_network_config()
    fuji_fork: NetworkConfig = _create_local_config()
    local: NetworkConfig = NetworkConfig(default_provider="test")
    default_network: str = LOCAL_NETWORK_NAME


class Avalanche(Ethereum):
    @property
    def config(self) -> AvalancheConfig:  # type: ignore
        return self.config_manager.get_config("avalanche")  # type: ignore
