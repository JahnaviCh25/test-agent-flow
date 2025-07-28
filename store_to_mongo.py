from pymongo import MongoClient
from datetime import datetime
from pathlib import Path

client = MongoClient("mongodb://localhost:27017")  # Or your Atlas URI
db = client.test_agent
collection = db.test_results

ticket_name = "ticket_001.md"
ticket_content = Path(f"prompts/{ticket_name}").read_text()
test_code = Path("tests/login.spec.ts").read_text()
result = "PASS"  # or FAIL if parsed from GitHub Actions

doc = {
    "ticket_name": ticket_name,
    "ticket_text": ticket_content,
    "test_code": test_code,
    "result": result,
    "timestamp": datetime.now()
}

collection.insert_one(doc)
print("✅ Logged to MongoDB.")
