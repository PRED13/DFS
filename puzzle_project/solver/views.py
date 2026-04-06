from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json

from .puzzle_lineal_DFS import buscar_solucion_DFS

def home(request):
    return render(request, "index.html")

@csrf_exempt
def resolver(request):

    if request.method == "POST":

        data = json.loads(request.body)

        estado_inicial = data["inicio"]
        solucion = data["meta"]

        nodo_solucion = buscar_solucion_DFS(
            estado_inicial,
            solucion
        )

        resultado = []

        nodo = nodo_solucion

        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()

        resultado.reverse()

        return JsonResponse({
            "ruta": resultado,
            "pasos": len(resultado)
        })