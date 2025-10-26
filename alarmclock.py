from datetime import datetime
from time import sleep
from playsound import playsound
time=input("Set the time for the alarm to ring (HH:MM):".zfill(5))
print(f"Entered time is {time}.Waiting...")
while True:
    now=datetime.now().strftime("%H:%M")
    if now==time:
        print("Alarm is going off")
        playsound(r"C:\Users\dell\OneDrive\Desktop\Python Shit\Big_Poppa.mp3")
        break
    sleep(5)

