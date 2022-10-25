from PyQt5.QtWidgets import QApplication
import sys

import ui


def main(argv: list[str]) -> None:
    app = QApplication(argv)
    lab = ui.LabUi()
    lab.show()
    sys.exit(app.exec_())
