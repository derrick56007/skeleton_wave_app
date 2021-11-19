from types import ModuleType
from typing import List, Optional, Tuple
from h2o_wave import Q


def get_module(name: str, page: str) -> ModuleType:
    module = __import__(name, fromlist=[page])
    attr = getattr(module, page)
    return attr


def get_page_and_args_from_route(q: Q, route: Optional[str]) -> Tuple[str, List[str]]:
    page = q.client.route if not route else route
    args = page.split("/")
    page = args[0]
    args = args[1:]

    return page, args
