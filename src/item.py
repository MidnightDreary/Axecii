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

class Item:
        """Represents an item in the game
        
        Attributes:
                name: The item's name
                attack: The item's attack value
                rAttack: The item's ranged attack value
                mAttack: The item's magic attack value
                value: The item's monetary value
                recipe: The item's crafting recipe
       """
        def __init__(self, name, attack, rAttack, mAttack, value):
                self.name = name
                self.attack = attack
                self.rAttack = rAttack
                self.mAttack = mAttack
                self.value = value
                self.recipe = recipe
                
        def wield(self):
                return "using {}.".format(self.name)
