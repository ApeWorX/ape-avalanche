from ape import plugins


@plugins.register(plugins.Config)
def config_class():
    from ape_avalanche.ecosystem import AvalancheConfig

    return AvalancheConfig


@plugins.register(plugins.EcosystemPlugin)
def ecosystems():
    from ape_avalanche.ecosystem import Avalanche

    yield Avalanche


@plugins.register(plugins.NetworkPlugin)
def networks():
    from ape.api.networks import (
        LOCAL_NETWORK_NAME,
        ForkedNetworkAPI,
        NetworkAPI,
        create_network_type,
    )

    from ape_avalanche.ecosystem import NETWORKS

    for network_name, network_params in NETWORKS.items():
        yield "avalanche", network_name, create_network_type(*network_params)
        yield "avalanche", f"{network_name}-fork", ForkedNetworkAPI

    # NOTE: This works for development providers, as they get chain_id from themselves
    yield "avalanche", LOCAL_NETWORK_NAME, NetworkAPI


@plugins.register(plugins.ProviderPlugin)
def providers():
    from ape.api.networks import LOCAL_NETWORK_NAME
    from ape_node import Node
    from ape_test import LocalProvider

    from ape_avalanche.ecosystem import NETWORKS

    for network_name in NETWORKS:
        yield "avalanche", network_name, Node

    yield "avalanche", LOCAL_NETWORK_NAME, LocalProvider


def __getattr__(name: str):
    if name == "NETWORKS":
        from ape_avalanche.ecosystem import NETWORKS

        return NETWORKS

    elif name == "Avalanche":
        from ape_avalanche.ecosystem import Avalanche

        return Avalanche

    elif name == "AvalancheConfig":
        from ape_avalanche.ecosystem import AvalancheConfig

        return AvalancheConfig

    else:
        raise AttributeError(name)


__all__ = ["NETWORKS", "Avalanche", "AvalancheConfig"]
