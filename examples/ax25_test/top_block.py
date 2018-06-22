#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Jun 22 17:37:35 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import math
import pmt
import sip
import sys
import tnc


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250e3

        ##################################################
        # Blocks
        ##################################################
        self.tnc_hdlc_framer_0 = tnc.hdlc_framer(preamble_length=50, postamble_length=7,verbose=False, use_scrambler=False)
        self.tnc_hdlc_deframer_0 = tnc.hdlc_deframer()
        self.tnc_ax25_framer_0 = tnc.ax25_framer(mycall="KI4MTT",destcall="KI4MTS",verbose=True)
        self.tnc_ax25_deframer_0 = tnc.ax25_deframer(mycall="KI4MTT",verbose=True)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=96,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=250,
                decimation=96,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=2,
        	bt=0.35,
        	verbose=False,
        	log=False,
        )
        self.digital_gmsk_demod_0 = digital.gmsk_demod(
        	samples_per_symbol=10,
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.blocks_unpacked_to_packed_xx_0 = blocks.unpacked_to_packed_bb(1, gr.GR_MSB_FIRST)
        self.blocks_random_pdu_0 = blocks.random_pdu(50, 50, chr(0xFF), 2)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, "packet_len")
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("TEST"), 500)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(1)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(-200, 0.1, 0, True)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.blocks_random_pdu_0, 'generate'))    
        self.msg_connect((self.blocks_random_pdu_0, 'pdus'), (self.tnc_ax25_framer_0, 'in'))    
        self.msg_connect((self.tnc_ax25_deframer_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))    
        self.msg_connect((self.tnc_ax25_framer_0, 'out'), (self.tnc_hdlc_framer_0, 'in'))    
        self.msg_connect((self.tnc_hdlc_deframer_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))    
        self.msg_connect((self.tnc_hdlc_deframer_0, 'out'), (self.tnc_ax25_deframer_0, 'in'))    
        self.msg_connect((self.tnc_hdlc_framer_0, 'out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))    
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.digital_gmsk_demod_0, 0))    
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.blocks_unpacked_to_packed_xx_0, 0))    
        self.connect((self.blocks_unpacked_to_packed_xx_0, 0), (self.digital_gmsk_mod_0, 0))    
        self.connect((self.digital_gmsk_demod_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.digital_gmsk_demod_0, 0), (self.tnc_hdlc_deframer_0, 0))    
        self.connect((self.digital_gmsk_mod_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_pwr_squelch_xx_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_quadrature_demod_cf_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_complex_to_mag_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
