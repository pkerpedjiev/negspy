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

print(nc.get_chromorder('hg19')) # -> ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY', 'chrM']
```


### Chromosome Ordering
