#!/usr/bin/env python3
"""Send a WebSocket ping carrying only a name and an ID.

Usage:
    python3 ping.py
"""

import argparse
import asyncio

import websockets

SERVER_IP = "10.50.52.215"
PORT = 8765
MESSAGE = "Akshat Gupta 12340160"


async def ping(host, port):
    uri = f"ws://{host}:{port}"
    async with websockets.connect(uri) as websocket:
        print(f"Connected to {uri}")
        await websocket.send(MESSAGE)
        print(f"Sent: {MESSAGE}")
        try:
            reply = await asyncio.wait_for(websocket.recv(), timeout=10)
            print(f"Reply: {reply}")
        except asyncio.TimeoutError:
            print("No reply within 10s (the server may not send one).")


parser = argparse.ArgumentParser(description="WebSocket ping with name and ID.")
parser.add_argument("--host", default=SERVER_IP)
parser.add_argument("--port", type=int, default=PORT)
args = parser.parse_args()

asyncio.run(ping(args.host, args.port))
