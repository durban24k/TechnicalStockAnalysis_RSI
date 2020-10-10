import websocket,json
from datetime import datetime

SOCKET="wss://stream.binance.com:9443/ws/ethusdt@kline_1m"
dt_time=""
close=""

def on_open(ws):
     print('Connection Open') 

def on_close(ws):
     print("Connection Closed")

def on_message(ws,message):
    global dt_time,close
    json_message=json.loads(message)
    close=json_message['k']['c']
    dt_time=datetime.fromtimestamp(json_message['E']/1000).strftime("%X")
    print(dt_time,close)

ws=websocket.WebSocketApp(SOCKET,on_open=on_open,on_close=on_close,on_message=on_message)
ws.run_forever()