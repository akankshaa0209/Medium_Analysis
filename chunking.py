from langchain_text_splitters import CharacterTextSplitter

# Step 2: Split Text Into Chunks

# Split documents into chunks of size 1000 with an overlap of 30 characters
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=30, separator="\n")
docs = text_splitter.split_documents(documents=documents)

# Print out the number of chunks and the first chunk
print(f"Number of chunks: {len(docs)}")
print(f"First chunk content: {docs[0].page_content[:500]}")  # Print first 500 chars of the first chunk