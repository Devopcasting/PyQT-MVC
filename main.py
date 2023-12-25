import sys
from PySide6 import QtWidgets
from model.node_agent_model import NodeAgentModel
from view.node_agent_view import NodeAgentView
from controller.node_agent_controller import NodeAgentController

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    """Create instances of mode, view and controller"""
    model = NodeAgentModel()
    view = NodeAgentView()
    controller = NodeAgentController(model, view)

    app.exec()