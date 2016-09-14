import negspy.coordinates as nc

def test_chr_pos_to_genome_pos():
    assert(nc.chr_pos_to_genome_pos('chr1', 100) == 100)
    assert(nc.chr_pos_to_genome_pos('chr2', 100) == 249250621 + 100)
    
