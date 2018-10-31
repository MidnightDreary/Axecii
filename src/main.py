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

from player import Player
from map import Map
import scaling
import getch

directions = {
	'w' : (0, -1),
	'a' : (-1, 0),
	's' : (0, 1),
	'd' : (1, 0)
}

def move(x, y, key, mapdata):
	"""Alters the player's location on the given map, if possible

	Args:
		x: Player's current X position
		y: Player's current Y position
		key: Pressed key as a string
		mapdata: Map on which player is moving

	Returns:
		The player's new coordinates after movement as a tuple
	"""
	global directions
	x2 = x + directions[key][0]
	y2 = y + directions[key][1]
	if mapdata.isValidLocation(x2, y2):
		return x2, y2
	return x, y

def saveAndQuit():
	pass

# Application entry point
if __name__ == "__main__":
	currentMap = Map.read("edalus.map")
	w, h = 0, 0
	x, y = 88, 18
	while True:
		w, h = scaling.getScale()
		key = getch.getch()
		if key == 'q':
			saveAndQuit()
			break
		elif key in "wasd":
			x, y = move(x, y, key, currentMap)
		visible = currentMap.getVisibleArea(x, y, w, h)
		visible = Map.mapToString(visible)
		print(visible)
