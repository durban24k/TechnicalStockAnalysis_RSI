import websocket, numpy as np,json,pprint,talib,pandas as pd,matplotlib.pyplot as plt
from datetime import datetime

SOCKET="wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

def on_open(ws):
     print('Connection Open') 

def on_close(ws):
     print("Connection Closed")

def on_message(ws,message):
     json_message=json.loads(message)
     close=json_message['k']['c']
     epoch_time=json_message['E']
     dt_time=datetime.fromtimestamp(epoch_time/1000)
     data=pd.DataFrame()
     data['Time']=dt_time.time()
     data['Close']=close

     plt.figure(figsize=(15,8))

     plt.plot(data['Time'],data['Close'],color='lightgray')
     plt.set_title("Adjusted Close Price",color="white")
     plt.show()

ws=websocket.WebSocketApp(SOCKET,on_open=on_open,on_close=on_close,on_message=on_message)
ws.run_forever()