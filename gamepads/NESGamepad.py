from _BaseGamePad import BaseGamePad
import uinput

CLICK_A_BUTTON = 12
CLICK_B_BUTTON = 13
CLICK_START_BUTTON = 14
CLICK_SELECT_BUTTON = 15
CLICK_LEFT_BUTTON = 16
CLICK_RIGHT_BUTTON = 17
CLICK_UP_BUTTON = 18
CLICK_DOWN_BUTTON = 19

class NESGamepad(BaseGamePad):
    commandMapping = {
        "a" : CLICK_A_BUTTON,
        "b" : CLICK_B_BUTTON,
        "start" : CLICK_START_BUTTON,
        "select" : CLICK_SELECT_BUTTON,
        "left" : CLICK_LEFT_BUTTON,
        "right" : CLICK_RIGHT_BUTTON,
        "up" : CLICK_UP_BUTTON,
        "down" : CLICK_DOWN_BUTTON
    }

    events = (uinput.BTN_A, uinput.BTN_B, uinput.BTN_START, uinput.BTN_SELECT,
              uinput.BTN_0, uinput.BTN_1, uinput.BTN_2, uinput.BTN_3)
    name = "uinput-virt-nes-gamepad"

    
    def runCommand(self, command):
        if command == CLICK_A_BUTTON:
            self._clickButton(uinput.BTN_A)
        elif command == CLICK_B_BUTTON:
            self._clickButton(uinput.BTN_B)
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
