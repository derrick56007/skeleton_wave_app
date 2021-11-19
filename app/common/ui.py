from h2o_wave import Q, ui, expando_to_dict


def show_versioning_card(q: Q) -> None:
    q.page["title_card"] = ui.header_card(
        box="1 1 2 1",
        title=q.app.title,
        subtitle=f"Version {q.app.version}",
        icon="ExploreData",
        icon_color="$grey",
    )


def init_meta(q: Q) -> None:
    q.page['meta'] = ui.meta_card(
        box='',
        icon='https://www.issgovernance.com/file/images/iss_triamond_favicon.png',
        title=q.app.title,
    )


def init_menu_card(q: Q) -> None:
    q.page["menu_card"] = ui.nav_card(box="1 2 2 9", items=[])


def show_menu_card(q: Q) -> None:
    q.page["menu_card"].items = [
        ui.nav_group(
            label='Menu',
            items=[
                ui.nav_item(name=f"#{p}", label=p)
                for p in q.app.pages
            ],
        ),
    ]


def init_main_card(q: Q) -> None:
    q.page['main_card'] = ui.form_card(box='3 2 8 9', items=[])


def init_nav_card(q: Q) -> None:
    q.page['top_card'] = ui.form_card(box='3 1 8 1', items=[])


def init_user_card(q: Q) -> None:
    q.page['user_card'] = ui.form_card(box='10 1 1 1', items=[])


def save_all_args(q: Q) -> None:
    # https://wave.h2o.ai/docs/arguments#interpreting-arguments
    args = expando_to_dict(q.args)
    client = expando_to_dict(q.client)

    # values of args that have changed can be accessible by
    # q.client.NAME_OF_ARG_changed
    post_fix = '_changed'

    for arg in set(args.keys()) | set(client.keys()):
        if not arg.endswith(post_fix):
            k = f'{arg}{post_fix}'
            q.client[k] = q.args[arg] != None and q.client[arg] != q.args[arg]

            if q.client[k]:
                print(k, f'new_{arg}={q.args[arg]}', f'old_{arg}={q.client[arg]}')

            q.client[arg] = q.args[arg] if q.client[k] else q.client[arg]
