from glob import glob
from routes_parser import FileParser
from pprint import pprint

routes = {}
file_parser = FileParser()

for filename in glob('resources/*.properties'):
    file_parser.read(filename)

    extracted_routes = file_parser.extractRoutes()
    routes.update(extracted_routes)

pprint(routes)