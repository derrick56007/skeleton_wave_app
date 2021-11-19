from h2o_wave import Q, ui
from typing import List, Optional


async def init_page(q: Q, args: Optional[List[str]] = None) -> None:
    show_content(q)


async def deinit_page(q):
    q.page['main_card'].items = []


def show_content(q: Q):
    additional_content = []

    if q.args.button1:
        additional_content.append(ui.text('button1 pressed'))

    if q.args.button2:
        additional_content.append(ui.text('button2 pressed'))

    q.page['main_card'].items = [
        ui.button(name='button1', label='button1'),
        ui.button(name='button2', label='button2'),
        *additional_content,
    ]


async def update_page(q: Q):
    if q.args.button1:
        print('button1 pressed')

    if q.args.button2:
        print('button2 pressed')

    if q.args.button1 or q.args.button2:
        show_content(q)
