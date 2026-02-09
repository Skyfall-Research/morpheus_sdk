import pytest
import gymnasium as gym


import morpheus_sdk.gym  # Registration
from morpheus_sdk.sdk.morpheus import ModelHttpClientInputs

@pytest.mark.integration
def test_live_gym_cycle():
    print("Starting Live Gym Cycle Test...")
    
    # Configure to connect to local server
    # Assuming server running on 8282 from user context
    settings = ModelHttpClientInputs(base_url="http://localhost:8282")
    
    # Initialize Environment
    # strict=True/False depends on gym version, but mainly we pass sdk_settings
    env = gym.make("Morpheus-v0", sdk_settings=settings)
    
    print("1. Environment created.")
    
    # Reset (Create World)
    try:
        obs, info = env.reset()
        print(f"2. Reset successful. World ID: {obs.get('world_id')}")
        assert obs.get("world_id"), "World ID should be present"
    except Exception as e:
        print(f"2. Reset FAILED: {e}")
        return

    # Step (Act)
    # Perform a safe read-only action: Get World Info
    # Route: GET /world/{world_id} which is handled by controlmart
    world_id = obs["world_id"]
    action = {
        "path": f"/world/{world_id}",
        "method": "GET",
        "body": {}
    }
    
    try:
        obs, reward, terminated, truncated, info = env.step(action)
        print("3. Step successful.")
        
        # Verify Action Result
        last_result = info.get("last_action_result", {})
        print(f"   Last Action Status: {last_result.get('status')}")
        
        if last_result.get("status") == 200:
            print("   Action returned 200 OK.")
        else:
            print(f"   Action failed or unexpected status: {last_result}")
            
    except Exception as e:
        print(f"3. Step FAILED: {e}")

    # Close
    env.close()
    print("4. Environment closed.")

if __name__ == "__main__":
    test_live_gym_cycle()
