from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging

def load_data(file_path):
    try:
        logging.info("Data loading started...")

        
        loader = SimpleDirectoryReader(file_path)
        documents=loader.load_data()
        logging.info("Data loading completed...")
        return documents

    except Exception as e:
        logging.error("Exception in loading data...")
        raise customexception(e, sys)


