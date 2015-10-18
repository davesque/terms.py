from __future__ import unicode_literals

import unittest

from ..tree import RuleBase, Rule, Symbol, Add, Expression


class TestTree(unittest.TestCase):
    EXPRESSIONS = (
        (
            Expression(Add, [Symbol('x'), Symbol('x')]),
            Expression(Add, [Symbol('a'), Symbol('a')]),
        ),
    )

    def setUp(self):
        self.base = RuleBase((
            Rule(Symbol('x'), Symbol('a')),
        ))

    def test_expressions_can_be_simplified(self):
        for e1, e2 in self.EXPRESSIONS:
            self.assertEqual(
                self.base.simplify(e1),
                e2,
            )


"""
>>> x = a
>>> x + x
a + a
"""
