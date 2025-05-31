
import arcade

class GameView(arcade.View):
    "Main game class"

    def __init__(self) -> None:
        super().__init__()
        self.setup()

    def setup(self) -> None:
        """Set up the game here."""
        pass

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
        """Render the screen."""
        self.clear() # always start with self.clear()