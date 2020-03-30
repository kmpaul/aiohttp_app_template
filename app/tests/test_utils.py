from app.utils import flatten, nested_update, unflatten


def test_flatten():
    nested_d = {'a': 1, 'b': 2, 'c': {'x': 7, 'y': {'u': 8, 'v': 9}}}
    flatnd_d = {'a': 1, 'b': 2, 'c_x': 7, 'c_y_u': 8, 'c_y_v': 9}
    assert flatten(nested_d) == flatnd_d
    assert unflatten(flatnd_d) == nested_d


def test_nested_update():
    d1 = {'a': 1, 'b': 2, 'c': {'x': 7, 'y': {'u': 8, 'v': 9}}}
    d2 = {'a': 3, 'c': {'x': 0, 'y': {'v': 8}, 'z': 5}}
    dx = {'a': 3, 'b': 2, 'c': {'x': 0, 'y': {'u': 8, 'v': 8}, 'z': 5}}
    assert nested_update(d1, d2) == dx
