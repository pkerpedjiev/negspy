import negspy.coordinates as nc

def test_chr_pos_to_genome_pos():
    '''
    Test the coordinate conversion script.
    '''
    genome_coord = nc.chr_pos_to_genome_pos('chr1', 10)

    assert(genome_coord == 10)

    genome_coord = nc.chr_pos_to_genome_pos('chr2', 10)

    assert(genome_coord == 249250631)
