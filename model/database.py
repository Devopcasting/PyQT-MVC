from pymongo import MongoClient

class NodeAgentDatabase:
    def __init__(self, host="localhost", port=27017, database_name="node_agent") -> None:
        self.client = MongoClient(host, port, serverSelectionTimeoutMS=1000)
        self.db = self.client[database_name]
    
    def get_collection(self, collection_name):
        return self.db[collection_name]