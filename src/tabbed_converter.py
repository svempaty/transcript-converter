#!/usr/bin/env python3

import streamlit as st
from io import StringIO
from transcript_formatter import TranscriptFormatter


vtt_file = st.file_uploader("Upload transcript")
if not vtt_file:
    st.write('Upload a vtt file')
    exit()


# Read file contents into string
stringio = StringIO(vtt_file.getvalue().decode("utf-8"))
vtt_text = stringio.read()

tab_vtt, tab_lines, tab_block, tab_para = st.tabs(['VTT', 'Lines', 'Block', 'Para'])

tf = TranscriptFormatter(vtt_text)

with tab_vtt:
   st.text_area(label='vtt',
                label_visibility='collapsed',
                value=vtt_text,
                height=500)

with tab_lines:
    st.text_area(label='lines',
                 label_visibility='collapsed',
                 value=tf.to_lines(),
                 height=500)

with tab_block:
    st.text_area(label='block',
                 label_visibility='collapsed',
                 value=tf.to_block(),
                 height=500)

with tab_para:
    st.text_area(label='para',
                 label_visibility='collapsed',
                 value=tf.to_paragraphs(),
                 height=500)