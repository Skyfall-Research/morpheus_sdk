# Morpheus SDK

The **Morpheus SDK** provides a high-level, developer-friendly interface for interacting with the Morpheus ControlMart API (the "Backend"). It is designed for two primary audiences:

1.  **Developers** building agents and automations who need a clean Pythonic client.
2.  **Reinforcement Learning (RL) Researchers** who need a Gymnasium-compatible environment to train and test agents.

---

## 1. Installation

To install the SDK and its dependencies (including `gymnasium` and `numpy`):

```bash
pip install git+https://github.com/Skyfall-Research/morpheus_sdk.git
```

Or for local development:

```bash
git clone https://github.com/Skyfall-Research/morpheus_sdk.git
cd morpheus_sdk
uv sync  # or pip install -e .
```

---

## 2. Using the Standard SDK

The standard SDK allows granular control over the Morpheus world via Python objects and methods. This is best for scripted agents, integration tests, or when you need direct access to strict types.

### Initialization

```python
from morpheus_sdk.sdk.morpheus import Morpheus, ModelCreateEnvInputs, ModelChaosConfig

# Initialize with default settings (localhost:8000 or defined via env vars)
sdk = Morpheus()

# Configure Chaos (Optional)
chaos_config = ModelChaosConfig(
    process_chaos_enabled=True, # Enable OD-level random deviations
    infra_chaos_enabled=True    # Enable infrastructure faults (network/db)
)

# Create a new private World
sdk.create(ModelCreateEnvInputs(
    name="Logistics Sim",
    layout="perishables-food-manufacturer",
    chaos=chaos_config
))

print(f"Connected to World ID: {sdk.world_id}")
```

### Core Operations

- **`act`**: Execute an API call against the simulated world.
- **`observe`**: Get the current state (logs, metrics, audit trails).
- **`verify`**: Check if specific conditions are met (e.g., "Did ticket #123 get resolved?").

```python
from morpheus_sdk.sdk.morpheus import ModelActInputs, ModelStateInputs

# 1. Perform an action (e.g., POST /shipments)
sdk.act(ModelActInputs(
    path="/api/v1/shipments",
    method="POST",
    body={"destination": "New York"}
))

# 2. Observe the consequences
state = sdk.observe(ModelStateInputs(include={"logs": True}))
print(state.logs)
```

---

## 3. Using with Gymnasium (RL Compatible)

For Reinforcement Learning, we provide a **Gymnasium** wrapper that makes Morpheus look like a standard RL environment.

### Registration & Make

The environment is registered as `Morpheus-v0`.

```python
import gymnasium as gym
import morpheus_sdk.gym  # Registers 'Morpheus-v0'

env = gym.make("Morpheus-v0")
observation, info = env.reset()

print("Initial Observation Keys:", observation.keys())
```

### Action Space (`spaces.Dict`)

Unlike simple environments with discrete actions (Left/Right), Morpheus is an **API-driven world**. The action space reflects this:

- `path` (Text): The API endpoint to hit (e.g., `/api/v1/user/login`).
- `method` (Text): HTTP verb (`GET`, `POST`, `PUT`, etc.).
- `body` (Text/Object): The payload. In Gym, this is often handled as a JSON string or dictionary.

```python
action = {
    "path": "/world/act",
    "method": "POST",
    "body": {"action": "check_inventory"}
}
obs, reward, terminated, truncated, info = env.step(action)
```

### Observation Space (`spaces.Dict`)

The observation is a JSON representation of the world state.

- `world_id` (Text): The ID of the current simulation instance.
- `raw_state_json` (Text): A serialized JSON string containing the full state returned by `sdk.observe()`. Use `json.loads()` to parse it.

---

## 4. How & Why This is Different

If you are coming from traditional RL environments (CartPole, Atari, MuJoCo), **Morpheus is fundamentally different**.

### A. Continuous & Persistent World (The "Real-Time" Choice)

We deliberately chose **not** to implement a "Turn-Based" (frozen time) architecture.

**Why?**

1.  **Sim-to-Real Gap**: Agents trained in frozen-time environments often fail in production because they cannot handle latency or asynchronous state changes.
2.  **Concurrency**: In a real supply chain, other actors (suppliers, logistics providers) do not pause while you compute your next move.
3.  **Lead Times**: Actions like "Order Inventory" have multi-day lead times. A turn-based system glosses over the complexity of pipeline management.

**Impact on RL**:

- **No Instant Step**: A `step()` triggers an API call, but the _consequence_ (e.g., shipment arrival) happens asynchronously in simulated time.
- **Robustness**: Your agent must be robust to the world changing state _while_ it is computing its next action.

> [!TIP]
> **Need to Pause?**
> While the world is designed to be continuous, you **can** pause it for debugging or stepping through logic manually.
>
> ```python
> # Freeze the business logic (trucks stop moving, orders stop processing)
> env.pause()
> # ... inspect state ...
> env.resume()
> ```
>
> Use this sparingly. Training on a paused world defeats the purpose of learning real-time robustness.

### B. "Reset" Reality

Calling `env.reset()` does **not** instantly "rewind" memory like an emulator.

- It effectively **destroys** the old world and **provisions** a brand new isolated container (or database namespace).
- This limits the frequency of resets compared to lightweight toy environments.

### C. Reward Signal

There is **no default reward function**.

- In a business sim, "success" is subjective (Profit? Speed? Customer Satisfaction?).
- You typically need to wrap `MorpheusEnv` and implement your own reward calculation based on the `raw_state_json` (e.g., `reward = current_capital - previous_capital`).

---

## 5. Hybrid Usage (Advanced)

You can use the Gym interface for the RL loop while accessing the underlying SDK for helper functions or debugging.

```python
import gymnasium as gym
import morpheus_sdk.gym

env = gym.make("Morpheus-v0")
env.reset()

# Access the underlying SDK instance
sdk_client = env.unwrapped.sdk

# Do standard stuff
print(f"The underlying world ID is: {sdk_client.world_id}")

# Do RL stuff
env.step({
    "path": "/some/api",
    "method": "GET"
})
```
