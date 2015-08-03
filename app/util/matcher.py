import editdistance as ed

LIMIT = 2


def match(usrinput, target, limit=None):
    limit = limit or LIMIT
    dist = ed.eval(usrinput, target)

    return True if dist <= limit else False