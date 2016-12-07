import csv
import os.path as op

class ChromosomeInfo:
    def __init__(self, name):
        self.name = name
        self.total_length = 0
        self.cum_chrom_lengths = {}

chromInfo = {}

def get_chromorder(assembly):
    with open(op.join(op.dirname(__file__), 'data/{}/chromOrder.txt'.format(assembly)), 'r') as f:
        chroms = [l.strip() for l in f.readlines()]
    
        return chroms

def get_chrominfo(assembly):
    with open(op.join(op.dirname(__file__), 'data/{}/chromInfo.txt'.format(assembly)), 'r') as f:
        chrom_info = ChromosomeInfo(assembly)
        reader = csv.reader(f, delimiter='\t')
        totalLength = 0

        for rec in reader:
            totalLength += int(rec[1])

            chrom_info.cum_chrom_lengths[rec[0]] = totalLength - int(rec[1])

        chrom_info.total_length = totalLength
    return chrom_info

def chr_pos_to_genome_pos(chromosome, nucleotide, assembly='hg19'):
    '''
    Convert chromsome / nucleotide coordinates to genome coordinates.

    Example: chr1:10 -> 10
    Example: chr2:10 -> 247,249,729 

    Where the length of chromosome 1 is 247,249,719.

    :param chromosome: The name of a chromosome (i.e. chr1)
    :param nucleotide: The nucleotide number within the chromosome
    :param chromInfo: The lengths of all the chromosomes in the genome assembly
    :return: A single integer representing the position of the read if all the chromosomes were
             concatenated
    '''
    if assembly not in chromInfo.keys():
        chromInfo[assembly] = get_chrominfo(assembly)

    return chromInfo[assembly].cum_chrom_lengths[chromosome] + nucleotide

