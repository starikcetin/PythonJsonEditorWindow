from typing import Callable
from event_params import EventParams
from event_response import EventResponse


class CustomEventHandler:
    def __init__(self, event_name: str, handler: Callable[[EventParams], EventResponse]):
        self.event_name = event_name
        self.handler = handler

    def handle(self, params: EventParams) -> EventResponse:
        if params.event is self.event_name:
            return self.handler(params)
        else:
            return EventResponse(False, False, params.values)
