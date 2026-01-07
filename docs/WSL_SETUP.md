# Running OM1 on Windows (via WSL)

This guide describes how to set up and run the OM1 stack on a Windows machine using WSL2.

## Prerequisites
1.  **Install WSL2**: Run `wsl --install` in PowerShell as Admin.
2.  **Install Ubuntu**: Ensure you are running Ubuntu 22.04+.

## Quick Start

### 1. Install uv
```bash
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
source $HOME/.local/bin/env

