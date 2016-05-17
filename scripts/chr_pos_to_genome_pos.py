#!/usr/bin/python

import negspy.coordinates as nc
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="""
    
    python chr_pos_to_genome_pos.py chr pos

    Convert a chromosome,position pair to a genome position. Assumes that the coordinates
    refer to the hg19 assembly.
""")

    parser.add_argument('chr', nargs=1)
    parser.add_argument('pos', nargs=1, type=int)
    parser.add_argument('-a', '--assembly', default='hg19')


    #parser.add_argument('-o', '--options', default='yo',
    #                     help="Some option", type='str')
    #parser.add_argument('-u', '--useless', action='store_true', 
    #                     help='Another useless option')

    args = parser.parse_args()

    print nc.chr_pos_to_genome_pos(args.chr[0], args.pos[0], args.assembly)
    

if __name__ == '__main__':
    main()


