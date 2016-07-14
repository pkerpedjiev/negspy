import csv
import os.path as op

chromInfo = {}

for assembly in ['hg19', 'hg38', 'mm9']:
    chromInfo[assembly] = {}
    with open(op.join(op.dirname(__file__), 'data/{}/chromInfo.txt'.format(assembly)), 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        totalLength = 0

        for rec in reader:
            totalLength += int(rec[1])

            chromInfo[assembly][rec[0]] = totalLength - int(rec[1])

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
        raise KeyError('No chromosome lengths for assembly {}'.format(assembly))

    return chromInfo[assembly][chromosome] + nucleotide

