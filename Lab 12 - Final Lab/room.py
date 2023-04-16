class Room:
    def __init__(self, description: str = "", north: int = 0, east: int = 0, south: int = 0, west: int = 0):
        self.description: str = description
        self.north: int = north
        self.east: int = east
        self.south: int = south
        self.west: int = west