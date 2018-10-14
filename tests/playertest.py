import unittest
import player

class TestPlayerMethods(unittest.TestCase):
    def testCreatePlayer(self):
        p = player.Player('Robert',100,10,15,10,20,'Warrior',['Swipe'],[])
        self.assertIsInstance(p, player.Player)
        self.assertEqual(p.name, 'Robert')
        self.assertEqual(p.health,100)
        self.assertEqual(p.magic, 10)
        self.assertEqual(p.atk,15)
        self.assertEqual(p.dfn,10)
        self.assertEqual(p.spd,20)
        self.assertEqual(p.type,'Warrior')
        self.assertEqual(p.moves,['Swipe'])
        self.assertEqual(p.status,[])

    def testWriteFile():
        p = player.Player('Robert',100,10,15,10,20,'Warrior',['Swipe'],[])
        self.assertIsInstance(p, player.Player)
        self.assertRaises(IOError, p.write("NotAPath"))


if __name__ == '__main__':
    unittest.main()
