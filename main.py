
import arcade
from gameview import GameView

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Chess"

def main() -> None:
    """Main function."""

    # Create the (unique) Window, setup our GameView, and launch
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game_view = GameView()
    window.show_view(game_view)
    arcade.run()


if __name__ == "__main__":
    main()
