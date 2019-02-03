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

from colorama import *
import time
init()  # Colorama initialises ANSI escape codes

fm = {  # Format
	"bold" : "0",
	"pale" : "2"
	}
	
fg = {  # Foreground
	"grey" : "30",
	"red" : "31",
	"green" : "32",
	"yellow" : "33",
	"blue" : "34",
	"pink" : "35",
	"cyan" : "36",
	"white" : "37"
	}
	
bg = {  # Background
	"black" : "40",
	"red" : "41",
	"green" : "42",
	"yellow" : "43",
	"blue" : "44",
	"pink" : "45",
	"cyan" : "46",
	"white" : "47"
	}
	
def paint(text, form="bold", foreground="grey", background="black"):  # Returns the ANSI escape code as a string
	return '\x1b[{};{};{}m{}\x1b[0m'.format(fm[form], fg[foreground], bg[background], text)
