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

import shutil

def getScale():
        """Retrieves the current width and height of the terminal
        
        Values:
                width: The width of the terminal
                height: The height of the terminal
        """
        width, height = shutil.get_terminal_size(fallback=(80,24))
        return (col, row)  # return width and height as tuple
