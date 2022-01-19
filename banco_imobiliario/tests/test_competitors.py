import pytest

from monopoly import Player, Competitors


def test_position():
    p1, p2 = Player(100), Player(300)
    c = Competitors([p1, p2])

    assert c[p1] == -1
    assert c[p2] == -1

    pos_a, pos_b = 10, 14

    c[p1] = pos_a
    c[p2] = pos_b

    assert c[p1] == pos_a
    assert c[p2] == pos_b

def test_remove():
    p1, p2 = Player(100), Player(300)
    c = Competitors([p1, p2])

    del c[p2]

    assert len(c) == 1

def test_iter():
    p1, p2, p3 = Player(100), Player(300), Player(200)

    c = Competitors([p1, p2, p3])

    it = iter(c)

    assert next(it) is p1
    assert next(it) is p2
    assert next(it) is p3

    with pytest.raises(StopIteration):
        next(it)

def test_all():
    p1, p2, p3 = Player(100), Player(300), Player(200)

    c = Competitors([p1, p2, p3])

    del c[p2]
    del c[p3]

    assert c.all == (p1, p2, p3)

def test_cycle():
    p1, p2, p3 = Player(100), Player(300), Player(200)
    c = Competitors([p1, p2, p3])

    it = c.cycle()

    assert next(it) == p1
    assert next(it) == p2
    assert next(it) == p3
    assert next(it) == p1

def test_cycle_until_only_one():
    p1, p2, p3 = Player(100), Player(300), Player(200)
    c = Competitors([p1, p2, p3])

    it = c.cycle()

    assert next(it) == p1

    del c[p1]

    assert next(it) == p2
    assert next(it) == p3
    assert next(it) == p2

    del c[p2]

    with pytest.raises(StopIteration):
        next(it)
