#Q1:embeddings (HuggingFace) 
from langchain_community.embeddings import HuggingFaceEmbeddings

class Embedder:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.embedding_model = HuggingFaceEmbeddings(model_name=self.model_name)

    def embed(self, documents):
        # documents : liste de chunks LangChain (Document objects)
        texts = [doc.page_content for doc in documents]
        return self.embedding_model.embed_documents(texts)
