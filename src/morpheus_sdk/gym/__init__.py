from gymnasium.envs.registration import register

register(
    id="Morpheus-v0", 
    entry_point="morpheus_sdk.gym.env:MorpheusEnv"
)
