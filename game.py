import pandas
from typing import *
from dataclasses import *

@dataclass
class Troop :

    TROOP_TYPES = ['Infantry', 'Tank', 'Officer']

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
    troops = List[Troop] = field(default_factory=[])

    # Place owned (AND UNPLACED) troops on owned triangles
    def place_troops() :       
        return 0
    
    # Build structures to earn cash.
    def build() :
        return 0

@dataclass 
class Board :
    triangles : List[Triangle]
    cap_locations : Dict[Player, Triangle]
    
    # Maybe finish this but definitely do that last
    def increase_size() :
        return 0

@dataclass 
class Game : 

    # Implement this close to the end.    
    GAME_TYPES : ClassVar[List] = ['Capitals', 'Domination', 'Corporations']
    turn : ClassVar[int] = 0

    players : List[Player]
    board : Board
    game_type : int

    def start(players) :
        triangles = []
        cap_locations = {}
        for i in range (0, len(players)) :
            triangle = Triangle(players[i].id, i, True, 10)
            triangles.append(triangle)
            cap_locations[players[i].id] = triangle
        board = Board(triangles, cap_locations)
        return board

    def play_turn(players, current_player) :
        # If the current turn is 0 (the game hasn't started yet), give everybody their troops and set everything up.
        if Game.turn == 0:
            for player in players: 
                player.add_troops() 

        turn += 1
    def add_money(player, amount) : 
        player.money += amount

    # Add a certain number of troops to a player's data
    def add_troops(player, amount, kind) :
        start_len = len(player.troops)
        for i in range(0, amount):
            player.troops.append(Troop(True, kind))
        if start_len == len(player.troops):
            return True
        return False