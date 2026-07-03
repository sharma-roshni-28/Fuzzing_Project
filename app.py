from flask import Flask, render_template, send_file
import subprocess
import os

app = Flask(__name__)

TOTAL_TESTS = 20

@app.route("/")
def home():
    return render_template(
        "index.html",
        logs="",
        report="",
        total=0,
        tests=TOTAL_TESTS,
        safe=TOTAL_TESTS
    )

@app.route("/run")
def run_fuzzer():

    subprocess.run(["python", "fuzzer.py"])
    subprocess.run(["python", "report_generator.py"])

    with open("crash_logs.txt", "r") as f:
        logs = f.read()

    with open("final_report.txt", "r") as f:
        report = f.read()

    crashes = logs.count("Input:")
    safe = TOTAL_TESTS - crashes

    return render_template(
        "index.html",
        logs=logs,
        report=report,
        total=crashes,
        tests=TOTAL_TESTS,
        safe=safe
    )

@app.route("/download")
def download():
    return send_file("final_report.txt", as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)