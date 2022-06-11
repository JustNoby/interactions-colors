from interactions import Extension
from typing import Optional
from typing_extensions import Self
import random


class interactionsColor(Extension):
    """
    A Class Color
    """

    @classmethod
    def random(cls) -> Self:
        return int(''.join([random.choice('ABCDEF0123456789') for i in range(6)]), 16)

    @classmethod
    def default(cls) -> Self:
        """Returns defualt color"""
        return 0

    @classmethod
    def aqua(cls) -> Self:
        """Returns aqua color"""
        return 1752220

    @classmethod
    def dark_aqua(cls) -> Self:
        """Returns dark aqua color"""
        return 1146986

    @classmethod
    def dark_green(cls) -> Self:
        """Returns dark green color"""
        return 2067276

    @classmethod
    def blue(cls) -> Self:
        """Returns blue color"""
        return 3447003

    @classmethod
    def dark_blue(cls) -> Self:
        """Returns dark blue color"""
        return 2123412
    
    @classmethod
    def purple(cls) -> Self:
        """Returns purple color"""
        return 10181046

    @classmethod
    def gold(cls) -> Self:
        """Returns gold color"""
        return 15844367

    @classmethod
    def dark_purple(cls) -> Self:
        """Returns dark purple color"""
        return 7419530

    @classmethod
    def green(cls) -> Self:
        """Returns green color"""
        return 3066993

    @classmethod
    def dark_gold(cls) -> Self:
        """Returns dark gold color"""
        return 12745742

    @classmethod
    def orange(cls) -> Self:
        """Returns orange color"""
        return 15105570

    @classmethod
    def dark_orange(cls) -> Self:
        return 11027200
    
    @classmethod
    def red(cls) -> Self:
        """Returns red color"""
        return 15158332

    @classmethod
    def dark_red(cls) -> Self:
        """Returns dark red color"""
        return 10038562

    @classmethod
    def grey(cls) -> Self:
        """Returns grey color"""
        return 9807270

    @classmethod
    def grey_but_darker(cls) -> Self:
        """Returns dark grey color"""
        return 8359053

    @classmethod
    def grey_but_lighter(cls) -> Self:
        """Returns light grey"""
        return 12370112

    @classmethod
    def navy(cls) -> Self:
        """Returns navy color"""
        return 3426654

    @classmethod
    def dark_navy(cls) -> Self:
        """Returns dark navy color"""
        return 2899536
    
    @classmethod
    def yellow(cls) -> Self:
        """Returns ugly color, aka yellow"""
        return 16776960

    @classmethod
    def white(cls) -> Self:
        """Returns white color"""
        return 16777215

    @classmethod
    def blurple(cls) -> Self:
        """Returns blurple color"""
        return 5793266
    
    @classmethod
    def greyple(cls) -> Self:
        """Returns greyple color?"""
        return 10070709
    
    @classmethod
    def not_black_but_dark(cls) -> Self:
        """Returns a dark, not black color"""
        return 2895667

    @classmethod
    def not_black_but_black(cls) -> Self:
        """Returns a dark color"""
        return 2303786

    @classmethod
    def black(cls) -> Self:
        """Returns a black color"""
        return 2303786

def setup() -> Optional[Extension]:
    return interactionsColor