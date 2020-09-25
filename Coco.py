import os
from datetime import datetime
import time
from tendo import singleton
me = singleton.SingleInstance()

url = "https://www.youtube.com/channel/UCS9uQI-jC3DE0L4IpXyvr6w/live"

def getFileName(url):
	now = datetime.now() # current date and time
	date_time = now.strftime("%m-%d-%Y,%H;%M;%S")
	file_name ="COCO_LiveStream_{}.mkv".format(date_time)
	return file_name

stream_test = "streamlink {}".format(url)

if not os.system(stream_test):
    print("Stream is Live")
    file_name = getFileName(url)
    command = "streamlink --hls-live-restart {} best -o {}".format(url, file_name)
    os.system(command)
    print("Stream Saved")
    time.sleep(300)
else:
    print("Waiting for stream to start")