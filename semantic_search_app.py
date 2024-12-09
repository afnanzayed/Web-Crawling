

import streamlit as st
from qdrant_client.models import SearchRequest
from transformers import AutoTokenizer, AutoModel
import torch
import pandas as pd
from qdrant_client import QdrantClient

# Initialize Qdrant client
client = QdrantClient(host="localhost", port=6333)

# Load Hugging Face transformer model
model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Function to generate embeddings from input text
def generate_embedding(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().tolist()

# Streamlit interface
st.title("Semantic Search for Contractors")
st.write("Enter your search query to find relevant contractors.")

# User input for the search query
search_query = st.text_input("Enter your search query:")

# Button to trigger the search
if st.button("Search"):
    if search_query:
        # Generate embedding for the user query
        query_embedding = generate_embedding(search_query)

        # Send the search query to Qdrant
        search_results = client.search(
            collection_name="contractors",
            query_vector=query_embedding,
            limit=5
        )

        # Display the results
        st.write("### Results:")
        if search_results:
            for result in search_results:
                # Display metadata fields (payload) for each result
                for key, value in result.payload.items():
                    st.write(f"- **{key}:** {value}")
                st.write("---")  # Separator between results
        else:
            # Message if no results are found
            st.write("No matching results found.")
    else:
        # Warning if search query is empty
        st.warning("Please enter a search query.")
