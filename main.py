import time
import winsound

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            for i in range(5):  # Beeps 5 times
                winsound.Beep(1000, 1000)  # Frequency: 1000 Hz, Duration: 1000 ms
            break
        time.sleep(1)

alarm_time = input("Enter alarm time in HH:MM:SS format: ")
set_alarm(alarm_time)