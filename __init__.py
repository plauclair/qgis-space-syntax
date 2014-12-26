def name():
  return "Space Syntax Analysis"

def description():
  return "This plugin calculates the basic space syntax parameters."

def version():
  return "Version 0.1"

def qgisMinimumVersion():
  return "1.0"

def authorName():
  return "Burak Beyhan"

def classFactory(iface):
  # load SpaceSyntax class from file spacesyntax.py
  from spacesyntax import SpaceSyntax
  return SpaceSyntax(iface)
