from h2o_wave import Q, main, app, ui

from common import ui as common_ui
from common import utils as common_utils


async def init_app(q: Q) -> None:
    ########### Menu Items ##############
    q.app.title = "Skeleton Wave App"
    q.app.version = '21.11.19a'
    q.app.default_route = "home"

    with open('CHANGELOG.md', 'r') as file:
        q.app.changelog = file.read()

    q.app.pages = [
        'home',
        'example',
        # add pages here
    ]


async def init_client(q: Q) -> None:
    q.client.route = q.app.default_route

    common_ui.init_meta(q)
    common_ui.init_nav_card(q)
    common_ui.init_main_card(q)
    common_ui.init_menu_card(q)
    common_ui.show_menu_card(q)
    common_ui.show_versioning_card(q)

    # show default page (home)
    await common_utils.get_module('pages', q.client.route).init_page(q)


@app('/skeleton-wave-app')
async def serve(q: Q) -> None:
    common_ui.save_all_args(q)

    if not q.app.initialized:
        await init_app(q)
        q.app.initialized = True

    if not q.client.initialized:
        await init_client(q)
        q.client.initialized = True

    page, args = common_utils.get_page_and_args_from_route(q, q.args["#"])

    route = page or q.client.route
    route_changed = route != q.client.route
    old_route = q.client.route
    q.client.route = route

    current_page_module = common_utils.get_module('pages', q.client.route)

    if route_changed:
        await common_utils.get_module('pages', old_route).deinit_page(q)
        await current_page_module.init_page(q, args)
    else:
        await current_page_module.update_page(q)

    common_ui.show_versioning_card(q)

    await q.page.save()
