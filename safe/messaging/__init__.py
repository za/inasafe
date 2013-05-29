"""
InaSAFE Disaster risk assessment tool developed by AusAid - **Paragraph.**

Contact : ole.moller.nielsen@gmail.com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.
"""

__author__ = 'marco@opengis.ch'
__revision__ = '$Format:%H$'
__date__ = '27/05/2013'
__copyright__ = ('Copyright 2012, Australia Indonesia Facility for '
                 'Disaster Reduction')

from .item.text import Text
from .item.strong_text import StrongText
from .item.em_text import EmText
from .item.heading import Heading
from .item.paragraph import Paragraph
from .item.success_paragraph import SuccessParagraph
from .item.item_list import ItemList
from .item.table import Table
from message import Message