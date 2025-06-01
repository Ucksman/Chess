
from dataclasses import dataclass
from pathlib import Path
from pieces import Piece, PieceKind, WPawn, GRID_PIXEL_SIZE, SPRITE_SCALING
import arcade



class GamePosition:
    '''This class creates a chess position from a txt file. Its properties make it possible for GameView to recreate and play any position'''
    __pieceList: arcade.SpriteList[Piece]
    def __init__(self, pos: str) -> None:
        super().__init__()
        self.__pieceList = arcade.SpriteList()
        self.ReadPosition(pos=pos)

    def add_piece(self, i: int, j: int, kind: PieceKind) -> None:
        new_piece = Piece(kind=kind, path_or_texture=GamePosition.match_PieceKind(kind=kind), center_x=j*GRID_PIXEL_SIZE, center_y=i*GRID_PIXEL_SIZE, scale=SPRITE_SCALING*0.8)
        self.__pieceList.append(new_piece)

    @staticmethod
    def match_PieceKind(kind: PieceKind) -> str:
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