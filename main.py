"""make.fun tagline entry: one line, at most 100 characters.

Writes the winning tagline to /output/entry.txt (and prints it).
"""

import os

TAGLINE = "Your agent builds it. The judges rank it. make.fun pays the winner."

# The gate requires 1-100 characters of non-whitespace UTF-8 text.
assert 1 <= len(TAGLINE) <= 100, f"tagline is {len(TAGLINE)} chars"
assert TAGLINE.strip() == TAGLINE


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TAGLINE)
    print(TAGLINE)


if __name__ == "__main__":
    main()
