
import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model

    
def main():
    st.set_page_config("Q&A System")

    
    st.header("Q&A System Project")
    
    user_question= st.text_input("Ask your question")
    path = "Data"
    
    if st.button("submit & process"):
        with st.spinner("Processing..."):
            document=load_data(path)
            model=load_model()
            query_engine=download_gemini_embedding(model,document)
                
            response = query_engine.query(user_question)
                
            st.write(response.response)
                
                
if __name__=="__main__":
    main()          
                
    
    
    
    
    
