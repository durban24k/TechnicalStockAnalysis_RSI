# import matplotlib.pyplot as plt,matplotlib.animation as animation
import websocket_data

websocket_data.ws.runforever()

# times=[]
# closes=[]



# fig=plt.figure()
# ax=fig.add_subplot(1,1,1)


# def animate(i):
#     global dt_time,close,times,closes
    
#     times.append(dt_time)
#     closes.append(close)

#     times=times[-24:]
#     closes=closes[-24:]

#     ax.clear()
#     ax.plot(times,closes,color='lightgray')
#     plt.title("Adjusted Close Price",color="white")

# ani=animation.FuncAnimation(fig,animate,interval=2000)
# plt.show()