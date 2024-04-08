import PathFinder


graphData = "List1/connection_graph.csv"
testingGraph = "List1/testingGraph.csv"

def main():
    
    pathFinder = PathFinder.PathFinder()

    pathFinder.loadGraph(graphData)
    
    # pathFinder.findPathDjikstra("Babimojska", "Biegasa", "t", "16:58:00")
    # pathFinder.findPathDjikstra("Kadłub NŻ", "Rogowska (P+R)", "t", "00:44:00")
    # pathFinder.findPathDjikstra("SPISKA (Ośrodek sportu)", "Wallenroda", "t", "14:45:00")
    # pathFinder.findPathDjikstra("most Grunwaldzki", "Krasińskiego", "t", "10:16:00")
    # pathFinder.findPathDjikstra("Bajana", "Smolec - Wrocławska", "t", "21:03:00")
    # pathFinder.findPathDjikstra("Krępicka", "Kadłub wieś", "t", "05:58:00")
    # pathFinder.findPathDjikstra("KOSZAROWA (Szpital)", "Brzezia Łąka - cmentarz", "t", "11:38:00")
    # pathFinder.findPathDjikstra("RĘDZIŃSKA", "TARNOGAJ", "t", "14:45:00")
    # pathFinder.findPathDjikstra("SPISKA (Ośrodek sportu)", "Wallenroda", "t", "01:44:00")
    # pathFinder.findPathDjikstra("Muchobór Wielki", "Wysoka - Lipowa", "t", "03:14:00")
    # pathFinder.findPathDjikstra("Maślicka (Osiedle)", "Iwiny - Kolejowa", "t", "16:07:00")
    # pathFinder.findPathDjikstra("Małkowice - Główna", "Kiełczów - Zgodna", "t", "10:39:00")

    # pathFinder.findPathAStar("Babimojska", "Biegasa", "t", "16:58:00")
    # pathFinder.findPathAStar("Kadłub NŻ", "Rogowska (P+R)", "t", "00:44:00")
    # pathFinder.findPathAStar("SPISKA (Ośrodek sportu)", "Wallenroda", "t", "14:45:00")
    # pathFinder.findPathAStar("most Grunwaldzki", "Krasińskiego", "t", "10:16:00")
    # pathFinder.findPathAStar("Bajana", "Smolec - Wrocławska", "t", "21:03:00")
    # pathFinder.findPathAStar("Krępicka", "Kadłub wieś", "t", "05:58:00")
    # pathFinder.findPathAStar("KOSZAROWA (Szpital)", "Brzezia Łąka - cmentarz", "t", "11:38:00")
    # pathFinder.findPathAStar("RĘDZIŃSKA", "TARNOGAJ", "t", "14:45:00")
    # pathFinder.findPathAStar("SPISKA (Ośrodek sportu)", "Wallenroda", "t", "01:44:00")
    # pathFinder.findPathAStar("Muchobór Wielki", "Wysoka - Lipowa", "t", "03:14:00")
    # pathFinder.findPathAStar("Maślicka (Osiedle)", "Iwiny - Kolejowa", "t", "16:07:00")
    # pathFinder.findPathAStar("Małkowice - Główna", "Kiełczów - Zgodna", "t", "10:39:00")

    pathFinder.findPathAStar("Babimojska", "Biegasa", "p", "16:58:00")
    pathFinder.findPathAStar("Kadłub NŻ", "Rogowska (P+R)", "p", "00:44:00")
    pathFinder.findPathAStar("SPISKA (Ośrodek sportu)", "Wallenroda", "p", "14:45:00")
    pathFinder.findPathAStar("most Grunwaldzki", "Krasińskiego", "p", "10:16:00")
    pathFinder.findPathAStar("Bajana", "Smolec - Wrocławska", "p", "21:03:00")
    pathFinder.findPathAStar("Krępicka", "Kadłub wieś", "p", "05:58:00")
    pathFinder.findPathAStar("KOSZAROWA (Szpital)", "Brzezia Łąka - cmentarz", "p", "11:38:00")
    # pathFinder.findPathAStar("RĘDZIŃSKA", "TARNOGAJ", "p", "14:45:00")
    # pathFinder.findPathAStar("SPISKA (Ośrodek sportu)", "Wallenroda", "p", "01:44:00")
    # pathFinder.findPathAStar("Muchobór Wielki", "Wysoka - Lipowa", "p", "03:14:00")
    # pathFinder.findPathAStar("Maślicka (Osiedle)", "Iwiny - Kolejowa", "p", "16:07:00")
    # pathFinder.findPathAStar("Małkowice - Główna", "Kiełczów - Zgodna", "p", "10:39:00")

    # pathFinder.findPathAStar("Babimojska", "Biegasa", "m", "16:58:00")
    # pathFinder.findPathAStar("Kadłub NŻ", "Rogowska (P+R)", "m", "00:44:00")
    # pathFinder.findPathAStar("SPISKA (Ośrodek sportu)", "Wallenroda", "m", "14:45:00")
    # pathFinder.findPathAStar("most Grunwaldzki", "Krasińskiego", "m", "10:16:00")
    # pathFinder.findPathAStar("Bajana", "Smolec - Wrocławska", "m", "21:03:00")
    # pathFinder.findPathAStar("Krępicka", "Kadłub wieś", "m", "05:58:00")
    # pathFinder.findPathAStar("KOSZAROWA (Szpital)", "Brzezia Łąka - cmentarz", "m", "11:38:00")
    # pathFinder.findPathAStar("RĘDZIŃSKA", "TARNOGAJ", "m", "14:45:00")
    # pathFinder.findPathAStar("SPISKA (Ośrodek sportu)", "Wallenroda", "m", "01:44:00")
    # pathFinder.findPathAStar("Muchobór Wielki", "Wysoka - Lipowa", "m", "03:14:00")
    # pathFinder.findPathAStar("Maślicka (Osiedle)", "Iwiny - Kolejowa", "m", "16:07:00")
    # pathFinder.findPathAStar("Małkowice - Główna", "Kiełczów - Zgodna", "m", "10:39:00")

    # pathFinder.findPathWithTabu("Tyrmanda", ["Kwiska", "FAT", "PL. GRUNWALDZKI","Złotniki","Młodych Techników"], "n", "8:40:00", float('inf'), 7)
    # pathFinder.findPathWithTabu("Tyrmanda", ["Kwiska", "FAT", "PL. GRUNWALDZKI","Złotniki","Młodych Techników"], "n", "8:40:00", 15, 8)
    
    # pathFinder.findPathWithTabu("Tyrmanda", ["Kwiska", "FAT", "PL. GRUNWALDZKI","Złotniki","Młodych Techników"], "t", "8:40:00", float('inf'), 7)
    # pathFinder.findPathWithTabu("Tyrmanda", ["Kwiska", "FAT", "PL. GRUNWALDZKI","Złotniki","Młodych Techników"], "t", "8:40:00", 15, 8)

    # pathFinder.findPathWithTabu("Tyrmanda", ["Kwiska", "FAT", "PL. GRUNWALDZKI","Złotniki","Młodych Techników"], "m", "8:40:00", float('inf'), 7)
    # pathFinder.findPathWithTabu("Tyrmanda", ["Kwiska", "FAT", "PL. GRUNWALDZKI","Złotniki","Młodych Techników"], "m", "8:40:00", 15, 8)

    # pathFinder.findPathWithTabu("Tyrmanda", ["Kwiska", "FAT", "PL. GRUNWALDZKI","Złotniki","Młodych Techników"], "s", "8:40:00", float('inf'), 7)
    # pathFinder.findPathWithTabu("Tyrmanda", ["Kwiska", "FAT", "PL. GRUNWALDZKI","Złotniki","Młodych Techników"], "s", "8:40:00", 15, 8)

    # pathFinder.findPathWithTabu("Tyrmanda", ["Kwiska", "FAT", "PL. GRUNWALDZKI","Złotniki","Młodych Techników"], "p", "8:40:00", float('inf'), 7)
    # pathFinder.findPathWithTabu("Tyrmanda", ["Kwiska", "FAT", "PL. GRUNWALDZKI","Złotniki","Młodych Techników"], "p", "8:40:00", 15, 8)

   


if __name__ == "__main__":
    main()

