from interactions import Client, Extension
from typing import Optional
from typing_extensions import Self


class interactionsColor(Extension):
    """
    A Class Color
    """
    @classmethod
    def green(cls) -> Self:
        """Returns green"""
        return int("3066993")

def setup() -> Optional[Extension]:
    return interactionsColor