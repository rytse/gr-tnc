#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Wed Mar 26 22:49:41 2014
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import pmt
import tnc
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.tnc_hdlc_framer_0 = tnc.hdlc_framer(preamble_length=50, postamble_length=7,verbose=False, use_scrambler=False)
        self.tnc_hdlc_deframer_0 = tnc.hdlc_deframer()
        self.tnc_ax25_framer_0 = tnc.ax25_framer(mycall="KI4MTT",destcall="KI4MTS",verbose=True)
        self.tnc_ax25_deframer_0 = tnc.ax25_deframer(mycall="KI4MTT",verbose=True)
        self.blocks_random_pdu_0 = blocks.random_pdu(50, 50)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, "packet_len")
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("TEST"), 1000)
        self.blocks_message_debug_0 = blocks.message_debug()

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.tnc_hdlc_deframer_0, 0))

        ##################################################
        # Asynch Message Connections
        ##################################################
        self.msg_connect(self.blocks_message_strobe_0, "strobe", self.blocks_random_pdu_0, "generate")
        self.msg_connect(self.blocks_random_pdu_0, "pdus", self.tnc_ax25_framer_0, "in")
        self.msg_connect(self.tnc_ax25_deframer_0, "out", self.blocks_message_debug_0, "print_pdu")
        self.msg_connect(self.tnc_ax25_framer_0, "out", self.tnc_hdlc_framer_0, "in")
        self.msg_connect(self.tnc_hdlc_framer_0, "out", self.blocks_pdu_to_tagged_stream_0, "pdus")
        self.msg_connect(self.tnc_hdlc_deframer_0, "out", self.tnc_ax25_deframer_0, "in")

# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()

