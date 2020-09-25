import schedule
import time
import os

def job():
    print("Running")
    os.system("python3 Coco.py")

schedule.every().hour.at("00:00").do(job)
schedule.every().hour.at("01:00").do(job)
schedule.every().hour.at("01:30").do(job)
schedule.every().hour.at("02:30").do(job)
schedule.every().hour.at("05:00").do(job)
schedule.every().hour.at("15:00").do(job)
schedule.every().hour.at("30:00").do(job)
schedule.every().hour.at("31:00").do(job)
schedule.every().hour.at("31:30").do(job)
schedule.every().hour.at("32:30").do(job)
schedule.every().hour.at("35:00").do(job)
schedule.every().hour.at("45:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)