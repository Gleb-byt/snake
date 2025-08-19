from src.game import Game
from src.instructure import Infrastructure

if __name__ == "__main__":
    game = Game(Infrastructure())
    game.loop()