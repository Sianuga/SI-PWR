import Djikstra
import Graph
import DataReader
import Astar
import Tabu
from timeit import default_timer as timer

class PathFinder:
    def __init__(self):
        self.graph = None

    def loadGraph(self, fileName):
        self.graph = DataReader.process_csv(fileName)

    def getGraph(self):
        return self.graph

    def findPathDjikstra(self, startStop, endStop, criteria, departureTime):
        start = timer()
        if criteria == "t":
            result = Djikstra.dijkstra_time(self.graph, startStop, endStop, departureTime)
            end = timer()
            print(" Czas wykonanie: ", end - start)
            return result
        elif criteria == "p":
            result = Djikstra.dijkstra_path(self.graph, startStop, endStop, departureTime)
            end = timer()
            print(" Czas wykonanie: ", end - start)
            return result
        else:
            return None

        
    def findPathAStar(self, startStop, endStop, criteria, departureTime):
        start = timer()
        if criteria == "t":
            result = Astar.a_star_time(self.graph, startStop, endStop, departureTime)
            end = timer()
            print(" Czas wykonanie: ", end - start)
            return result
        elif criteria == "p":
            result = Astar.a_star_path(self.graph, startStop, endStop, departureTime)
            end = timer()
            print(" Czas wykonanie: ", end - start)
            return result
        elif criteria == "m":
            result = Astar.a_star_min_modified(self.graph, startStop, endStop, departureTime)
            end = timer()
            print(" Czas wykonanie: ", end - start)
            return result
        else:
            return None
        
    def findPathWithTabu(self, startStop, stopLists, criteria, departureTime, tabuListSize, maxIterations):
        start = timer()
        if criteria == "n":
            result = Tabu.tabu_no_limit(stopLists, maxIterations, tabuListSize, departureTime, self.graph)
            end = timer()
            print(" Czas wykonanie: ", end - start)
            return result
        elif criteria == "t":
            result = Tabu.tabu_tab_length(self.graph, startStop, stopLists, departureTime, tabuListSize, maxIterations)
            end = timer()
            print(" Czas wykonanie: ", end - start)
            return result
        elif criteria == "m":
            result = Tabu.tabu_cost_min(self.graph, startStop, stopLists, departureTime, tabuListSize, maxIterations)
            end = timer()
            print(" Czas wykonanie: ", end - start)
            return result
        elif criteria == "s":
            result = Tabu.tabu_sampling(self.graph, startStop, stopLists, departureTime, tabuListSize, maxIterations)
            end = timer()
            print(" Czas wykonanie: ", end - start)
            return result
        else:
            return None