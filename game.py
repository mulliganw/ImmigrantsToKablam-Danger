import pandas
from typing import *
from dataclasses import *

@dataclass
class Troop :

    TROOP_TYPES = ['Infantry', 'Tank', 'Officer']

    amount : int
    is_unplaced : bool
    kind : int

@dataclass 
class Triangle : 
    owner : int
    # ID is defined by the order of triangle creation. The higher the ID, the newer the triangle. 
    # In the beginning position, the upper triangle is Triangle ID 1, increasing clockwise up to the amount of players.
    id : int
    troops : int
    has_capital : bool

    def divide(self) : 
        return 0


@dataclass 
class Card : 
    owner : int
    id : int

@dataclass
class Player :
    id : int
    name : str
    cap_location : Triangle
    money : int = 10000
    triangles_owned : int = 1

@dataclass 
class Board :
    num_triangles : int
    cap_locations : Dict[Player, Triangle]

@dataclass 
class Game : 
    
    GAME_TYPES = ['Capitals', 'Domination', 'Corporations']
    
    players : List[Player]
    board : Board
    game_type : int