#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).parent

# Repositories configuration
REPOS = {
    "advent-of-code": {
        "title": "🎄 Advent of Code",
        "url": "https://github.com/LorranSutter/advent-of-code",
        "branch": "main",
    },
    "everybody-codes": {
        "title": "🦆 Everybody Codes",
        "url": "https://github.com/LorranSutter/everybody-codes",
        "branch": "main",
    },
    "leet-code": {
        "title": "💡 LeetCode",
        "url": "https://github.com/LorranSutter/leet-code",
        "branch": "main",
    }
}

def extract_summary_block(readme_path: Path) -> str:
    """Extracts everything between <!-- SUMMARY:START --> and <!-- SUMMARY:END -->."""
    if not readme_path.exists():
        return ""
    content = readme_path.read_text()
    match = re.search(r"<!-- SUMMARY:START -->\s*(.*?)\s*<!-- SUMMARY:END -->", content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def rewrite_relative_links(text: str, repo_url: str, branch: str) -> str:
    """Replaces relative links like [name](./path) with absolute GitHub links."""
    # Matches [text](./path/to/thing)
    pattern = r"\[([^\]]+)\]\(\./([^\)]*)\)"
    replacement = rf"[\1]({repo_url}/tree/{branch}/\2)"
    return re.sub(pattern, replacement, text)

def parse_stats(text: str, repo_id: str):
    """Parses solved numbers from the 'Overall' line in the summary."""
    if not text:
        return None
    
    if repo_id in ("advent-of-code", "everybody-codes"):
        # Pattern: > **Overall: 95/100 parts solved (95%)**
        match = re.search(r"Overall:\s*(\d+)/(\d+)\s*parts solved", text)
        if match:
            return {
                "solved": int(match.group(1)),
                "total": int(match.group(2)),
                "type": "parts"
            }
    elif repo_id == "leet-code":
        # Pattern: > **Overall: X problems solved**
        match = re.search(r"Overall:\s*(\d+)\s*problems solved", text)
        if match:
            return {
                "solved": int(match.group(1)),
                "total": None,
                "type": "problems"
            }
    return None

def main():
    dashboard_readme = ROOT / "README.md"
    if not dashboard_readme.exists():
        print(f"⚠️ README.md not found at {dashboard_readme}")
        return

    extracted_sections = {}
    stats = {}

    for repo_id, config in REPOS.items():
        sibling_readme = ROOT.parent / repo_id / "README.md"
        raw_summary = extract_summary_block(sibling_readme)
        
        if raw_summary:
            # Extract statistics
            repo_stats = parse_stats(raw_summary, repo_id)
            if repo_stats:
                stats[repo_id] = repo_stats
            
            # Clean up the local summary header (e.g. remove "## 📊 Progress" since we make our own structure)
            clean_summary = re.sub(r"^## 📊 Progress\s*\n", "", raw_summary)
            
            # Rewrite links
            rewritten = rewrite_relative_links(clean_summary, config["url"], config["branch"])
            extracted_sections[repo_id] = rewritten
        else:
            extracted_sections[repo_id] = f"*(No stats available for {config['title']})*"

    # Build the dashboard content
    lines = []
    lines.append("## 📊 Consolidated Progress")
    lines.append("")

    # Calculate Grand Totals
    total_challenges = 0
    aoc_solved = stats.get("advent-of-code", {}).get("solved", 0)
    aoc_total = stats.get("advent-of-code", {}).get("total", 0)
    ebc_solved = stats.get("everybody-codes", {}).get("solved", 0)
    ebc_total = stats.get("everybody-codes", {}).get("total", 0)
    lc_solved = stats.get("leet-code", {}).get("solved", 0)

    total_challenges = aoc_solved + ebc_solved + lc_solved

    # Overall Badge-like summary
    lines.append(f"> ### 🏆 **Grand Total: {total_challenges} coding challenges completed!**")
    lines.append(">")
    if "advent-of-code" in stats:
        lines.append(f"> - **Advent of Code**: {aoc_solved}/{aoc_total} parts ({aoc_solved/aoc_total*100:.1f}%)")
    if "everybody-codes" in stats:
        lines.append(f"> - **Everybody Codes**: {ebc_solved}/{ebc_total} parts ({ebc_solved/ebc_total*100:.1f}%)")
    if "leet-code" in stats:
        lines.append(f"> - **LeetCode**: {lc_solved} problems solved")
    lines.append("")

    # Detail sections for each repo
    for repo_id, config in REPOS.items():
        lines.append(f"### [{config['title']}]({config['url']})")
        lines.append("")
        lines.append(extracted_sections[repo_id])
        lines.append("")
        lines.append("---")
        lines.append("")

    # Remove the trailing horizontal rule
    if lines and lines[-2] == "---":
        lines = lines[:-3]

    unified_summary = "\n".join(lines).strip()

    # Inject into the dashboard README
    content = dashboard_readme.read_text()
    start_marker = "<!-- SUMMARY:START -->"
    end_marker = "<!-- SUMMARY:END -->"
    block = f"{start_marker}\n{unified_summary}\n{end_marker}"

    if start_marker in content and end_marker in content:
        pattern = re.compile(
            re.escape(start_marker) + r".*?" + re.escape(end_marker),
            re.DOTALL,
        )
        new_content = pattern.sub(block, content)
        dashboard_readme.write_text(new_content)
        print(f"✅ Successfully updated {dashboard_readme}")
    else:
        print("❌ Could not find markers in README.md. Please make sure <!-- SUMMARY:START --> and <!-- SUMMARY:END --> exist.")

if __name__ == "__main__":
    main()
