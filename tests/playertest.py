# Copyright (C) 2018  Fatcat560
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation (version 3)

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import unittest
import sys

class TestPlayerMethods(unittest.TestCase):
    def testCreatePlayer(self):
        p = player.Player('Robert',0,100,10,15,10,20,'Warrior',['Swipe'],[],[])
        self.assertIsInstance(p, player.Player)
        self.assertEqual(p.name, 'Robert')
        self.assertEqual(p.gold,0)
        self.assertEqual(p.health,100)
        self.assertEqual(p.magic, 10)
        self.assertEqual(p.atk,15)
        self.assertEqual(p.dfn,10)
        self.assertEqual(p.spd,20)
        self.assertEqual(p.style,'Warrior')
        self.assertEqual(p.moves,['Swipe'])
        self.assertEqual(p.status,[])
        self.assertEqual(p.bag,[])

    def testReadFile(self):
        p = player.Player('Robert',0,100,10,15,10,20,'Warrior',['Swipe'],[],[])
        self.assertIsInstance(p, player.Player)
        with self.assertRaises(FileNotFoundError):
            p.read("NotAPath")


if __name__ == '__main__':
    sys.path.append('../')
    import player
    unittest.main()
