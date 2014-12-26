

# Space Syntax Analysis plugin for Quantum GIS - Python version
#
# Copyright (C) Burak Beyhan
# 
# This plugin constructs adjusted graphs, calculate geodesic distance between the
# features and basic space syntax parameters. For a user guide and further explanations
# please refer to the following papers and book if you use this plugin in your studies;
#
# Beyhan, B. (2011) "Developing Space Syntax Tools for Free and Open Source Software for GIS", 
# in Proceedings of the 19th International Conference on Geoinformatics (Geoinformatics 2011), 
# Shanghai, China.
#
# Beyhan, B. (2012) "Developing Graph Theoretic Analysis Tools in FOSS4GIS: An Experiment in 
# OpenJUMP with a Specific Focus on Space Syntax", FOSS4G-CEE and Geoinformatics, Prague 2012.
#
# Beyhan, B. (2012) "A simple installation and user's guide for the plugins and scripts 
# developed to conduct space syntax analysis (SSA) in FOSS4GIS: OpenJUMP, gvSIG, OrbisGIS,
# Quantum GIS, OpenEv, Thuban, MapWindow GIS, SAGA, and R Project", 
# http://mekandizim.mersin.edu.tr/. 
#
# Beyhan, B. (2012) "Plugins and Scripts Developed to Conduct Space Syntax Analysis in FOSS4GIS: 
# OpenJUMP, gvSIG, OrbisGIS, Quantum GIS, OpenEv, Thuban, MapWindow GIS, SAGA, and R Project", 
# http://mekandizim.mersin.edu.tr/, forthcoming.
#
# This program is free software; you can redistribute it and/or modify it under the terms of 
# the GNU General Public License as published by the Free Software Foundation; either version 2 
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see http://www.gnu.org/licenses or write to the Free 
# Software Foundation,Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA


from PyQt4 import QtCore, QtGui 
from ui_qgsspacesyntaxbase import Ui_QgsSpaceSyntaxBase
# create the dialog for mapserver export
class SpaceSyntaxDialog(QtGui.QDialog): 
  def __init__(self):
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_QgsSpaceSyntaxBase() 
    self.ui.setupUi(self) 




