
from llama_index.core import VectorStoreIndex
from llama_index.core import ServiceContext
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

import sys
from exception import customexception
from logger import logging

def download_gemini_embedding(gemini_llm ,document):
    
    try:
        logging.info("")
        gemini_embedding = GeminiEmbedding(gemini_llm=gemini_llm)
        service_context = ServiceContext.from_defaults(llm=gemini_llm, embed_model=gemini_embedding)
        
        logging.info("")
        index = VectorStoreIndex.from_documents(document, service_context=service_context)
        index.storage_context.persist()
        
        logging.info("")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexception(e,sys)
