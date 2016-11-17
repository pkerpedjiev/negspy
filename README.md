## Example

Convert chromosome / position pairs to coordinates along the genome.

### Command Line

```
[peter@dbmipkedjievmbp negspy] [master]$ chr_pos_to_genome_pos.py
chr2 10
249250631
```

Or

```
[peter@dbmipkedjievmbp negspy] [master]$ chr_pos_to_genome_pos.py -c 1,2:3,4
chr2 10 chr1 100
249250631 100
```

### API

```python
import negspy.coordinates as nc

print(nc.chr_pos_to_genome_pos('chr1', 1000, 'hg19')) # -> 1000
```
