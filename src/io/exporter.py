"""
Export logic for USD and Alembic formats.
"""

class USDExporter:
    def export(self, data, path):
        print(f"Exporting to USD at {path}")

class AlembicExporter:
    def export(self, data, path):
        print(f"Exporting to Alembic at {path}")
