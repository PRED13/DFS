from http.server import BaseHTTPRequestHandler
import json
from puzzle_lineal_DFS import buscar_solucion_DFS


class handler(BaseHTTPRequestHandler):

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        data = json.loads(body)

        estado_inicial = data["inicio"]
        solucion = data["meta"]

        nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)

        resultado = []
        nodo = nodo_solucion

        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()

        resultado.reverse()

        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()

        self.wfile.write(json.dumps(resultado).encode())