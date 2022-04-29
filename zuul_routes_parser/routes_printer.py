from rich.console import Console
from rich.table import Table


def print_as_table(routes):
    table = Table(title="ms-gateway routes", show_lines=True)
    table.add_column("#", justify="right", style="cyan", no_wrap=True)
    table.add_column("Name", justify="left", style="green", no_wrap=True)

    keys_list = []
    for route in routes:
        for key in route.keys():
            if key in keys_list or key == "name":
                continue
            keys_list.append(key)
            table.add_column(key.capitalize(), justify="left", no_wrap=True)

    for count, route in enumerate(routes, start=1):
        values_to_show = [route.get(key, None) for key in keys_list]
        table.add_row(str(count), route["name"], *values_to_show)

    console = Console()
    console.print(table)
