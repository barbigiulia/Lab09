import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):

        self._controller = None
        self._grafo = nx.Graph()  # GRAFO NON ORIENTATO, PESATO
        self._nodes = DAO.getAllNodes()  # recupero tutti i nodi dalla query
        self.aeroportiMap = {}
        for n in self._nodes:
            self.aeroportiMap[n.ID] = n             # {id: Aeroporto1, id: Aeroporto2 ...}
        # Attenzione, "n" è un oggetto Aeroporto, quindi accedo all'attributo id con il punto


    def buildGraph(self, distanza_minima):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._nodes)  # ho aggiunto tutti i nodi (Aeroporti)
        self.addEdges(distanza_minima)  # aggiungo archi pesati

    def addEdges(self, distanza_minima):

        raw_flights = DAO.getAllFlights()

        # dizionario per tenere traccia dei dati
        dict_pesi = {}

        for id1,id2, dist in raw_flights:
            if id1> id2:
                id1, id2 = id2, id1   # normalizzo la coppia
                # il grafo non è orientato!
            if (id1, id2) not in dict_pesi:
                dict_pesi[(id1, id2)] = {"somma_distanze": 0, "num_voli": 0}  # se usassi il ramo else: il primo arco non viene mai aggiornato
            dict_pesi[(id1, id2)]["somma_distanze"] += dist
            dict_pesi[(id1, id2)]["num_voli"] += 1
        # calcolo le medie
        for (id1, id2), data in dict_pesi.items():
            if data["num_voli"] == 0:
                continue
            media = data["somma_distanze"] / data["num_voli"]

            if media > distanza_minima:
                # posso aggiungerlo come arco al grafo
                aeroporto_1 = self.aeroportiMap[id1]
                aeroporto_2 = self.aeroportiMap[id2]
                self._grafo.add_edge(aeroporto_1, aeroporto_2, weight=media)



    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

    # serve questa funzione per iterare archi con peso
    def getEdges(self):
        return self._grafo.edges(data=True)

    # senza data=True --> (A,B), (C,D) ....
    # con data=True --> (A, B, {'weight': 4300}), (C, D, {'weight': 3900})



    # SE VOLESSI ORDINARE LA DISTANZA IN ORDINE DECRESCENTE
    #def getEdgesSorted(self):
       # return sorted(self._grafo.edges(data=True), key=lambda x: x[2]['weight'],reverse=True   )