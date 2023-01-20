# Quick Start

Ecosystem Plugin for Avalanche (C-Chain) support in Ape

## Dependencies

- [python3](https://www.python.org/downloads) version 3.8 or greater, python3-dev

## Installation

### via `ape`

You can install this plugin using `ape`:

```bash
ape plugins install avalanche
```

or via config file:

```yaml
# ape-config.yaml
plugins:
  - name: avalanche
```

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-avalanche
```

### via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/ApeWorX/ape-avalanche.git
cd ape-avalanche
python3 setup.py install
```

## Quick Usage

Installing this plugin adds support for the Avalanche ecosystem:

```bash
ape console --network avalanche:mainnet
```

## Development

This project is in development and should be considered a beta.
Things might not be in their final state and breaking changes may occur.
Comments, questions, criticisms and pull requests are welcomed.
