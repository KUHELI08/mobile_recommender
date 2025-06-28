import chromadb
import pandas as pd
from sentence_transformers import SentenceTransformer
import os
import tf_keras as keras

def create_embeddings():
    """
    Create and store embeddings for mobile phone data in ChromaDB.
    """
    try:
        # Check if cleaned dataset exists
        dataset_path = "Flipkart_mobile_brands_cleaned.csv"
        if not os.path.exists(dataset_path):
            raise FileNotFoundError(f"Cleaned dataset not found at {dataset_path}")

        # Load cleaned dataset
        df = pd.read_csv(dataset_path)
        print(f"Loaded {len(df)} records from cleaned dataset")

        # Generate text descriptions
        df['Text'] = df.apply(
            lambda x: f"{x['Brand']} {x['Model']} {x['Memory']}GB RAM "
                     f"{x['Storage']}GB Storage {x['Color']} Rating: {x['Rating']}", 
            axis=1
        )

        # Load embedding model
        print("Loading embedding model...")
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        
        # Generate embeddings
        print("Generating embeddings...")
        embeddings = model.encode(df['Text'].tolist())

        # Initialize ChromaDB client
        print("Initializing ChromaDB...")
        client = chromadb.PersistentClient(path="chroma_db")
        collection = client.get_or_create_collection(name="mobile_recommendations")

        # Clear existing data
        collection.delete(ids=[str(i) for i in range(len(df))])

        # Store embeddings in ChromaDB
        batch_size = 100
        for i in range(0, len(df), batch_size):
            batch_end = min(i + batch_size, len(df))
            batch_ids = [str(j) for j in range(i, batch_end)]
            batch_texts = df['Text'].iloc[i:batch_end].tolist()
            batch_embeddings = [e.tolist() for e in embeddings[i:batch_end]]
            
            collection.add(
                ids=batch_ids,
                documents=batch_texts,
                embeddings=batch_embeddings
            )
            print(f"Processed {batch_end}/{len(df)} records")

        print("ChromaDB embeddings stored successfully!")
        return True

    except Exception as e:
        print(f"Error during embedding creation: {str(e)}")
        return False

if __name__ == "__main__":
    create_embeddings()