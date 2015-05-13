#!/usr/bin/python
# -*- coding: utf-8 -*-

import thread
import time
from xbee import ZigBee
import serial
import datetime
import Gnuplot
import Gnuplot.PlotItems
import Gnuplot.funcutils
import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
a = 0

real_time_plot = 0
PATH = '/home/pheonix/Desktop/Farm_Monitor/'
NODE_TXT_in = [0, '"'+PATH + 'NODE_1.txt"', '"'+PATH + 'NODE_2.txt"', '"'+PATH + 'NODE_3.txt"']
NODE_TXT = [0, PATH+'NODE_1.txt', PATH+'NODE_2.txt', PATH+'NODE_3.txt', PATH+'NODE_4.txt']
def plot():
    g = Gnuplot.Gnuplot(debug=0, persist=1 )
    g('set grid')
    g('set terminal wxt size 1700,800')

#     # g('set term png')
#     # g('set output "/home/pheonix/Desktop/output.png"')
    g('set xdata time')
    g('set style data lines')
    g('set timefmt "%d-%m-%Y-%H:%M:%S"')
    g('set format x "%d-%m-%H:%M"')
    g('set xlabel "Time"')
    g('set multiplot')
    g('set size 1,.33')
    g('set origin 0.0,0.66')
    g("set title 'MSP Supply Voltage (Volts)'")
    g('plot [] [] '+NODE_TXT_in[1]+' u 7:2 w lp title "VCC-1",'+NODE_TXT_in[2] +
      ' u 7:2 w lp title "VCC-2",'+NODE_TXT_in[3]+' u 7:2 w lp title "VCC-3"')
    g('set origin 0.0,0.33')
    g("set title 'LM35 Temperature (Deg C)'")
    g('plot [] [] '+NODE_TXT_in[1]+' u 7:6 w lp title "LM35-1",'+NODE_TXT_in[2] +
      ' u 7:6 w lp title "LM35-2",'+NODE_TXT_in[3]+' u 7:6 w lp title "LM35-3"')
    g('set origin 0.0,0.00')
    g("set title 'Light Intensity (%)'")
    g('plot [] [] '+NODE_TXT_in[1]+' u 7:4 w lp title "LIGHT-1",'+NODE_TXT_in[2] +
      ' u 7:4 w lp title "LIGHT-2",'+NODE_TXT_in[3]+' u 7:4 w lp title "LIGHT-3"')
def Tplot():
    g = Gnuplot.Gnuplot(debug=0, persist=1)
    g('set grid')
    g('set terminal wxt size 1700,800')

#     # g('set term png')
#     # g('set output "/home/pheonix/Desktop/output.png"')
    g('set xdata time')
    g('set style data lines')
    g('set timefmt "%d-%m-%Y-%H:%M:%S"')
    g('set format x "%d-%m-%H:%M"')
    g('set xlabel "Time"')
    g("set title 'LM35 Temperature (Deg C)'")
    g('plot [] [] '+NODE_TXT_in[1]+' u 7:6 w lp title "LM35-1",'+NODE_TXT_in[2] +
      ' u 7:6 w lp title "LM35-2",'+NODE_TXT_in[3]+' u 7:6 w lp title "LM35-3"')
def Vplot():
    g = Gnuplot.Gnuplot(debug=0, persist=1)
    g('set grid')
    g('set terminal wxt size 1700,800')


#     # g('set term png')
#     # g('set output "/home/pheonix/Desktop/output.png"')
    g('set xdata time')
    g('set style data lines')
    g('set timefmt "%d-%m-%Y-%H:%M:%S"')
    g('set format x "%d-%m-%H:%M"')
    g('set xlabel "Time"')
    g("set title 'MSP Supply Voltage (Volts)'")
    g('plot [] [] '+NODE_TXT_in[1]+' u 7:2 w lp title "VCC-1",'+NODE_TXT_in[2] +
      ' u 7:2 w lp title "VCC-2",'+NODE_TXT_in[3]+' u 7:2 w lp title "VCC-3"')
def Lplot():
    g = Gnuplot.Gnuplot(debug=0, persist=1)
    g('set grid')
    g('set terminal wxt size 1700,800')

#     # g('set term png')
#     # g('set output "/home/pheonix/Desktop/output.png"')
    g('set xdata time')
    g('set style data lines')
    g('set timefmt "%d-%m-%Y-%H:%M:%S"')
    g('set format x "%d-%m-%H:%M"')
    g('set xlabel "Time"')
    g("set title 'Light Intensity (%)'")
    g('plot [] [] '+NODE_TXT_in[1]+' u 7:4 w lp title "LIGHT-1",'+NODE_TXT_in[2] +
      ' u 7:4 w lp title "LIGHT-2",'+NODE_TXT_in[3]+' u 7:4 w lp title "LIGHT-3"')
def N1plot():
    g = Gnuplot.Gnuplot(debug=0, persist=1)
    g('set grid')
    g('set terminal wxt size 1700,800')

#     # g('set term png')
#     # g('set output "/home/pheonix/Desktop/output.png"')
    g('set xdata time')
    g('set style data lines')
    g('set timefmt "%d-%m-%Y-%H:%M:%S"')
    g('set format x "%d-%m-%H:%M"')
    g('set xlabel "Time"')
    g('set multiplot')
    g('set size 1,.33')
    g('set origin 0.0,0.66')
    g("set title 'MSP Supply Voltage (Volts)'")
    g('plot [] [] '+NODE_TXT_in[1]+' u 7:2 w lp title "VCC-1"')
    g('set origin 0.0,0.33')
    g("set title 'LM35 Temperature (Deg C)'")
    g('plot [] [] '+NODE_TXT_in[1]+' u 7:6 w lp title "LM35-1"')
    g('set origin 0.0,0.00')
    g("set title 'Light Intensity (%)'")
    g('plot [] [] '+NODE_TXT_in[1]+' u 7:4 w lp title "LIGHT-1"')
def N2plot():
    g = Gnuplot.Gnuplot(debug=0, persist=1)
    g('set grid')
    g('set terminal wxt size 1700,800')

#     # g('set term png')
#     # g('set output "/home/pheonix/Desktop/output.png"')
    g('set xdata time')
    g('set style data lines')
    g('set timefmt "%d-%m-%Y-%H:%M:%S"')
    g('set format x "%d-%m-%H:%M"')
    g('set xlabel "Time"')
    g('set multiplot')
    g('set size 1,.33')
    g('set origin 0.0,0.66')
    g("set title 'MSP Supply Voltage (Volts)'")
    g('plot [] [] '+NODE_TXT_in[2] +' u 7:2 w lp title "VCC-2"')
    g('set origin 0.0,0.33')
    g("set title 'LM35 Temperature (Deg C)'")
    g('plot [] [] '+NODE_TXT_in[2] + ' u 7:6 w lp title "LM35-2"')
    g('set origin 0.0,0.00')
    g("set title 'Light Intensity (%)'")
    g('plot [] [] '+NODE_TXT_in[2]+' u 7:4 w lp title "LIGHT-2"')
def N3plot():
    g = Gnuplot.Gnuplot(debug=0, persist=1)
    g('set grid')
    g('set terminal wxt size 1700,800')

#     # g('set term png')
#     # g('set output "/home/pheonix/Desktop/output.png"')
    g('set xdata time')
    g('set style data lines')
    g('set timefmt "%d-%m-%Y-%H:%M:%S"')
    g('set format x "%d-%m-%H:%M"')
    g('set xlabel "Time"')
    g('set multiplot')
    g('set size 1,.33')
    g('set origin 0.0,0.66')
    g("set title 'MSP Supply Voltage (Volts)'")
    g('plot [] [] '+NODE_TXT_in[3]+' u 7:2 w lp title "VCC-3"')
    g('set origin 0.0,0.33')
    g("set title 'LM35 Temperature (Deg C)'")
    g('plot [] [] '+NODE_TXT_in[3]+' u 7:6 w lp title "LM35-3"')
    g('set origin 0.0,0.00')
    g("set title 'Light Intensity (%)'")
    g('plot [] [] '+NODE_TXT_in[3]+' u 7:4 w lp title "LIGHT-3"')
def stop():
    global a
    if a==1:
        print "stop"

        a = 0
def real_time_plotting():
    global real_time_plot
    if real_time_plot == 1:
        real_time_plot = 0
    else:
        real_time_plot = 1
class Ui_Frame(object):
    def __init__(self,Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        #Frame.resize(1360, 700)
        Frame.resize(711, 441)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        Frame.setWindowIcon(QtGui.QIcon('/home/pheonix/Desktop/Farm_Monitor/Farm_Monitor_Icon.jpeg'))
        self.Stop_Button = QtGui.QPushButton(Frame)
        self.Stop_Button.setGeometry(QtCore.QRect(0, 0, 530, 71))
        self.Stop_Button.setObjectName(_fromUtf8("Stop_Button"))
        self.Start_Button = QtGui.QPushButton(Frame)
        self.Start_Button.setGeometry(QtCore.QRect(0, 0, 530, 71))
        self.Start_Button.setObjectName(_fromUtf8("Start_Button"))
        self.Configure_Button = QtGui.QPushButton(Frame)
        self.Configure_Button.setGeometry(QtCore.QRect(530, 0, 181, 71))
        self.Configure_Button.setObjectName(_fromUtf8("Configure_Button"))
        self.Exit_Button = QtGui.QPushButton(Frame)
        self.Exit_Button.setGeometry(QtCore.QRect(350, 370, 361, 71))
        self.Exit_Button.setObjectName(_fromUtf8("Exit_Button"))
        self.PLOT_Button = QtGui.QPushButton(Frame)
        self.PLOT_Button.setGeometry(QtCore.QRect(0, 370, 351, 71))
        self.PLOT_Button.setObjectName(_fromUtf8("PLOT_Button"))
        self.RealTimePlotcheckBox = QtGui.QCheckBox(Frame)
        self.RealTimePlotcheckBox.setGeometry(QtCore.QRect(0, 80, 171, 41))
        self.RealTimePlotcheckBox.setObjectName(_fromUtf8("RealTimePlotcheckBox"))
        self.LightIntencityButton = QtGui.QPushButton(Frame)
        self.LightIntencityButton.setGeometry(QtCore.QRect(0, 290, 171, 81))
        self.LightIntencityButton.setObjectName(_fromUtf8("LightIntencityButton"))
        self.VoltageButton = QtGui.QPushButton(Frame)
        self.VoltageButton.setGeometry(QtCore.QRect(0, 130, 171, 81))
        self.VoltageButton.setObjectName(_fromUtf8("VoltageButton"))
        self.TemperatureButton = QtGui.QPushButton(Frame)
        self.TemperatureButton.setGeometry(QtCore.QRect(0, 210, 171, 81))
        self.TemperatureButton.setObjectName(_fromUtf8("TemperatureButton"))
        self.NODE3Button = QtGui.QPushButton(Frame)
        self.NODE3Button.setGeometry(QtCore.QRect(530, 70, 181, 61))
        self.NODE3Button.setObjectName(_fromUtf8("NODE3Button"))
        self.NODE2Button = QtGui.QPushButton(Frame)
        self.NODE2Button.setGeometry(QtCore.QRect(350, 70, 181, 61))
        self.NODE2Button.setObjectName(_fromUtf8("NODE2Button"))
        self.NODE1Button = QtGui.QPushButton(Frame)
        self.NODE1Button.setGeometry(QtCore.QRect(170, 70, 181, 61))
        self.NODE1Button.setObjectName(_fromUtf8("NODE1Button"))
        self.widget = QtGui.QWidget(Frame)
        self.widget.setGeometry(QtCore.QRect(170, 130, 541, 241))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.N3_DeviceVoltage_LCD = QtGui.QLCDNumber(self.widget)
        self.N3_DeviceVoltage_LCD.setObjectName(_fromUtf8("N3_DeviceVoltage_LCD"))
        self.gridLayout.addWidget(self.N3_DeviceVoltage_LCD, 0, 2, 1, 1)
        self.N2_Temperature_LCD = QtGui.QLCDNumber(self.widget)
        self.N2_Temperature_LCD.setObjectName(_fromUtf8("N2_Temperature_LCD"))
        self.gridLayout.addWidget(self.N2_Temperature_LCD, 1, 1, 1, 1)
        self.N3_Light_LCD = QtGui.QLCDNumber(self.widget)
        self.N3_Light_LCD.setObjectName(_fromUtf8("N3_Light_LCD"))
        self.gridLayout.addWidget(self.N3_Light_LCD, 2, 2, 1, 1)
        self.N2_DeviceVoltage_LCD = QtGui.QLCDNumber(self.widget)
        self.N2_DeviceVoltage_LCD.setObjectName(_fromUtf8("N2_DeviceVoltage_LCD"))
        self.gridLayout.addWidget(self.N2_DeviceVoltage_LCD, 0, 1, 1, 1)
        self.N1_Light_LCD = QtGui.QLCDNumber(self.widget)
        self.N1_Light_LCD.setObjectName(_fromUtf8("N1_Light_LCD"))
        self.gridLayout.addWidget(self.N1_Light_LCD, 2, 0, 1, 1)
        self.N3_Temperature_LCD = QtGui.QLCDNumber(self.widget)
        self.N3_Temperature_LCD.setObjectName(_fromUtf8("N3_Temperature_LCD"))
        self.gridLayout.addWidget(self.N3_Temperature_LCD, 1, 2, 1, 1)
        self.N2_Light_LCD = QtGui.QLCDNumber(self.widget)
        self.N2_Light_LCD.setObjectName(_fromUtf8("N2_Light_LCD"))
        self.gridLayout.addWidget(self.N2_Light_LCD, 2, 1, 1, 1)
        self.N1_Temperature_LCD = QtGui.QLCDNumber(self.widget)
        self.N1_Temperature_LCD.setObjectName(_fromUtf8("N1_Temperature_LCD"))
        self.gridLayout.addWidget(self.N1_Temperature_LCD, 1, 0, 1, 1)
        self.N1_DeviceVoltage_LCD = QtGui.QLCDNumber(self.widget)
        self.N1_DeviceVoltage_LCD.setObjectName(_fromUtf8("N1_DeviceVoltage_LCD"))
        self.gridLayout.addWidget(self.N1_DeviceVoltage_LCD, 0, 0, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QObject.connect(self.Start_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start)
        QtCore.QObject.connect(self.Start_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Stop_Button.raise_)
        QtCore.QObject.connect(self.Stop_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), stop)
        QtCore.QObject.connect(self.Stop_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Start_Button.raise_)

        QtCore.QObject.connect(self.Configure_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), Frame.hide)
        QtCore.QObject.connect(self.Configure_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), gui_configure)

        QtCore.QObject.connect(self.PLOT_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), plot)
        QtCore.QObject.connect(self.NODE1Button, QtCore.SIGNAL(_fromUtf8("clicked()")), N1plot)
        QtCore.QObject.connect(self.NODE2Button, QtCore.SIGNAL(_fromUtf8("clicked()")), N2plot)
        QtCore.QObject.connect(self.NODE3Button, QtCore.SIGNAL(_fromUtf8("clicked()")), N3plot)
        QtCore.QObject.connect(self.TemperatureButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Tplot)
        QtCore.QObject.connect(self.VoltageButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Vplot)
        QtCore.QObject.connect(self.LightIntencityButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Lplot)
        QtCore.QObject.connect(self.RealTimePlotcheckBox,QtCore.SIGNAL(_fromUtf8("pressed()")),real_time_plotting)
        QtCore.QObject.connect(self.Exit_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), sys.exit)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        #QtCore.QObject.connect(Ou)
    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Farm Monitor", None))
        self.Start_Button.setText(_translate("Frame", "START", None))
        self.Stop_Button.setText(_translate("Frame", "STOP", None))
        self.Configure_Button.setText(_translate("Frame", "Configure", None))
        self.Exit_Button.setText(_translate("Frame", "EXIT", None))
        self.PLOT_Button.setText(_translate("Frame", "PLOT", None))
        self.RealTimePlotcheckBox.setText(_translate("Frame", "           Real Time Plot", None))
        self.LightIntencityButton.setText(_translate("Frame", " Light Intensity", None))
        self.VoltageButton.setText(_translate("Frame", "   Device Voltage", None))
        self.TemperatureButton.setText(_translate("Frame", "   Node  Temperature  ", None))
        self.NODE3Button.setText(_translate("Frame", "NODE 3", None))
        self.NODE2Button.setText(_translate("Frame", "NODE 2", None))
        self.NODE1Button.setText(_translate("Frame", "NODE 1", None))
    def start(self):
        global a
        if a==0:
            print "start"
            a = 1
            self.workThread = WorkThread()
            QtCore.QObject.connect(self.workThread, QtCore.SIGNAL("V[1]"), self.N1_DeviceVoltage_LCD.display)
            QtCore.QObject.connect(self.workThread, QtCore.SIGNAL("V[2]"), self.N2_DeviceVoltage_LCD.display)
            QtCore.QObject.connect(self.workThread, QtCore.SIGNAL("V[3]"), self.N3_DeviceVoltage_LCD.display)
            QtCore.QObject.connect(self.workThread, QtCore.SIGNAL("LM35[1]"), self.N1_Temperature_LCD.display)
            QtCore.QObject.connect(self.workThread, QtCore.SIGNAL("LM35[2]"), self.N2_Temperature_LCD.display)
            QtCore.QObject.connect(self.workThread, QtCore.SIGNAL("LM35[3]"), self.N3_Temperature_LCD.display)
            QtCore.QObject.connect(self.workThread, QtCore.SIGNAL("LDR[1]"), self.N1_Light_LCD.display)
            QtCore.QObject.connect(self.workThread, QtCore.SIGNAL("LDR[2]"), self.N2_Light_LCD.display)
            QtCore.QObject.connect(self.workThread, QtCore.SIGNAL("LDR[3]"), self.N3_Light_LCD.display)
            self.workThread.start()
class WorkThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
            g = Gnuplot.Gnuplot(debug=0, persist=1)
            NODE_ADD = [0, '\x00\x13\xa2\x00@\xbb\x00W', '\x00\x13\xa2\x00@\xb5\xb0\xc7', '\x00\x13\xa2\x00@\xb5\xb0\xc3']
            Un16BitAdd = '\xff\xfe'
            PATH = '/home/pheonix/Desktop/Farm_Monitor/'
            NODE_TXT_in = [0, '"'+PATH + 'NODE_1.txt"', '"'+PATH + 'NODE_2.txt"', '"'+PATH + 'NODE_3.txt"']
            NODE_TXT = [0, PATH+'NODE_1.txt', PATH+'NODE_2.txt', PATH+'NODE_3.txt', PATH+'NODE_4.txt']
            D = [0, datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%Y-%H:%M:%S'),
                 datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%Y-%H:%M:%S'),
                 datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%Y-%H:%M:%S')]
            V = [0, 'N /A', 'N /A', 'N /A']
            LDR = [0, 'NA', 'NA', 'NA']
            LM35 = [0, 'NA', 'NA', 'NA']
            PIR = ['0', '0', '0', '0']
            PIR_A = ['0', '0', '0', '0']
            Start_FID = '\x01'
            Data_FID = '\x02'
            Delay_FID = '\x03'
            PIR_FID = '\x04'
            ONtime_FID = '\x05'
            Activate_A_FID = '\x06'
            EofON_Alert_FID = '\x07'
            head = 0

            def plot():
                g('set grid')
        #     # g('set term png')
        #     # g('set output "/home/pheonix/Desktop/output.png"')
                g('set xdata time')
                g('set style data lines')
                g('set timefmt "%d-%m-%Y-%H:%M:%S"')
                g('set format x "%d-%m-%H:%M"')
                g('set xlabel "Time"')
                g('set multiplot')
                g('set size 1,.33')
                g('set origin 0.0,0.66')
                g("set title 'MSP Supply Voltage (Volts)'")
                g('plot [] [] '+NODE_TXT_in[1]+' u 7:2 w lp title "VCC-1",'+NODE_TXT_in[2] +
                  ' u 7:2 w lp title "VCC-2",'+NODE_TXT_in[3]+' u 7:2 w lp title "VCC-3"')
                g('set origin 0.0,0.33')
                g("set title 'LM35 Temperature (Deg C)'")
                g('plot [] [] '+NODE_TXT_in[1]+' u 7:6 w lp title "LM35-1",'+NODE_TXT_in[2] +
                  ' u 7:6 w lp title "LM35-2",'+NODE_TXT_in[3]+' u 7:6 w lp title "LM35-3"')
                g('set origin 0.0,0.00')
                g("set title 'Light Intensity (%)'")
                g('plot [] [] '+NODE_TXT_in[1]+' u 7:4 w lp title "LIGHT-1",'+NODE_TXT_in[2] +
                  ' u 7:4 w lp title "LIGHT-2",'+NODE_TXT_in[3]+' u 7:4 w lp title "LIGHT-3"')

            def clear_all():
                for i in range(1, 5, 1):
                    if i == 1:
                        f = open(NODE_TXT[1], 'w')
                    elif i == 2:
                        f = open(NODE_TXT[2], 'w')
                    elif i == 3:
                        f = open(NODE_TXT[3], 'w')
                    else:
                        f = open(NODE_TXT[4], 'w')
                    f.write('VCC ' + str(0))
                    f.write(' LDR ' + str(0))
                    f.write(' LM35 ' + str(0))
                    f.write('  ' + str(D[1]) + '\n')
                    f.write('VCC ' + str(0))
                    f.write(' LDR ' + str(0))
                    f.write(' LM35 ' + str(0))
                    f.write('  ' + str(D[1]) + '\n')

            def configure_sleep_time(minutes, node_add):
                if minutes > 200:
                    minutes = 200
                counter = int(minutes*325)
                counter_high = chr(counter/256)
                counter_low = chr(counter % 256)
                count = 'TAFD'+counter_high+counter_low
                xbee.tx(dest_addr_long=node_add, dest_addr=Un16BitAdd, data=count, frame_id=Delay_FID)

            def configure_pir_alert(status, seconds, node_add):
                if status == 'ON':
                    if seconds > 50:
                        seconds = 50
                    counter = int(seconds*5)
                    counter = chr(counter % 256)
                    count = 'TAFPS'+counter
                    xbee.tx(dest_addr_long=node_add, dest_addr=Un16BitAdd, data=count, frame_id=PIR_FID)
                elif status == 'OFF':
                    xbee.tx(dest_addr_long=node_add, dest_addr=Un16BitAdd, data='TAFPRT', frame_id=PIR_FID)

            def configure_on_time(milliseconds, node_add):
                if milliseconds > 500000:
                    seconds = 500000
                counter = int(seconds/8)
                counter_high = chr(counter/256)
                counter_low = chr(counter % 256)
                count = 'TAFO'+counter_high+counter_low
                xbee.tx(dest_addr_long=node_add, dest_addr=Un16BitAdd, data=count, frame_id=ONtime_FID)

            def configure_end_of_on_time(status, node_add):
                if status == 'ON':
                    xbee.tx(dest_addr_long=node_add, dest_addr=Un16BitAdd, data='TAFEAS', frame_id=Activate_A_FID)
                elif status == 'OFF':
                    xbee.tx(dest_addr_long=node_add, dest_addr=Un16BitAdd, data='TAFEAR', frame_id=Activate_A_FID)

            def terminal_print_node_data(node, p):
                if p == 0:
                    print '                Sampling Time        Device Voltage     Soil Temperature   Light Intensity'
                    p = 1
                print 'NODE', node, ':    ', D[node], '    ', V[node], 'Volts            ', LM35[node],\
                    '°C            ', LDR[node], '%            ', PIR[node]
                return p

            def process_node_data(node, p):
                PIR[node] = '0'
                PIR_A[node] = '0'
                V[node] = (ord(data['rf_data'][0]) * 256) + ord(data['rf_data'][1])
                if V[node] > 32000:
                    V[node] -= 32768
                    PIR_A[node] = str(1)
                V[node] /= 341.0  # Device Specific
                V[node] = str(V[node])
                V[node] = V[node][0:4]
                LDR[node] = (ord(data['rf_data'][2]) * 256) + ord(data['rf_data'][3])
                LDR[node] /= 10.0
                if LDR[node] > 100:
                    LDR[node] = 100
                LDR[node] = str(LDR[node])
                LM35[node] = (ord(data['rf_data'][4]) * 256) + ord(data['rf_data'][5])
                if LM35[node] > 32000:
                    LM35[node] -= 32768
                    PIR[node] = str(1)
                LM35[node] = str((150*LM35[node])/1023)
                D[node] = datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%Y-%H:%M:%S')
                f = open(NODE_TXT[node], 'a')
                f.write('VCC ' + V[node])
                f.write(' LDR1 ' + LDR[node])
                f.write(' LM35 ' + LM35[node])
                f.write('  ' + str(D[node]) + ' PIR ' + PIR[node] + '\n')
                if PIR[node] == '1'and PIR_A[node] == '1':
                    at = datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%Y-%H:%M:%S')
                    print '\n                          Motion Detected at', at, '\n'
                    p = 0
                elif PIR[node] == '1':
                    print '\n                          Motion Detected in past sleep period\n'
                    p = 0
                p = terminal_print_node_data(node, p)
                return p
            global a
            while True:
                while a == 1:
                    print 'Starting UP'
                    serial_port = serial.Serial('/dev/ttyUSB0', 9600)
                    xbee = ZigBee(serial_port)
                    data = xbee.wait_read_frame()
        #           #       clear_all()

                    #configure_sleep_time(120, NODE_ADD[1])
                    #configure_on_time(100, NODE_ADD[1])

                    #configure_sleep_time(120, NODE_ADD[2])
                    #configure_on_time(100, NODE_ADD[2])

                    #configure_sleep_time(120, NODE_ADD[3])
                    #configure_on_time(100, NODE_ADD[3])

                    global a
                    print 'a=', a
                    while a == 1:
                        print 'New Sample Arrived'
                        try:
                            if data['id'] == 'rx':
                                if data['rf_data'][6] == Start_FID:
                                    if data['source_addr_long'] == NODE_ADD[1]:
                                        print '                       STARTING NODE 1'
                                        head = 0
                                    elif data['source_addr_long'] == NODE_ADD[2]:
                                        print '                       STARTING NODE 2'
                                        head = 0
                                    elif data['source_addr_long'] == NODE_ADD[3]:
                                        print '                       STARTING NODE 3'
                                        head = 0
                                elif data['rf_data'][6] == Data_FID:
                                    if data['source_addr_long'] == NODE_ADD[1]:
                                        head = process_node_data(1, head)
                                    elif data['source_addr_long'] == NODE_ADD[2]:
                                        head = process_node_data(2, head)
                                    elif data['source_addr_long'] == NODE_ADD[3]:
                                        head = process_node_data(3, head)
                                    else:
                                        print data
                                    global real_time_plot
                                    print real_time_plot
                                    if real_time_plot == 1:
                                        plot()
                                elif data['rf_data'][6] == EofON_Alert_FID:
                                    if data['source_addr_long'] == NODE_ADD[1]:
                                        print '                       NODE_1 to Sleep Mode'
                                        head = 0
                                    elif data['source_addr_long'] == NODE_ADD[2]:
                                        print '                       NODE_2 to Sleep Mode'
                                        head = 0
                                    elif data['source_addr_long'] == NODE_ADD[3]:
                                        print '                       NODE_3 to Sleep Mode'
                                else:
                                    print data
                                    head = 0
                            elif data['id'] == 'tx_status':
                                if (data['frame_id'] == Delay_FID) & (data['deliver_status'] == '\x00'):
                                    print "\n                          Successfully Updated Sleep Time Delay\n"
                                    head = 0
                                elif (data['frame_id'] == PIR_FID) & (data['deliver_status'] == '\x00'):
                                    print "\n                          Successfully Updated PIR Configuration\n"
                                    head = 0
                                elif (data['frame_id'] == ONtime_FID) & (data['deliver_status'] == '\x00'):
                                    print "\n                          Successfully Updated ON Time Delay\n"
                                    head = 0
                                elif (data['frame_id'] == Activate_A_FID) & (data['deliver_status'] == '\x00'):
                                    print "\n                          Successfully Updated End of ON Time Alert\n"
                                    head = 0
                                else:
                                    print data
                                    head = 0
                            else:
                                print data
                                head = 0
                            global VN1
                            VN1 = V[1]
                            self.emit( QtCore.SIGNAL('V[1]'), V[1])
                            self.emit( QtCore.SIGNAL('V[2]'), V[2])
                            self.emit( QtCore.SIGNAL('V[3]'), V[3])
                            self.emit( QtCore.SIGNAL('LDR[1]'), LDR[1])
                            self.emit( QtCore.SIGNAL('LDR[2]'), LDR[2])
                            self.emit( QtCore.SIGNAL('LDR[3]'), LDR[3])
                            self.emit( QtCore.SIGNAL('LM35[1]'), LM35[1])
                            self.emit( QtCore.SIGNAL('LM35[2]'), LM35[2])
                            self.emit( QtCore.SIGNAL('LM35[3]'), LM35[3])
                            data = xbee.wait_read_frame()

                        except a != 1:
                            serial_port.close()
                            break

                    print 'Stopping'

class Ui_Frame_1(object):
    def __init__(self,Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(711, 441)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.OK_Button = QtGui.QPushButton(Frame)
        self.OK_Button.setGeometry(QtCore.QRect(0, 350, 350, 71))
        self.OK_Button.setObjectName(_fromUtf8("OK_Button"))
        self.Cancel_Button = QtGui.QPushButton(Frame)
        self.Cancel_Button.setGeometry(QtCore.QRect(350, 350, 350, 71))
        self.Cancel_Button.setObjectName(_fromUtf8("Cancel_Button"))

        self.checkBox_N1_ON = QtGui.QCheckBox(Frame)
        self.checkBox_N1_ON.setGeometry(QtCore.QRect(41, 95, 139, 23))
        self.checkBox_N1_ON.setObjectName(_fromUtf8("checkBox_N1_ON"))
        self.checkBox_N2_ON = QtGui.QCheckBox(Frame)
        self.checkBox_N2_ON.setGeometry(QtCore.QRect(266, 95, 139, 23))
        self.checkBox_N2_ON.setObjectName(_fromUtf8("checkBox_N2_ON"))
        self.checkBox_N3_ON = QtGui.QCheckBox(Frame)
        self.checkBox_N3_ON.setGeometry(QtCore.QRect(491, 95, 139, 23))
        self.checkBox_N3_ON.setObjectName(_fromUtf8("checkBox_N3_ON"))
        self.checkBox_N1_SLEEP = QtGui.QCheckBox(Frame)
        self.checkBox_N1_SLEEP.setGeometry(QtCore.QRect(41, 199, 154, 23))
        self.checkBox_N1_SLEEP.setObjectName(_fromUtf8("checkBox_N1_SLEEP"))
        self.checkBox_N2_SLEEP = QtGui.QCheckBox(Frame)
        self.checkBox_N2_SLEEP.setGeometry(QtCore.QRect(266, 199, 154, 23))
        self.checkBox_N2_SLEEP.setObjectName(_fromUtf8("checkBox_N2_SLEEP"))
        self.checkBox_N3_SLEEP = QtGui.QCheckBox(Frame)
        self.checkBox_N3_SLEEP.setGeometry(QtCore.QRect(491, 199, 154, 23))
        self.checkBox_N3_SLEEP.setObjectName(_fromUtf8("checkBox_N3_SLEEP"))
        self.spinBox_N3_ON = QtGui.QSpinBox(Frame)
        self.spinBox_N3_ON.setGeometry(QtCore.QRect(540, 147, 61, 23))
        self.spinBox_N3_ON.setObjectName(_fromUtf8("spinBox_N3_ON"))
        self.spinBox_N1_SLEEP = QtGui.QSpinBox(Frame)
        self.spinBox_N1_SLEEP.setGeometry(QtCore.QRect(90, 251, 61, 23))
        self.spinBox_N1_SLEEP.setObjectName(_fromUtf8("spinBox_N1_SLEEP"))
        self.spinBox_N2_SLEEP = QtGui.QSpinBox(Frame)
        self.spinBox_N2_SLEEP.setGeometry(QtCore.QRect(320, 251, 61, 23))
        self.spinBox_N2_SLEEP.setObjectName(_fromUtf8("spinBox_N2_SLEEP"))
        self.spinBox_N3_SLEEP = QtGui.QSpinBox(Frame)
        self.spinBox_N3_SLEEP.setGeometry(QtCore.QRect(540, 251, 61, 23))
        self.spinBox_N3_SLEEP.setObjectName(_fromUtf8("spinBox_N3_SLEEP"))
        self.spinBox_N1_ON = QtGui.QSpinBox(Frame)
        self.spinBox_N1_ON.setGeometry(QtCore.QRect(90, 147, 61, 23))
        self.spinBox_N1_ON.setObjectName(_fromUtf8("spinBox_N1_ON"))
        self.spinBox_N2_ON = QtGui.QSpinBox(Frame)
        self.spinBox_N2_ON.setGeometry(QtCore.QRect(320, 147, 61, 23))
        self.spinBox_N2_ON.setObjectName(_fromUtf8("spinBox_N2_ON"))

        self.retranslateUi(Frame)
        QtCore.QObject.connect(self.OK_Button, QtCore.SIGNAL(_fromUtf8("pressed()")), gui)
        QtCore.QObject.connect(self.Cancel_Button, QtCore.SIGNAL(_fromUtf8("pressed()")), gui)

        QtCore.QObject.connect(self.OK_Button, QtCore.SIGNAL(_fromUtf8("pressed()")), Frame.hide)
        QtCore.QObject.connect(self.Cancel_Button, QtCore.SIGNAL(_fromUtf8("pressed()")), Frame.hide)

        QtCore.QObject.connect(self.checkBox_N1_ON, QtCore.SIGNAL(_fromUtf8("pressed()")), N1ON)
        QtCore.QObject.connect(self.checkBox_N2_ON, QtCore.SIGNAL(_fromUtf8("pressed()")), N2ON)
        QtCore.QObject.connect(self.checkBox_N3_ON, QtCore.SIGNAL(_fromUtf8("pressed()")), N3ON)
        QtCore.QObject.connect(self.checkBox_N1_SLEEP, QtCore.SIGNAL(_fromUtf8("pressed()")), N1SL)
        QtCore.QObject.connect(self.checkBox_N2_SLEEP, QtCore.SIGNAL(_fromUtf8("pressed()")), N2SL)
        QtCore.QObject.connect(self.checkBox_N3_SLEEP, QtCore.SIGNAL(_fromUtf8("pressed()")), N3SL)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.checkBox_N1_ON.setText(_translate("Frame", "NODE 1    ON Time", None))
        self.checkBox_N2_ON.setText(_translate("Frame", "NODE 2    ON Time", None))
        self.checkBox_N3_ON.setText(_translate("Frame", "NODE 3    ON Time", None))
        self.checkBox_N1_SLEEP.setText(_translate("Frame", "NODE 1    SLEEP Time", None))
        self.checkBox_N2_SLEEP.setText(_translate("Frame", "NODE 2    SLEEP Time", None))
        self.checkBox_N3_SLEEP.setText(_translate("Frame", "NODE 3    SLEEP Time", None))

        self.OK_Button.setText(_translate("Frame", "OK", None))
        self.Cancel_Button.setText(_translate("Frame", "Cancel", None))

def N1ON():
    print 'N1ON'
def N2ON():
    print 'N2ON'
def N3ON():
    print 'N3ON'
def N1SL():
    print 'N1SL'
def N2SL():
    print 'N2SL'
def N3SL():
    print 'N3SL'




def gui():
    Frame.show()
def gui_configure():
    Frame_1.show()
def gui_configure_exit():
    Frame_1.leaveEvent(Frame_1)
try:
    #thread.start_new_thread(gui, ())
    #thread.start_new_thread(acquire_data, ("Thread-2",))
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame(Frame)
    Frame_1 = QtGui.QFrame()
    ui_1 = Ui_Frame_1(Frame_1)
    gui()
    sys.exit(app.exec_())
except a==0:
    print "Error: unable to start thread"
while 1:
    pass
