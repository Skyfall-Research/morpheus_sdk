import unittest
import os
import pytest
from uuid import uuid4

@pytest.mark.integration

from morpheus_sdk.sdk.morpheus import (
    Morpheus, 
    ModelCreateEnvInputs,
    ModelChaosConfig
)

class TestChaosIntegration(unittest.TestCase):
    def setUp(self):
        self.sdk = Morpheus()
        if os.environ.get("MORPHEUS_API_URL"):
             self.sdk.settings.base_url = os.environ.get("MORPHEUS_API_URL")
             print(f"Using API URL: {self.sdk.settings.base_url}")
        self.created_world_id = None

    def tearDown(self):
        if self.created_world_id:
            try:
                self.sdk.world_id = self.created_world_id
                self.sdk.delete()
                print(f"Deleted world: {self.created_world_id}")
            except Exception as e:
                print(f"Teardown failed to delete world {self.created_world_id}: {e}")

    def test_create_world_with_chaos(self):
        print("\n[Chaos] Testing Create World with Chaos Config...")
        
        chaos_config = ModelChaosConfig(
            process_chaos_enabled=True,
            infra_chaos_enabled=True
        )
        
        create_input = ModelCreateEnvInputs(
            name=f"Chaos Test World {uuid4()}",
            description="Integration test world for chaos config",
            layout="perishables-food-manufacturer",
            real_hours_per_sim_day=1,
            chaos=chaos_config
        )
        
        try:
            result = self.sdk.create(create_input)
        except Exception as e:
            self.fail(f"SDK create call failed: {e}")
        
        if not result.data:
            self.fail("Create returned no data")

        self.created_world_id = self.sdk.world_id
        self.assertIsNotNone(self.created_world_id)
        
        # Verify chaos config in response
        world_data = result.data.get("world", {})
        chaos_out = world_data.get("chaos")
        
        print(f"Returned Chaos Config: {chaos_out}")
        
        self.assertIsNotNone(chaos_out, "Chaos config missing in response")
        self.assertTrue(chaos_out.get("processChaosEnabled"), "processChaosEnabled should be True")
        self.assertTrue(chaos_out.get("infraChaosEnabled"), "infraChaosEnabled should be True")

if __name__ == "__main__":
    unittest.main()
