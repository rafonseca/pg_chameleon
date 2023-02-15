from typing import Optional


def microseconds_to_seconds(value: str) -> Optional[str]:
    if value=="NULL":
        return "NULL"
    elif isinstance(value,str) and value.startswith('"') and value.endswith('"'):
        result = f'"{str(int(value[1:-1]) / 1_000_000)}"'
    elif value is None:
        result = None
    else:
        result= str(int(value) / 1_000_000)
    return result
