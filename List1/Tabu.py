import datetime

def parse_departure_time(departure_time):
    if isinstance(departure_time, datetime.datetime):
        return departure_time
    elif isinstance(departure_time, str):
        return datetime.datetime.strptime(departure_time, "%H:%M:%S")
    else:
        raise ValueError("Nieobsługiwany typ danych dla czasu odjazdu/przyjazdu.")

solution_with_costs = {}

def haversine(lat1, lon1, lat2, lon2):

    # convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6371 * c 
    velocity = 50
    return km/velocity

def objective_function(solution, departureTime, graph):
    solution_typle = tuple(solution)

    if solution_typle in solution_with_costs:
        return solution_with_costs[solution_typle]
    
    departure_datetime = parse_departure_time(departureTime)
    start_stop = solution[0]
    end_stop = solution[-1]

    solution_copy = solution.copy()
    solution_copy.insert(0, start_stop)

    sum_cost = 0

    for stop in range(len(solution_copy) - 1):
        current_stop = solution_copy[stop]
        next_stop = solution_copy[stop + 1]

        current_stop_node = [node_id for node_id in graph.nodes if graph.nodes[node_id]['name'] == current_stop][0]
        next_stop_node = [node_id for node_id in graph.nodes if graph.nodes[node_id]['name'] == next_stop][0]

        travel_time = haversine(float(graph.nodes[current_stop_node]['lat']), float(graph.nodes[current_stop_node]['lon']), float(graph.nodes[next_stop_node]['lat']), float(graph.nodes[next_stop_node]['lon']))

        sum_cost += travel_time

    solution_with_costs[solution_typle] = sum_cost
    return sum_cost

from math import asin, cos, radians, sin, sqrt
import random

sampleSize = 7

def getNeighboursSample(neighbours):
    return random.sample(neighbours, sampleSize)

def get_neighbors(current_solution):
    neighbors = []
    
    for i in range(len(current_solution)):
        for j in range(i + 1, len(current_solution)):
            neighbor = current_solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)

    return getNeighboursSample(neighbors)

def get_neighbors_sorted(current_solution, departureTime, graph, sampleSize):
    neighbors = []
    
    for i in range(len(current_solution)):
        for j in range(i + 1, len(current_solution)):
            neighbor = current_solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    
    sorted_neighbors = sorted(neighbors, key=lambda x: objective_function(x, departureTime, graph))
    
    # Return the top performing neighbors as per the objective function
    top_neighbors = sorted_neighbors[:sampleSize]

    return top_neighbors



def tabu_no_limit(initial_solution, max_iterations, tabu_list_size, departureTime, graph):
    current_solution = initial_solution
    best_solution = initial_solution
    tabu_list = []

    for i in range(max_iterations):
        neighbours = get_neighbors(current_solution)
        best_neighbour = None
        best_neighbour_fittness = float('inf')

        for neighbour in neighbours:
            if neighbour not in tabu_list:
                neighbour_fitness = objective_function(neighbour, departureTime,graph)
                if neighbour_fitness < best_neighbour_fittness:
                    best_neighbour = neighbour
                    best_neighbour_fittness = neighbour_fitness

        if best_neighbour is None:
            print("No better solution found: ", best_neighbour)
            break

        current_solution = best_neighbour
        tabu_list.append(best_neighbour)
        if len(tabu_list) > tabu_list_size:
            tabu_list.pop(0)

        if best_neighbour_fittness < objective_function(best_solution, departureTime, graph):
            best_solution = best_neighbour

    print("Best solution: ", best_solution)
    print("Best solution fitness: ", objective_function(best_solution, departureTime, graph))

    import Astar

    # Calculate total cost and road for best solution

    departure_datetime = parse_departure_time(departureTime)
    start_stop = best_solution[0]
    total_cost = 0

    for stop in best_solution[1:]:
        _, cost, arrival_time = Astar.a_star_min_modified(graph, start_stop, stop, departureTime)
        print(f"From {start_stop} to {stop} cost: {cost}")
        print(f"Arrival time: {arrival_time}")
        start_stop = stop
        total_cost += cost

    print(f"Total cost: {total_cost}")



    return best_solution


def tabu_aspiration(initial_solution, max_iterations, tabu_list_size, departureTime, graph):
    current_solution = initial_solution
    best_solution = initial_solution
    tabu_list = []

    for i in range(max_iterations):
        neighbours = get_neighbors(current_solution)
        best_neighbour = None
        best_neighbour_fittness = float('inf')
        best_global_fitness = objective_function(best_solution, departureTime, graph)

        for neighbour in neighbours:
            if neighbour not in tabu_list:
                neighbour_fitness = objective_function(neighbour, departureTime,graph)
                # Aspiration criterion: Accept a tabu move if it has better fitness than the best global fitness.
                if neighbour_fitness < best_neighbour_fittness  and (neighbour not in tabu_list or neighbour_fitness < best_global_fitness):
                    best_neighbour = neighbour
                    best_neighbour_fittness = neighbour_fitness

        if best_neighbour is None:
            print("No better solution found: ", best_neighbour)
            break

        current_solution = best_neighbour
        tabu_list.append(best_neighbour)
        if len(tabu_list) > tabu_list_size:
            tabu_list.pop(0)

        if best_neighbour_fittness < best_global_fitness:
            best_solution = best_neighbour
            best_global_fitness = best_neighbour_fittness

    print("Best solution: ", best_solution)
    print("Best solution fitness: ", objective_function(best_solution, departureTime, graph))

    import Astar

    # Calculate total cost and road for best solution

    departure_datetime = parse_departure_time(departureTime)
    start_stop = best_solution[0]
    total_cost = 0

    for stop in best_solution[1:]:
        _, cost, arrival_time = Astar.a_star_min_modified(graph, start_stop, stop, departureTime)
        print(f"From {start_stop} to {stop} cost: {cost}")
        print(f"Arrival time: {arrival_time}")
        start_stop = stop
        total_cost += cost

    print(f"Total cost: {total_cost}")



    return best_solution

def tabu_neigboursStrat(initial_solution, max_iterations, tabu_list_size, departureTime, graph):
    current_solution = initial_solution
    best_solution = initial_solution
    tabu_list = []

    for i in range(max_iterations):
       
        top_neighbours = get_neighbors_sorted(current_solution, departureTime, graph, sampleSize)
        
        best_neighbour = None
        best_neighbour_fittness = float('inf')

        for neighbour in top_neighbours:
            if neighbour not in tabu_list:
                neighbour_fitness = objective_function(neighbour, departureTime,graph)
                if neighbour_fitness < best_neighbour_fittness:
                    best_neighbour = neighbour
                    best_neighbour_fittness = neighbour_fitness

        if best_neighbour is None:
            print("No better solution found: ", best_neighbour)
            break

        current_solution = best_neighbour
        tabu_list.append(best_neighbour)
        if len(tabu_list) > tabu_list_size:
            tabu_list.pop(0)

        if best_neighbour_fittness < objective_function(best_solution, departureTime, graph):
            best_solution = best_neighbour

    print("Best solution: ", best_solution)
    print("Best solution fitness: ", objective_function(best_solution, departureTime, graph))

    import Astar

    # Calculate total cost and road for best solution

    departure_datetime = parse_departure_time(departureTime)
    start_stop = best_solution[0]
    total_cost = 0

    for stop in best_solution[1:]:
        _, cost, arrival_time = Astar.a_star_min_modified(graph, start_stop, stop, departureTime)
        print(f"From {start_stop} to {stop} cost: {cost}")
        print(f"Arrival time: {arrival_time}")
        start_stop = stop
        total_cost += cost

    print(f"Total cost: {total_cost}")



    return best_solution
