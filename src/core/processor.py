"""
Core geometry and material processing logic.
"""

class GeometryProcessor:
    def process(self, data):
        data["processed"] = True
        data["note"] = "Processed successfully"
        return data

class MaterialAssigner:
    def assign(self, data, material):
        data["material"] = material
        return data
