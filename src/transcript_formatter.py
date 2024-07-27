#!/usr/bin/env python3

import logging
import re

SENTENCES_PER_PARA = 5

class TranscriptFormatter:

    def __init__(self, vtt_text):
        logging.info('Initializing TranscriptFormatter')
        # Normalize line endings
        self.vtt = vtt_text.replace('\r\n', '\n').replace('\r', '\n')
        self.lines = None
        self.block = None
        self.paragraphs = None

    def to_lines(self):
        if self.lines:
            return self.lines
        
        logging.info('Converting to lines')
        lines = self.vtt.split('\n')
        # Remove the first line 'WEBVTT', blank lines, and ones with timestamps
        self.lines = '\n'.join(line for line in lines
                               if line
                               and line.find('WEBVTT') < 0
                               and line.find('-->') < 0)
        return self.lines
    
    def to_block(self):
        if self.block:
            return self.block
        if not self.lines:
            self.to_lines()

        logging.info('Converting to block')
        # Remove newlines between lines
        self.block = self.lines.replace('\n', ' ')
        # Remove multiple contiguous spaces
        re.sub(r'\s+', ' ', self.block)
        return self.block
    
    def to_paragraphs(self):
        if self.paragraphs:
            return self.paragraphs
        if not self.block:
            self.to_block()
    
        logging.info('Converting to paragraphs')
        # Split the text into sentences using a regular expression
        # Note: Sentences are not the same as lines
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',
                             self.block)
        # Group sentences into paragraphs
        paragraphs = [' '.join(sentences[i:i+SENTENCES_PER_PARA])
                      for i in range(0, len(sentences), SENTENCES_PER_PARA)]

        self.paragraphs = '\n\n'.join(paragraphs)
        return self.paragraphs
