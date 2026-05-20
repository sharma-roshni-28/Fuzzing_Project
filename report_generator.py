with open("crash_logs.txt", "r") as file:

    data = file.read()

# Count crashes
total_crashes = data.count("Input:")

# Create report
report = f"""
FUZZ TESTING REPORT
===================

Total Vulnerabilities Found: {total_crashes}

Detailed Logs:
----------------

{data}
"""

# Save report
with open("final_report.txt", "w") as report_file:

    report_file.write(report)

print("Final Report Generated Successfully")