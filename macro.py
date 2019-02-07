#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pynput import keyboard


class Macro:
    def __init__(self, combo):
        self.combination = combo

    def action(self):
        print("detected")

    def test(self, current):
        if all(k in current for k in self.combination):
            return True


class Exit(Macro):
    def __init__(self, combo=[]):
        if len(combo) > 0:
            super().__init__(combo)
        else:
            super().__init__([keyboard.Key.esc])

    def action(self):
        print("Bye")
        return False


class MacroEngine:
    def __init__(self):
        self.macros = list()
        self.current = set()
        self.listener = keyboard.Listener(on_press=self.press, on_release=self.release)

    def press(self, key):
        self.current.add(key)
        res = None
        for e in self.macros:
            if e.test(self.current):
                res = e.action()
                break
        return res

    def release(self, key):
        self.current.remove(key)

    def append(self, macro):
        self.macros.append(macro)

    def start(self):
        self.listener.start()
        self.listener.join()


def main(**kwargs):
    me = MacroEngine()
    me.append(Exit())
    me.start()


if __name__ == "__main__":
    main()