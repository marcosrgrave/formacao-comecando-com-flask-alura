from uuid import uuid1, uuid4, uuid5
from random import randint


class GenerateID:
    @staticmethod
    def unique_id() -> str:
        """Inspired in AppSheet's UNIQUEID function."""
        return hex(randint(0, 4294967295))[2:]

    @staticmethod
    def unique_id_uuid() -> str:
        return str(uuid5(uuid1(), str(uuid4())))
