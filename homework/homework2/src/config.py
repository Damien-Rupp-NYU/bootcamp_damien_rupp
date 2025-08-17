import os
from typing import Optional

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    print("get key was imported")
    return os.getenv(name, default)