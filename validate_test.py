import subprocess
import sys

print("✅ Validating test code before committing...")

try:
    result = subprocess.run(["npx", "playwright", "test", "--project=chromium"], check=True)
    print("✅ Test ran successfully.")
except subprocess.CalledProcessError as e:
    print("❌ Test failed. Error log:")
    print(e.output)
    sys.exit(1)
