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

import uinput, time

NAME_DEFAULT = "python-uinput"
BUSTYPE_DEFAULT = 0
VENDOR_DEFAULT = 0
PRODUCT_DEFAULT = 0
VERSION_DEFAULT = 0

CLICK_PADDING = 0.1

class BaseGamePad(object):
    commandMapping = {}
    events = ()
    name = NAME_DEFAULT
    bustype = BUSTYPE_DEFAULT
    vendor = VENDOR_DEFAULT
    product = PRODUCT_DEFAULT
    version = VERSION_DEFAULT

    def connect(self):
        self.device = uinput.Device(self.events, self.name,
                                    self.bustype, self.vendor, self.product,
                                    self.version)

    def translateInputMessage(self, message):
        if message in self.commandMapping:
            return self.commandMapping[message]

    def _clickButton(self, button):
        self.device.emit(button, 1)
        time.sleep(CLICK_PADDING)
        self.device.emit(button, 0)
        time.sleep(CLICK_PADDING)

    def runCommand(self, command):
        raise NotImplementedError()
