"""A tiny helper for UI state management."""
from typing import Any, Callable, Dict, List

class UIState:
    """Manages key-value UI state and notifies listeners on changes."""
    def __init__(self) -> None:
        self._data: Dict[str, Any] = {}
        self._listeners: Dict[str, List[Callable[[Any], None]]] = {}

    def set_state(self, key: str, value: Any) -> None:
        self._data[key] = value
        if key in self._listeners:
            for cb in self._listeners[key]:
                cb(value)

    def get_state(self, key: str) -> Any:
        return self._data.get(key)

    def register_listener(self, key: str, callback: Callable[[Any], None]) -> None:
        self._listeners.setdefault(key, []).append(callback)

if __name__ == "__main__":
    state = UIState()

    def theme_changed(new):
        print(f"Theme updated to: {new}")

    state.register_listener("theme", theme_changed)

    print("Initial theme:", state.get_state("theme"))
    state.set_state("theme", "dark")
    state.set_state("theme", "light")