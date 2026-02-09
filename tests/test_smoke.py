import unittest
from morpheus_sdk.sdk.morpheus import Morpheus

class TestSmoke(unittest.TestCase):
    def test_import(self):
        """Verify that the SDK can be imported and instantiated (smoke test)."""
        try:
            sdk = Morpheus()
            self.assertIsInstance(sdk, Morpheus)
        except Exception as e:
            self.fail(f"Failed to instantiate Morpheus SDK: {e}")

if __name__ == "__main__":
    unittest.main()
