
from enum import Enum, auto
from arcade import Vec2
import arcade
import math

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

class Player(Enum):
    WHITE = auto()
    BLACK = auto()

class Square(arcade.Sprite):
    def __init__(self, path_or_texture: str , scale: float,  center_x: int, center_y: int) -> None:
        super().__init__(path_or_texture=path_or_texture, scale=scale, center_x=center_x, center_y=center_y)

class Piece(arcade.Sprite):
    '''This class represent any piece of the classical chessboard'''

    __kind: PieceKind
    __realPos: tuple[float, float]
    __player: Player

    def __init__(self, kind: PieceKind, center_x: int = 0, center_y: int = 0, scale: float = SPRITE_SCALING) -> None:
        path_or_texture = Piece.match_PieceKind_to_str(kind=kind)
        super().__init__(path_or_texture=path_or_texture, center_x=center_x, center_y=center_y, scale=scale)
        self.__kind = kind
        self.__realPos = self.position
        self.__player = Piece.match_color(kind=kind)

    @property
    def kind(self) -> PieceKind:
        return self.__kind
    
    @property
    def realPos(self) -> tuple[float, float]:
        return self.__realPos
    
    @realPos.setter
    def realPos(self, new_position: tuple[float, float]) -> None:
        self.__realPos = new_position
    
    
    @staticmethod
    def match_PieceKind_to_str(kind: PieceKind) -> str:
        match kind:
            case PieceKind.WHITE_PAWN: return "assets/chess_set/PNG_No_shadow/w_pawn_svg_NoShadow.png"
            case PieceKind.BLACK_PAWN: return "assets/chess_set/PNG_No_shadow/b_pawn_svg_NoShadow.png"
            case PieceKind.WHITE_KNIGHT: return "assets/chess_set/PNG_No_shadow/w_knight_svg_NoShadow.png"
            case PieceKind.BLACK_KNIGHT: return "assets/chess_set/PNG_No_shadow/b_knight_svg_NoShadow.png"
            case PieceKind.WHITE_BISHOP: return "assets/chess_set/PNG_No_shadow/w_bishop_svg_NoShadow.png"
            case PieceKind.BLACK_BISHOP: return "assets/chess_set/PNG_No_shadow/b_bishop_svg_NoShadow.png"
            case PieceKind.WHITE_ROOK: return "assets/chess_set/PNG_No_shadow/w_rook_svg_NoShadow.png"
            case PieceKind.BLACK_ROOK: return "assets/chess_set/PNG_No_shadow/b_rook_svg_NoShadow.png"
            case PieceKind.WHITE_QUEEN: return "assets/chess_set/PNG_No_shadow/w_queen_svg_NoShadow.png"
            case PieceKind.BLACK_QUEEN: return "assets/chess_set/PNG_No_shadow/b_queen_svg_NoShadow.png"
            case PieceKind.WHITE_KING: return "assets/chess_set/PNG_No_shadow/w_king_svg_NoShadow.png"
            case PieceKind.BLACK_KING: return "assets/chess_set/PNG_No_shadow/b_king_svg_NoShadow.png"

    @staticmethod
    def match_PieceKind_to_type(kind: PieceKind) -> str:
        match kind:
            case PieceKind.WHITE_PAWN: return 'p'
            case PieceKind.BLACK_PAWN: return 'p'
            case PieceKind.WHITE_KNIGHT: return 'n'
            case PieceKind.BLACK_KNIGHT: return 'n'
            case PieceKind.WHITE_BISHOP: return 'b'
            case PieceKind.BLACK_BISHOP: return 'b'
            case PieceKind.WHITE_ROOK: return 'r'
            case PieceKind.BLACK_ROOK: return 'r'
            case PieceKind.WHITE_QUEEN: return 'q'
            case PieceKind.BLACK_QUEEN: return 'q'
            case PieceKind.WHITE_KING: return 'k'
            case PieceKind.BLACK_KING: return 'k'

    @staticmethod
    def match_color(kind: PieceKind) -> Player:
        match kind:
            case PieceKind.WHITE_PAWN: return Player.WHITE
            case PieceKind.BLACK_PAWN: return Player.BLACK
            case PieceKind.WHITE_KNIGHT: return Player.WHITE
            case PieceKind.BLACK_KNIGHT: return Player.BLACK
            case PieceKind.WHITE_BISHOP: return Player.WHITE
            case PieceKind.BLACK_BISHOP: return Player.BLACK
            case PieceKind.WHITE_ROOK: return Player.WHITE
            case PieceKind.BLACK_ROOK: return Player.BLACK
            case PieceKind.WHITE_QUEEN: return Player.WHITE
            case PieceKind.BLACK_QUEEN: return Player.BLACK
            case PieceKind.WHITE_KING: return Player.WHITE
            case PieceKind.BLACK_KING: return Player.BLACK
    
    def can_move(self, spot: Square) -> bool:
        return True

    def __repr__(self) -> str:
        return f"({int(self.center_x/GRID_PIXEL_SIZE)+1}, {int(self.center_y/GRID_PIXEL_SIZE)+1}, {self.kind.value})"
    
class Pawn(Piece):
    '''The classic pawn and its properties'''
    
    def __init__(self, kind: PieceKind, center_x: int = 0, center_y: int = 0, scale: float = SPRITE_SCALING) -> None:
        super().__init__(kind=kind, center_x=center_x, center_y=center_y, scale=scale)

    def can_move(self, spot: Square) -> bool:
        return False
    
    @property
    def player(self) -> Player:
        return self.__player
    
class Knight(Piece):
    '''The classic knight and its properties'''
    
    def __init__(self, kind: PieceKind, center_x: int = 0, center_y: int = 0, scale: float = SPRITE_SCALING) -> None:
        super().__init__(kind=kind, center_x=center_x, center_y=center_y, scale=scale)

    def can_move(self, spot: Square) -> bool:
        return False
    
    @property
    def player(self) -> Player:
        return self.__player
    
class Bishop(Piece):
    '''The classic bishop and its properties'''
    
    def __init__(self, kind: PieceKind, center_x: int = 0, center_y: int = 0, scale: float = SPRITE_SCALING) -> None:
        super().__init__(kind=kind, center_x=center_x, center_y=center_y, scale=scale)

    def can_move(self, spot: Square) -> bool:
        return False
    
    @property
    def player(self) -> Player:
        return self.__player
    
class Rook(Piece):
    '''The classic rook and its properties'''
    
    def __init__(self, kind: PieceKind, center_x: int = 0, center_y: int = 0, scale: float = SPRITE_SCALING) -> None:
        super().__init__(kind=kind, center_x=center_x, center_y=center_y, scale=scale)

    def can_move(self, spot: Square) -> bool:
        return False
    
    @property
    def player(self) -> Player:
        return self.__player
    
class Queen(Piece):
    '''The classic queen and its properties'''
    
    def __init__(self, kind: PieceKind, center_x: int = 0, center_y: int = 0, scale: float = SPRITE_SCALING) -> None:
        super().__init__(kind=kind, center_x=center_x, center_y=center_y, scale=scale)

    def can_move(self, spot: Square) -> bool:
        return False
    
    @property
    def player(self) -> Player:
        return self.__player
    
class King(Piece):
    '''The classic king and its properties'''
    
    def __init__(self, kind: PieceKind, center_x: int = 0, center_y: int = 0, scale: float = SPRITE_SCALING) -> None:
        super().__init__(kind=kind, center_x=center_x, center_y=center_y, scale=scale)

    def can_move(self, spot: Square) -> bool:
        return False
    
    @property
    def player(self) -> Player:
        return self.__player