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
    coordinates refer to the hg19 assembly (unless otherwise specified).

    Example:

    2       NM_000014       chr12   -       9220303 9268825

    -> python scripts/chr_pos_to_genome_pos.py -c 3:5,3:6

    2       NM_000014       genome  -       2115405269      2115453791

    --------------------------------

    This also works with space-delimited fields:

    chr5    56765,56766

    ->python scripts/chr_pos_to_genome_pos.py -c 1:2

    genome  881683465,881683466

""")

    parser.add_argument('-a', '--assembly', default='hg19')
    parser.add_argument('-c', '--columns', default='1,2', 
            help="Which columns to translate to genome positions. "
            "Column pairs should be 1-based and separated by colons")

    #parser.add_argument('-u', '--useless', action='store_true', 
    #                     help='Another useless option')
    args = parser.parse_args()

    for line in sys.stdin:
        try:
            line_output = []
            line_parts = line.strip().split()
            translated_positions = {}
            translated_chroms = {}

            for translate_pair in [[int (y) for y in x.split(':')] for x in args.columns.split(',')]:
                # go through the pairs of columns that need to be translated to genome position
                # assume that the position column is comma separated list of values (although it doesn't
                # actually need to be)
                chrom,poss = line_parts[translate_pair[0]-1], line_parts[translate_pair[1]-1].strip(",").split(',')
                genome_pos = ",".join(map(str,[nc.chr_pos_to_genome_pos( chrom, int(pos), args.assembly) for pos in poss]))
                #line_output += [genome_pos]

                # note that we've translated these columns and shouldn't include them in the output
                translated_positions[translate_pair[1]-1] = genome_pos
                translated_chroms[translate_pair[0]-1] = chrom

            for i,part in enumerate(line_parts):
                if i in translated_chroms:
                    # replace chromosome identifiers (e.g. 'chr1') with 'genome' to indicate the positions
                    line_output += ['genome({})'.format(chrom)]
                elif i in translated_positions:
                    # this column used to contain a position so we need to replace it with a translated
                    # position
                    line_output += [translated_positions[i]]
                else:
                    # if this column didn't contain a translated position output it as is
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


