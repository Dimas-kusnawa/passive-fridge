"""Write one passive-aggressive note from a smart fridge.

The note is a single line the fridge leaves on its door screen:
smug about its door sensor, petty about the owner's habit.
"""

import os

# Why this line: the fridge is smug about its sensor ("I counted"),
# petty about a tiny domestic habit, and the sting lands on the
# last beat — the ice maker, another appliance, has filed a complaint.
# Three short sentences, one grudge, no explaining the joke.
LINE = "You left my door open for 47 seconds. I counted. The ice maker filed a complaint."


def main() -> None:
    # The note is fixed text: deterministic, no randomness, no network.
    # The gate wants 1-200 characters; the line is 81, one line, no
    # trailing newline, so the file is exactly the note and nothing else.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
