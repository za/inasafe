# coding=utf-8
"""
InaSAFE Disaster risk assessment tool by AusAid -**InaSAFE Wizard**

This module provides an abstract class for wizard steps

Contact : ole.moller.nielsen@gmail.com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""
__author__ = 'qgis@borysjurgiel.pl'
__revision__ = '$Format:%H$'
__date__ = '15/03/2016'
__copyright__ = ('Copyright 2012, Australia Indonesia Facility for '
                 'Disaster Reduction')

import re
import os

# noinspection PyPackageRequirements
from PyQt4.QtGui import QWidget

from safe.impact_functions.impact_function_manager import ImpactFunctionManager
from safe.utilities.keyword_io import KeywordIO
from safe.utilities.resources import get_ui_class


def get_wizard_step_ui_class(py_file_name):
    return get_ui_class(os.path.join(
        'wizard', re.sub(r"pyc?$", "ui", os.path.basename(py_file_name))))


class WizardStep(QWidget):
    """An abstract step.
       Each step is a tab meant to be placed in the wizard.
       Each derived class must implement mandatory methods.
    """

    def __init__(self, parent=None):
        """Constructor

        :param parent: parent - widget to use as parent.
        :type parent: QWidget
        """
        QWidget.__init__(self, parent)
        self.parent = parent
        self.setupUi(self)

        self.keyword_io = KeywordIO()
        self.impact_function_manager = ImpactFunctionManager()

    # noinspection PyUnresolvedReferences,PyMethodMayBeStatic
    def auto_select_one_item(self, list_widget):
        """Select item in the list in list_widget if it's the only item.

        :param list_widget: The list widget that want to be checked.
        :type list_widget: QListWidget
        """
        if list_widget.count() == 1 and list_widget.currentRow() == -1:
            list_widget.setCurrentRow(0)

    def is_ready_to_next_step(self):
        """Check if the step is complete. If so, there is
           no reason to block the Next button.

           This method must be implemented in derived classes.
           Otherwise no exception is raised but the return value is False.

        :returns: True if new step may be enabled.
        :rtype: bool
        """
        return False

    def get_previous_step(self):
        """Find the proper step when user clicks the Previous button.

           This method must be implemented in derived classes.

        :returns: The step to be switched to
        :rtype: WizardStep instance or None
        """
        raise NotImplementedError("The current step class doesn't implement \
            the get_previous_step method")

    def get_next_step(self):
        """Find the proper step when user clicks the Next button.

           This method must be implemented in derived classes.

        :returns: The step to be switched to
        :rtype: WizardStep instance or None
        """
        raise NotImplementedError("The current step class doesn't implement \
            the get_next_step method")

    def set_widgets(self):
        """Set all widgets on the tab.

           This method must be implemented in derived classes.
        """
        raise NotImplementedError("The current step class doesn't implement \
            the set_widgets method")

    @property
    def step_type(self):
        """Whether it's a IFCW step or Keyword Wizard Step."""
        if 'stepfc' in self.__class__.__name__.lower():
            return 'step_fc'
        if 'stepkw' in self.__class__.__name__.lower():
            return 'step_kw'
