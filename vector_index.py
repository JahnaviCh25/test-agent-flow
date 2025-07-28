from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from pathlib import Path
import pickle

# Load all ticket descriptions
ticket_dir = Path("prompts")
tickets = [p.read_text() for p in ticket_dir.glob("*.md")]
ticket_names = [p.name for p in ticket_dir.glob("*.md")]

# Generate embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(tickets)

# Build FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# Save
with open("ticket_names.pkl", "wb") as f:
    pickle.dump(ticket_names, f)
faiss.write_index(index, "ticket_index.faiss")

print("✅ VectorDB index created and saved.")
