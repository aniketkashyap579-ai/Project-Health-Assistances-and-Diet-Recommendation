import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

PDF_file="data/nutrition.pdf"

def create_rag():
  if not os.path.exists(PDF_file):
    raise FileNotFoundError("File Not Found")
  else:
      document=PyPDFLoader(PDF_file).load()
      splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
      chunks=splitter.split_documents(document)
      embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"
)
      db=FAISS.from_documents(chunks,embedding)
      db.save_local("vector_db")
      return len (chunks)

def load_rag():
    embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db=FAISS.load_local("vector_db",embedding,allow_dangerous_deserialization=True)
    return db

