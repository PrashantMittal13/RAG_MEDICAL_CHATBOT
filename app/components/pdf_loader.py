import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException


from app.config.config import DATA_PATH, CHUNK_SIZE,CHUNK_OVERLAP

logger = get_logger(__name__)

# def pdf_loader(path: str):
#     return PyPDFLoader(path)

def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException("Data Path does not exist")   
        
        logger.info(f"Loading files from {DATA_PATH}")

        documents = []

        for file_name in os.listdir(DATA_PATH):
            if file_name.endswith(".pdf"):
                file_path = os.path.join(DATA_PATH, file_name)
                loader = PyPDFLoader(file_path)
                docs = loader.load()
                documents.extend(docs)


        # loader = DirectoryLoader(DATA_PATH, glob = "*.pdf", loader_cls= PyPDFLoader)
 
        # documents = loader.load()

        if not documents:
            logger.warning("No pdfs were found")

        else:
            logger.info(f"Succefully fetched {len(documents)} documents")

        return documents
    except Exception as e:
        error_message = CustomException("failed to load pdf", e)
        logger.error(str(error_message))
        return []
    
def create_text_chunks(documents):
    try:
        if not documents:
            raise CustomException("No documents were found")
        
        logger.info(f"splitting {len(documents)} documents into chunks")


        text_splitter = RecursiveCharacterTextSplitter(chunk_size = CHUNK_SIZE,chunk_overlap = CHUNK_OVERLAP)

        text_chunks = text_splitter.split_documents(documents)

        logger.info(f"Generated {len(text_chunks)} text chunks")
        return text_chunks
    
    except Exception as e:
        error_message = CustomException("failed to create chunks", e)
        logger.error(str(error_message))
        return []
        

    








