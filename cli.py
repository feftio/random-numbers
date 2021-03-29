from rich.table import Table
from rich.console import Console

console = Console()


def items_to_string(items):
    for i in range(len(items)):
        if isinstance(items[i], list):
            for j in range(len(items[i])):
                items[i][j] = str(items[i][j])
        if isinstance(items[i], (int, float, str)):
            items[i] = [str(items[i])]
    return items


class cli:

    @staticmethod
    def out(*args, **kwargs):
        console.print(*args, **kwargs)

    @staticmethod
    def wait():
        console.input()

    @staticmethod
    def table(headers, rows, *args, autoheader=None, autostart=1, autoformat='{}', **kwargs):
        table = Table(show_header=True,
                      header_style='magenta', *args, **kwargs)
        rows = items_to_string(rows)
        if isinstance(autoheader, str):
            table.add_column(autoheader)
            for i in range(len(rows)):
                rows[i].insert(0, autoformat.format(i + autostart))
        for header in headers:
            table.add_column(str(header))
        for row in rows:
            table.add_row(*row)
        console.print(table)

    @staticmethod
    def str(*args, **kwargs):
        return str(console.input(*args, **kwargs))

    @staticmethod
    def int(*args, **kwargs):
        return int(console.input(*args, **kwargs))

    @staticmethod
    def float(*args, **kwargs):
        return float(console.input(*args, **kwargs))

    @staticmethod
    def float_list(*args, **kwargs):
        return [float(value) for value in console.input(*args, **kwargs).split()]

    @staticmethod
    def int_list(*args, **kwargs):
        return [int(value) for value in console.input(*args, **kwargs).split()]
