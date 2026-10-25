class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        source_cities = set()
        destination_cities = set()

        for source, destination in paths:
            source_cities.add(source)
            destination_cities.add(destination)

        for city in destination_cities:
            if city not in source_cities:
                return city
