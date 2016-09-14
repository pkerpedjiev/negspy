#!/usr/bin/python

import Bio.SeqIO as bsio
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="""
    
    python create_chrominfo.py [genome.fa/-]

    Create a chrominfo file for a genome
""")

    #parser.add_argument('argument', nargs=1)
    parser.add_argument('fasta_file')

    args = parser.parse_args()

    if args.fasta_file == '-':
        f = sys.stdin
    else:
        f = open(args.fasta_file, 'r')

    fseq = bsio.parse(f, 'fasta')

    #parser.add_argument('argument', nargs=1)
    #parser.add_argument('-o', '--options', default='yo',
    #					 help="Some option", type='str')
    #parser.add_argument('-u', '--useless', action='store_true', 
    #					 help='Another useless option')
    for record in fseq:
        print("{}\t{}".format(record.id, len(record.seq)))

    args = parser.parse_args()

    

if __name__ == '__main__':
    main()


