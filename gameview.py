
from arcade import Vec2
from game_position import GamePosition
from pieces import PieceKind, Piece, GRID_PIXEL_SIZE, SPRITE_SCALING, SPRITE_PIXEL_SIZE, Square
import arcade


class GameView(arcade.View):
    "Main game class"

    moveCount: int
    piece_is_picked: bool
    picked_piece: arcade.SpriteList[Piece]
    mouse_x: int
    mouse_y: int
    board: arcade.SpriteList[Square]
    camera: arcade.camera.Camera2D
    starting_pos: GamePosition
    pieceList: arcade.SpriteList[Piece]

    def __init__(self) -> None:
        super().__init__()
        self.moveCount = 0
        self.piece_is_picked = False
        self.picked_piece = arcade.SpriteList()
        self.mouse_x = 0
        self.mouse_y = 0
        self.background_color = arcade.csscolor.BEIGE
        self.setup()
        self.starting_pos = GamePosition("STARTING_POSITION.txt")
        self.pieceList = self.starting_pos.pieceList

    def setup(self) -> None:
        """Sets up the game."""

        self.board = arcade.SpriteList()
        self.camera = arcade.camera.Camera2D()
        self.camera.position = Vec2(300, 300)

        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    sprite = Square(
                        "assets/chess_set/board_squares/square_brown_dark.png",
                        scale=SPRITE_SCALING,
                        center_x=GRID_PIXEL_SIZE*i,
                        center_y=GRID_PIXEL_SIZE*j
                    )
                else:
                    sprite = Square(
                        "assets/chess_set/board_squares/square_brown_light.png",
                        scale=SPRITE_SCALING,
                        center_x=GRID_PIXEL_SIZE*i,
                        center_y=GRID_PIXEL_SIZE*j
                    )
                self.board.append(sprite)


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        match button:
            case arcade.MOUSE_BUTTON_LEFT:
                sprites: list[Piece] = arcade.get_sprites_at_point(Vec2(x-GRID_PIXEL_SIZE*0.75, y-GRID_PIXEL_SIZE*0.75), self.pieceList)
                if len(sprites) == 0:
                    return None
                
                sprite: Piece = sprites[0]
                new_pos = self.camera.unproject((x, y))
                sprite.position = (new_pos.x, new_pos.y)
                self.piece_is_picked = True
                self.picked_piece.append(sprite)
            case arcade.MOUSE_BUTTON_RIGHT:
                pass
    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int) -> None:
        match button:
            case arcade.MOUSE_BUTTON_LEFT:
                if self.piece_is_picked:
                    sprite = self.picked_piece[0]
                    spot = min(self.board, key=lambda square: GameView.distance_between(sprite, square))
                    self.piece_is_picked = False
                    self.picked_piece.pop()
                    if sprite.can_move(spot=spot):
                        self.replace(sprite)
                        sprite.realPos = sprite.position
                    else:
                        sprite.position = sprite.realPos
            case arcade.MOUSE_BUTTON_RIGHT:
                pass

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int) -> None:
        self.mouse_x = x + int(GRID_PIXEL_SIZE * 0.75)
        self.mouse_y = y + int(GRID_PIXEL_SIZE * 0.75)

    def on_update(self, delta_time : float) -> None:
        
        if self.piece_is_picked:
            new_pos = self.camera.unproject(self.camera.unproject((self.mouse_x, self.mouse_y)))
            self.picked_piece[0].position = (new_pos.x, new_pos.y)

    def on_draw(self) -> None:
        """Renders the screen."""
        self.clear() # always start with self.clear()
        with self.camera.activate():
            self.board.draw()
            self.pieceList.draw()

    @staticmethod
    def distance_between(sprite1: arcade.Sprite, sprite2: arcade.Sprite) -> float:
        return max(abs(sprite1.center_x - sprite2.center_x), abs(sprite1.center_y - sprite2.center_y))

    def replace(self, sprite: Piece) -> None:
        best_spot = min(self.board, key=lambda square: GameView.distance_between(sprite, square))
        sprite.center_x = best_spot.center_x
        sprite.center_y = best_spot.center_y