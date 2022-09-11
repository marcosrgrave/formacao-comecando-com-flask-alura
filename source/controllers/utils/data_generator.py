from source.models.game import GameModel


class DataInit:

    @staticmethod
    def generate_games(amount: int) -> list[GameModel]:
        return [GameModel(name=f"Game {i}", category=f"Category {i}") for i in range(1, amount + 1)]
