import time

# Get the current time in seconds
start_time = time.time()

# Define the target time in seconds
target_time = 5

while True:
    # Get the current time in seconds
    current_time = time.time()
    
    # Calculate the elapsed time
    elapsed_time = current_time - start_time
    
    # Check if the elapsed time has reached the target time
    if elapsed_time >= target_time:
        # Do the action
        print("Time has reached 5 seconds!")
        break
    
    # Wait for a short period of time before checking again
    time.sleep(0.1)