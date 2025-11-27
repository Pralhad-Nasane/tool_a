"""
Utility functions for Tool A.
"""

def normalize_name(name):
    return name.strip().lower().replace(" ", "_")

def get_next_version(existing_versions):
    return max(existing_versions) + 1 if existing_versions else 1
