# pbbs-characterization-gem5

Experiments and analysis for characterizing PBBS benchmarks on single-core systems using gem5.

Evaluates how input size, processor type (in-order vs. out-of-order), and cache hierarchy affect PBBS workload behavior. 
All experiments were run on gem5 using Python automation and post-processed with matplotlib.

## Built With

[![Python][python-shield]][python-url]  
[![gem5][gem5-shield]][gem5-url]  
[![Matplotlib][matplotlib-shield]][matplotlib-url]  
[![NumPy][numpy-shield]][numpy-url]

## Contents

- `analysis/`: data parsing and plotting code
- `benchmarks/`: benchmarking binary files
- `data/`: simulation outputs
- `inputs/`: generated simulation inputs
- `scripts/`: python simulation scripts

> The gem5 binaries used in these experiments can be found at [gem5.org](https://www.gem5.org).


## Experiments
### Exploration 1: Input Size Scaling
Analyzes how runtime and instruction mix change as input size increases.

### Exploration 2: In-order vs Out-of-order
Compares MinorCPU and O3CPU across benchmarks to assess ILP sensitivity.

### Exploration 3: Cache Hierarchy Sweeps
Tests different cache designs (SIMPLE, HARVARD, BIG_L1D, L2) and analyzes sensitivity.

<!-- MARKDOWN LINKS & IMAGES -->
[python-shield]: https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/

[gem5-shield]: https://img.shields.io/badge/gem5-orange?style=for-the-badge&logo=gnu&logoColor=white
[gem5-url]: https://www.gem5.org/

[matplotlib-shield]: https://img.shields.io/badge/Matplotlib-ff69b4.svg?style=for-the-badge&logo=plotly&logoColor=white
[matplotlib-url]: https://matplotlib.org/

[numpy-shield]: https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[numpy-url]: https://numpy.org/
