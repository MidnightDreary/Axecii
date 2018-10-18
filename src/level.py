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

def convertExp(exp):
        """Returns the player's level based on exp gathered
        
        Returns:
                The level as an integer
        """
        lvl = lambda x: int(((x // 25)** 0.5) // 1)
        return lvl(exp)
