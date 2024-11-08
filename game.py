import pandas
from typing import *
from dataclasses import *

@dataclass
class Troop :

    TROOP_TYPES = ['Infantry', 'Tank', 'Officer']

    amount : int
    is_unplaced : bool
    kind : int

    def attack() :
        return 0
    
    def move() : 
        return 0
    
    def split() :
        return 0

@dataclass 
class Triangle : 
    newest_id : ClassVar[int] = 6
    owner : int
    # ID is defined by the order of triangle creation. The higher the ID, the newer the triangle. 
    # In the beginning position, the upper triangle is Triangle ID 1, increasing clockwise up to the amount of players.
    id : int
    has_capital : bool = field(default=False)
    troops : int = field(default=1)

    def divide(self) : 
        return [self, Triangle(self.owner, Triangle.newest_id)]

@dataclass 
class Card : 
    owner : int
    id : int

    def randomize() :
        return 0

@dataclass
class Player :
    id : int
    name : str
    cap_location : Triangle
    money : int = field(default=10000)
    triangles_owned : int = field(default=1)
      
    def build() :
        return 0

@dataclass 
class Board :
    triangles : List[Triangle]
    cap_locations : Dict[Player, Triangle]

    def increase_size() :
        return 0

@dataclass 
class Game : 
    
    GAME_TYPES : ClassVar[List] = ['Capitals', 'Domination', 'Corporations']
    
    players : List[Player]
    board : Board
    game_type : int

    def start(players) :
        triangles = []
        cap_locations = {}
        for i in range (0, len(players)) :
            triangle = Triangle(players[i].id, i, True)
            triangles.append(triangle)
            cap_locations[players[i].id] = triangle
        board = Board(triangles, cap_locations)

    def play_turn() :
        return 0

    def add_money(Player) : 
        return 0
    
    def add_troops(Player) :
        return 0