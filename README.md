## Server

### For windows

```shell
python -m venv venv
pip install -r requirements.txt
.\venv\Scripts\Activate.ps1
python src\server.py
```

### Send

```json
{
  "host_address": "0.0.0.0",
  "target_address": "localhost",
  "port": 8080,
  "buffer_size": 1024,
  "timeout": 1.0
}
```

プロジェクトに`config.json`を作る。

```python
import json

config = json.load(open("config.json"))


def get(key: str, default):
    if key in config:
        return config[key]
    return default


def get_host_address():
    return get("host_address", "localhost")


def get_target_address():
    return get("target_address", "localhost")


def get_port():
    return get("port", 8080)


def get_buffer_size():
    return get("buffer_size", 1024)


def get_timeout():
    return get("timeout", 1)

```

上を`config_loader.py`として保存する。

```python
import socket

import config_loader as config

server_ip = config.get_target_address()
server_port = config.get_port()
server_addr_port = (server_ip, server_port)

def send(message):
    bytes_to_send = str.encode(message)
    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_client_socket.sendto(bytes_to_send, server_addr_port)
```

上を`send.py`と保存する。