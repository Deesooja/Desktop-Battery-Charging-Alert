import psutil
import winsound
import time

while True:
    battery = psutil.sensors_battery()
    is_ac_power_connected = battery.power_plugged
    if battery:
        if (is_ac_power_connected):
        
                print(f"Battery percentage: {battery.percent}%")
                if battery.percent > 90:
                    # Play a sound (default beep sound)
                    winsound.Beep(1000, 1000)  # Frequency: 1000Hz, Duration: 1000ms
                    winsound.PlaySound("alert.wav", winsound.SND_FILENAME)
        else:
            
            print(f"Battery percentage: {battery.percent}%")
            if battery.percent < 75:
                # Play a sound (default beep sound)
                winsound.Beep(1000, 1000)  # Frequency: 1000Hz, Duration: 1000ms
                winsound.PlaySound("alert.wav", winsound.SND_FILENAME)
           
    else:
        print("No battery information available.")
    
    time.sleep(60)

