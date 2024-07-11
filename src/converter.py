#!/usr/bin/env python3

import logging
import streamlit as st
from io import StringIO
import pypandoc
from transcript_formatter import TranscriptFormatter

FILE_EXT = '.txt'
FILE_SUFFIX_LINES = '_lines'
FILE_SUFFIX_BLOCK = '_block'
FILE_SUFFIX_PARA = '_para'

def convert(file_suffix, format_func, container):
    filename = st.session_state.base_filename + file_suffix + FILE_EXT
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(format_func())
    container.write('Downloaded file {f}'.format(f=filename))

def btn_lines_clicked(container):
    convert(FILE_SUFFIX_LINES, st.session_state.tf.to_lines, container)

def btn_block_clicked(container):
    convert(FILE_SUFFIX_BLOCK, st.session_state.tf.to_block, container)

def btn_para_clicked(container):
    convert(FILE_SUFFIX_PARA, st.session_state.tf.to_paragraphs, container)

def btn_all_clicked(container):
    btn_lines_clicked(container)
    btn_block_clicked(container)
    btn_para_clicked(container)

def vtt_file_changed():
    print('vtt_file_changed() called')
    st.session_state.vtt_file_changed = True

st.session_state.vtt_file = st.file_uploader(label='Upload transcript file',
                                             on_change=vtt_file_changed)
if not st.session_state.vtt_file:
    st.stop()

if 'vtt_file_changed' in st.session_state and st.session_state.vtt_file_changed:
    # Read file contents into string
    print(st.session_state.vtt_file)
    filename = st.session_state.vtt_file.name
    if filename.rsplit('.')[-1] == 'docx':
        vtt_text = pypandoc.convert_file(filename, 'plain', format='docx')
    else:
        stringio = StringIO(st.session_state.vtt_file.getvalue().decode('utf-8'))
        vtt_text = stringio.read()
    st.session_state.base_filename = filename.split('.')[0]
    st.session_state.tf = TranscriptFormatter(vtt_text)
    st.session_state.vtt_file_changed = False

# Container: widgets for lines
con_lines = st.container(border=True)
con_lines.button(label='Convert to lines',
                 key='btn_lines',
                 on_click=btn_lines_clicked,
                 kwargs=dict(container=con_lines))

# Container: widgets for block
con_block = st.container()
con_block.button(label='Convert to block',
                 key='btn_block',
                 on_click=btn_block_clicked,
                 kwargs=dict(container=con_block))

con_para = st.container()
con_para.button(label='Convert to paragraphs',
                key='btn_para',
                on_click=btn_para_clicked,
                kwargs=dict(container=con_para))

con_all = st.container()
con_all.button(label='Convert to all formats',
               key='btn_all',
               on_click=btn_all_clicked,
               kwargs=dict(container=con_all))
