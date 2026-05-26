# 🏆 Coding Challenges Dashboard

Welcome to my central hub for tracking coding challenges! This repository consolidates my progress across various programming platforms and events.

Rather than pinning multiple individual repositories, this dashboard dynamically aggregates and displays up-to-date stats from my active challenge repositories.

## 🔗 Repositories Included

- **[Advent of Code](https://github.com/LorranSutter/advent-of-code)**: Annual December coding puzzles (Python).
- **[Everybody Codes](https://github.com/LorranSutter/everybody-codes)**: Annual November story-based coding challenges (Python).
- **[LeetCode](https://github.com/LorranSutter/leet-code)**: Algorithm and problem-solving practice (Go).

---

<!-- SUMMARY:START -->
## 📊 Consolidated Progress

> ### 🏆 **Grand Total: 275 coding challenges completed!**
>
> - **Advent of Code**: 95/100 parts (95.0%)
> - **Everybody Codes**: 52/54 parts (96.3%)
> - **LeetCode**: 128 problems solved

### [🎄 Advent of Code](https://github.com/LorranSutter/advent-of-code)

> **Overall: 95/100 parts solved (95%)**

### [2023](https://github.com/LorranSutter/advent-of-code/tree/main/2023/)

`███████████████████░` **28/30** parts solved (93%)

### [2024](https://github.com/LorranSutter/advent-of-code/tree/main/2024/)

`███████████████████░` **45/48** parts solved (94%)

### [2025](https://github.com/LorranSutter/advent-of-code/tree/main/2025/)

`████████████████████` **22/22** parts solved (100%)

---

### [🦆 Everybody Codes](https://github.com/LorranSutter/everybody-codes)

> **Overall: 52/54 parts solved (96%)**

### [2024 — Story: Echoes of Enigmatus](https://github.com/LorranSutter/everybody-codes/tree/main/2024/story/)

`████████████████████` **9/9** parts solved (100%)

### [2025 — Event: The Song of Ducks and Dragons](https://github.com/LorranSutter/everybody-codes/tree/main/2025/event/)

`███████████████████░` **43/45** parts solved (96%)

---

### [💡 LeetCode](https://github.com/LorranSutter/leet-code)

> **Overall: 128 problems solved**
<!-- SUMMARY:END -->

---

## 🛠️ How It Works

This repository is fully automated:
1. A **GitHub Actions Workflow** (`update-dashboard.yml`) runs daily.
2. It dynamically clones the latest `main` branches of the three source repositories.
3. It executes `generate_dashboard.py` to scan each repository's `README.md` progress markers, rewrite relative links to absolute ones, calculate the grand totals, and update this file.
4. If and only if changes are detected, it commits and pushes the updated README.
