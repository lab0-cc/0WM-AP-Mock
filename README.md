# 0WM AP Mock

The 0WM AP Mock is a simple mock access point for 0WM.

It mimics the API of a Zyxel NWA50AX running OpenWRT with our [OpenWRT configuration](https://github.com/lab0-cc/0WM-AP-OpenWRT). This allows you to test the [0WM Client](https://github.com/lab0-cc/0WM-Client) and [0WM Server](https://github.com/lab0-cc/0WM-Server) without needing actual hardware.

## Usage

The mock AP is a lightweight Python HTTP server that can simply be tested with:

```bash
python3 server.py 8003
```

## Integration

Use this mock when running the 0WM Client in the browser emulator.

1. Run this mock on port 8003.
2. Configure the server to treat `http://localhost:8003` as the AP.
3. The mock will serve standard CGI scripts (`/cgi-bin/info`, `/cgi-bin/scan`) that return fake Wi-Fi measurement data.

**Note:** This is for development only. For real surveys, you must use a physical access point.
