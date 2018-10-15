# Copyright (C) 2018  Arc676/Alessandro Vinciguerra <alesvinciguerra@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation (version 3)

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

class Map:
	"""Represents a single map in the game

	Attributes:
		map: The map itself represented as a 2D array
	"""

	def __init__(map):
		self.map = map
	
	def write(filename):
		"""Writes the map to disk

		Args:
			filename: Destination file for map data
		"""
		file = open(filename, "w")
		file.write("\n".join(
			["".join(line) for line in map]))
		file.close()
	
	@staticmethod
	def read(filename):
		"""Reads a map from disk

		Args:
			filename: Source file for map data

		Returns:
			A Map object constructed from the data in the file
		"""
		file = open(filename, "r")
		map = [list(line) for line in file.readlines()]
		file.close()
