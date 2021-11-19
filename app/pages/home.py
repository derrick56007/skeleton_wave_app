from h2o_wave import Q, ui
from typing import List, Optional


async def init_page(q: Q, args: Optional[List[str]] = None) -> None:
    q.page['main_card'].items = [ui.text(q.app.changelog)]


async def deinit_page(q):
    q.page['main_card'].items = []


async def update_page(q: Q):
    pass
