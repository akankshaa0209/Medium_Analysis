# Step 5: Load FAISS Vector Store

# Load the saved FAISS index
new_vectorstore = FAISS.load_local("faiss_index_react", embeddings, allow_dangerous_deserialization=True)

# Confirm it's loaded
print("FAISS index loaded.")