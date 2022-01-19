import random
from unittest.mock import DEFAULT
from monopoly import Board, Competitors

class Game:
    DEFAULT_INITIAL_BALANCE= 300
    DEFAULT_MAX_TURNS = 1000
    DEFAULT_SALARY = 100

    def __init__(self, players, properties,
                 initial_balance=DEFAULT_INITIAL_BALANCE,
                 salary=DEFAULT_SALARY,
                 max_turns=DEFAULT_MAX_TURNS):
        self.initial_balance = initial_balance
        self.max_turns = max_turns
        self.salary = salary
        self.competitors = Competitors(players, self.initial_balance)
        self.board = Board(self.competitors, properties, self.salary)

    @property
    def leader(self):
        return self.competitors.leader

    @staticmethod
    def dice():
        return random.randint(1, 6)

    def run(self, counter=0):
        turn_count = counter

        for p in self.competitors.cycle():

            self.board.turn(p, self.dice())
            turn_count += 1

            if turn_count >= self.max_turns:
                break

        return self.leader
