# Morpheus SDK

The Morpheus SDK provides a high-level, developer-friendly interface for interacting with the Morpheus ControlMart API. It allows agents and developers to create simulation environments ("Worlds"), perform actions, observe state, verify outcomes, and manage tasks.

## Installation

To install from GitHub:
```bash
pip install git+https://github.com/TalkShopClub/morpheus_sdk.git
```

Or for development:
```bash
git clone https://github.com/TalkShopClub/morpheus_sdk.git
cd morpheus_sdk
uv sync
```

## Quick Start

```python
from morpheus_sdk.sdk.morpheus import Morpheus, ModelCreateEnvInputs

# Initialize the SDK
sdk = Morpheus()

# Create a new private World environment
env_output = sdk.create(ModelCreateEnvInputs(
    name="My Simulation",
    description="Testing agent behavior",
    real_hours_per_sim_day=24
))

print(f"World created: {sdk.world_id}")
```

## Core Concepts

The SDK is built around the `Morpheus` class (and its async counterpart `AsyncMorpheus`). This class manages the connection to the backend and maintains the context of the current `world_id`.

### Initialization
You can initialize the SDK with custom settings or an existing `world_id`.

```python
from morpheus_sdk.sdk.morpheus import Morpheus, ModelHttpClientInputs

settings = ModelHttpClientInputs(base_url="http://localhost:8000")
sdk = Morpheus(settings=settings, world_id="existing-world-id")
```

## API Reference

### 1. Environment Management (`create`, `delete`, `reset`)

Manage the lifecycle of your simulation world.

**Create a World:**
```python
from morpheus_sdk.sdk.morpheus import ModelCreateEnvInputs

output = sdk.create(ModelCreateEnvInputs(
    name="Logistics Sim",
    layout="Standard Warehouse"
))
```

**Reset World:**
Resets the current world to its initial state.
```python
sdk.reset()
```

**Delete World:**
Deletes the current world.
```python
sdk.delete()
```

### 2. Action Space (`action_space`)

Discover available actions and retrieve trajectory details.

**Get Service Documentation:**
```python
from morpheus_sdk.sdk.morpheus import ModelActionSpaceMeshDocsInputs

docs = sdk.action_space(ModelActionSpaceMeshDocsInputs(
    service="tms",
    method="POST"
))
```

**Get Trajectory (OD):**
```python
from morpheus_sdk.sdk.morpheus import ModelActionSpaceTrajectoryInputs

traj = sdk.action_space(ModelActionSpaceTrajectoryInputs(
    od_id="trajectory-id"
))
```

### 3. Act (`act`)

Execute actions within the simulated environment.

```python
from morpheus_sdk.sdk.morpheus import ModelActInputs

observation = sdk.act(ModelActInputs(
    path="/api/v1/shipments",
    method="POST",
    body={"destination": "New York"}
))
```

### 4. Observe (`observe`)

Retrieve the current state of the world, including audit logs and operational logs.

```python
from morpheus_sdk.sdk.morpheus import ModelStateInputs

state = sdk.observe(ModelStateInputs(
    include={"audit_log": True, "logs": True},
    limit=50
))
```

### 5. Verify (`verify`)

Verify the state of specific entities or tickets.

**Verify a Ticket:**
```python
from morpheus_sdk.sdk.morpheus import ModelVerifyTicketInputs

result = sdk.verify(ModelVerifyTicketInputs(
    ticket_id="ticket-123"
))
```

**Verify an Entity:**
```python
from morpheus_sdk.sdk.morpheus import ModelVerifyEntityInputs

result = sdk.verify(ModelVerifyEntityInputs(
    od_id="flow-1",
    entity_id="shipment-555",
    entity_type="shipment"
))
```

### 6. Tasks (`task`)

List or retrieve ITSM tasks assigned to the world.

```python
from morpheus_sdk.sdk.morpheus import ModelTaskInputs

# List all tasks
tasks = sdk.task(ModelTaskInputs())

# Filter tasks
# (See ModelTaskFilters for advanced filtering)
```

## Async Support

The SDK provides first-class support for `asyncio` via `AsyncMorpheus`.

```python
import asyncio
from morpheus_sdk.sdk.morpheus import AsyncMorpheus, ModelCreateEnvInputs

async def main():
    sdk = AsyncMorpheus()
    await sdk.connect() # Optional explicit connection check
    
    await sdk.create(ModelCreateEnvInputs(name="Async World"))
    print(f"World: {sdk.world_id}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Models & Exports

All necessary classes and models are exported from `morpheus_sdk.sdk.morpheus`.

```python
from morpheus_sdk.sdk.morpheus import (
    Morpheus, 
    AsyncMorpheus,
    Client,
    ModelCreateEnvInputs,
    ModelActInputs,
    ModelStateInputs,
    ModelVerifyInputs,
    ModelTaskInputs,
    ModelActionSpaceInputs
)
```
