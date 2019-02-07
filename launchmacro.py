#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from macro import Macro, MacroEngine
import subprocess
import psutil
from pynput import keyboard


class Launch(Macro):
    def __init__(self, combo, processname, command):
        super().__init__(combo)
        self.command = command
        self.pid = None
        self.procname = processname

    def action(self):
        if self.procname not in (p.name for p in psutil.process_iter()):
            self.pid = subprocess.Popen(self.command).pid
        return True


def main(**kwargs):
    me = MacroEngine()
    me.append(Launch([keyboard.KeyCode.from_char("o")], "obs", ["obs"]))
    me.start()


if __name__ == "__main__":
    main()