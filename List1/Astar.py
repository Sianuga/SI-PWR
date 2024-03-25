import datetime
import heapq
from math import radians, cos, sin, asin, sqrt
import Graph

def h_geographic_euclidian(graph, node1, node2):
    lat1, lon1 = float(graph.nodes[node1]['lat']), float(graph.nodes[node1]['lon'])
    lat2, lon2 = float(graph.nodes[node2]['lat']), float(graph.nodes[node2]['lon'])
    degree_to_km = 111
    lat_km = abs(lat1 - lat2) * degree_to_km
    lon_km = abs(lon1 - lon2) * degree_to_km * cos(radians((lat1 + lat2) / 2))
    return sqrt(lat_km ** 2 + lon_km ** 2)

def h_geographic_manhattan(graph, node1, node2):
    lat1, lon1 = float(graph.nodes[node1]['lat']), float(graph.nodes[node1]['lon'])
    lat2, lon2 = float(graph.nodes[node2]['lat']), float(graph.nodes[node2]['lon'])
    degree_to_km = 111 
    lat_km = abs(lat1 - lat2) * degree_to_km
    lon_km = abs(lon1 - lon2) * degree_to_km * cos(radians((lat1 + lat2) / 2))  
    return lat_km + lon_km

def parse_time(departure_time):
    if isinstance(departure_time, datetime.datetime):
        return departure_time
    elif isinstance(departure_time, str):
        return datetime.datetime.strptime(departure_time, "%H:%M:%S")
    else:
        raise ValueError("Nieobsługiwany typ danych dla czasu odjazdu/przyjazdu.")

def a_star_time(graph, start_stop, end_stop, departure_time_str):
    departure_time = parse_time(departure_time_str)

    start_node = next((node for node in graph.nodes if graph.nodes[node]['name'] == start_stop), None)
    end_node = next((node for node in graph.nodes if graph.nodes[node]['name'] == end_stop), None)
    if not start_node or not end_node:
        return "Nie można znaleźć przystanku początkowego lub końcowego."
    
    open_set = [(0, start_node, departure_time, [])]

    heapq.heappush(open_set, (0, start_node, departure_time, []))
    closed_set = set()
    g_costs = {start_node: 0}

    print("C", graph.get_neighbors_with_times_and_lines(start_stop, departure_time))
    i=0
    while open_set:
        _, current_node, current_time, path = heapq.heappop(open_set)

        

        current_stop_name = graph.nodes[current_node]['name']
        print("B", current_node, current_time, path)

        if current_node == end_node:
            print(f"Testcase: {start_stop} -> {end_stop}")
            print(f"Optimization: t")
            print(f"Start Time: {departure_time_str}")
            print("Harmonogram przejazdu:")
            for segment in path[1:]:
                _, line, dep, arr, _ = segment
                if line:
                    print(f"Linia {line}, z {segment[0]} (odj. {dep.strftime('%H:%M:%S')}) do {segment[4]} (przyj. {arr.strftime('%H:%M:%S')})")
            total_travel_time = (current_time - departure_time).total_seconds() / 60
            print(f"\nCałkowity czas podróży: {total_travel_time:.0f} minut")
            
            return path + [end_node]

        closed_set.add(current_node)
     
        for neighbor_name, dep_time_str, arr_time_str, line in graph.get_neighbors_with_times_and_lines(current_stop_name, current_time):
            dep_time = parse_time(dep_time_str)
            arr_time = parse_time(arr_time_str)
            neighbor_node = next((node for node in graph.nodes if graph.nodes[node]['name'] == neighbor_name), None)

            if neighbor_node in closed_set or dep_time < current_time:
                continue

            new_g = g_costs[current_node] + (arr_time - dep_time).total_seconds()

            print("D", neighbor_node, dep_time, arr_time, line)
            print("E", g_costs[neighbor_node] if neighbor_node in g_costs else None, new_g)

            if neighbor_node not in g_costs or new_g < g_costs[neighbor_node]:
                g_costs[neighbor_node] = new_g
                # print("G", current_node)

                print("H", g_costs)

                f =  new_g + h_geographic_manhattan(graph, neighbor_node, end_node)

                print("I", f)
                heapq.heappush(open_set, (f, neighbor_node, arr_time, path + [current_node]))

        i+=1

        if i==1:
            break


    print("A ",current_node, current_time, path)

    return "Nie znaleziono ścieżki."
