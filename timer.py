import time

# Ask the user how many seconds the timer should run.
timer = int(input("Enter the time in seconds: "))

# Count down from the timer value to 1.
for x in range(timer, 0, -1):
    # Convert the remaining seconds into hours, minutes, and seconds.
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)

    # Print the time in 00:00:00 format.
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
