#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path


def main() -> None:
    base_dir = Path(__file__).resolve().parents[1] / "算数・数学"
    today = datetime.now().strftime("%Y-%m-%d")
    target = base_dir / f"{today}.md"
    if target.exists():
        print(f"File already exists: {target}")
        return
    base_dir.mkdir(parents=True, exist_ok=True)
    template = "#算数・数学"
    target.write_text(template, encoding="utf-8")
    print(f"Created {target}")


if __name__ == "__main__":
    main()