import unittest
from balance_parens import balance_parens


class TestBalancedParentheses(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(balance_parens("()"), "()")

    def test_case_2(self):
        self.assertEqual(balance_parens("(a)(bdd)c)"), "(a)(bdd)c")

    def test_case_3(self):
        self.assertEqual(balance_parens("a(b)(c)())"), "a(b)(c)()")

    def test_case_4(self):
        self.assertEqual(balance_parens("((((("), "")

    def test_case_5(self):
        self.assertEqual(balance_parens("abc(d)e(fgh))(i)j)k"),
                         "abc(d)e(fgh)(i)jk")

    def test_case_6(self):
        self.assertEqual(balance_parens("abc((d)e(fgh)(i)j(k"),
                         "abc(d)e(fgh)(i)jk")

        # # Add more test cases!...
        # print(balance_parens("abc(d)e(fgh))(i)j)k") == "abc(d)e(fgh)(i)jk")
        # print(balance_parens("abc((d)e(fgh)(i)j(k") == "abc(d)e(fgh)(i)jk")

        # # Challenge: nested parentheses...
        # print(balance_parens("abc(d)(ef(g(h))ij)k)lm()o)p") == "abc(d)(ef(g(h))ij)klm()op")
