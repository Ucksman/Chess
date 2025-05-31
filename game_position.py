
from enum import Enum, auto
from dataclasses import dataclass
import arcade

class PieceKind(Enum):
    PAWN = auto()
    KNIGHT = auto()
    BISHOP = auto()
    ROOK = auto()
    QUEEN = auto()
    KING = auto()

class Player(Enum):
    WHITE = auto()
    BLACK = auto()

@dataclass
class Piece:
    '''This class represent any piece as its position, its kind, and its player.'''
    __x: int
    __y: int
    __kind: PieceKind
    __player: Player

    @property
    def x(self) -> int:
        return self.__x
    
    @property
    def y(self) -> int:
        return self.__y
    
    @property
    def kind(self) -> PieceKind:
        return self.__kind
    
    @property
    def player(self) -> Player:
        return self.__player

class Game(arcade.View):
    '''This class creates a chess position from a txt file. Its properties make it possible for GameView to recreate and play any position'''
    __pieceList: list[Piece]
    def __init__(self, pos: str) -> None:
        super().__init__()
        self.ReadPosition(pos=pos)

    def ReadPosition(self, pos: str) -> None:
        '''Creates a chess position from a txt file.'''
        pass
    
    @property
    def pieceList(self) -> list[Piece]:
        return self.__pieceList