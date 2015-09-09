# -*- coding: utf-8 -*-

#==================
#はじめてつくるQGIS plugin 
#@DaisukeChen　
#
#==================

# import main class from main.py

def classFactory(iface):
  from .main import main
  return main(iface)