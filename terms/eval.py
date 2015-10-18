class Head(object):
    pass


class Add(Head):
    pass


class Symbol(object):
    def __init__(self, label):
        self.label = label

    def __eq__(self, other):
        return self.label == other.label

    def __hash__(self):
        return hash(self.label)


class Expression(object):
    def __init__(self, head, terms):
        self.head = head
        self.terms = terms

    def __eq__(self, other):
        return (
            self.head is other.head and
            all(i == j for i, j in zip(self.terms, other.terms))
        )


class Rule(object):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __iter__(self):
        yield self.lhs
        yield self.rhs


class RuleBase(dict):
    def add(self, r):
        self[r.lhs] = r.rhs

    def simplify(self, e):
        return Expression(e.head, map(self._simplify_item, e.terms))

    def _simplify_item(self, x):
        if isinstance(x, Expression):
            return self.simplify(x)

        if isinstance(x, Symbol):
            try:
                return self[x]
            except KeyError:
                pass

        return x
