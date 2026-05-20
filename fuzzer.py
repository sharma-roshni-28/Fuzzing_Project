import random
import string
import subprocess
import time

# Open log file
log_file = open("crash_logs.txt", "w")

# Generate random inputs
def generate_random_input():

    characters = string.ascii_letters + string.digits

    length = random.randint(5, 40)

    random_data = ''.join(
        random.choice(characters)
        for i in range(length)
    )

    return random_data


# Dangerous test cases
special_inputs = [
    "CRASH",
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    "123456789012345678901234567890"
]

# Start fuzz testing
for i in range(20):

    if i < len(special_inputs):
        test_input = special_inputs[i]
    else:
        test_input = generate_random_input()

    print("Testing Input:", test_input)

    process = subprocess.Popen(
        ["python", "vulnerable_app.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output, error = process.communicate(input=test_input)

    print(output)

    # Detect crash
    if "Crash Detected" in output:

        print("Vulnerability Found!")

        log_file.write("=================================\n")
        log_file.write(f"Input: {test_input}\n")
        log_file.write(output)
        log_file.write("\n")

    time.sleep(1)

log_file.close()

print("Fuzz Testing Completed")