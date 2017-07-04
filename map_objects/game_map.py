from map_objects.tile import Tile

class GameMap:
    def __init__(self, width, height):
        self.width= width
        self.height=height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles=[[Tile(False) for y in range(self.height)] for x in range(self.width)]
        for x in range(self.width):
            tiles[x][self.height-1].blocked=True
        for y in range(self.height):
            tiles[self.width-1][y].blocked=True

        return tiles
    
    def is_blocked(self,x,y):
        if self.tiles[x][y].blocked:
            return True
        else:
            return False
