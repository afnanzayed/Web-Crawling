# README: Web Crawling and Semantic Search Project

## Overview

This project extracts contractor information from a website, processes the data for efficient semantic search, and presents it in an easy-to-use web application. By leveraging modern technologies, it ensures seamless data handling, embedding generation, and intelligent search capabilities.

---

## Features

- **Web Crawler**: Extracts key contractor details such as company name, size, interests, location, and email.
- **Embedding Generation**: Uses machine learning to convert text data into meaningful numerical representations for semantic search.
- **Semantic Search**: Allows users to search contractors based on context and relevance, not just keywords.
- **User Interface**: A simple and intuitive **Streamlit app** for querying the data.

---

## Key Files

The project relies on two main files:
- **`filtered_contractors_data.csv`**: Contains the cleaned and structured contractor data extracted by the crawler.
- **`contractors_with_embeddings.csv`**: Includes the contractor data with generated embeddings for semantic search.

---

## How to Use

1. **Run the Web Crawler**:
   - Collect contractor information and save it in the `filtered_contractors_data.csv` file.

2. **Generate Embeddings**:
   - Process the `filtered_contractors_data.csv` file to generate embeddings and save the results in `contractors_with_embeddings.csv`.

3. **Upload to Database**:
   - Store the `contractors_with_embeddings.csv` data in a vector database (Qdrant) for fast querying.

4. **Launch the App**:
   - Use the Streamlit app to input queries and retrieve relevant contractors.

---

## Key Benefits

- **Context-Aware Search**: Results are ranked based on semantic similarity, ensuring relevant matches.
- **Scalable Solution**: Built to handle large datasets efficiently.
- **User-Friendly**: Simple setup and intuitive interface for end-users.

---
