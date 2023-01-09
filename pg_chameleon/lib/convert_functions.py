from typing import Optional


def microseconds_to_seconds(value: str) -> Optional[str]:

    if value is None:
        result = None
    else:
        result= str(int(value) / 1_000_000)
    return result
