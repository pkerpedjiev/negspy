#!/usr/bin/python

import negspy.coordinates as nc
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="""
    
    python chrom_sizes.py assembly

    Print the chromosome sizes for the given assembly.
""")

    parser.add_argument('assembly')
    #parser.add_argument('argument', nargs=1)
    #parser.add_argument('-o', '--options', default='yo',
    #					 help="Some option", type='str')
    #parser.add_argument('-u', '--useless', action='store_true', 
    #					 help='Another useless option')

    args = parser.parse_args()

    for chr in nc.get_chromorder(args.assembly):
        print chr + "\t" + str(nc.get_chrominfo('hg19').chrom_lengths[chr])

    

if __name__ == '__main__':
    main()


