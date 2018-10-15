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

import pickle

class Player:
	"""Represents a player in the game

	Attributes:
		name: The player's name
		gold: The player's amount of gold coins
		health: The player's remaining HP
		magic: The player's magic points
		atk: The player's attack points
		dfn: The player's defense points
		spd: The player's speed points
		style: The player's combatant style
		moves: A list of the player's moves
		status: A list of the player's status effects
		bag: A list of the player's inventory items
	"""
	def __init__(self, name, gold, health, magic, atk, dfn, spd, style, moves, status, bag):
		self.name = name
		self.gold = gold
		self.health = health
		self.magic = magic
		self.atk = atk
		self.dfn = dfn
		self.spd = spd
		self.style =style
		self.moves = moves
		self.status = status
		self.bag = bag

	def write(self, filename):
		"""Writes player data to disk

		Args:
			filename: Destination file for player data
		"""
		file = open(filename, "wb")
		pickle.dump(self, file)
		file.close()

	@staticmethod
	def read(filename):
		"""Reads player data from disk

		Args:
			filename: Source file for player data

		Returns:
			A Player object reconstructed from the file
		"""
		file = open(filename, "rb")
		player = pickle.load(file)
		file.close()
		return player
	
	def bleed(self, damage):
		"""Reduces player health value by damage amount
		Triggers self.death() if health <= 0
		
		Args:
			damage: amount to reduce health by
		"""
		self.health -= damage
		
		"""if self.health <= 0:
		    self.death()
		"""
