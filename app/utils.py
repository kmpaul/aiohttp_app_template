from collections.abc import MutableMapping


def flatten(d, _key=None):
    _d = {}
    for k, v in d.items():
        _k = f'{_key}_{k}' if _key else k
        if isinstance(v, MutableMapping):
            _d.update(flatten(v, _key=_k))
        else:
            _d[_k] = v
    return _d


def unflatten(d):
    d1 = {}
    for k, v in d.items():
        ks = k.split('_', 1)
        if len(ks) == 1:
            d2 = {ks[0]: v}
        else:
            d2 = {ks[0]: unflatten({ks[1]: v})}
        d1 = nested_update(d1, d2)
    return d1


def nested_update(d1, d2):
    d = d1.copy()
    for k, v in d2.items():
        nest = k in d1 and isinstance(d1[k], MutableMapping) and isinstance(v, MutableMapping)
        d[k] = nested_update(d1[k], v) if nest else v
    return d
