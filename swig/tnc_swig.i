/* -*- c++ -*- */

#define TNC_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "tnc_swig_doc.i"

%{
#include "tnc/square_ff.h"
%}


%include "tnc/square_ff.h"
GR_SWIG_BLOCK_MAGIC2(tnc, square_ff);
