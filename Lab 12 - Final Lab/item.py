class Item:
    def __init__(self, description: str = "", room_num: int = 0, name: str = ""):
        self.description: str = description
        self.room_num: int = room_num
        self.name: str = name