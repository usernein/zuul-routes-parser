import json
import pandas as pd

from glob import glob
from rich import print
from rich.progress import track
from sys import argv
from zuul_routes_parser.config import print_as_table, FileParser

def write_found_result(lenght, file_count):
     print(f"\n>>> Total de [bold green]{lenght}[/] rotas encontradas, dentre [bold green]{file_count}[/] arquivos analisados")

def main():
    routes = []
    file_parser = FileParser()
    file_count = 0
    extracted_routes = []
    
    for filename in track(glob('*.properties'), description="Lendo arquivos...", transient=True):
        file_count += 1
        try:
            file_parser.read(filename)
        except Exception as e:
            print(f"[red]{filename}:")
            print(e)
            continue

        extracted_routes = file_parser.extractRoutes()
        routes.extend(extracted_routes)

    lenght = len(extracted_routes)
    
    view_mode = (argv[1] if len(argv) > 1 else "table").lower()
    if view_mode == "json":
        print(json.dumps([*extracted_routes]))
        return
    elif view_mode == "csv":
        write_found_result(lenght, file_count)

        filename = input("\nInsira o nome do arquivo de destino do CSV:\n>>> ")

        dataframe = pd.DataFrame(data=extracted_routes)

        dataframe.to_csv(filename)
        print(f"\n:white_check_mark: Rotas exportadas com sucesso para [green]{filename}!")
    elif view_mode == "table":
        print_as_table(extracted_routes)
        write_found_result(lenght, file_count)
    

if __name__ == "__main__":
    main()