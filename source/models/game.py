from source.controllers.utils.id_generator import GenerateID


class GameModel:
    __id: str
    name: str
    category: str

    def __init__(self, name: str, category: str):
        self.__id = GenerateID.unique_id()
        self.name = name
        self.category = category

    def to_json(self):
        return {"id": self.id, "name": self.name, "category": self.category}

    @property
    def id(self) -> str:
        return self.__id
