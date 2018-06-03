# Python implementation of a genetic algorithm for FJSP.

Based on a paper written by Xinyu Li and Liang Gao [1].


## Code structure

The code has been designed to be read along the section 4 of this paper.

- Workflow of the proposed HA (4.1)
    - main.py
- Encoding and decoding (4.2)
    - encoding.py, decoding.py
- Genetic operators (4.3)
    - genetic.py
- Local search by tabu search (4.4)
    - This section has been ignored
- Terminate criteria (4.5)
    - termination.py

## Usage

To run the algorithm on the Mk02 problem from the Brandimarte data:

```
$ python3 main.py test_data/Brandimarte_Data/Text/Mk02.fjs 
```

Test data can be found on [this site](http://people.idsia.ch/~monaldo/fjsp.html).

## References 

[1] Xinyu Li and Liang Gao. An effective hybrid genetic algorithm and tabu searchfor  flexible  job  shop  scheduling  problem.International  Journal  of  ProductionEconomics, 174 :93 – 110, 2016