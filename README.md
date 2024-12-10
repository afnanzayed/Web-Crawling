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

## Challenges and Solutions

### 1. Pagination
- **Challenge:** Handling multiple pages of articles during crawling.
- **Solution:** Implemented a loop to navigate through pages using dynamic URL patterns and verified the extracted data at each step to ensure accuracy.

### 2. Dynamic Content (Emails)
- **Challenge:** Extracting email addresses loaded dynamically using JavaScript.
- **Solution:** Used Selenium with a regular expression to locate and extract emails after the page was fully rendered by the browser.

### 3. Vector Database Integration
- **Challenge:** Storing and retrieving embeddings in the vector database (Qdrant) for semantic search.
- **Solution:**
  - Generated embeddings using Hugging Face Transformers.
  - Adjusted vector dimensions to match the database requirements.
  - Stored and retrieved data effectively with Qdrant's APIs.

#### 4. **OpenAI API Limitation**
- **Challenge:** Due to time constraints and API limitations (rate limits), using OpenAI embeddings was not feasible.
- **Solution:** Switched to Hugging Face Transformers as a suitable alternative. While the solution is appropriate, its accuracy for semantic similarity tasks may not be fully optimal.
