"""
Simple UI state helper: manages a named state and notifies listeners on change.
"""

class UIStateHelper:
    def __init__(self, initial=None):
        self._state = initial
        self._listeners = []

    @property
    def state(self):
        return self._state

    def set(self, value):
        if value != self._state:
            self._state = value
            for callback in self._listeners:
                callback(self._state)

    def toggle(self):
        if isinstance(self._state, bool):
            self.set(not self._state)

    def register(self, callback):
        self._listeners.append(callback)

if __name__ == "__main__":
    import time

    def listener(state):
        print(f"[Listener] State changed to: {state}")

    ui = UIStateHelper(False)
    ui.register(listener)
    print(f"Initial state: {ui.state}")
    for _ in range(5):
        ui.toggle()
        time.sleep(0.5)