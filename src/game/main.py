from ursina import Ursina
from game.controllers import GameController

def main() -> None:
    """
    Ponto de entrada do jogo.
    """
    app = Ursina()
    controller = GameController()
    app.input  = controller.input
    app.update = controller.update
    app.run()


if __name__ == '__main__':
    main()
