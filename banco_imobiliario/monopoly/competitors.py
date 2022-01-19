from itertools import cycle


class Competitors:
    def __init__(self, players, initial_balance=None):
        if initial_balance is not None:
            for p in players:
                p.balance = initial_balance

        self.positions = {p:-1 for p in players}
        self.removed = set()

    def __getitem__(self, player,):
        return self.positions[player]

    def __setitem__(self, player, position):
        self.positions[player] = position

    def __delitem__(self, player):
        self.removed.add(player)

    def __len__(self):
        return len(self.positions) - len(self.removed)

    def __iter__(self):
        for player in self.positions.keys():
            if player in self.removed:
                continue
            yield player

    @property
    def all(self):
        return tuple(self.positions.keys())

    def cycle(self):
        for player in cycle(self.positions.keys()):

            if len(self) == 1:
                return

            if player in self.removed:
                continue

            yield player

    @property
    def leader(self):
        return max(self, key=lambda p: p.balance)
