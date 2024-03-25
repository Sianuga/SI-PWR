import PathFinder


graphData = "List1/connection_graph.csv"
testingGraph = "List1/testingGraph.csv"

def main():
    
    pathFinder = PathFinder.PathFinder()

    pathFinder.loadGraph(graphData)
    
    # print(pathFinder.findPathDjikstra("Babimojska", "Biegasa", "t", "16:58:00"))
    # print(pathFinder.findPathDjikstra("Kadłub NŻ", "Rogowska (P+R)", "t", "00:44:00"))
    # print(pathFinder.findPathDjikstra("SPISKA (Ośrodek sportu)", "Wallenroda", "t", "14:45:00"))
    # print(pathFinder.findPathDjikstra("most Grunwaldzki", "Krasińskiego", "t", "10:16:00"))
    # print(pathFinder.findPathDjikstra("Bajana", "Smolec - Wrocławska", "t", "21:03:00"))
    # print(pathFinder.findPathDjikstra("Krępicka", "Kadłub wieś", "t", "05:58:00"))
    # print(pathFinder.findPathDjikstra("KOSZAROWA (Szpital)", "Brzezia Łąka - cmentarz", "t", "11:38:00"))
    # print(pathFinder.findPathDjikstra("RĘDZIŃSKA", "TARNOGAJ", "t", "14:45:00"))
    # print(pathFinder.findPathDjikstra("SPISKA (Ośrodek sportu)", "Wallenroda", "t", "01:44:00"))
    # print(pathFinder.findPathDjikstra("Muchobór Wielki", "Wysoka - Lipowa", "t", "03:14:00"))
    # print(pathFinder.findPathDjikstra("Maślicka (Osiedle)", "Iwiny - Kolejowa", "t", "16:07:00"))
    # print(pathFinder.findPathDjikstra("Małkowice - Główna", "Kiełczów - Zgodna", "t", "10:39:00"))

    print(pathFinder.findPathAStar("Babimojska", "Biegasa", "t", "16:58:00"))
    # print(pathFinder.findPathAStar("Kadłub NŻ", "Rogowska (P+R)", "t", "00:44:00"))
    # print(pathFinder.findPathAStar("SPISKA (Ośrodek sportu)", "Wallenroda", "t", "14:45:00"))
    # print(pathFinder.findPathAStar("most Grunwaldzki", "Krasińskiego", "t", "10:16:00"))
    # print(pathFinder.findPathAStar("Bajana", "Smolec - Wrocławska", "t", "21:03:00"))
    # print(pathFinder.findPathAStar("Krępicka", "Kadłub wieś", "t", "05:58:00"))
    # print(pathFinder.findPathAStar("KOSZAROWA (Szpital)", "Brzezia Łąka - cmentarz", "t", "11:38:00"))
    # print(pathFinder.findPathAStar("RĘDZIŃSKA", "TARNOGAJ", "t", "14:45:00"))
    # print(pathFinder.findPathAStar("SPISKA (Ośrodek sportu)", "Wallenroda", "t", "01:44:00"))
    # print(pathFinder.findPathAStar("Muchobór Wielki", "Wysoka - Lipowa", "t", "03:14:00"))
    # print(pathFinder.findPathAStar("Maślicka (Osiedle)", "Iwiny - Kolejowa", "t", "16:07:00"))
    # print(pathFinder.findPathAStar("Małkowice - Główna", "Kiełczów - Zgodna", "t", "10:39:00"))

    # print(pathFinder.findPathWithTabu("Babimojska", ["Biegasa"], "n", "16:58:00"))
    # print(pathFinder.findPathWithTabu("Kadłub NŻ", ["Rogowska (P+R)"], "n", "00:44:00"))
    # print(pathFinder.findPathWithTabu("SPISKA (Ośrodek sportu)", ["Wallenroda"], "n", "14:45:00"))
    # print(pathFinder.findPathWithTabu("most Grunwaldzki", ["Krasińskiego"], "n", "10:16:00"))
    # print(pathFinder.findPathWithTabu("Bajana", ["Smolec - Wrocławska"], "n", "21:03:00"))
    # print(pathFinder.findPathWithTabu("Krępicka", ["Kadłub wieś"], "n", "05:58:00"))
    # print(pathFinder.findPathWithTabu("KOSZAROWA (Szpital)", ["Brzezia Łąka - cmentarz"], "n", "11:38:00"))
    # print(pathFinder.findPathWithTabu("RĘDZIŃSKA", ["TARNOGAJ"], "n", "14:45:00"))
    # print(pathFinder.findPathWithTabu("SPISKA (Ośrodek sportu)", ["Wallenroda"], "n", "01:44:00"))
    # print(pathFinder.findPathWithTabu("Muchobór Wielki", ["Wysoka - Lipowa"], "n", "03:14:00"))
    # print(pathFinder.findPathWithTabu("Maślicka (Osiedle)", ["Iwiny - Kolejowa"], "n", "16:07:00"))
    # print(pathFinder.findPathWithTabu("Małkowice - Główna", ["Kiełczów - Zgodna"], "n", "10:39:00"))


    

   


if __name__ == "__main__":
    main()

