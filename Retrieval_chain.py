from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.llms import Ollama

# Step 6: Set Up Retrieval and QA Chain

# Set up the Ollama model
llm = Ollama(model="llama3.2")  # Use your preferred Ollama model

# Create a Retrieval QA chain
retrieval_qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=new_vectorstore.as_retriever())

# Ask a sample question
question = "What do you mean by transformer-based models?"
response = retrieval_qa.run(question)

# Print the response
print(f"Answer to '{question}': {response}")
