from PyQt6.QtWidgets import QSizePolicy
from PyQtUIkit.core import KitFont
from PyQtUIkit.widgets import KitLabel, KitVBoxLayout

from TestGeneratorPluginLib import SideTab, BackendManager


class Aside(SideTab):
    def __init__(self, bm: BackendManager):
        super().__init__(bm, "Aside", 'solid-apps')

        layout = KitVBoxLayout()
        layout.border = 1
        layout.padding = 10
        layout.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setWidget(layout)

        label = KitLabel("This is a Test plugin")
        label.main_palette = 'Warning'
        label.font_size = KitFont.Size.SUPER_BIG
        layout.addWidget(label)
