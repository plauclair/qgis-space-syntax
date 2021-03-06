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


import os
import sys
import string
import math
import time

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *


# Import the code for the dialog
from spacesyntaxdialog import SpaceSyntaxDialog

# initialize Qt resources from file resouces.py
import resources


class SpaceSyntax:
    def __init__(self, iface):
        # save reference to the QGIS interface
        self.iface = iface

    def initGui(self):
        # create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/spacesyntax/icon.png"), \
                              "Space Syntax Analysis", \
                              self.iface.mainWindow())
        self.action.setWhatsThis("Space syntax analysis tool")
        self.action.setStatusTip("Space syntax analysis tool")
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
        # add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToVectorMenu("&Space Syntax Analysis", self.action)

    def unload(self):
        # remove the plugin menu item and icon
        self.iface.removePluginMenu("&Space Syntax Analysis", self.action)
        self.iface.removeToolBarIcon(self.action)


    def run(self):
        self.dlg = SpaceSyntaxDialog()
        vlayer = self.iface.activeLayer()

        if vlayer:

            vprovider = vlayer.dataProvider()
            all_attrs = vprovider.attributeIndexes()
            # vprovider.select( all_attrs )
            my_fields = vprovider.fields()
            print my_fields

            # script for GUI actions

            for i in my_fields:
                self.dlg.ui.comboBox.addItem(unicode(i.name()))

            QObject.connect(self.dlg.ui.buttonBox, SIGNAL("accepted()"), self.ok_clicked)
            QObject.connect(self.dlg.ui.checkbox_network_file, SIGNAL("clicked(bool)"), self.toggleDL)
            QObject.connect(self.dlg.ui.checkbox_geodes_matrix, SIGNAL("clicked(bool)"), self.toggleDL)
            QObject.connect(self.dlg.ui.radioButton, SIGNAL("clicked(bool)"), self.toggleCF)
            QObject.connect(self.dlg.ui.radioButton_2, SIGNAL("clicked(bool)"), self.toggleCF)

            self.dlg.show()

        else:
            QMessageBox.critical(self.iface.mainWindow(), "Error", "Please select a layer")

    def toggleDL(self, boolDL):
        dm = self.dlg.ui.checkbox_network_file.isChecked() or self.dlg.ui.checkbox_geodes_matrix.isChecked()
        self.dlg.ui.checkbox_loc_network_file.setEnabled(dm)
        self.dlg.ui.radioButton.setEnabled(dm)
        self.dlg.ui.radioButton_2.setEnabled(dm)
        self.dlg.ui.comboBox.setEnabled(dm and self.dlg.ui.radioButton.isChecked())
        self.dlg.ui.comboBox_1.setEnabled(self.dlg.ui.checkbox_network_file.isChecked())

    def toggleCF(self, boolSF):
        if self.dlg.ui.radioButton.isChecked() and (
            self.dlg.ui.checkbox_network_file.isChecked() or self.dlg.ui.checkbox_geodes_matrix.isChecked()):
            self.dlg.ui.comboBox.setEnabled(True)
        else:
            self.dlg.ui.comboBox.setEnabled(False)

    # main script constructing adjusted graph, calculating geodesic and space syntax parameters

    def ok_clicked(self):
        start_time = time.time()

        layer = self.iface.activeLayer()
        provider = layer.dataProvider()

        fname = layer.source()
        lname = layer.name()
        nedge = fname[:-4]
        dir_name = nedge[:-len(lname)]
        obj = layer.featureCount()

        etiket = []
        betiket = []
        for i in range(obj):
            betiket.append((i + 1).__str__())

        if self.dlg.ui.radioButton.isChecked() and (self.dlg.ui.checkbox_network_file.isChecked() or self.dlg.ui.checkbox_geodes_matrix.isChecked()):
            fieldim = self.dlg.ui.comboBox.currentText()
            fieldin = provider.fieldNameIndex(fieldim)
            all_attrs = provider.attributeIndexes()
            provider.select(all_attrs)
            my_fields = provider.fields()
            feat = QgsFeature()
            while provider.nextFeature(feat):
                attributeMap = feat.attributeMap()
                etiket.append(str(attributeMap[fieldin].toString()))

        if self.dlg.ui.radioButton_2.isChecked():
            etiket = betiket

        if self.dlg.ui.checkbox_loc_network_file.isChecked():
            fnamem = QFileDialog.getSaveFileName(None, 'Save files', dir_name, "")
            nedge = fnamem

        netip = self.dlg.ui.comboBox_1.currentText()
        if self.dlg.ui.checkbox_network_file.isChecked():
            if netip == ".dl":
                edges = open(nedge + '.dl', 'w')
                edges.write("dl n=" + obj.__str__())
                edges.write('\n')
                edges.write("format = edgelist1")
                edges.write('\n')
                edges.write("labels embedded")
                edges.write('\n')
                edges.write("data:")
                edges.write('\n')
                betiket = etiket
            else:
                edges = open(nedge + '.net', 'w')
                edges.write("*Vertices " + obj.__str__())
                edges.write('\n')
                for n in range(obj):
                    edges.write((n + 1).__str__() + " " + chr(34) + etiket[n] + chr(34))
                    edges.write('\n')
                edges.write("*Arcs")
                edges.write('\n')

        if self.dlg.ui.checkbox_geodes_matrix.isChecked():
            geodesic = open(nedge + '.txt', 'w')

        feat = QgsFeature()
        beat = QgsFeature()

        sna = []
        for i in range(obj):
            sna.append([])
            for j in range(obj):
                sna[i].append(0)

        atr = []

        nufi = provider.fields().count()

        # adding space syntax parameters as new fields to the attribute table

        provider.addAttributes([
            QgsField("Lineno", QVariant.Int),
            QgsField("Connectivity", QVariant.Int),
            QgsField("TotalDepth", QVariant.Int),
            QgsField("MeanDepth", QVariant.Double),
            QgsField("GlobalInteg", QVariant.Double),
            QgsField("LocalDepth", QVariant.Int),
            QgsField("LocalInteg", QVariant.Double),
            QgsField("Control", QVariant.Double),
        ])
        layer.startEditing()
        fortas = []

        # construction of adjusted graph

        for s1 in range(obj):
            provider.getFeatures(QgsFeatureRequest().setFilterFid(s1).setSubsetOfAttributes([])).nextFeature(feat)
            cntr = 0

            iliski = []

            for s2 in range(obj):
                provider.getFeatures(QgsFeatureRequest().setFilterFid(s2).setSubsetOfAttributes([])).nextFeature(beat)
                kesisme = feat.geometry().intersects(beat.geometry())

                if kesisme and (s1 != s2):
                    sna[s1][s2] = 1
                    cntr += 1
                    if self.dlg.ui.checkbox_network_file.isChecked():
                        edges.write(betiket[s1])
                        edges.write(" ")
                        edges.write(betiket[s2])
                        edges.write('\n')
                    iliski.append(s2)

            atr.append(cntr)
            fortas.append(iliski)

        if self.dlg.ui.checkbox_network_file.isChecked():
            edges.close()

        dst = sna

        # calculation of geodesic distance

        for mas in range(obj):
            for kas in range(obj - 1):
                fas = 1
                for sas in range(obj):
                    if (dst[mas][sas] == (kas + 1)) and (sas != mas):
                        iliski = fortas[sas]
                        size_of_list = len(iliski)
                        for sIndex in range(size_of_list):
                            tas = iliski[sIndex]
                            if (tas != mas) and ((dst[mas][tas] > (kas + 1)) or (dst[mas][tas] == 0)):
                                dst[mas][tas] = kas + 2
                                fas += 1
                if fas == 1:
                    break

        if self.dlg.ui.checkbox_geodes_matrix.isChecked():
            for mas in range(obj):
                geodesic.write(" ")
                geodesic.write(etiket[mas])
            geodesic.write('\n')
            for mas in range(obj):
                geodesic.write(etiket[mas])
                for kas in range(obj):
                    geodesic.write(" ")
                    geodesic.write(dst[mas][kas].__str__())
                geodesic.write('\n')
            geodesic.close()

        connectivity = []
        global_integration = []

        # calculation of space syntax parameters

        for s1 in range(obj):

            provider.getFeatures(QgsFeatureRequest().setFilterFid(s1).setSubsetOfAttributes([])).nextFeature(feat)

            td = 0
            locd = int(self.dlg.ui.param.text())
            deg3 = 0
            ld3 = 0
            cntrl = 0
            cnt = 0
            fobj = float(obj)

            dvl = (2 * (fobj * (math.log((fobj + 2) / 3, 2) - 1) + 1)) / ((fobj - 1) * (fobj - 2))

            for vas in range(obj):
                td = td + dst[s1][vas]
                if dst[s1][vas] == 1:
                    cnt += 1
                    cntrl += 1 / float(atr[vas])
                if dst[s1][vas] < locd:
                    ld3 = ld3 + dst[s1][vas]
                    deg3 += 1

            md = float(td) / (fobj - 1)
            ra = 2 * (md - 1) / (fobj - 2)
            rr = ra / dvl
            gint = 1 / rr

            fdeg3 = float(deg3)
            lmd = float(ld3) / (fdeg3 - 1)
            lra = 2 * (lmd - 1) / (fdeg3 - 2)

            ldvl = (2 * (fdeg3 * (math.log((fdeg3 + 2) / 3, 2) - 1) + 1)) / ((fdeg3 - 1) * (fdeg3 - 2))

            lrr = lra / ldvl
            lint = 1 / lrr

            layer.changeAttributeValue(feat.id(), nufi, s1 + 1)     # line number
            layer.changeAttributeValue(feat.id(), nufi + 1, cnt)    # connectivity
            layer.changeAttributeValue(feat.id(), nufi + 2, td)     # total depth
            layer.changeAttributeValue(feat.id(), nufi + 3, md)     # mean depth
            layer.changeAttributeValue(feat.id(), nufi + 4, gint)   # global integration
            layer.changeAttributeValue(feat.id(), nufi + 5, ld3)    # local depth
            layer.changeAttributeValue(feat.id(), nufi + 6, lint)   # local integration
            layer.changeAttributeValue(feat.id(), nufi + 7, cntrl)  # control

            connectivity.append(float(cnt))
            global_integration.append(gint)

        layer.commitChanges()

        # calculation of intelligibility value

        if self.dlg.ui.checkbox_intel_val.isChecked():
            intelvalue = getPearsonCorrelation(connectivity, global_integration)
            QMessageBox.information(self.iface.mainWindow(), "Result", "Intelligibility value: " + str(intelvalue))

        # check execution
        QMessageBox.information(self.iface.mainWindow(), "Result", "Time: " + str(time.time() - start_time))

# script for Pearson correlation function required to calculate intelligibility value


def getPearsonCorrelation(var1, var2):
    result = 0
    tot_sq_x = 0
    tot_sq_y = 0
    tot_coproduct = 0
    mean_x = 0
    mean_y = 0
    for i in range(len(var1)):
        mean_x += var1[i] / len(var1)
        mean_y += var2[i] / len(var1)
    for i in range(len(var1)):
        dlt_x = var1[i] - mean_x
        dlt_y = var2[i] - mean_y
        tot_sq_x += (dlt_x * dlt_x)
        tot_sq_y += (dlt_y * dlt_y)
        tot_coproduct += (dlt_x * dlt_y)
    result = tot_coproduct / (math.sqrt(tot_sq_x) * math.sqrt(tot_sq_y))
    return result
