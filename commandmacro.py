#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from macro import Macro, MacroEngine, Exit
import os
from pynput import keyboard


class Command(Macro):
    def __init__(self, combo, cmd='notify-send "Achtung" "Dies ist eine wichtige Meldung"'):
        super().__init__(combo)
        self.command = cmd

    def action(self):
        os.system(self.command)


def main(**kwargs):
    me = MacroEngine()
    me.append(Exit())
    me.append(Command([keyboard.KeyCode.from_char("n")]))
    me.start()


if __name__ == "__main__":
    main()