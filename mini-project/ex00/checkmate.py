def checkmate(board):
    ALLOWED = set("KQRBP.")

    # --- Input Validation ---
    if not isinstance(board, str):
        print("Error: Input must be string")
        return

    clean_board = board.replace('\r\n', '\n').strip('\n')
    if not clean_board:
        print("Error: Empty board")
        return

    rows = clean_board.split('\n')
    size = len(rows)

    for r in rows:
        if len(r) != size:
            print("Error: Board is not a square")
            return

    king_count = 0
    king_pos = None

    for r in range(size):
        for c in range(size):
            char = rows[r][c]
            if char not in ALLOWED:
                print("Error: Allowed only 'K Q R B P .'")
                return
            if char == 'K':
                king_count += 1
                king_pos = (r, c)

    if king_count > 1:
        print("Error: Why U put more than 1 King?")
        return
    elif king_pos is None:
        print("Error: Where is the King?")
        return


    # --- Check Logic ---
    king_r, king_c = king_pos
    
    def in_bounds(r, c):
        return 0 <= r < size and 0 <= c < size

    pawn_check = [
        (king_r + 1, king_c - 1),
        (king_r + 1, king_c + 1)
    ]

    for pr, pc in pawn_check:
        if in_bounds(pr, pc) and rows[pr][pc] == 'P':
            print("Success")
            return

    orthogonals = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diagonals   = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    def scan(directions, threats):
        for dr, dc in directions:
            r, c = king_r + dr, king_c + dc
            
            while in_bounds(r, c):
                piece = rows[r][c]
                
                if piece in threats:
                    return True
                
                if piece != '.':
                    break
                
                r += dr
                c += dc
        return False

    if scan(orthogonals, set("RQ")):
        print("Success")
        return

    if scan(diagonals, set("BQ")):
        print("Success")
        return

    print("Fail")
