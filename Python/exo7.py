def calculate_end_time(start_hour, start_minute, duration_minutes):
    end_minute = start_minute + duration_minutes+ start_hour*60
    end_hour = (end_minute // 60)%24
    end_minute %= 60
    return end_hour, end_minute

start_hour = int(input("Enter the start hour (24-hour format): "))
start_minute = int(input("Enter the start minute: "))
duration_minutes = int(input("Enter the duration in minutes: "))

end_hour, end_minute = calculate_end_time(start_hour, start_minute, duration_minutes)

print(f"The event ends at {end_hour:02d}:{end_minute:02d}")