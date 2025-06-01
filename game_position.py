
from dataclasses import dataclass
from pathlib import Path
from pieces import Piece, PieceKind, GRID_PIXEL_SIZE, SPRITE_SCALING, Pawn, Knight, Bishop, Rook, Queen, King
import arcade


class GamePosition:
    '''This class creates a chess position from a txt file. Its properties make it possible for GameView to recreate and play any position'''
    __pieceList: arcade.SpriteList[Piece]
    def __init__(self, pos: str) -> None:
        super().__init__()
        self.__pieceList = arcade.SpriteList()
        self.ReadPosition(pos=pos)

    def add_piece(self, i: int, j: int, kind: PieceKind) -> None:
        new_piece = Piece(kind=kind, center_x=j*GRID_PIXEL_SIZE, center_y=i*GRID_PIXEL_SIZE, scale=SPRITE_SCALING*0.8)
        self.__pieceList.append(new_piece)

    def new_piece(self, i: int, j: int, kind :PieceKind) -> Piece:
        match Piece.match_PieceKind_to_type(kind=kind):
            case 'p': return Pawn(kind=kind, center_x=j*GRID_PIXEL_SIZE, center_y=i*GRID_PIXEL_SIZE, scale=SPRITE_SCALING*0.8)
            case 'n': return Knight(kind=kind, center_x=j*GRID_PIXEL_SIZE, center_y=i*GRID_PIXEL_SIZE, scale=SPRITE_SCALING*0.8)
            case 'b': return Bishop(kind=kind, center_x=j*GRID_PIXEL_SIZE, center_y=i*GRID_PIXEL_SIZE, scale=SPRITE_SCALING*0.8)
            case 'r': return Rook(kind=kind, center_x=j*GRID_PIXEL_SIZE, center_y=i*GRID_PIXEL_SIZE, scale=SPRITE_SCALING*0.8)
            case 'q': return Queen(kind=kind, center_x=j*GRID_PIXEL_SIZE, center_y=i*GRID_PIXEL_SIZE, scale=SPRITE_SCALING*0.8)
            case 'k': return King(kind=kind, center_x=j*GRID_PIXEL_SIZE, center_y=i*GRID_PIXEL_SIZE, scale=SPRITE_SCALING*0.8)
            case _: raise ValueError(f"Unknown match_PieceKind_to_type output {Piece.match_PieceKind_to_type(kind=kind)}")

    def ReadPosition(self, pos: str) -> None:
        '''Creates a chess position from a txt file.'''
        file_path = Path(__file__).parent / "initial_positions" / pos
        with open(file_path, "r", encoding="utf-8", newline='\n') as file:
            data = file.readlines()

        for i in range(8):
            for j in range(len(data[i])):
                character = data[i][j]
                match character:
                    case PieceKind.WHITE_PAWN.value: self.add_piece(7-i, j, PieceKind.WHITE_PAWN)
                    case PieceKind.BLACK_PAWN.value: self.add_piece(7-i, j, PieceKind.BLACK_PAWN)
                    case PieceKind.WHITE_KNIGHT.value: self.add_piece(7-i, j, PieceKind.WHITE_KNIGHT)
                    case PieceKind.BLACK_KNIGHT.value: self.add_piece(7-i, j, PieceKind.BLACK_KNIGHT)
                    case PieceKind.WHITE_BISHOP.value: self.add_piece(7-i, j, PieceKind.WHITE_BISHOP)
                    case PieceKind.BLACK_BISHOP.value: self.add_piece(7-i, j, PieceKind.BLACK_BISHOP)
                    case PieceKind.WHITE_ROOK.value: self.add_piece(7-i, j, PieceKind.WHITE_ROOK)
                    case PieceKind.BLACK_ROOK.value: self.add_piece(7-i, j, PieceKind.BLACK_ROOK)
                    case PieceKind.WHITE_QUEEN.value: self.add_piece(7-i, j, PieceKind.WHITE_QUEEN)
                    case PieceKind.BLACK_QUEEN.value: self.add_piece(7-i, j, PieceKind.BLACK_QUEEN)
                    case PieceKind.WHITE_KING.value: self.add_piece(7-i, j, PieceKind.WHITE_KING)
                    case PieceKind.BLACK_KING.value: self.add_piece(7-i, j, PieceKind.BLACK_KING)
    
    
    @property
    def pieceList(self) -> arcade.SpriteList[Piece]:
        return self.__pieceList