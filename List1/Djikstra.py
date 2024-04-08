import heapq
import datetime

def parse_departure_time(departure_time):
    if isinstance(departure_time, datetime.datetime):
        return departure_time
    elif isinstance(departure_time, str):
        return datetime.datetime.strptime(departure_time, "%H:%M:%S")
    else:
        raise ValueError("Nieobsługiwany typ danych dla czasu odjazdu/przyjazdu.")


def dijkstra_time(graph, start_stop, end_stop, departure_time_str):
    departure_datetime = parse_departure_time(departure_time_str)
    
    queue = []
    heapq.heappush(queue, (0, start_stop, departure_datetime, [(start_stop, None, departure_datetime, departure_datetime, None)]))

    visited = set()
    while queue:
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
           
        for neighbor, departure, arrival, line in graph.get_neighbors_with_times_and_lines(current_stop, current_datetime):
            next_departure_datetime, next_arrival_datetime = departure, arrival
            wait_time = (next_departure_datetime - current_datetime).total_seconds() if next_departure_datetime > current_datetime else 0
            travel_time = (next_arrival_datetime - next_departure_datetime).total_seconds()
            new_current_datetime = next_arrival_datetime
            new_time = current_time + travel_time + wait_time
            heapq.heappush(queue, (new_time, neighbor, new_current_datetime, path + [(neighbor, line, next_departure_datetime, next_arrival_datetime, current_stop)]))

    return (float('inf'), [])

