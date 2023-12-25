from typing import Optional
from PySide6 import QtCore
from PySide6.QtCore import QObject
from model.node_agent_model import NodeAgentModel
from view.node_agent_view import NodeAgentView
import json
import requests

class NodeAgentController(QtCore.QObject):
    def __init__(self, model, view) -> None:
        super().__init__()
        self.model = model
        self.view = view

        """Set the initial status text"""
        self.view.update_status_text(self.model.get_registration_status())

        """Connect signals and slots"""
        self.view.register_button_pressed_signal.connect(self.register_button_pressed)
        self.view.sync_activate_button_pressed_signal.connect(self.sync_activate_button_pressed)
    
    def register_button_pressed(self):
        CONTROLLER_URL = self.view.get_controller_url()
        CONTROLLER_PORT = self.view.get_controller_port()

        if not CONTROLLER_URL:
            return self.view.update_status_text("Controller URL is required")
            # self.view.popup_window.popup_message("Controller URL is required")
            # self.open_popup_dialog()

        if not CONTROLLER_PORT:
            CONTROLLER_PORT = "8080"

        """Send request to node agent service for registering the node agent"""
        data = {
            "macid": "502b73c0ce53",
            "controller_url": CONTROLLER_URL,
            "controller_port": CONTROLLER_PORT
        }
        HEADER = {'Content-Type': 'application/json'}
        response = requests.post("http://localhost:8082/request-node-agent-registration", data=json.dumps(data), headers=HEADER)
        if response.status_code == 200:
            self.view.update_status_text("Node registered successfully")

    def sync_activate_button_pressed(self):
        """Collect sync data from DB"""
        result = list(self.model.get_sync_data())
        data = {
            "controller_url": result[0]["controller_url"],
            "controller_port": result[0]["controller_port"],
            "macid": result[0]["macid"],
            "accessToken": result[0]["accessToken"],
            "ipAddress": {"wireless": "192.168.1.7"},
            "hostName": "funix"
        }
        HEADER = {'Content-Type': 'application/json'}
        response = requests.post("http://localhost:8082/sync-activate",data=json.dumps(data), headers=HEADER)
        if response.status_code == 200:
            self.view.update_status_text("Node Sync_Activation done")


    def open_popup_dialog(self):
        """Access the PopupWindow instance from the NodeAgentView"""
        popup_window = self.view.popup_window.popup_ui
        self.view.popup_window.center()
        popup_window.show()
        