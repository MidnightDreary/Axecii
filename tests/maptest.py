# Copyright (C) 2018 Arc676/Alessandro Vinciguerra <alesvinciguerra@gmail.com>

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

mapdata = [
	['.', '.', '.'],
	['.', 'O', '.'],
	['.', '.', '.']
]
keypoints = [['.' for i in range(3)] for j in range(3)]

class TestMapMethods(unittest.TestCase):
	def testCreateMap(self):
		map = Map(mapdata, keypoints)
		self.assertEqual(map.getVisibleArea(1, 1, 1, 1), [["O"]])
		self.assertEqual(map.getVisibleArea(1, 1, 3, 3), mapdata)
		self.assertEqual(map.getVisibleArea(1, 1, 10, 10), mapdata)
	
	def testWriteMap(self):
		map = Map(mapdata, keypoints)
		map.write("test")
		map1 = Map.read("test")
		self.assertEqual(map1.map, mapdata)
		self.assertEqual(map.map, map1.map)
	
	def testNewlineRemoval(self):
		map = Map(mapdata, keypoints)
		map.write("test2")
		file = open("test2", "a")
		file.write("\n")
		file.close()
		map1 = Map.read("test")
		self.assertEqual(map1.map, mapdata)

if __name__ == '__main__':
	sys.path.append('../src')
	from map import Map
	unittest.main()
