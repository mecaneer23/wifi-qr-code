#!/usr/bin/env python3
"""Generate a qrcode to share the current wifi name and password"""

def get_ssid() -> str:
    """Fetch the current wifi ssid"""
    raise NotImplementedError()


def get_password(ssid: str) -> str:
    """Fetch a stored wifi password using the current wifi name"""
    raise NotImplementedError()


def create_wifi_string(ssid: str, password: str) -> str:
    """Create a qr-code readable wifi string"""
    return f"WIFI:T:WPA;S:{ssid};P:{password};;"


def print_qrcode(string: str) -> None:
    """Print a qrcode holding `string`"""
    raise NotImplementedError()


def main() -> None:
    """Entry point"""
    name = get_ssid()
    print_qrcode(create_wifi_string(name, get_password(name)))


if __name__ == "__main__":
    main()
