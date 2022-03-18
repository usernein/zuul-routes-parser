import re

class FileParser:
    contents = ""

    def read(self, filename):
         with open(filename) as f:
            self.contents = f.read()
    
    def extractRoutes(self):
        routes = {}

        for match in re.finditer('(?<!\#)zuul\.routes\.(.+?)\.(.+?)=(.+)', self.contents):
            name, property, value = match.groups()

            if name not in routes:
                routes[name] = {}
            routes[name][property] = value
        
        return routes