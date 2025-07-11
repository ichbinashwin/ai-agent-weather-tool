import os
from pathlib import Path

def is_running_in_docker() -> bool:
    return Path("/.dockerenv").exists()
