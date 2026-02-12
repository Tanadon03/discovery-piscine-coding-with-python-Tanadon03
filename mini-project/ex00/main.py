#!/usr/bin/env python
from checkmate import checkmate

def main():
    print("--- 1. Normal Case (Success: Rook) ---")
    checkmate("""\
....
.K..
.R..
....""")

    print("\n--- 2. Normal Case (Fail) ---")
    checkmate("""\
....
.K..
.P..
.R..""")

    print("\n--- 3. Pawn Attack (Fail) ---")
    checkmate("""\
..P.
.K..
....
....""")

    print("\n--- 4. Error: Invalid Character ---")
    checkmate("""\
....
.K..
.X..
....""")

    print("\n--- 5. Error: Non-Square Board ---")
    checkmate("""\
...
.K..
...""")

    print("\n--- 6. Error: No King ---")
    checkmate("""\
....
....
....
....""")

    print("\n--- 7. Error: Multiple Kings ---")
    checkmate("""\
K...
.K..
....
....""")

    print("\n--- 8. Error: Empty Board ---")
    checkmate("")

if __name__ == "__main__":
    main()
