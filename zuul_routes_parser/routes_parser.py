import pathlib
import re


class FileParser:
    contents = ""

    def read(self, filename):
        self.contents = pathlib.Path(filename).read_text()

    def extractRoutes(self):
        routes = {}

        for match in re.finditer(
            r"(?<!\#)zuul\.routes\.(.+?)\.(.+?)=(.+)", self.contents
        ):
            name, property, value = match.groups()

            if name not in routes:
                routes[name] = {"name": name}
            routes[name][property] = value

        return routes.values()
