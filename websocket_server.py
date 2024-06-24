# websocket_server.py
import asyncio
import websockets
import random
import json

WS_PORT = 6790  # 使用するポート番号

async def random_coordinates_sender(websocket, path):
    print("Client connected")  # 接続確認のログ
    try:
        while True:
            x = random.randint(0, 800)  # キャンバスの幅に合わせて値を調整
            y = random.randint(0, 600)  # キャンバスの高さに合わせて値を調整
            coordinates = {'x': x, 'y': y}
            print(f"Sending coordinates: {coordinates}")  # 送信データのログ
            await websocket.send(json.dumps(coordinates))  # JSON形式で送信
            await asyncio.sleep(1)  # 1秒ごとに座標を送信
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    async with websockets.serve(random_coordinates_sender, "localhost", WS_PORT):
        print(f"WebSocket server is listening on ws://localhost:{WS_PORT}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())

