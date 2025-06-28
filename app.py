import sys
import streamlit as st
from recommender import get_recommendations
import chromadb

# Streamlit App
st.title("📱 AI-Powered Mobile Recommendation Chatbot")
st.write("Ask for mobile suggestions based on your preferences!")

# User Query Input
query = st.text_input("Enter your requirements (e.g., 'Best 6GB RAM phone under 20000'):")

if query:
    results = get_recommendations(query)
    
    st.subheader("Top Mobile Recommendations:")
    for mobile in results:
        st.write(f"**{mobile['Brand']} {mobile['Model']}**")
        st.write(f"- RAM: {mobile['Memory']} | Storage: {mobile['Storage']}")
        st.write(f"- Color: {mobile['Color']} | Rating: {mobile['Rating']}")
        st.write(f"- Price: {mobile['Price']}")
        st.write("---")
