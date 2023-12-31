#Ejercicio 1

def pertenece1 (s: list[int], e: int) -> bool:
    res = False
    i = 0
    while (i < len(s)): 
        if s[i] == e:
            res = True
        i += 1
    return res


def pertenece2 (s: list[int], e: int) -> bool:
    for i in range(len(s)):
        if s[i] == e:
            return True
    return False


#Ejercicio 2

def divideATodos(s: list[int], e: int) -> bool:
    res = True
    i = 0
    if s[i] % e != 0 and i <= len(s):
        res = False
        i += 1
    return res


#Ejercicio 3

def sumaTotal(s: list[int]) -> int:
    suma = 0
    for i in range(len(s)):
        suma += s[i]
    return suma


#Ejercicio 4

def ordenados(s: list[int]) -> bool:
    for i in range(1,len(s)):
        if s[i-1] >= s[i]:
            return False
    return True
    
            
#Ejercicio 5

def longPalabra(l: list[str]) -> bool:
    for i in range(len(l)):
        if len(l[i]) > 7:
            return True
    return False


#¿y si quiero que todas las palabras sean de longitud superior a 7?
def longPalabra1(l: list[str]) -> bool:
    for i in range(len(l)):
        if len(l[i]) <= 7:
            return False
    return True


#Ejercicio 6

def esPalindroma(s: str) -> bool:
    i = 0
    while i < int(len(s)/2):
        if s[i] == s[-i-1]:
            return True
        i += 1
    return False

    
def tieneMinus(s: str) -> bool:
    for i in range(len(s)):
        if s[i].islower():
            return True
    return False


def tieneMayus(s: str) -> bool:
    for i in range(len(s)):
        if s[i].isupper():
            return True
    return False


def esNumero(n: str) -> bool:
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if n in numeros:
        return True
    return False


def tieneNum(s: str) -> bool:
    for i in range(len(s)):
        if esNumero(s[i]):
            return True
    return False


def esContraseñaSegura(s: str) -> str:
    if len(s) > 8:
        if tieneMinus(s) and tieneMayus(s) and tieneNum(s):  
            return "VERDE"
    if len(s) < 5:
        return "ROJA"
    else:
        return "AMARILLA"


#Ejercicio 8

def saldoActual(l: list[(str,int)]) -> int:
    saldo = 0
    for i in range(len(l)): 
        if l[i][0] == "I":
            saldo += l[i][1]
        if l[i][0] == "R":
            saldo -= l[i][1]
    return saldo


#Ejercicio 9

def pertenece(s: list(), e) -> bool:
    for i in range(len(s)):
        if s[i] == e:
            return True
    return False


vocales = ["a", "e", "i", "o", "u"]

def numeroDeVocalesDistintas(s:str) -> int:
    apariciones = []
    contador = 0
    for i in range(len(s)):
        if pertenece(vocales, s[i]) and not pertenece(apariciones,s[i]):
            apariciones.append(s[i])
            contador += 1
    return contador


def vocalesDistintas(s: str) -> bool:
    if numeroDeVocalesDistintas(s) == 3:
        return True
    else:
        return False


#SEGUNDA PARTE

#Ejercicio 1

def cambiaPosicionesPares(l: list[int]) -> list[int]:
    i = 0
    while i < len(l):
        if esPar(i):
            l.insert(i,0)
            l.pop(i+1)
        i += 1
    return l 


def esPar(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False


#Ejercicio 2

def cambiaPosicionesPares2(l: list[int]) -> list[int]:
    i = 0
    l1 = []
    while i < len(l):
        if esPar(i):
            l1.append(0)
        else:
            l1.append(l[i])
        i += 1
    return l1


#Ejercicio 3

def sinVocales(s: str) -> str:
    nuevaS = s
    for i in range(len(s)):
        if pertenece(vocales, s[i]):
            nuevaS = nuevaS.replace(s[i], "")
    return nuevaS


#Ejercicio 4

def reemplazaVocales(s: str) -> str:
    nuevaS = s
    for i in range(len(s)):
        if pertenece(vocales, s[i]):
            nuevaS = nuevaS.replace(s[i], " ")
    return nuevaS


#Ejercicio 5

def daVueltaStr(s: str) -> str:
    nuevaS = ""
    for i in range(1,len(s)+1):
        nuevaS = nuevaS + s[-i]
    return nuevaS


#Ejercicio 6

def perteneceAcadaUno(l: list(list[int]), elem: int) -> list[bool]:
    res = []
    for i in range(len(l)):
        if pertenece(l[i], elem):
            res.append(True)
        else:
            res.append(False)
    return res


#Ejercicio 7

def esMatriz(m: list[list[int]]) -> bool:
    if len(m) == 0 | len(m[0]) == 0:
        return False
    for i in range(len(m)):
        if len(m[0]) != len(m[i]):
             return False
    return True


def ordenados(s: list[int]) -> bool:
    for i in range(1,len(s)):
        if s[i-1] >= s[i]:
            return False
    return True


#Ejercicio 8

def filasOrdenadas(m: list[list[int]]) -> list[bool]:
    i = 0
    res = []
    while i < len(m):
        if ordenados(m[i]):
            res.append(True)
        else:
            res.append(False)
        i += 1
    return res


