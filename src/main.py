"""
Main entry point for the Tool A application.
"""

from core.processor import GeometryProcessor
from pipelines.publisher import AssetPublisher

def main():
    data = {"name": "Character_GEO"}
    processor = GeometryProcessor()
    processed = processor.process(data)

    publisher = AssetPublisher()
    publisher.publish(name="character", version=1, path="/project/assets/character.usd")

if __name__ == "__main__":
    main()
