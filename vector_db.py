from langchain_community.vectorstores import FAISS

#  Step 4: Store Embeddings in FAISS Vector Store

# Create a FAISS vector store from the embeddings
vectorstore = FAISS.from_documents(docs, embeddings)

# Save the vector store locally
vectorstore.save_local("faiss_index_react")

# Check if FAISS index has been saved
print("FAISS index saved.")