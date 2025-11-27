"""
Publishing logic to pipeline systems.
"""

class AssetPublisher:
    def publish(self, name, version, path):
        print(f"Publishing {name}_v{version} to {path}")
