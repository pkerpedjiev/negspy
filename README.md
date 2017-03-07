## Example

Convert chromosome / position pairs to coordinates along the genome.

### Converting chromosome based coordinates to genome-based coordinates

Chromosome coordinates contain a chromsome and a position. Genome coordinates
just contain positions. They assume that each chromosome is laid down end to
end and thus require a chromsome ordering.

#### Command Line

```
[peter@dbmipkedjievmbp negspy] [master]$ chr_pos_to_genome_pos.py
chr2 10
249250631
```

#### API

```

Warning, GRCh37 is currently exactly the same hg19, except with chromosome names that match GRCh37 (e.g. "1" vs "chr1").

### API

```python
import negspy.coordinates as nc

print(nc.chr_pos_to_genome_pos('chr1', 1000, 'hg19')) # -> 1000
```

### Chromosome Ordering


```python
import negspy.coordinates as nc

print(nc.get_chromorder('hg19')) # -> ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY', 'chrM']
```

### Print the chromosome lengths

```python
python scripts/chrom_sizes.py hg19
```
...
```
cr1    249250621
chr2    243199373
chr3    198022430
chr4    191154276
chr5    180915260
chr6    171115067
chr7    159138663
chr8    146364022
chr9    141213431
chr10   135534747
chr11   135006516
chr12   133851895
chr13   115169878
chr14   107349540
chr15   102531392
chr16   90354753
chr17   81195210
chr18   78077248
chr19   59128983
chr20   63025520
chr21   48129895
chr22   51304566
chrX    155270560
chrY    59373566
chrM    16571
```

## Adding new assemblies

To add a new assembly, it's necessary to add a file called
`negspy/data/${ASSEMBLY/chromInfo.txt` to the root repo directory. this file
should contain chromosome names and sizes:


```
chr1	249250621
chr2	243199373
chr3	198022430
...
```

One can also add `negspy/data/${ASSEMBLY}/chromSizes.txt` which defines how the
chromosomes should be ordered if presented in a linear fashion. There's no
correct ordering, but for many assemblies convention dictates having the
numbered chromosomes first, followed by X, Y, M and the extra contigs. Example
from hg19:

```
chr1
chr2
chr3
chr4
chr5
chr6
chr7
chr8
chr9
chr10
chr11
chr12
chr13
chr14
chr15
chr16
chr17
chr18
chr20
chr19
chr22
chr21
chrX
chrY
chrM
...
```


