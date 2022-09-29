from django.shortcuts import render
import math

def home(request):
    return render(request, 'systemoperator/home.html')

def about(request):
    return render(request, 'systemoperator/about.html')


def primos(request):
    return render(request, 'systemoperator/primos.html')

def multiplos(request):
    return render(request, 'systemoperator/multiplos.html')

def factorial(request):
    return render(request, 'systemoperator/factorial.html')

def logaritmo(request):
    return render(request, 'systemoperator/logaritmo.html')
    
def rPrimo(request):
    x = int(request.GET.get('num'))
    contador = 0
    resultado = ''
    for i in range(1,x):
        if i == 1 or i == x:
            continue
        if x % i == 0:
            contador += 1
    if contador == 0:
        resultado = "si es un número primo"
    else:
        resultado = "no es un número primo"
    return render(request, 'systemoperator/rPrimo.html', {'resultadoPrimo': f'{x} {resultado}'})

def rMultiplo(request):
    numero = int(request.GET.get('numero'))
    rangoFinal = int(request.GET.get('rangoFinal'))
    resultado = []
    for i in range(0, rangoFinal + 1, numero):
        if i == 0:
            continue
        resultado.append(i)
    return render(request, 'systemoperator/rMultiplo.html', {'resultadoMultiplo': f'Los múltiplos de {numero} del 0 al {rangoFinal} son: {resultado}'})

def rFactorial(request):
    n = int(request.GET.get('factorial'))
    resultado = 1
    if n != 0:
        for i in range(1, n + 1):
            resultado = resultado * i
    return render(request, 'systemoperator/rFactorial.html', {'resultadoFactorial': f'El factorial de {n} es: {resultado}'})

def rLogaritmo(request):
    xNum = int(request.GET.get('numF'))
    base = int(request.GET.get('base'))
    return render(request, 'systemoperator/rLogaritmo.html', {'resultadoLogaritmo': f'El Logaritmo de {xNum} con base {base} es: {math.log(xNum) / math.log(base)}'})