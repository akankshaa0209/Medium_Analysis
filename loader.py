import os

# Edge user-agent string
os.environ["USER_AGENT"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31"
)

from langchain_community.document_loaders import WebBaseLoader

# Step 1: Load Web Page Content

# Set URL
url = "https://medium.com/techartifact-technology-learning/understanding-genai-in-depth-c820289ddeb3"  # Replace with any URL 

# Load web page content
loader = WebBaseLoader(url)
documents = loader.load()

# Check the loaded documents
print(f"Number of documents loaded: {len(documents)}")
print(f"First document content: {documents[0].page_content[:500]}")  # Print first 500 chars of the first document

doc = documents[0]
print("Document metadata:", doc.metadata)
print("Content preview:", doc.page_content[:300])