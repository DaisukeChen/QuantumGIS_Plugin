# -*- coding: utf-8 -*-

#==================
#はじめてつくるQGIS plugin 
#@DaisukeChen　
#
#==================

from PyQt4.Qtcore import *
from PyQt4.QtGui import *


# road resorce
try:
	from . import resource 
except ImportError:
	pass

#main class 
class Qgis_main:

	def __init__(self,iface):
		self.iface = iface

	# plugin_menu
	def initMenu(self):
		#small_menu
		self.action = QAction(QIcon(":Qgis/plugin/icon/DaisukeChen_Sample"),u"サンプル一号",self.iface.mainWindow())
		self.action.setObjectName("Sample1")

		#big_menu
		self.menu = QMenu(self.iface.mainWindow())
		self.menu.setObejctName("first_qgis")
		self.menu.setTitle(u"cat_nya")
		self.menu.addAction(self.action)

	