#!/usr/bin/env python3
"""Simple in-memory todo list."""

class TodoList:
    def __init__(self):
        self._items = []

    def add(self, text):
        text = str(text).strip()
        if not text:
            raise ValueError('empty todo')
        self._items.append(text)
        return text

    def list(self):
        return list(self._items)

    def clear(self):
        self._items.clear()
