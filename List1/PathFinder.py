import Djikstra
import Graph
import DataReader
import Astar
import Tabu

class PathFinder:
    def __init__(self):
        self.graph = None

    def loadGraph(self, fileName):
        self.graph = DataReader.process_csv(fileName)

    def getGraph(self):
        return self.graph

    def findPathDjikstra(self, startStop, endStop, criteria, departureTime):
        if criteria == "t":
            return Djikstra.dijkstra_time(self.graph, startStop, endStop, departureTime)
        elif criteria == "p":
            return Djikstra.dijkstra_path(self.graph, startStop, endStop, departureTime)
        else:
            return None
        
    def findPathAStar(self, startStop, endStop, criteria, departureTime):
        if criteria == "t":
            return Astar.a_star_time(self.graph, startStop, endStop, departureTime)
        elif criteria == "p":
            return Astar.a_star_path(self.graph, startStop, endStop, departureTime)
        elif criteria == "m":
            return Astar.a_star_min_modified(self.graph, startStop, endStop, departureTime)
        else:
            return None
        
    def findPathWithTabu(self, startStop, stopLists, criteria, departureTime):
        if criteria == "n":
            return Tabu.tabu_no_limit(self.graph, startStop, stopLists, departureTime)
        elif criteria == "t":
            return Tabu.tabu_tab_length(self.graph, startStop, stopLists, departureTime)
        elif criteria == "m":
            return Tabu.tabu_cost_min(self.graph, startStop, stopLists, departureTime)
        elif criteria == "s":
            return Tabu.tabu_sampling(self.graph, startStop, stopLists, departureTime)
        else:
            return None