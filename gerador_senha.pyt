#imports
import random

#valor da senha
senha = ""

#arrays
letrasMaiusculas = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]
letrasMinusculas = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y",
    "z"
]
caracterEspecial = [
    "!","@","#","$","%","^","&","*","(",")","_","+","-","=","[","]","{","}","|",";",":",",",".","<",">","?","/"
]
numeros = [
    "0","1","2","3","4","5","6","7","8","9"
]

#variaveis boolean
addMaiusculas = False
addMinusculas = False
addEspeciais = False
addNumeros = False

#variavel de quantidades de caracteres na senha
caracter = 0

#perguntas
perguntaAddMaiusculas = input("deseja letras maiusculas na sua senha?(SIM/NÃO)")
perguntaAddMinusculas = input("deseja letras minusculas na sua senha?(SIM/NÃO)")
perguntaAddEspeciais = input("deseja caracter especial na sua senha?(SIM/NÃO)")
perguntaAddNumeros = input("deseja numeros na sua senha?(SIM/NÃO)")
perguntaQuantidadeCaracteres = int(input("didgite quantos caracteres tera sua senha?(Apenas numeros)"))

#definindo numero de caracteres
caracter = perguntaQuantidadeCaracteres

#ajustando especificações da senha 
if perguntaAddMaiusculas == "sim":
    addMaiusculas = True

if perguntaAddMinusculas == "sim":
    addMinusculas = True

if perguntaAddEspeciais == "sim":
    addEspeciais = True

if perguntaAddNumeros == "sim":
    addNumeros = True

def resAddMaiusculas():
    maiusculasAleatoria = random.choice(letrasMaiusculas)
    return maiusculasAleatoria

def resAddMinusculas():
    minusculasAleatoria = random.choice(letrasMinusculas)
    return minusculasAleatoria

def resAddEspeciais():
    especiaisAleatorio = random.choice(caracterEspecial)
    return especiaisAleatorio

def resAddNumeros():
    numerosAleatorio = random.choice(numeros)
    return numerosAleatorio

#gerando a senha
index = 1

while index <= caracter:

    if addMaiusculas:
        senha += resAddMaiusculas()
        index = index +1
    
    if index <= caracter:
        if addMinusculas:
            senha += resAddMinusculas()
            index = index +1

    if index <= caracter:
        if addEspeciais:
            senha += resAddEspeciais()
            index = index +1

    if index <= caracter:
        if addNumeros:
            senha += resAddNumeros()
            index = index +1
    
if perguntaAddEspeciais == "nao" and perguntaAddMaiusculas == "nao" and perguntaAddMinusculas == "nao" and perguntaAddNumeros == "nao":
    print("impossivel gerar senha sem nenhuma especificação")
else :
    print("sua senha é: ",senha)