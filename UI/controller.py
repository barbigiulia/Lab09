import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_aeroporti(self, e):
        distanza_minima = self._view.txt_distanzaMinima.value
        self._view.txt_result.controls.clear()

        try:
            distanza = int(distanza_minima)
            self._model.buildGraph(distanza)  # GRAFO

            self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato",
                                                          color="green"))
            self._view.txt_result.controls.append(ft.Text(f"Il grafo contiente "
                                                          f"{self._model.getNumArchi()} archi e"
                                                          f" {self._model.getNumNodi()} nodi", color="blue"))

            self._view.txt_result.controls.append(ft.Text("Di seguito gli archi con la loro distanza relativa"))

            for u, v, d in self._model.getEdges():  # funzione di model con data=True
                # (u, v, {'weight': 4300.1234})  --> d è un dizionario!
                self._view.txt_result.controls.append(ft.Text(f"{u.IATA_CODE} - {v.IATA_CODE} : {d['weight']} miglia"))

            self._view.update_page()
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione, inserire una distanza valida",
                                                          color="red"))
            self._view.update_page()




