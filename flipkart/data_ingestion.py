# from langchain_astradb import AstraDBVectorStore
# from langchain_huggingface import HuggingFaceEndpointEmbeddings
# from flipkart.data_converter import DataConverter
# from flipkart.config import Config

# class DataIngestor:
#     def __init__(self):
#         self.embedding = HuggingFaceEndpointEmbeddings(model=Config.EMBEDDING_MODEL)

#         self.vstore = AstraDBVectorStore(
#             embedding=self.embedding,
#             collection_name="flipkart_database",
#             api_endpoint=Config.ASTRA_DB_API_ENDPOINT,
#             token=Config.ASTRA_DB_APPLICATION_TOKEN,
#             namespace=Config.ASTRA_DB_KEYSPACE
#         )

#     def ingest(self,load_existing=True):
#         if load_existing==True:
#             return self.vstore
        
#         docs = DataConverter("D:\\Flipkart Product Recommender\\data\\flipkart_product_review.csv").convert()

#         self.vstore.add_documents(docs)

#         return self.vstore

# if __name__=="__main__":
#     ingestor = DataIngestor()
#     ingestor.ingest(load_existing=False)

from langchain_astradb import AstraDBVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from flipkart.data_converter import DataConverter
from flipkart.config import Config

class DataIngestor:
    def __init__(self):
        # FAST + LOCAL + ZERO API ERRORS
        self.embedding = HuggingFaceEmbeddings(
            model_name=Config.EMBEDDING_MODEL
        )

        self.vstore = AstraDBVectorStore(
            embedding=self.embedding,
            collection_name="flipkart_database",
            api_endpoint=Config.ASTRA_DB_API_ENDPOINT,
            token=Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace=Config.ASTRA_DB_KEYSPACE
        )

    def ingest(self, load_existing=True):
        if load_existing:
            return self.vstore
        
        docs = DataConverter(
            r"D:\Flipkart Product Recommender\data\flipkart_product_review.csv"
        ).convert()

        self.vstore.add_documents(docs)
        print("✅ Documents successfully ingested!")
        return self.vstore


if __name__ == "__main__":
    ingestor = DataIngestor()
    ingestor.ingest(load_existing=False)

