import datetime
import time
import os

def sound_alarm():
    # Check the operating system and use the appropriate method to play a sound
    if os.name == 'nt':  # Windows
        import winsound
        winsound.Beep(440, 1000)  # Frequency 440 Hz, Duration 1000 ms
    else:
        # For non-Windows systems, just print an alert message
        print('\a')  # ASCII Bell character

def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")
    while True:
        # Get the current time
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        
        # Check if the current time matches the alarm time
        if current_time == alarm_time:
            print("Wake up! It's time!")
            sound_alarm()
            break
        
        # Wait for 1 second before checking again
        time.sleep(1)

def main():
    print("Welcome to the Alarm Clock!")
    alarm_hour = input("Enter the hour for the alarm (HH): ")
    alarm_minute = input("Enter the minute for the alarm (MM): ")
    alarm_second = input("Enter the second for the alarm (SS): ")
    
    alarm_time = f"{alarm_hour.zfill(2)}:{alarm_minute.zfill(2)}:{alarm_second.zfill(2)}"
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
