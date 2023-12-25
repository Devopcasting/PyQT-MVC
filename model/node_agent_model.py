from typing import Optional
from PySide6 import QtCore
from PySide6.QtCore import QObject
from .database import NodeAgentDatabase

class NodeAgentModel(QtCore.QObject):
    def __init__(self) -> None:
        super().__init__()
    
    def get_registration_status(self):
        try:
            db_connection = NodeAgentDatabase()
            db_collection = db_connection.get_collection("registration")
            accessToken_key = db_collection.find_one({"accessToken": {"$exists": True}})
            isSyncActivated_key = db_collection.find_one({"isSyncActivated": {"$exists": True}})
            if accessToken_key and isSyncActivated_key:
                return "Registered and Sync_Activated"
            elif accessToken_key:
                return "Node Registered"
            else:
                return "Waiting for Registration and Sync_Activation"
        except Exception as error:
            return "Database connectivity failed"
    
    def get_sync_data(self):
        try:
            db_connection = NodeAgentDatabase()
            db_collection = db_connection.get_collection("registration")
            query = {"macid": "502b73c0ce53"}
            return db_collection.find(query)

        except Exception as error:
            return "Database connectivity failed"