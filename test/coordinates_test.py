import negspy.coordinates as nc

def test_chr_pos_to_genome_pos():
    assert(nc.chr_pos_to_genome_pos('chr1', 100) == 100)
    assert(nc.chr_pos_to_genome_pos('chr2', 100) == 249250621 + 100)
    assert(nc.chr_pos_to_genome_pos('1', 100, 'grch37') == 100)

def test_chr_pos_to_chromorder():
    print("chromSizes:",
            nc.chr_pos_to_genome_pos('chr6', 0))

    assert(nc.chr_pos_to_genome_pos('chr6', 0) ==
            1062541960)
    assert(nc.chr_pos_to_genome_pos('chr7', 0) ==
            1233657027)
    assert(nc.chr_pos_to_genome_pos('chr8', 0) ==
            1392795690)
    
def test_chrom_order():
    assert(nc.get_chromorder('hg19')[0] == 'chr1')
    assert(nc.get_chromorder('hg19')[-1] == 'chrM')

def test_chrom_sizes():
    assert(nc.get_chromsizes('hg19')[0] == 249250621)
    assert(nc.get_chromsizes('hg19')[1] == 243199373)

