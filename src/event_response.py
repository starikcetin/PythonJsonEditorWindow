class EventResponse:
    def __init__(self, handled: bool, should_relaunch: bool, values):
        self.should_relaunch = should_relaunch
        self.values = values
        self.handled = handled
