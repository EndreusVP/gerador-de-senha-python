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
perguntaAddMinuscuças = input("deseja letras minusculas na sua senha?(SIM/NÃO)")
perguntaAddEspeciais = input("deseja caracter especial na sua senha?(SIM/NÃO)")
perguntaAddNumeros = input("deseja numeros na sua senha?(SIM/NÃO)")
perguntaQuantidadeCaracteres = int(input("didgite quantos caracteres tera sua senha?(Apenas numeros)"))

#definindo numero de caracteres
caracter = perguntaQuantidadeCaracteres

#ajustando especificações da senha 
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
index = 0

while index <= caracter:
    if perguntaAddMaiusculas == "sim":
        senha += resAddEspeciais()
    
    if perguntaAddMinuscuças == "sim":
        senha += resAddMinusculas()
    
    if perguntaAddEspeciais == "sim":
        senha += resAddEspeciais()

    if perguntaAddNumeros == "sim":
        senha += resAddNumeros()

print(senha)