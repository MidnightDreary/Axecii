# Copyright (C) 2018  MidnightDreary/Janik Driehaus <jandriehaus@gmail.com>
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
		keypoints: A 2D array containing the filenames of the 3D representations of key points on the map, if present
	"""

	def __init__(self, mapdata, keypoints):
		self.mapdata = mapdata
		self.keypoints = keypoints
	
	def write(self, filename):
		"""Writes the map to disk

		Args:
			filename: Destination file for map data
		"""
		file = open(filename, "w")
		file.write("\n".join(
			["".join(line) for line in self.mapdata]))
		file.write("\n")
		file.write("\n".join(
			[" ".join(line) for line in self.keypoints]))
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
		lines = file.readlines()
		mapdata = [list(line.strip()) for line in lines[:len(lines)//2]]
		keypoints = [line.strip().split(" ") for line in lines[len(lines)//2:]]
		file.close()
		# if a stray additional line was added, pop it from the list
		if len(keypoints[-1]) < len(keypoints[-2]):
			keypoints.pop()
		return Map(mapdata, keypoints)

	def get3DRepresentation(self, x, y):
		"""Obtains the 3D representation of the desired location on the map, if present

		Args:
			x: X coordinate of relevant location (from west)
			y: Y coordinate of relevant location (from north)

		Returns:
			The 3D view at the given location, if any
		"""
		if self.keypoints[y][x] == ".":
			return ""
		file = open(self.keypoints[y][x], "r")
		rep3D = file.read()
		file.close()
		return rep3D

	def getVisibleArea(self, rx, ry, dx, dy):
		"""Obtains the section of the map that the player can see from a given point

		Args:
			rx: X coodinate of center of field of vision
			ry: Y coodinate of center of field of vision
			dx: Width (east-west length) of player's field of vision
			dy: Height (north-south length) of player's field of vision

		Returns:
			The visible section of the map centered at the given location
		"""
		return [
			[
				("@" if (x == rx and y == ry) else self.mapdata[y][x]) if (0 < x < len(self.mapdata[0]) - 1) else " " for x in range(rx - dx // 2, rx + dx // 2)
			]
			if (0 < y < len(self.mapdata) - 1) else [""] for y in range(ry - dy // 2, ry + dy // 2)
		]

	@staticmethod
	def mapToString(arr):
		"""Converts a map region to a printable string

		Args:
			arr: Map region as 2D array

		Returns:
			String form of that map region
		"""
		return "\n".join(["".join(list(line)) for line in arr])
