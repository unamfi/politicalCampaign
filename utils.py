# vim: set fileencoding=utf-8 fileformat=unix :


def subdict(dct, keys, exclude=[]):
    """
    Get dictionary containing only specified keys.
    """
    items = ((k, v) for k, v in dct.items() if k in keys and not k in exclude)
    return dict(items)
