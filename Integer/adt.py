import pytest

'''
        for upper_bound, klass in cls.types.items():
            if n < upper_bound:
                break
        return klass(n)
'''

class IntervalMap(dict):
    def get(self, index):

        if index >= sorted(self.keys())[-1]:
            raise KeyError

        for k, v in self.items():
            if index < k:
                break

        return v


def test_interval_map():
    m = IntervalMap()

    m[5] = 'cinco'
    m[10] = 'dez'
    m[15] = 'quinze'

    assert m.get(0) == 'cinco'
    assert m.get(4) == 'cinco'
    assert m.get(5) == 'dez'
    assert m.get(9) == 'dez'
    assert m.get(10) == 'quinze'
    assert m.get(14) == 'quinze'

    with pytest.raises(KeyError):
        m.get(15)