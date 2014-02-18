##    Copyright (C) 2014 ntfwc <ntfwc@yahoo.com>
##
##    This program is free software; you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation; either version 2 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License along
##    with this program; if not, write to the Free Software Foundation, Inc.,
##    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from _BaseGamePad import BaseGamePad
import uinput

CLICK_A_BUTTON = 12
CLICK_B_BUTTON = 13
CLICK_X_BUTTON = 14
CLICK_Y_BUTTON = 15
CLICK_L_BUTTON = 16
CLICK_R_BUTTON = 17
CLICK_START_BUTTON = 18
CLICK_SELECT_BUTTON = 19
CLICK_LEFT_BUTTON = 20
CLICK_RIGHT_BUTTON = 21
CLICK_UP_BUTTON = 22
CLICK_DOWN_BUTTON = 23

class SNESGamepad(BaseGamePad):
    commandMapping = {
        "a" : CLICK_A_BUTTON,
        "b" : CLICK_B_BUTTON,
        "y" : CLICK_Y_BUTTON,
        "x" : CLICK_X_BUTTON,
        "r" : CLICK_R_BUTTON,
        "l" : CLICK_L_BUTTON,
        "start" : CLICK_START_BUTTON,
        "select" : CLICK_SELECT_BUTTON,
        "left" : CLICK_LEFT_BUTTON,
        "right" : CLICK_RIGHT_BUTTON,
        "up" : CLICK_UP_BUTTON,
        "down" : CLICK_DOWN_BUTTON
    }

    events = (uinput.BTN_A, uinput.BTN_B, uinput.BTN_START, uinput.BTN_SELECT,
              uinput.BTN_0, uinput.BTN_1, uinput.BTN_2, uinput.BTN_3,
              uinput.BTN_4, uinput.BTN_5, uinput.BTN_6, uinput.BTN_7)
    name = "uinput-virt-snes-gamepad"

    
    def runCommand(self, command):
        if command == CLICK_A_BUTTON:
            self._clickButton(uinput.BTN_A)
        elif command == CLICK_B_BUTTON:
            self._clickButton(uinput.BTN_B)
        elif command == CLICK_Y_BUTTON:
            self._clickButton(uinput.BTN_4)
        elif command == CLICK_X_BUTTON:
            self._clickButton(uinput.BTN_5)
        elif command == CLICK_L_BUTTON:
            self._clickButton(uinput.BTN_6)
        elif command == CLICK_R_BUTTON:
            self._clickButton(uinput.BTN_7)
        elif command == CLICK_START_BUTTON:
            self._clickButton(uinput.BTN_START)
        elif command == CLICK_SELECT_BUTTON:
            self._clickButton(uinput.BTN_SELECT)
        elif command == CLICK_LEFT_BUTTON:
            self._clickButton(uinput.BTN_0)
        elif command == CLICK_RIGHT_BUTTON:
            self._clickButton(uinput.BTN_1)
        elif command == CLICK_UP_BUTTON:
            self._clickButton(uinput.BTN_2)
        elif command == CLICK_DOWN_BUTTON:
            self._clickButton(uinput.BTN_3)
