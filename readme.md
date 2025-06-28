# 📱 AI-Powered Mobile Phone Recommender

An intelligent recommendation system that helps users find the best mobile phones based on their natural language queries. Powered by modern NLP, vector search, and a user-friendly Streamlit interface.

---

## 🚀 Features

- **Natural Language Query:** Ask for phones using everyday language (e.g., "Best 6GB RAM phone under 20000").
- **Semantic Search:** Uses sentence embeddings and vector similarity for relevant recommendations.
- **Clean Data Pipeline:** Automated data cleaning and preprocessing.
- **Fast & Scalable:** Efficient vector search with ChromaDB.
- **Interactive UI:** Simple and intuitive Streamlit web app.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit** (Web UI)
- **ChromaDB** (Vector database)
- **Sentence Transformers** (NLP embeddings)
- **Pandas** (Data processing)

---

## 📂 Project Structure

```
mobile_recommender/
│
├── app.py                    # Streamlit web app
├── recommender.py            # Recommendation engine
├── Data_preprocessing.py     # Data cleaning script
├── embedding_store.py        # Embedding creation and storage
├── Flipkart_mobile_brands_data.csv      # Raw dataset (add your own)
├── Flipkart_mobile_brands_cleaned.csv   # Cleaned dataset (auto-generated)
└── requirements.txt          # Python dependencies
```

---

## ⚡ Quick Start

1. **Clone the repository**
    ```bash
    git clone https://github.com/KUHELI08/mobile_recommender.git
    cd mobile_recommender
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Prepare the data**
    - Place your raw dataset as `Flipkart_mobile_brands_data.csv` in the project folder.

4. **Run data preprocessing**
    ```bash
    python Data_preprocessing.py
    ```

5. **Create and store embeddings**
    ```bash
    python embedding_store.py
    ```

6. **Launch the Streamlit app**
    ```bash
    streamlit run app.py
    ```

---

## 📝 Example Usage

- **Query:** `Best 8GB RAM phone under 25000`
- **Query:** `Good camera phone for selfies`
- **Query:** `Budget phone with long battery life`

The app will return a list of top matching phones with details like brand, model, RAM, storage, color, rating, and price.

---

## 🧠 How It Works

1. **Data Preprocessing:** Cleans and standardizes the raw mobile phone dataset.
2. **Embedding Creation:** Generates text embeddings for each phone using a pre-trained Sentence Transformer.
3. **Vector Storage:** Stores embeddings in ChromaDB for fast similarity search.
4. **User Query:** Converts user input into an embedding and retrieves the most similar phones.
5. **Display:** Shows recommendations in a clean, interactive UI.

---


## 🤝 Contributing

Pull requests and suggestions are welcome! Please open an issue first to discuss changes.

---

## 📄 License


## 🙋‍♂️ Author

- KUHELI DEY