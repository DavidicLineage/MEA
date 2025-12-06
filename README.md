# MEA  
Median–Extremes Alternation

A deterministic, reversible permutation defined by alternating center and edge extraction.

**DOI:** https://doi.org/10.5281/zenodo.17799015  
**Archive:** https://zenodo.org/records/17799015

---

## Overview

MEA (Median–Extremes Alternation) is a novel, length-preserving permutation on finite sequences.  
It alternates between removing elements from the **center** and from the **extremes** to produce a deterministic permutation πₙ for each length *n*.

MEA is:

- deterministic  
- reversible  
- mathematically linear-time (O(n))  
- structure-rich  
- simple to implement in any language  

It is useful for combinatorics, deterministic shuffling, reversible transforms, and experimental cryptographic constructions.

---

## How MEA Works

Given an ordered list `[1, 2, …, n]`:

1. **Center extraction**  
   - If *n* is **odd** → remove the middle element.  
   - If *n* is **even** → remove both central elements (lower median first).

2. **Edge extraction**  
   - Remove the current **leftmost** element.  
   - Remove the current **rightmost** element.

3. **Repeat**  
   Alternate **Center → Edges → Center → Edges → …**  
   until the list is empty.

After the initial center removal (one or two elements), all remaining removals occur in pairs.

---

## Complexity Note

The **MEA operator itself is O(n)** and has a closed-form, single-pass construction (see spec and traversal paper).

The file **`mea.py`** is a **pedagogical reference implementation**.  
It uses Python list pops and therefore runs in **O(n²)**.  
It is not optimized.

---

## Examples

Applying MEA to the identity sequence:

```
n=1: 1
n=2: 12
n=3: 213
n=4: 2314
n=5: 31524
n=6: 341625
n=7: 4173526
```

---

## Python Reference Implementation

```python
from mea import mea_order, mea_inverse

print(mea_order(7))     # [4, 1, 7, 3, 5, 2, 6]
print(mea_inverse(7))   # [2, 6, 4, 1, 5, 7, 3]
```

### Complexity of This Implementation
- Time: O(n²)  
- Space: O(n)

---

## Applications & Research Directions

### Combinatorics
- cycle structure of πₙ  
- parity / sign  
- behavior under iteration  
- closed forms and recurrences  

### Cryptography (experimental)
- P-boxes  
- reversible scramblers  
- lightweight PRP components  
- format-preserving transforms  

### Deterministic Shuffling & Mixing
- deck/card orderings  
- reversible data interleaving  

---

## Citation

Carr, D. (2025). *MEA: Median–Extremes Alternation* (Version 1.0.1) [Software]. Zenodo.  
https://doi.org/10.5281/zenodo.17799015

---

## License

Released under the Apache License 2.0.  
See `LICENSE` for details.

---

## Contributing

Optimizations, analyses, proofs, and alternative implementations are welcome.  
Open an issue or pull request.
.
