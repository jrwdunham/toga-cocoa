from rubicon.objc import objc_method, get_selector

from toga.interface import MenuItem as MenuItemInterface

from .base import WidgetMixin
from ..libs import *
from ..utils import process_callback


class TogaMenuItem(NSMenuItem):
    @objc_method
    def onPress_(self, obj) -> None:
        if self._interface.on_press:
            process_callback(self._interface.on_press(self._interface))


class MenuItem(MenuItemInterface, WidgetMixin):
    def __init__(self, label, id=None, style=None, on_press=None,
                 key_equivalent=None):
        super().__init__(label, id=id, style=style, on_press=on_press,
                         key_equivalent=key_equivalent)
        self._create()

    def create(self):
        self._impl = TogaMenuItem.alloc().init()
        self._impl._interface = self
        self._impl.setTarget_(self._impl)

    def _set_label(self, label):
        self._impl.setTitle_(self.label)
        self.rehint()

    def rehint(self):
        pass

    def _set_on_press(self, value):
        self._impl.setAction_(get_selector('onPress:'))

    def _set_key_equivalent(self, value):
        self._impl.setKeyEquivalent_(value)

    def _add_child(self, child):
        super()._add_child(child)
        # The child of a ``MenuItem`` must be a ``Menu``
        self._impl.setSubmenu_(child._impl)
