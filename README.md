
# Algorithm X

An efficient Python implementation of [Algorithm
X](https://arxiv.org/abs/cs/0011047), which finds solutions to instances of the
[Exact Cover problem](https://en.wikipedia.org/wiki/Exact_cover).

## Installation

```bash
$ pip install algorithm-x
```

## Usage

```python
from algorithm_x import AlgorithmX

solver = AlgorithmX(7)
solver.appendRow([2, 4, 5], 'row 1')
solver.appendRow([0, 3, 6], 'row 2')
solver.appendRow([1, 2, 5], 'row 3')
solver.appendRow([0, 3], 'row 4')
solver.appendRow([1, 6], 'row 5')
solver.appendRow([3, 4, 6], 'row 6')

for solution in solver.solve():
    print(solution)
```

