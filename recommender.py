import chromadb
import pandas as pd
from sentence_transformers import SentenceTransformer
import os

def get_recommendations(query, top_k=2):
    """
    Get mobile recommendations based on user query using ChromaDB.

     
    Args:
        query (str): User's query string
        top_k (int): Number of recommendations to return
        
    Returns:
        list: List of dictionaries containing mobile recommendations
    """
    # Check if ChromaDB directory exists, if not create it
    if not os.path.exists("chroma_db"):
        os.makedirs("chroma_db")
        
    try:
        # Check if dataset exists
        dataset_path = "Flipkart_mobile_brands_cleaned.csv"
        if not os.path.exists(dataset_path):
            raise FileNotFoundError(f"Dataset not found at {dataset_path}")
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
        return []
        
    # Load cleaned dataset
    df = pd.read_csv(dataset_path)
    
    # Initialize ChromaDB client
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection(name="mobile_recommendations")
    
    # Load embedding model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    query_embedding = model.encode([query]).tolist()
    
    # Search in ChromaDB
    results = collection.query(query_embeddings=query_embedding, n_results=top_k, include=["documents", "metadatas"])
    
    # Fetch top results
    recommendations = []
    try:
        for doc_id in results['ids'][0]:
            try:
                mobile = df.iloc[int(doc_id)]
                recommendations.append({
                    "Brand": mobile['Brand'],
                    "Model": mobile['Model'],
                    "Memory": f"{mobile['Memory']}GB",
                    "Storage": f"{mobile['Storage']}GB",
                    "Color": mobile['Color'],
                    "Rating": mobile['Rating'],
                    "Price": f"₹{mobile['Selling Price']}"
                })
            except (IndexError, KeyError) as e:
                print(f"Error processing mobile with id {doc_id}: {str(e)}")
                continue
    except Exception as e:
        print(f"Error in processing results: {str(e)}")
        
    
    return recommendations

# Ensure all error handling is properly nested within the function's try blocks.

# Example usage
if __name__ == "__main__":
    query = "Best 6GB RAM phone under 20000"
    results = get_recommendations(query)
    for r in results:
        print(r)
