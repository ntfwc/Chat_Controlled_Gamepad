Platforms
--------------------------
Linux

Dependencies
--------------------------
python 2.7
twisted words
python-uinput

Purpose
--------------------------
Inspired by the Twitch plays Pokemon stream, this software aims to make it easy to set up similar streams with any software that supports gamepads.

Design
--------------------------
The gamepad object executes commands and can be asked to translate the string representations of those commands.
The chat client provides commands from users.
The command selector acts as the bridge between these systems. It controls what commands are sent to the gamepad.

The chat client and command selector are separated into different threads.

Set-up
--------------------------
For now, you alter the python code directly to configure it. 
main.py should contain basically everything you need. Just a few alterations there and you should be good to go.

Note:
Programs can have trouble picking up button clicks if the time between press and release is too short. So if you are
having trouble getting an emulator to pick up clicks from a virtual gamepad, go to gamepads/_BaseGamePad.py and try adjusting the CLICK_PADDING time.

Running
---------------------------

In a terminal emulator, run: 
python main.py

Use ctrl-C to stop it.