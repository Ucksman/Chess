
from enum import Enum, auto
from arcade import Vec2
from game_position import GamePosition, PieceKind, Piece, GRID_PIXEL_SIZE, SPRITE_SCALING, SPRITE_PIXEL_SIZE
import arcade


class GameView(arcade.View):
    "Main game class"

    moveCount: int
    board: arcade.SpriteList[arcade.Sprite]
    camera: arcade.camera.Camera2D
    starting_pos: GamePosition
    pieceList: arcade.SpriteList[Piece]

    def __init__(self) -> None:
        super().__init__()
        self.moveCount = 0
        self.background_color = arcade.csscolor.BEIGE
        self.setup()
        self.starting_pos = GamePosition("scholar's_mate.txt")
        self.pieceList = self.starting_pos.pieceList

    def setup(self) -> None:
        """Sets up the game."""

        self.board = arcade.SpriteList()
        self.camera = arcade.camera.Camera2D()
        self.camera.position = Vec2(300, 300)

        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    sprite = arcade.Sprite(
                        "assets/chess_set/board_squares/square_brown_dark.png",
                        scale=SPRITE_SCALING,
                        center_x=GRID_PIXEL_SIZE*i,
                        center_y=GRID_PIXEL_SIZE*j
                    )
                else:
                    sprite = arcade.Sprite(
                        "assets/chess_set/board_squares/square_brown_light.png",
                        scale=SPRITE_SCALING,
                        center_x=GRID_PIXEL_SIZE*i,
                        center_y=GRID_PIXEL_SIZE*j
                    )
                self.board.append(sprite)


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        match button:
            case arcade.MOUSE_BUTTON_LEFT:
                pass
            case arcade.MOUSE_BUTTON_RIGHT:
                pass
    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int) -> None:
        match button:
            case arcade.MOUSE_BUTTON_LEFT:
                pass
            case arcade.MOUSE_BUTTON_RIGHT:
                pass

    def on_draw(self) -> None:
        """Renders the screen."""
        self.clear() # always start with self.clear()
        with self.camera.activate():
            self.board.draw()
            self.pieceList.draw()