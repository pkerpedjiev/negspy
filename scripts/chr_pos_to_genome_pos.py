#!/usr/bin/python
from __future__ import print_function

import negspy.coordinates as nc
import sys
import argparse

from itertools import tee

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

def main():
    parser = argparse.ArgumentParser(description="""
    
    python chr_pos_to_genome_pos.py -t 1,2:3,4

    Convert chromosome,position pairs to genome_positions. Assumes that the
    coordinates refer to the hg19 assembly.

""")

    parser.add_argument('-a', '--assembly', default='hg19')
    parser.add_argument('-c', '--columns', default='1,2', 
            help="Which columns to translate to genome positions. Column pairs should be separated by colons")

    #parser.add_argument('-u', '--useless', action='store_true', 
    #                     help='Another useless option')
    args = parser.parse_args()

    for line in sys.stdin:
        try:
            line_output = []
            line_parts = line.strip().split()
            translated = set()
            for translate_pair in [[int (y) for y in x.split(',')] for x in args.columns.split(':')]:
                # go through the pairs of columns that need to be translated to genome position
                chrom,pos = line_parts[translate_pair[0]-1], line_parts[translate_pair[1]-1]
                genome_pos = nc.chr_pos_to_genome_pos( chrom, int(pos), args.assembly)
                line_output += [genome_pos]

                # note that we've translated these columns and shouldn't include them in the output
                translated.add(translate_pair[0]-1)
                translated.add(translate_pair[1]-1)

            for i,part in enumerate(line_parts):
                if i not in translated:
                    line_output += [part]

            try:
                print("\t".join(map(str, line_output)))
            except BrokenPipeError:
                # Output is probably being run through "head" or something similar
                break
        except KeyError as ke:
            print("KeyError:", ke, line.strip(), file=sys.stderr)
    

if __name__ == '__main__':
    main()


