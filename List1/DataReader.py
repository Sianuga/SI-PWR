import csv
import datetime
from Graph import Graph

def parse_custom_time(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    days_passed = hours // 24
    remaining_hours = hours % 24
    time_obj = datetime.datetime.strptime(f"{remaining_hours}:{minutes}:{seconds}", "%H:%M:%S")
    time_obj += datetime.timedelta(days=days_passed)
    return time_obj

def process_csv(file_path):
    graph = Graph()

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            departure_time = parse_custom_time(row["departure_time"])
            arrival_time = parse_custom_time(row["arrival_time"])
            
            graph.add_node(row["start_stop"], row["start_stop_lat"], row["start_stop_lon"])
            graph.add_node(row["end_stop"], row["end_stop_lat"], row["end_stop_lon"])
            graph.add_edge(row["start_stop"], row["end_stop"], departure_time, arrival_time, row["line"])

    return graph
