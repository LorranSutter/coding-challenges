# 🏆 Coding Challenges Dashboard

Welcome to my central hub for tracking coding challenges! This repository consolidates my progress across various programming platforms and events.

Rather than pinning multiple individual repositories, this dashboard dynamically aggregates and displays up-to-date stats from my active challenge repositories.

## 🔗 Repositories Included

- **[Advent of Code](https://github.com/LorranSutter/advent-of-code)**: Annual December coding puzzles (Python).
- **[Everybody Codes](https://github.com/LorranSutter/everybody-codes)**: Annual November story-based coding challenges (Python).
- **[Flip Flop Codes](https://github.com/LorranSutter/flip-flop-codes)**: Coding puzzle series with three-part increasing difficulty (Python).
- **[LeetCode](https://github.com/LorranSutter/leet-code)**: Algorithm and problem-solving practice (Go).
- **[URI Online Judge](https://github.com/LorranSutter/URI-Online-Judge)**: Archive of online judge problems (Python).

---

<!-- SUMMARY:START -->
## 📊 Consolidated Progress

> ### 🏆 **Grand Total: 670 coding challenges completed!**
>
> - **Advent of Code**: 100/124 parts (80.6%)
> - **Everybody Codes**: 55/69 parts (79.7%)
> - **Flip Flop Codes**: 31/57 parts (54.4%)
> - **LeetCode**: 128 problems solved
> - **URI Online Judge**: 356 problems solved

### [🎄 Advent of Code](https://github.com/LorranSutter/advent-of-code)

> **Overall: 100/124 parts solved (81%)**

### [2023](https://github.com/LorranSutter/advent-of-code/tree/main/2023/)

`██████████████████████████████████░░░░░░░░░░░░░░░░` **34/50** parts solved (68%)

### [2024](https://github.com/LorranSutter/advent-of-code/tree/main/2024/)

`█████████████████████████████████████████████░░░░░` **45/50** parts solved (90%)

### [2025](https://github.com/LorranSutter/advent-of-code/tree/main/2025/)

`█████████████████████░░░` **21/24** parts solved (88%)

---

### [🦆 Everybody Codes](https://github.com/LorranSutter/everybody-codes)

> **Overall: 55/69 parts solved (80%)**

### [2024 — Story: Echoes of Enigmatus](https://github.com/LorranSutter/everybody-codes/tree/main/2024/story/)

`█████████` **9/9** parts solved (100%)

### [2025 — Event: The Song of Ducks and Dragons](https://github.com/LorranSutter/everybody-codes/tree/main/2025/event/)

`██████████████████████████████████████████████░░░░░░░░░░░░░░` **46/60** parts solved (77%)

---

### [🔀 Flip Flop Codes](https://github.com/LorranSutter/flip-flop-codes)

> **Overall: 31/57 parts solved (54%)**

### [2025](https://github.com/LorranSutter/flip-flop-codes/tree/main/2025/)

`████████████████░░░░░` **16/21** parts solved (76%)

### [2026](https://github.com/LorranSutter/flip-flop-codes/tree/main/2026/)

`███████████████░░░░░░░░░░░░░░░░░░░░░` **15/36** parts solved (42%)

---

### [💡 LeetCode](https://github.com/LorranSutter/leet-code)

[![Solved Challenges](https://img.shields.io/badge/Solved%20Challenges-128-brightgreen?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/)

---

### [🌐 URI Online Judge](https://github.com/LorranSutter/URI-Online-Judge)

[![Solved Challenges](https://img.shields.io/badge/Solved%20Challenges-356-brightgreen?style=for-the-badge&logo=python&logoColor=white)](https://www.beecrowd.com.br/)
<!-- SUMMARY:END -->

---

## 🛠️ How It Works

This repository is fully automated:
1. A **GitHub Actions Workflow** (`update-dashboard.yml`) runs daily.
2. It dynamically clones the latest `main` branches of the five source repositories.
3. It executes `generate_dashboard.py` to scan each repository's `README.md` progress markers, rewrite relative links to absolute ones, calculate the grand totals, and update this file.
4. If and only if changes are detected, it commits and pushes the updated README.
