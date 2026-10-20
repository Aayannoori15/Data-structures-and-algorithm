# Data Structures & Algorithms (DSA) — CRUD & LeetCode

This repository contains my personal implementations of key Data Structures and Algorithms (DSA) in Python.
It has two halves:

1. **`CRUD/`** — data structures built **from scratch**, around core *Create, Read, Update, Delete* operations.
2. **`Approaches/`** — LeetCode solutions organised by **approach / pattern**, following my
   [DSA Approach Roadmap](Approaches/README.md).
3. **`Pandas/`** — LeetCode database & pandas solutions, kept out of the DSA roadmap.

**143 LeetCode problems solved** ([profile](https://leetcode.com/u/aayan15/)) — 86 Easy · 54 Medium · 3 Hard.
104 of them are DSA pattern problems; 39 are pandas/database.

---

## 📁 Repository Structure

### `CRUD/` — structures from scratch

*   `linkedlist/` — Singly, Doubly, Circular, and Circular Doubly Linked Lists.
*   `Stack/` — Stack implementations using lists, linked lists, composition, and inheritance.
*   `queues/` — Queue implementations using lists and linked lists.
*   `dequeue/` — Double-ended queues.
*   `priority queue/` — Priority queues using lists and linked lists.
*   `heap/` — Binary heap.
*   `Tree/` — BST using linked nodes, plus BFS and DFS traversal.
*   `graph/` — Adjacency list & matrix representations, plus BFS and DFS.
*   `pythonbasics/` — Python fundamentals and OOP concepts.

### `Approaches/` — patterns, in learning order

| | Area | Patterns inside |
| --- | --- | --- |
| `00` | Fundamentals | sorting algorithms, linear & binary search |
| `01` | Arrays / Strings | two pointers, sliding window, prefix sum, hashing, sorting + two pointers, binary search |
| `02` | Linked List | fast & slow pointer, reverse, merge two lists, dummy node |
| `03` | Stack | monotonic stack, next greater element, balanced parentheses, expression evaluation |
| `04` | Queue / Deque | sliding window maximum, BFS simulation, circular queue |
| `05` | Recursion / Backtracking | recursion tree, subsets & permutations, constraint exploration |
| `06` | Trees | DFS traversal, BFS level order, path problems, divide & conquer, BST logic |
| `07` | Graphs | DFS, BFS, topological sort, shortest path, union-find, MST |
| `08` | Advanced | greedy, dynamic programming, monotonic stack/queue, binary search on answer |
| `09` | Math & Basics | warm-ups that aren't really a pattern — math, string basics, array basics |
| `10` | Design | "implement this data structure" problems |

Every file is named `<leetcode-id>-<slug>` and carries the problem link, difficulty, and the accepted
submission's runtime/memory in its header. A `-v2` file is a local rewrite kept next to the version
that was actually submitted.

Empty folders are intentional — they are patterns **not started yet**. Progress per pattern is tracked
in [`Approaches/README.md`](Approaches/README.md).

### `Pandas/` — not DSA

*   `database/` — 24 SQL-style query problems answered with DataFrame operations.
*   `intro-to-pandas/` — 15 problems from LeetCode's *Introduction to Pandas* study plan.

---

## 🛠 Features covered

### Linear Data Structures
*   **Linked Lists:** Custom pointer structures with full insertion, search, traversal, and deletion.
*   **Stacks:** LIFO operations.
*   **Queues & Dequeues:** FIFO and double-ended insertion/removal.
*   **Priority Queues:** Elements ordered by priority.
*   **Heap:** Array-backed binary heap.

### Non-Linear Data Structures
*   **Binary Search Tree (BST):** Hierarchical nodes with recursion, traversal, and dynamic manipulation.
*   **Graphs:** Adjacency list and adjacency matrix, with BFS and DFS traversal.

---

## 🚀 How to Run

Any script can be executed directly with Python 3:

```bash
# Example: Running the Singly Linked List script
python3 CRUD/linkedlist/Linkedlist.py
```

`Approaches/` and `Pandas/` files are LeetCode-style snippets (`class Solution`, or a function taking a
DataFrame) — import them or paste into the judge.

---

## 🔗 LeetCode

Profile: [leetcode.com/u/aayan15](https://leetcode.com/u/aayan15/)
