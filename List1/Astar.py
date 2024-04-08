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

normalizer = 100

def haversine(lat1, lon1, lat2, lon2):
    """Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)"""
    # convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6371 * c 
    velocity = 50

    return km/velocity * normalizer

def parse_departure_time(departure_time):
    if isinstance(departure_time, datetime.datetime):
        return departure_time
    elif isinstance(departure_time, str):
        return datetime.datetime.strptime(departure_time, "%H:%M:%S")
    else:
        raise ValueError("Nieobsługiwany typ danych dla czasu odjazdu/przyjazdu.")

def a_star_time(graph, start_stop, end_stop, departure_time_str):
    departure_datetime = parse_departure_time(departure_time_str)
    
    queue = []
    heapq.heappush(queue, (0, start_stop, departure_datetime, [(start_stop, None, departure_datetime, departure_datetime, None)]))

    visited = set()
    while queue:
        # Progress indicator
        # stopsCount = len(visited)/len(graph.nodes)
        # print(f"Progress: {stopsCount:.2f}")

        current_time, current_stop, current_datetime, path = heapq.heappop(queue)

        if current_stop in visited:
            continue
        visited.add(current_stop)

        if current_stop == end_stop:
            print(f"Testcase: {start_stop} -> {end_stop}")
            print(f"Optimization: t")
            print(f"Start Time: {departure_time_str}")
            print("Harmonogram przejazdu:")
            for segment in path[1:]:  
                _, line, dep, arr, _ = segment
                if line:  
                    print(f"Linia {line}, z {segment[4]} (odj. {dep.strftime('%H:%M:%S')}) do {segment[0]} (przyj. {arr.strftime('%H:%M:%S')})")
            total_travel_time = (current_datetime - departure_datetime).total_seconds() / 60  
            print(f"\nCałkowity czas podróży: {total_travel_time:.0f} minut")
            return path
        current_node = [node_id for node_id in graph.nodes if graph.nodes[node_id]['name'] == current_stop][0]
        for neighbor, departure, arrival, line in graph.get_neighbors_with_times_and_lines(current_stop, current_datetime):
            next_departure_datetime, next_arrival_datetime = departure, arrival
            wait_time = (next_departure_datetime - current_datetime).total_seconds() if next_departure_datetime > current_datetime else 0
            travel_time = (next_arrival_datetime - next_departure_datetime).total_seconds()
            new_current_datetime = next_arrival_datetime

            neighbor_node = [node_id for node_id in graph.nodes if graph.nodes[node_id]['name'] == neighbor][0]
            new_time = current_time + travel_time + wait_time + haversine(float(graph.nodes[current_node]['lat']), float(graph.nodes[current_node]['lon']), float(graph.nodes[neighbor_node]['lat']), float(graph.nodes[neighbor_node]['lon']))
            heapq.heappush(queue, (new_time, neighbor, new_current_datetime, path + [(neighbor, line, next_departure_datetime, next_arrival_datetime, current_stop)]))

    return (float('inf'), [])


def a_star_path(graph, start_stop, end_stop, departure_time_str):
    departure_datetime = parse_departure_time(departure_time_str)
    
    queue = []
    heapq.heappush(queue, (0, start_stop, departure_datetime, [(start_stop, None, departure_datetime, departure_datetime, None)]))

    visited = set()
    while queue:
        # Progress indicator
        # stopsCount = len(visited)/len(graph.nodes)
        # print(f"Progress: {stopsCount:.2f}")

        current_stops, current_stop, current_datetime, path = heapq.heappop(queue)

        if current_stop in visited:
            continue
        visited.add(current_stop)

        if current_stop == end_stop:
            print(f"Testcase: {start_stop} -> {end_stop}")
            print(f"Optimization: t")
            print(f"Start Time: {departure_time_str}")
            print("Harmonogram przejazdu:")
            for segment in path[1:]:  
                _, line, dep, arr, _ = segment
                if line:  
                    print(f"Linia {line}, z {segment[4]} (odj. {dep.strftime('%H:%M:%S')}) do {segment[0]} (przyj. {arr.strftime('%H:%M:%S')})")
            total_travel_time = (current_datetime - departure_datetime).total_seconds() / 60  
            print(f"\nCałkowity czas podróży: {total_travel_time:.0f} minut")
            print(f"Całkowita liczba przesiadek: {current_stops}")
            return path
        current_node = [node_id for node_id in graph.nodes if graph.nodes[node_id]['name'] == current_stop][0]
        current_line = path[-1][1]
        for neighbor, departure, arrival, line in graph.get_neighbors_with_times_and_lines(current_stop, current_datetime):
            next_departure_datetime, next_arrival_datetime = departure, arrival
            new_current_datetime = next_arrival_datetime
            changedLinesPenalty = 0 if current_line == line else 10
            neighbor_node = [node_id for node_id in graph.nodes if graph.nodes[node_id]['name'] == neighbor][0]
            new_stops_number = current_stops + changedLinesPenalty + haversine(float(graph.nodes[current_node]['lat']), float(graph.nodes[current_node]['lon']), float(graph.nodes[neighbor_node]['lat']), float(graph.nodes[neighbor_node]['lon']))
            heapq.heappush(queue, (new_stops_number, neighbor, new_current_datetime, path + [(neighbor, line, next_departure_datetime, next_arrival_datetime, current_stop)]))

    return (float('inf'), [])


def a_star_min_modified(graph, start_stop, end_stop, departure_time_str):
    departure_datetime = parse_departure_time(departure_time_str)
    
    queue = []
    heapq.heappush(queue, (0, start_stop, departure_datetime, [(start_stop, None, departure_datetime, departure_datetime, None)]))

    visited = set()
    while queue:
        # Progress indicator
        # stopsCount = len(visited)/len(graph.nodes)
        # print(f"Progress: {stopsCount:.2f}")

        current_value, current_stop, current_datetime, path = heapq.heappop(queue)

        if current_stop in visited:
            continue
        visited.add(current_stop)

        if current_stop == end_stop:
            print(f"Testcase: {start_stop} -> {end_stop}")
            print(f"Start Time: {departure_time_str}")
            print("Harmonogram przejazdu:")
            for segment in path[1:]:  
                _, line, dep, arr, _ = segment
                if line:  
                    print(f"Linia {line}, z {segment[4]} (odj. {dep.strftime('%H:%M:%S')}) do {segment[0]} (przyj. {arr.strftime('%H:%M:%S')})")
            total_travel_time = (current_datetime - departure_datetime).total_seconds() / 60  
            arrival_time = current_datetime.strftime('%H:%M:%S')
            return path, total_travel_time, arrival_time
        current_node = [node_id for node_id in graph.nodes if graph.nodes[node_id]['name'] == current_stop][0]
        current_line = path[-1][1]
        for neighbor, departure, arrival, line in graph.get_neighbors_with_times_and_lines(current_stop, current_datetime):
            next_departure_datetime, next_arrival_datetime = departure, arrival
            wait_time = (next_departure_datetime - current_datetime).total_seconds() if next_departure_datetime > current_datetime else 0
            travel_time = (next_arrival_datetime - next_departure_datetime).total_seconds()
            new_current_datetime = next_arrival_datetime
            changedLinesPenalty = 0 if current_line == line else 10

            neighbor_node = [node_id for node_id in graph.nodes if graph.nodes[node_id]['name'] == neighbor][0]
            new_stops_number = current_value+ wait_time+ travel_time+ changedLinesPenalty+   + haversine(float(graph.nodes[current_node]['lat']), float(graph.nodes[current_node]['lon']), float(graph.nodes[neighbor_node]['lat']), float(graph.nodes[neighbor_node]['lon']))
            heapq.heappush(queue, (new_stops_number, neighbor, new_current_datetime, path + [(neighbor, line, next_departure_datetime, next_arrival_datetime, current_stop)]))

    return (float('inf'), [])