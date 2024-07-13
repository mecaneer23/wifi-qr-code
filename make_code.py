#!/usr/bin/env python3
"""Generate a qrcode to share the current wifi name and password"""

try:
    from qrcode.main import QRCode

    QRCODE_EXISTS = True
except ModuleNotFoundError:
    QRCODE_EXISTS = False  # pyright: ignore[reportConstantRedefinition]


def get_ssid() -> str:
    """Fetch the current wifi ssid"""
    raise NotImplementedError()


def get_password(ssid: str) -> str:
    """Fetch a stored wifi password using the current wifi name"""
    raise NotImplementedError()


def create_wifi_string(ssid: str, password: str) -> str:
    """Create a qr-code readable wifi string"""
    return f"WIFI:T:WPA;S:{ssid};P:{password};;"


def print_qrcode(data: str) -> None:
    """Print a qrcode holding `string`"""
    if not QRCODE_EXISTS:
        print("`qrcode` not installed: run `pip install qrcode`")
        return
    qr = QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    qr.print_ascii(invert=True)


def main() -> None:
    """Entry point"""
    name = get_ssid()
    print_qrcode(create_wifi_string(name, get_password(name)))


if __name__ == "__main__":
    main()
