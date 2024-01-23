from typing import cast

from ape_ethereum.ecosystem import (
    BaseEthereumConfig,
    Ethereum,
    NetworkConfig,
    create_network_config,
)

NETWORKS = {
    # chain_id, network_id
    "mainnet": (43114, 43114),
    "fuji": (43113, 43113),
}


class AvalancheConfig(BaseEthereumConfig):
    mainnet: NetworkConfig = create_network_config(block_time=3, required_confirmations=1)
    fuji: NetworkConfig = create_network_config(block_time=3, required_confirmations=1)


class Avalanche(Ethereum):
    fee_token_symbol: str = "AVAX"

    @property
    def config(self) -> AvalancheConfig:  # type: ignore
        return cast(AvalancheConfig, self.config_manager.get_config("avalanche"))
