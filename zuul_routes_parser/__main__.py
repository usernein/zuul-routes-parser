import json

from glob import glob
from rich import print
from rich.progress import track
from sys import argv
from zuul_routes_parser.config import print_as_table, FileParser

def main():
    routes = {}
    file_parser = FileParser()
    file_count = 0
    extracted_routes = {}
    
    for filename in track(glob('*.properties'), description="Lendo arquivos...", transient=True):
        file_count += 1
        file_parser.read(filename)

        extracted_routes = file_parser.extractRoutes()
        routes.update(extracted_routes)

    lenght = len(extracted_routes)
    
    view_mode = (argv[1] if len(argv) > 1 else "table").lower()
    if view_mode == "json":
        print(json.dumps(extracted_routes))
        return
    elif view_mode == "csv":
        return
    elif view_mode == "xls":
        return
    elif view_mode == "table":
        print_as_table(extracted_routes)

    print(f"\n>>> Total de [bold green]{lenght}[/] rotas encontradas, dentre [bold green]{file_count}[/] arquivos analisados")

if __name__ == "__main__":
    main()