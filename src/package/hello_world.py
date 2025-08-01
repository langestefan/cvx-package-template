"""A Sample Python file."""


def hello_world(i: int = 0) -> str:
    """Doc String."""
    return f"string-{i}"


def good_night() -> str:
    """Doc String."""
    return "string"


def hello_goodbye() -> None:
    """Doc String."""
    hello_world(1)
    good_night()
