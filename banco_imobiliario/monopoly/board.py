from monopoly.player import AbortInvestment, NotEnoughMoney, OutOfMoney


DEFAULT_SALARY = 100

class Board:
    def __init__(self, competitors, properties, salary=DEFAULT_SALARY):
        self.competitors = competitors
        self.properties = properties
        self.salary = salary

    def move(self, player, steps):
        cur_pos = self.competitors[player]
        new_lap, new_pos = divmod(cur_pos + steps, len(self))
        self.competitors[player] = new_pos

        if new_lap:
            player.receive(self.salary)

        return self.properties[new_pos]

    def __len__(self):
        return len(self.properties)

    def remove(self, player):
        for rs in self.properties:
            if rs.owner_is(player):
                rs.foreclose()

        del self.competitors[player]

    def turn(self, player, steps):
        real_state = self.move(player, steps)

        try:
            real_state.deal(player)
        except (AbortInvestment, NotEnoughMoney):
            pass
        except OutOfMoney:
            self.remove(player)
