import unittest

from cowpy import cow

class TestCowsay(unittest.TestCase):
    def test_cowsay(self):
        self.maxDiff = None
        turtle = cow.Turtle()
        # pylint: disable=trailing-whitespace
        want = """ _____ 
< Sup >
 ----- 
    \\                                  ___-------___
     \\                             _-~~             ~~-_
      \\                         _-~                    /~-_
             /^\\__/^\\         /~  \\                   /    \\
           /|  O|| O|        /      \\_______________/        \\
          | |___||__|      /       /                \\          \\
          |          \\    /      /                    \\          \\
          |   (_______) /______/                        \\_________ \\
          |         / /         \\                      /            \\
           \\         \\^\\\\         \\                  /               \\     /
             \\         ||           \\______________/      _-_       //\\__//
               \\       ||------_-~~-_ ------------- \\ --/~   ~\\    || __/
                 ~-----||====/~     |==================|       |/~~~~~
                  (_(__/  ./     /                    \\_\\      \\.
                         (_(___/                         \\_____)_)"""
        self.assertEqual(want, turtle.milk("Sup"))


if __name__ == "__main__":
    unittest.main()
