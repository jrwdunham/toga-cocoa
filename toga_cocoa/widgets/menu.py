from rubicon.objc import objc_method, get_selector

from toga.interface import Menu as MenuInterface

from .base import WidgetMixin
from ..libs import *
from ..utils import process_callback


class TogaMenu(NSMenu):
    pass


class Menu(MenuInterface, WidgetMixin):
    def __init__(self, label, id=None, style=None):
        super().__init__(label, id=id, style=style)
        self._create()

    def create(self):
        self._impl = TogaMenu.alloc().init()
        self._impl._interface = self

    def _set_label(self, label):
        self._impl.setTitle_(self.label)
        self.rehint()

    def rehint(self):
        pass

    def _add_child(self, child):
        super()._add_child(child)
        # The child of a ``Menu`` must be a ``MenuItem``
        self._impl.addItem_(child._impl)

    def add_separator(self):
        self._impl.addItem_(NSMenuItem.separatorItem())
