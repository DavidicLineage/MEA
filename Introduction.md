This project contains two connected but independent components.
The first is a mathematically defined traversal of the integers from the center outward, the MEA permutation.
The second is a meaning-evaluation framework that uses the same structural principles to stabilize conceptual analysis.
Both share the same logic: begin at the center, alternate symmetrically, preserve anchors, and expose dependencies.

SECTION 1 — The Traversal
The MEA traversal is defined on the set {1 to n}. It starts in the exact center (a single center for odd n, a central pair for even n) and alternates outward in a left–right pattern that preserves perfect reflection symmetry for even n and four-directional expansion for odd n.
The code in mea.py provides the reference implementation of the permutation and its inverse.
The traversal paper and the theorem document contain the formal definition, the parity split, the closed forms, and the proofs of existence and uniqueness.
The centered-operator note describes the same object as a “double spiral” operator and gives the cycle structure.

SECTION 2 — The MEA Framework
The meaning framework defines four primitives: concepts, dependencies, anchors, and frames.
Concepts are decomposable semantic units.
Dependencies describe what relies on what.
Anchors are the fixed, non-negotiable semantic invariants.
Frames define the boundary of an analysis.
The I5 pipeline describes the process that all analyses follow:
Illuminate the claim,
Elucidate its structure,
Explain the dependency graph,
Experience it through examples,
Examine it for contradictions or anchor violations.
The purpose note and the example walkthrough demonstrate this on a natural-language statement.

SECTION 3 — Canonical Examples
The canonical examples file shows MEA in action on a consistent test set: the numbers zero through ten, plus sword, shield, love, glory, honor, wisdom, logos, logic, and constellation.
Each concept has correct cases, incorrect cases, and borderline cases that depend on frame selection.
This is the practical teaching set for humans and the test set for any future implementation.

SECTION 4 — Intended Use
MEA is not an ideology and does not generate meaning from nowhere. It forces clarity.
It exposes the structure already present in a claim, checks it against fixed anchors, and ensures the reasoning chain is reproducible and consistent.
The permutation provides the mathematical backbone.
The kernel provides the rules for conceptual analysis.
The examples provide the demonstration.

SECTION 5 — Repository Map
The code defines the permutation.
The math documents define the traversal and its properties.
The kernel documents define the meaning architecture.
The examples demonstrate all of it.
