def process_input(data):

    # Simulated Buffer Overflow
    if len(data) > 20:
        raise Exception("Buffer Overflow Detected")

    # Simulated Runtime Crash
    if "CRASH" in data:
        x = 1 / 0

    return "Input Processed Successfully"


while True:

    user_input = input("Enter Input: ")

    try:
        result = process_input(user_input)
        print(result)

    except Exception as e:
        print("Crash Detected:", e)