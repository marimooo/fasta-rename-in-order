#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from io import StringIO
import argparse
import csv

parser = argparse.ArgumentParser(description='Rename FASTA header in specific order.')
parser.add_argument('fasta', metavar='FASTA', nargs=1,
                     help='a original FASTA file')
parser.add_argument('file', metavar='file', nargs=1,
                     help='a file with new names in specific order, per line')
parser.add_argument('--version', action='version', version='v0.1')
args = parser.parse_args()

new_header = list()
with open(args.file[0], mode='r') as file:
    table = csv.reader(file)
    for row in table:
        new_header.append(row[0])
print(new_header)

new_seqs = list()

i=0
for record in SeqIO.parse(args.fasta[0], 'fasta'):
    new = new_header[0]
    new_seqs.append(SeqRecord(record.seq, id=new, description=""))
    i+=1

output = StringIO()
SeqIO.write(new_seqs, output, 'fasta')
print(output.getvalue())