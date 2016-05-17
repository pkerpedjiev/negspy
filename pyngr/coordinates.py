def chr_num_to_genome_num(chromosome, nucleotide, chromInfo):
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
    pass

