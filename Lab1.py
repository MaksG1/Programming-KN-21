class Route:
    def __init__(self, start, finish, *lengths):
        self.start = start
        self.finish = finish
        self.lengths = list(map(int, lengths))

    def __str__(self):
        return f"{self.start} - {self.finish}: {' + '.join(map(str, self.lengths))} = {self.get_length()} km"

    def get_length(self):
        return sum(self.lengths)

    def number_of_stops(self):
        return len(self.lengths)

    def __lt__(self, other):
        return self.get_length() < other.get_length()

    def __eq__(self, other):
        return self.get_length() == other.get_length()


def display_routes_with_max_stops(routes):
    max_stops = max(routes, key=lambda r: r.number_of_stops()).number_of_stops()
    for route in routes:
        if route.number_of_stops() == max_stops:
            print(route)


def display_route_with_longest_segment(routes):
    longest_segment = max(routes, key=lambda r: max(r.lengths))
    print(longest_segment)


def display_routes_with_start_or_end(routes, point):
    for route in routes:
        if route.start == point or route.finish == point:
            print(route)


routes = [
    Route("Київ", "Одеса", 10, 15, 20),
    Route("Львів", "Харків", 5, 10, 15),
    Route("Тернопіль", "Чернівці", 7, 6, 4),
    Route("Дніпро", "Запоріжжя", 20, 30, 10),
    Route("Івано-Франківськ", "Львів", 15, 10),
    Route("Одеса", "Львів", 5, 5, 5),
    Route("Харків", "Київ", 8, 8, 12),
    Route("Ужгород", "Львів", 10, 5, 5),
    Route("Чернівці", "Київ", 12, 12, 12),
    Route("Запоріжжя", "Дніпро", 5, 5, 5, 5)
]

routes.sort()

print("Routes with the maximum number of stops:")
display_routes_with_max_stops(routes)

print("\nRoute with the longest segment:")
display_route_with_longest_segment(routes)

print("\nRoutes with start or end at 'Київ':")
display_routes_with_start_or_end(routes, "Київ")