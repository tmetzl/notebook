"""SelectionContainer class.  

Represents a multipage container that can be used to group other widgets into
pages.
"""
#-----------------------------------------------------------------------------
# Copyright (c) 2013, the IPython Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
from .widget_container import ContainerWidget
from IPython.utils.traitlets import Unicode, Dict, CInt
from IPython.utils.warn import DeprecatedClass

#-----------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------
class _SelectionContainer(ContainerWidget):
    _titles = Dict(help="Titles of the pages", sync=True)
    selected_index = CInt(0, sync=True)

    # Public methods
    def set_title(self, index, title):
        """Sets the title of a container page.

        Parameters
        ----------
        index : int
            Index of the container page
        title : unicode
            New title"""
        self._titles[index] = title
        self.send_state('_titles')

    def get_title(self, index):
        """Gets the title of a container pages.

        Parameters
        ----------
        index : int
            Index of the container page"""
        if index in self._titles:
            return self._titles[index]
        else:
            return None


class Accordion(_SelectionContainer):
    _view_name = Unicode('AccordionView', sync=True)


class Tab(_SelectionContainer):
    _view_name = Unicode('TabView', sync=True)

_SelectionContainerWidget = DeprecatedClass(_SelectionContainer, '_SelectionContainerWidget')
AccordionWidget = DeprecatedClass(Accordion, 'AccordionWidget')
TabWidget = DeprecatedClass(Tab, 'TabWidget')
