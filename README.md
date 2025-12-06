# MEA
Median-Extremes Alternation

A deterministic, reversible permutation algorithm based on alternating center and edge extraction.

**DOI:** https://doi.org/10.5281/zenodo.17799015  
**Archive:** https://zenodo.org/records/17799015

---

## Overview

MEA (Median–Extremes Alternation) is a novel, length-preserving permutation on finite sequences.  
It alternates between removing elements from the **center** and from the **extremes** of a list until all elements have been consumed. The resulting output order defines a deterministic permutation πₙ for each sequence length *n*.

MEA is:

- deterministic  
- reversible  
- linear-time (O(n))  
- length-preserving  
- structure-rich  
- simple to implement in any language  

It is suitable for combinatorics research, deterministic shuffling, reversible mixing, and experimental cryptographic constructions (e.g., P-boxes, PRPs, reversible transforms).

---

## How MEA Works

Given a list of ordered elements:

1. **Center extraction**  
   - If length is **odd** → remove the single middle element  
   - If length is **even** → remove the central *pair* (lower median first, then upper median)

2. **Edge extraction**  
   - Remove the current **leftmost** element  
   - Remove the current **rightmost** element  

3. Repeat  
   Always alternate in the order:  
   **Center → Edges → Center → Edges → …**  
   until no elements remain.

After the first step (which may be a single element), all further steps occur in **pairs**.

The MEA permutation is a deterministic, reversible traversal that removes elements in an alternating pattern: center(s), then extremes, then center(s), and so on.
It is defined mathematically by a closed-form, single-pass O(n) construction.
The reference code included here (mea.py) is a simple pedagogical implementation and runs in O(n²) due to Python list operations. It is not optimized and is provided only as a minimal working example.

For the formal definition, proofs, and full system context, see the documents in this repository (MEAspec.pdf, traversal paper, introduction materials, etc.).

See mea.py for the reference implementation.
---

## Examples

Applying MEA to the identity sequences:

n=1: 1
n=2: 12
n=3: 213
n=4: 2314
n=5: 31524
n=6: 341625
n=7: 4173526


These are the images of `[1, 2, ..., n]` under πₙ.

---

## Python Reference Implementation

The file `mea.py` contains the canonical implementation.

Example use:

```python
from mea import mea_order, mea_inverse

print(mea_order(7))     # [4, 1, 7, 3, 5, 2, 6]
print(mea_inverse(7))   # [2, 6, 4, 1, 5, 7, 3]
Complexity

Time: O(n)

Space: O(n)

MEA performs a fixed sequence of pop operations with minimal overhead.

Applications and Research Directions

Combinatorics

cycle structure of πₙ

parity/sign of the permutation

behavior under repeated application

closed forms and recurrences

Cryptography (experimental)

P-box construction

reversible scramblers

lightweight PRP components

format-preserving transforms

Deterministic Shuffling

deck/card ordering

reversible mixing

data interleaving

Citation

If you use or reference MEA, please cite:

Carr, D. (2025). MEA: Median–Extremes Alternation (Version 1.0.1) [Software]. Zenodo.
https://doi.org/10.5281/zenodo.17799015

License

Released under the Apache License 2.0.
See LICENSE for details.

Contributing

Analysis, optimizations, proofs, and alternate implementations are welcome.
Open an issue or pull request if you'd like to contribute.
