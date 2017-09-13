import csv
import os
import os.path as op
import numpy as np

class ChromosomeInfo:
    def __init__(self, name):
        self.name = name
        self.total_length = 0
        self.cum_chrom_lengths = {}
        self.chrom_lengths = {}
        self.chrom_order = []

chromInfo = {}
cumChromSizes = {}

def available_chromsizes():
    '''
    List the assemblies for which we have chromosome sizes.

    All size files should be stored in data/{assembly}/chromInfo.txt
    '''
    available_assemblies = []

    for assembly in os.listdir(op.join(op.dirname(__file__), 'data/')):
        if op.exists(op.join(op.dirname(__file__), 'data/', assembly, 'chromInfo.txt')):
            available_assemblies += [assembly]

    return available_assemblies

def get_chromorder_from_file(filename):
    with open(filename, 'r') as f:
        chroms = [l.strip().split()[0] for l in f.readlines()]
    
        return chroms

def get_chromorder(assembly):
    chrominfo_filename = op.join(op.dirname(__file__), 'data/{}/chromInfo.txt'.format(assembly))

    return get_chromorder_from_file(chrominfo_filename)


def get_chromsizes_from_file(filename):
    order = get_chromorder_from_file(filename)
    chrominfo = get_chrominfo_from_file(filename)

    sizes = [chrominfo.chrom_lengths[o] for o in order]

    return sizes

def get_chromsizes(assembly):
    order = get_chromorder(assembly)
    chrominfo = get_chrominfo(assembly)

    sizes = [chrominfo.chrom_lengths[o] for o in order]
    return sizes

def get_chrominfo_from_file(filename, assembly = None):
    with open(filename, 'r') as f:
        chrom_info = ChromosomeInfo(assembly if assembly is not None else filename)
        reader = csv.reader(f, delimiter='\t')
        totalLength = 0

        for rec in reader:
            totalLength += int(rec[1])

            chrom_info.cum_chrom_lengths[rec[0]] = totalLength - int(rec[1])
            chrom_info.chrom_lengths[rec[0]] = int(rec[1])
            chrom_info.chrom_order += [rec[0]]

        chrom_info.total_length = totalLength
    return chrom_info

def get_chrominfo(assembly):
    filename = op.join(op.dirname(__file__), 'data/{}/chromInfo.txt'.format(assembly))

    return get_chrominfo_from_file(filename, assembly=assembly)

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
    if assembly not in cumChromSizes:
        cumChromSizes[assembly] = dict(zip(get_chromorder(assembly),
            np.cumsum([0] + get_chromsizes(assembly))[:-1]))

    return cumChromSizes[assembly][chromosome] + nucleotide
