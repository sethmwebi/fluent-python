from typing import Union


def parse_token(token: str) -> str | float:
    try:
        return float(token)
    except ValueError:
        return token
