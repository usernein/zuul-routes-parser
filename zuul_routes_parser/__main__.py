import json
import pandas as pd
import sys
import time

from glob import glob
from rich import print
from rich.progress import track, Progress, BarColumn
from zuul_routes_parser.config import print_as_table, FileParser


def write_found_result(total_routes, file_count):
    print(
        f"\n>>> Total de [bold green]{total_routes}[/] rotas encontradas,"
        f" dentre [bold green]{file_count}[/] arquivos analisados"
    )


def main():
    routes = []
    file_parser = FileParser()
    files = glob("*.properties")

    for filename in track(
        files,
        description="Lendo arquivos...",
        transient=True,
        total=len(files),
    ):
        try:
            file_parser.read(filename)
        except Exception as e:
            print(f"[red]{filename}:")
            print(e)
            continue

        extracted_routes = file_parser.extractRoutes()
        routes.extend(extracted_routes)

        time.sleep(0.01)

    view_mode = (sys.argv[1] if len(sys.argv) > 1 else "table").lower()

    with Progress(
        "[progress.description]{task.description}", BarColumn(), transient=True
    ) as progress:
        progress.add_task("Formatando dados...", start=False)

        if view_mode == "json":
            print(json.dumps([*routes]))
        elif view_mode == "csv":
            progress.stop()
            write_to_csv(progress, len(routes), len(files), routes)
        elif view_mode == "table":
            print_as_table(routes)
            write_found_result(len(routes), len(files))


def write_to_csv(progress, total_routes, file_count, routes):
    write_found_result(total_routes, file_count)

    if not routes:
        print("\n:yawning_face: Nada foi exportado...")
        return

    csv_filename = (
        sys.argv[2]
        if len(sys.argv) > 2
        else input("\nInsira o nome do arquivo de destino do CSV:\n>>> ")
    )

    dataframe = pd.DataFrame(data=routes)
    dataframe.to_csv(csv_filename)

    print(
        "\n:white_check_mark: Rotas exportadas com"
        f" sucesso para [green]{csv_filename}!"
    )


if __name__ == "__main__":
    main()
