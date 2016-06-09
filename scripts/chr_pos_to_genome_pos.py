#!/usr/bin/python

import negspy.coordinates as nc
import sys
import argparse

from itertools import tee, izip

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)

def main():
    parser = argparse.ArgumentParser(description="""
    
    python chr_pos_to_genome_pos.py 

    Convert chromosome,position pairs to genome_positions. Assumes that the
    coordinates refer to the hg19 assembly.

""")

    parser.add_argument('-a', '--assembly', default='hg19')


    parser.add_argument('-e', '--extra-columns', default='',
                         help="Some option", type=str)
    #parser.add_argument('-u', '--useless', action='store_true', 
    #                     help='Another useless option')
    args = parser.parse_args()

    for line in sys.stdin:
        try:
            line_output = []
            line_parts = line.strip().split()
            for chrom, pos in pairwise(line_parts):
                genome_pos = nc.chr_pos_to_genome_pos( chrom, int(pos), args.assembly)
                line_output += [genome_pos]
            for col in args.extra_columns.split(','):
                line_output += [line_parts[int(col)-1]]
            print "\t".join(map(str, line_output))
        except KeyError as ke:
            print >>sys.stderr, "KeyError:", ke, line.strip()
    

if __name__ == '__main__':
    main()


