
from enum import Enum
import arcade

SPRITE_SCALING = 0.5
SPRITE_PIXEL_SIZE = 150
GRID_PIXEL_SIZE = int(SPRITE_PIXEL_SIZE * SPRITE_SCALING)

class PieceKind(Enum):
    WHITE_PAWN = "P"
    WHITE_KNIGHT = "N"
    WHITE_BISHOP = "B"
    WHITE_ROOK = "R"
    WHITE_QUEEN = "Q"
    WHITE_KING = "K"
    BLACK_PAWN = "p"
    BLACK_KNIGHT = "n"
    BLACK_BISHOP = "b"
    BLACK_ROOK = "r"
    BLACK_QUEEN = "q"
    BLACK_KING = "k"


class Piece(arcade.Sprite):
    '''This class represent any piece of the classical chessboard'''
    __kind: PieceKind
    def __init__(self, kind: PieceKind, path_or_texture: str | None = None, center_x: int = 0, center_y: int = 0, scale: float = SPRITE_SCALING) -> None:
        super().__init__(path_or_texture=path_or_texture, center_x=center_x, center_y=center_y, scale=scale)
        self.__kind = kind

    @property
    def kind(self) -> PieceKind:
        return self.__kind
    
    def __repr__(self) -> str:
        return f"({int(self.center_x/GRID_PIXEL_SIZE)+1}, {int(self.center_y/GRID_PIXEL_SIZE)+1}, {self.kind.value})"
    

class Pawn(Piece):
    ...

class WPawn(Pawn):

    def __init__(self, kind: PieceKind, center_x: int = 0, center_y: int = 0, scale: float = SPRITE_SCALING) -> None:
        super().__init__(kind=kind, path_or_texture="assets/chess_set/PNG_No_shadow/w_pawn_svg_NoShadow.png", center_x=center_x, center_y=center_y, scale=scale)
    
    def can_move(self) -> bool:
        return False