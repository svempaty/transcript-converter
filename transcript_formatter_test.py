#!/usr/bin/env python3

from transcript_formatter import TranscriptFormatter

if __name__ == "__main__":
    vtt_file = 'output.vtt'
    with open(vtt_file) as file:
        text = file.read()
        tf = TranscriptFormatter(text)
        print('Lines: \n' + tf.to_lines() + '\n')
        print('Block: \n' + tf.to_block() + '\n')
        print('Paragraphs: \n' + tf.to_paragraphs())