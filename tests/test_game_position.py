
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from game_position import GamePosition, Piece, PieceKind

def test1()-> None:
    game = GamePosition("STARTING_POSITION.txt")
    plist = game.pieceList
    assert len(plist) == 32
    for piece in plist:
        print(piece.center_x, piece.center_y)

test1()