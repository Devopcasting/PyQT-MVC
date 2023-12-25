import os
from typing import Optional
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget

loader = QUiLoader()
basedir = os.path.dirname(__file__)

class NodeAgentView(QtWidgets.QWidget):
    """Define a custom signal for the register button pressed event"""
    register_button_pressed_signal = QtCore.Signal()

    """Define a custom signal for the sync_activate button pressed event"""
    sync_activate_button_pressed_signal = QtCore.Signal()

    def __init__(self) -> None:
        super().__init__()
        
        """Load Main window ui"""
        self.ui = loader.load(os.path.join(basedir, '../ui/main_window.ui'), None)

        """Connect to Register pushButton"""
        register_pushButton = self.ui.findChild(QtWidgets.QPushButton, "pushButton_register")
        register_pushButton.pressed.connect(self.register_button_pressed)

        """Connect to Sync_Activate pushButton"""
        sync_activate_pushButton = self.ui.findChild(QtWidgets.QPushButton, "pushButton_sync_activate")
        sync_activate_pushButton.pressed.connect(self.sync_activate_button_pressed)

        """Show main window"""
        self.center()
        self.ui.show()

        """Create the popup window instance"""
        self.popup_window = PopupWindow()
    
    def center(self) -> None:
        """Launch the main window on the center of the screen"""
        screen = QtWidgets.QApplication.primaryScreen()
        centerPoint = screen.availableGeometry().center()
        self.ui.move(centerPoint - self.ui.rect().center())
    
    def update_status_text(self, text):
        self.ui.findChild(QtWidgets.QLabel, "label_status_result").setText(text)
    
    def get_controller_url(self) -> str:
        controller_url = self.ui.findChild(QtWidgets.QLineEdit, "lineEdit_controllerURL")
        controller_url_text = controller_url.text()
        return controller_url_text

    def get_controller_port(self) -> str:
        controller_port = self.ui.findChild(QtWidgets.QLineEdit, "lineEdit_controllerURLPort")
        controller_port_text = controller_port.text()
        return controller_port_text

    def register_button_pressed(self):
        self.register_button_pressed_signal.emit()

    def sync_activate_button_pressed(self):
        self.sync_activate_button_pressed_signal.emit()

class PopupWindow(QtWidgets.QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.popup_ui = loader.load(os.path.join(basedir, '../ui/popup.ui'), None)
    
    def center(self):
        """Launch the popup window on the center of the screen"""
        screen = QtWidgets.QApplication.primaryScreen()
        centerPoint = screen.availableGeometry().center()
        self.popup_ui.move(centerPoint - self.popup_ui.rect().center())
    
    def popup_message(self, text):
        self.popup_ui.findChild(QtWidgets.QLabel, "popup_label").setText(text)