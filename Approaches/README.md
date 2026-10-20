# DSA Approach Roadmap

DSA is not just topics — it's **patterns applied on structures**. This folder is organised by
*approach*, not by problem number, so every file answers "which pattern solves this shape?".

Each file is named `<leetcode-id>-<slug>` and carries the problem link, difficulty, and the
runtime/memory of the accepted submission in its header. A `-v2` file is a local rewrite kept
alongside the originally accepted version.

Folders are numbered in learning order. **An empty folder is a pattern not started yet** — it is
a deliberate placeholder, not an oversight.

<!-- generated from the files on disk; counts below are real -->

---

**104 LeetCode problems** filed by pattern, plus 8 fundamental algorithm implementations.
The 39 Pandas / database solutions live in [`../Pandas/`](../Pandas) — they are not DSA patterns.

---

## 00 · Fundamentals

> Raw algorithm implementations, not LeetCode patterns — the building blocks everything else assumes.

### Sorting

*bubble, modified bubble, insertion, selection, merge, quick*

`bubblesort.py`, `insertionsort.py`, `mergesort.py`, `modifiedbubblesort.py`, `quicksort.py`, `selectionsort.py`

### Searching

*linear search, binary search*

`binarysearch.py`, `linearsearch.py`

---

## 🟢 01 · Arrays / Strings  ·  **44 solved**

### Two pointers — 17

| # | Problem | Difficulty |
| --- | --- | --- |
| 11 | [Container With Most Water](01-arrays-strings/twopointer/0011-container-with-most-water.py) | Medium |
| 26 | [Remove Duplicates from Sorted Array](01-arrays-strings/twopointer/0026-remove-duplicates-from-sorted-array.py) | Easy |
| 27 | [Remove Element](01-arrays-strings/twopointer/0027-remove-element.java) | Easy |
| 31 | [Next Permutation](01-arrays-strings/twopointer/0031-next-permutation.py) | Medium |
| 42 | [Trapping Rain Water](01-arrays-strings/twopointer/0042-trapping-rain-water.py) | Hard |
| 75 | [Sort Colors](01-arrays-strings/twopointer/0075-sort-colors.py) | Medium |
| 80 | [Remove Duplicates from Sorted Array II](01-arrays-strings/twopointer/0080-remove-duplicates-from-sorted-array-ii.java) | Medium |
| 88 | [Merge Sorted Array](01-arrays-strings/twopointer/0088-merge-sorted-array.java) | Easy |
| 151 | [Reverse Words in a String](01-arrays-strings/twopointer/0151-reverse-words-in-a-string.py) | Medium |
| 283 | [Move Zeroes](01-arrays-strings/twopointer/0283-move-zeroes.py) | Easy |
| 345 | [Reverse Vowels of a String](01-arrays-strings/twopointer/0345-reverse-vowels-of-a-string.py) | Easy |
| 392 | [Is Subsequence](01-arrays-strings/twopointer/0392-is-subsequence.py) | Easy |
| 443 | [String Compression](01-arrays-strings/twopointer/0443-string-compression.py) | Medium |
| 977 | [Squares of a Sorted Array](01-arrays-strings/twopointer/0977-squares-of-a-sorted-array.py) | Easy |
| 986 | [Interval List Intersections](01-arrays-strings/twopointer/0986-interval-list-intersections.py) | Medium |
| 1768 | [Merge Strings Alternately](01-arrays-strings/twopointer/1768-merge-strings-alternately.py) | Easy |
| 2210 | [Count Hills and Valleys in an Array](01-arrays-strings/twopointer/2210-count-hills-and-valleys-in-an-array.py) | Easy |

### Sliding window — 6

| # | Problem | Difficulty |
| --- | --- | --- |
| 3 | [Longest Substring Without Repeating Characters](01-arrays-strings/slidingwindow/0003-longest-substring-without-repeating-characters.py) | Medium |
| 485 | [Max Consecutive Ones](01-arrays-strings/slidingwindow/0485-max-consecutive-ones.py) | Easy |
| 643 | [Maximum Average Subarray I](01-arrays-strings/slidingwindow/0643-maximum-average-subarray-i.py) | Easy |
| 1004 | [Max Consecutive Ones III](01-arrays-strings/slidingwindow/1004-max-consecutive-ones-iii.py) | Medium |
| 1456 | [Maximum Number of Vowels in a Substring of Given Length](01-arrays-strings/slidingwindow/1456-maximum-number-of-vowels-in-a-substring-of-given-length.py) | Medium |
| 1493 | [Longest Subarray of 1's After Deleting One Element](01-arrays-strings/slidingwindow/1493-longest-subarray-of-1s-after-deleting-one-element.py) | Medium |

### Prefix sum — 5

| # | Problem | Difficulty |
| --- | --- | --- |
| 238 | [Product of Array Except Self](01-arrays-strings/prefixsum/0238-product-of-array-except-self.py) | Medium |
| 523 | [Continuous Subarray Sum](01-arrays-strings/prefixsum/0523-continuous-subarray-sum.py) | Medium |
| 560 | [Subarray Sum Equals K](01-arrays-strings/prefixsum/0560-subarray-sum-equals-k.py) | Medium |
| 724 | [Find Pivot Index](01-arrays-strings/prefixsum/0724-find-pivot-index.py) | Easy |
| 1732 | [Find the Highest Altitude](01-arrays-strings/prefixsum/1732-find-the-highest-altitude.py) | Easy |

### Hashing — 10

| # | Problem | Difficulty |
| --- | --- | --- |
| 1 | [Two Sum](01-arrays-strings/hashing/0001-two-sum.py) | Easy |
| 448 | [Find All Numbers Disappeared in an Array](01-arrays-strings/hashing/0448-find-all-numbers-disappeared-in-an-array.py) | Easy |
| 645 | [Set Mismatch](01-arrays-strings/hashing/0645-set-mismatch.py) | Easy |
| 1207 | [Unique Number of Occurrences](01-arrays-strings/hashing/1207-unique-number-of-occurrences.py) | Easy |
| 1365 | [How Many Numbers Are Smaller Than the Current Number](01-arrays-strings/hashing/1365-how-many-numbers-are-smaller-than-the-current-number.py) | Easy |
| 1657 | [Determine if Two Strings Are Close](01-arrays-strings/hashing/1657-determine-if-two-strings-are-close.py) | Medium |
| 1679 | [Max Number of K-Sum Pairs](01-arrays-strings/hashing/1679-max-number-of-k-sum-pairs.py) | Medium |
| 2215 | [Find the Difference of Two Arrays](01-arrays-strings/hashing/2215-find-the-difference-of-two-arrays.py) | Easy |
| 2352 | [Equal Row and Column Pairs](01-arrays-strings/hashing/2352-equal-row-and-column-pairs.py) | Medium |
| 3487 | [Maximum Unique Subarray Sum After Deletion](01-arrays-strings/hashing/3487-maximum-unique-subarray-sum-after-deletion.py) | Easy |

### Sorting + two pointers — 2

| # | Problem | Difficulty |
| --- | --- | --- |
| 15 | [3Sum](01-arrays-strings/sorting-twopointer/0015-3sum.py) | Medium |
| 881 | [Boats to Save People](01-arrays-strings/sorting-twopointer/0881-boats-to-save-people.py) | Medium |

### Binary search — 4

| # | Problem | Difficulty |
| --- | --- | --- |
| 4 | [Median of Two Sorted Arrays](01-arrays-strings/binarysearch/0004-median-of-two-sorted-arrays.py) | Hard |
| 35 | [Search Insert Position](01-arrays-strings/binarysearch/0035-search-insert-position.py) | Easy |
| 374 | [Guess Number Higher or Lower](01-arrays-strings/binarysearch/0374-guess-number-higher-or-lower.py) | Easy |
| 2300 | [Successful Pairs of Spells and Potions](01-arrays-strings/binarysearch/2300-successful-pairs-of-spells-and-potions.py) | Medium |

---

## 🟢 02 · Linked List  ·  **13 solved**

### Fast & slow pointer (cycle detection) — 5

| # | Problem | Difficulty |
| --- | --- | --- |
| 141 | [Linked List Cycle](02-linkedlist/fastslow-pointer/0141-linked-list-cycle.py) | Easy |
| 234 | [Palindrome Linked List](02-linkedlist/fastslow-pointer/0234-palindrome-linked-list.py) | Easy |
| 287 | [Find the Duplicate Number](02-linkedlist/fastslow-pointer/0287-find-the-duplicate-number.py) | Medium |
| 2095 | [Delete the Middle Node of a Linked List](02-linkedlist/fastslow-pointer/2095-delete-the-middle-node-of-a-linked-list.py) | Medium |
| 2130 | [Maximum Twin Sum of a Linked List](02-linkedlist/fastslow-pointer/2130-maximum-twin-sum-of-a-linked-list.py) | Medium |

### Reverse a list — 2

| # | Problem | Difficulty |
| --- | --- | --- |
| 92 | [Reverse Linked List II](02-linkedlist/reverse/0092-reverse-linked-list-ii.py) | Medium |
| 206 | [Reverse Linked List](02-linkedlist/reverse/0206-reverse-linked-list.py) | Easy |

### Merge two lists — 2

| # | Problem | Difficulty |
| --- | --- | --- |
| 21 | [Merge Two Sorted Lists](02-linkedlist/merge-two-lists/0021-merge-two-sorted-lists.py) | Easy |
| 23 | [Merge k Sorted Lists](02-linkedlist/merge-two-lists/0023-merge-k-sorted-lists.py) | Hard |

### Dummy node technique — 4

| # | Problem | Difficulty |
| --- | --- | --- |
| 19 | [Remove Nth Node From End of List](02-linkedlist/dummy-node/0019-remove-nth-node-from-end-of-list.py) | Medium |
| 24 | [Swap Nodes in Pairs](02-linkedlist/dummy-node/0024-swap-nodes-in-pairs.py) | Medium |
| 237 | [Delete Node in a Linked List](02-linkedlist/dummy-node/0237-delete-node-in-a-linked-list.py) | Medium |
| 328 | [Odd Even Linked List](02-linkedlist/dummy-node/0328-odd-even-linked-list.py) | Medium |

---

## 🟢 03 · Stack  ·  **10 solved**

### Monotonic stack 🔥 — 2

| # | Problem | Difficulty |
| --- | --- | --- |
| 739 | [Daily Temperatures](03-stack/monotonic-stack/0739-daily-temperatures.py) | Medium |
| 901 | [Online Stock Span](03-stack/monotonic-stack/0901-online-stock-span.py) | Medium |

### Next greater element — 1

| # | Problem | Difficulty |
| --- | --- | --- |
| 496 | [Next Greater Element I](03-stack/next-greater-element/0496-next-greater-element-i.py) | Easy |

### Balanced parentheses — 2

| # | Problem | Difficulty |
| --- | --- | --- |
| 20 | [Valid Parentheses](03-stack/balanced-parentheses/0020-valid-parentheses.py) | Easy |
| 678 | [Valid Parenthesis String](03-stack/balanced-parentheses/0678-valid-parenthesis-string.py) | Medium |

### Expression evaluation — 1

| # | Problem | Difficulty |
| --- | --- | --- |
| 150 | [Evaluate Reverse Polish Notation](03-stack/expression-evaluation/0150-evaluate-reverse-polish-notation.py) | Medium |

### Stack simulation — 4

*extra bucket — problems where the stack *is* the simulation*

| # | Problem | Difficulty |
| --- | --- | --- |
| 71 | [Simplify Path](03-stack/stack-simulation/0071-simplify-path.py) | Medium |
| 735 | [Asteroid Collision](03-stack/stack-simulation/0735-asteroid-collision.py) | Medium |
| 1441 | [Build an Array With Stack Operations](03-stack/stack-simulation/1441-build-an-array-with-stack-operations.py) | Medium |
| 2390 | [Removing Stars From a String](03-stack/stack-simulation/2390-removing-stars-from-a-string.py) | Medium |

---

## 🟢 04 · Queue / Deque  ·  **2 solved**

### Sliding window maximum (deque)

*Not started — `04-queue-deque/sliding-window-maximum/` is an empty placeholder.*

### BFS simulation

*Not started — `04-queue-deque/bfs-simulation/` is an empty placeholder.*

### Circular queue logic

*Not started — `04-queue-deque/circular-queue/` is an empty placeholder.*

### Queue simulation — 2

*extra bucket*

| # | Problem | Difficulty |
| --- | --- | --- |
| 649 | [Dota2 Senate](04-queue-deque/queue-simulation/0649-dota2-senate.py) | Medium |
| 933 | [Number of Recent Calls](04-queue-deque/queue-simulation/0933-number-of-recent-calls.py) | Easy |

---

## 🔵 05 · Recursion / Backtracking

### Recursion tree

*Not started — `05-recursion-backtracking/recursion-tree/` is an empty placeholder.*

### Permutations / subsets

*Not started — `05-recursion-backtracking/subsets-permutations/` is an empty placeholder.*

### Constraint exploration

*Not started — `05-recursion-backtracking/constraint-exploration/` is an empty placeholder.*

---

## 🟣 06 · Trees  ·  **12 solved**

> From-scratch tree implementations (BST, BFS, DFS) live in [`../CRUD/Tree/`](../CRUD/Tree).

### DFS — preorder / inorder / postorder — 3

*subtree & path problems*

| # | Problem | Difficulty |
| --- | --- | --- |
| 94 | [Binary Tree Inorder Traversal](06-trees/dfs-traversal/0094-binary-tree-inorder-traversal.py) | Easy |
| 100 | [Same Tree](06-trees/dfs-traversal/0100-same-tree.py) | Easy |
| 872 | [Leaf-Similar Trees](06-trees/dfs-traversal/0872-leaf-similar-trees.py) | Easy |

### BFS — level order — 1

*shortest depth, level problems*

| # | Problem | Difficulty |
| --- | --- | --- |
| 102 | [Binary Tree Level Order Traversal](06-trees/bfs-level-order/0102-binary-tree-level-order-traversal.py) | Medium |

### Path-based (root → leaf, backtracking)

*root sum path, max path sum*

*Not started — `06-trees/path-problems/` is an empty placeholder.*

### Divide & conquer (solve L, solve R, combine) — 1

*diameter, height*

| # | Problem | Difficulty |
| --- | --- | --- |
| 104 | [Maximum Depth of Binary Tree](06-trees/divide-and-conquer/0104-maximum-depth-of-binary-tree.py) | Easy |

### BST logic (inorder = sorted, binary search on tree) — 7

*search, insert/delete, kth smallest*

| # | Problem | Difficulty |
| --- | --- | --- |
| 230 | [Kth Smallest Element in a BST](06-trees/bst/0230-kth-smallest-element-in-a-bst.py) | Medium |
| 450 | [Delete Node in a BST](06-trees/bst/0450-delete-node-in-a-bst.py) | Medium |
| 501 | [Find Mode in Binary Search Tree](06-trees/bst/0501-find-mode-in-binary-search-tree.py) | Easy |
| 700 | [Search in a Binary Search Tree](06-trees/bst/0700-search-in-a-binary-search-tree.py) | Easy |
| 701 | [Insert into a Binary Search Tree](06-trees/bst/0701-insert-into-a-binary-search-tree.py) | Medium |
| 783 | [Minimum Distance Between BST Nodes](06-trees/bst/0783-minimum-distance-between-bst-nodes.py) | Easy |
| 897 | [Increasing Order Search Tree](06-trees/bst/0897-increasing-order-search-tree.py) | Easy |

---

## 🔴 07 · Graphs  ·  **1 solved**

> From-scratch graph implementations (adjacency list/matrix, BFS, DFS) live in [`../CRUD/graph/`](../CRUD/graph).

### DFS (recursive / stack)

*cycle detection, connected components*

*Not started — `07-graphs/dfs/` is an empty placeholder.*

### BFS (queue)

*shortest path unweighted, level traversal*

*Not started — `07-graphs/bfs/` is an empty placeholder.*

### Topological sort — DFS based

*course scheduling, dependencies*

*Not started — `07-graphs/topological-sort/dfs-based/` is an empty placeholder.*

### Topological sort — Kahn's (BFS indegree)

*same, iterative*

*Not started — `07-graphs/topological-sort/kahns-algorithm/` is an empty placeholder.*

### Shortest path — BFS (unweighted)

*Not started — `07-graphs/shortest-path/bfs-unweighted/` is an empty placeholder.*

### Shortest path — Dijkstra

*weighted, non-negative*

*Not started — `07-graphs/shortest-path/dijkstra/` is an empty placeholder.*

### Shortest path — Bellman-Ford

*negative weights*

*Not started — `07-graphs/shortest-path/bellman-ford/` is an empty placeholder.*

### Union-Find / DSU

*path compression, union by rank*

*Not started — `07-graphs/union-find/` is an empty placeholder.*

### MST — Kruskal (greedy + DSU)

*Not started — `07-graphs/mst/kruskal/` is an empty placeholder.*

### MST — Prim (greedy + heap)

*Not started — `07-graphs/mst/prim/` is an empty placeholder.*

### Graph basics — 1

*extra bucket — degree counting etc.*

| # | Problem | Difficulty |
| --- | --- | --- |
| 1791 | [Find Center of Star Graph](07-graphs/graph-basics/1791-find-center-of-star-graph.py) | Easy |

---

## 🟡 08 · Advanced  ·  **4 solved**

### Greedy — 4

| # | Problem | Difficulty |
| --- | --- | --- |
| 55 | [Jump Game](08-advanced/greedy/0055-jump-game.java) | Medium |
| 121 | [Best Time to Buy and Sell Stock](08-advanced/greedy/0121-best-time-to-buy-and-sell-stock.java) | Easy |
| 334 | [Increasing Triplet Subsequence](08-advanced/greedy/0334-increasing-triplet-subsequence.py) | Medium |
| 605 | [Can Place Flowers](08-advanced/greedy/0605-can-place-flowers.py) | Easy |

### Dynamic programming

*Not started — `08-advanced/dynamic-programming/` is an empty placeholder.*

### Monotonic stack / queue

*see also `03-stack/monotonic-stack/`*

*Not started — `08-advanced/monotonic-stack-queue/` is an empty placeholder.*

### Binary search on answer

*Not started — `08-advanced/binary-search-on-answer/` is an empty placeholder.*

---

## ⚪ 09 · Math & Basics  ·  **14 solved**

> Beyond the roadmap — solved problems that are warm-ups rather than a pattern.

### Math — 5

| # | Problem | Difficulty |
| --- | --- | --- |
| 7 | [Reverse Integer](09-math-and-basics/math/0007-reverse-integer.py) | Medium |
| 9 | [Palindrome Number](09-math-and-basics/math/0009-palindrome-number.java) | Easy |
| 1071 | [Greatest Common Divisor of Strings](09-math-and-basics/math/1071-greatest-common-divisor-of-strings.py) | Easy |
| 1492 | [The kth Factor of n](09-math-and-basics/math/1492-the-kth-factor-of-n.java) | Medium |
| 2396 | [Strictly Palindromic Number](09-math-and-basics/math/2396-strictly-palindromic-number.py) | Medium |

### String basics — 4

| # | Problem | Difficulty |
| --- | --- | --- |
| 28 | [Find the Index of the First Occurrence in a String](09-math-and-basics/string-basics/0028-find-the-index-of-the-first-occurrence-in-a-string.java) | Easy |
| 58 | [Length of Last Word](09-math-and-basics/string-basics/0058-length-of-last-word.java) | Easy |
| 2678 | [Number of Senior Citizens](09-math-and-basics/string-basics/2678-number-of-senior-citizens.java) | Easy |
| 3136 | [Valid Word](09-math-and-basics/string-basics/3136-valid-word.py) | Easy |

### Array basics — 5

| # | Problem | Difficulty |
| --- | --- | --- |
| 412 | [Fizz Buzz](09-math-and-basics/array-basics/0412-fizz-buzz.py) | Easy |
| 1431 | [Kids With the Greatest Number of Candies](09-math-and-basics/array-basics/1431-kids-with-the-greatest-number-of-candies.py) | Easy |
| 1470 | [Shuffle the Array](09-math-and-basics/array-basics/1470-shuffle-the-array.py) | Easy |
| 1929 | [Concatenation of Array](09-math-and-basics/array-basics/1929-concatenation-of-array.py) | Easy |
| 3151 | [Special Array I](09-math-and-basics/array-basics/3151-special-array-i.java) | Easy |

---

## ⚪ 10 · Design  ·  **4 solved**

> Beyond the roadmap — "implement this data structure" problems.

### Design — 4

| # | Problem | Difficulty |
| --- | --- | --- |
| 155 | [Min Stack](10-design/0155-min-stack.py) | Medium |
| 232 | [Implement Queue using Stacks](10-design/0232-implement-queue-using-stacks.py) | Easy |
| 703 | [Kth Largest Element in a Stream](10-design/0703-kth-largest-element-in-a-stream.py) | Easy |
| 707 | [Design Linked List](10-design/0707-design-linked-list.py) | Medium |

---
