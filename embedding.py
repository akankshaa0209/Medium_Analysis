from langchain_community.embeddings import OllamaEmbeddings

# Use Ollama embeddings model
embeddings = OllamaEmbeddings(model="llama3.2")  # Use the model you prefer

# Create embeddings for the documents
embedded_docs = embeddings.embed_documents([doc.page_content for doc in docs])

# Print the first embedding (a numerical vector)
print(f"First document embedding (vector): {embedded_docs[0][:10]}...")  # Print first 10 values of the first embedding vector