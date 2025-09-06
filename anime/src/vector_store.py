import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma   # ✅ updated import
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

class VectorStoreBuilder:
    def __init__(self, csv_path: str, persist_dir: str = "chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    def build_and_save_vectorstore(self):
        """Build a new Chroma DB if it doesn’t exist, otherwise load the existing one."""
        if os.path.exists(self.persist_dir):
            print(f"🔄 Loading existing Chroma DB from: {self.persist_dir}")
            return self.load_vector_store()

        print("⚡ Building new Chroma DB...")
        loader = CSVLoader(
            file_path=self.csv_path,
            encoding="utf-8",
            metadata_columns=[]
        )
        data = loader.load()

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = splitter.split_documents(data)

        db = Chroma.from_documents(
            documents=texts,
            embedding=self.embedding,
            persist_directory=self.persist_dir
        )
        return db  # persistence is automatic in Chroma >= 0.4.x

    def load_vector_store(self):
        """Load an existing Chroma DB"""
        return Chroma(
            persist_directory=self.persist_dir,
            embedding_function=self.embedding
        )
