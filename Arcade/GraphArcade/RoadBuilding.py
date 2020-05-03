"""
Question: https://app.codesignal.com/arcade/graphs-arcade/kingdom-roads/CSzczQWdnYwmyEjvv
Every city should be connected to every other. Find out all the roads that are missing or not connected to some city.
Note: While missing routes are found, the roads should be appended to missing_routes list in the way [city1 < city2].

Time: O(cities*cities)
Space: O(cities*cities)

Code:
"""
def roadsBuilding(cities, roads):
    adj = [[0]*cities for i in range(cities)]
    for i, j in roads:
        adj[i][j] = 1
        adj[j][i] = 1
    missing_routes = []
    for i in range(cities-1):
        for j in range(i + 1, cities):
            if adj[i][j] == 0:
                missing_routes.append([i, j])
    return missing_routes
"""
Alternatively:
"""
def roadsBuilding(cities, roads):
    visited = set()
    new_routes = []

    for road in roads:
        x = road[0] if road[0] < road[1] else road[1]
        y = road[1] if road[1] > road[0] else road[0]

        visited.add((x, y))

    for city in range(cities):
        for route in range(cities):
            if city != route:
                x = city if city < route else route
                y = route if route > city else city

                if (x, y) not in visited:
                    visited.add((x, y))
                    new_routes.append([x, y])


    return new_routes
    


