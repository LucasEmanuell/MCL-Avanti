# 1. Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.
def filtrar_impares(lista):
    
    return [num for num in lista if num % 2 != 0]


def main():
    
    entrada = input("Digite uma lista de números separados por espaço: ")
    
    #Converte a entrada em uma lista de inteiros
    numeros = list(map(int, entrada.split()))
    
    impares = filtrar_impares(numeros)

    print("Os números ímpares são:", impares)

#Executa a função principal
if __name__ == "__main__":
    main()

# 2. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.
def eh_primo(num):
    #Verifica se é primo
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filtrar_primos(lista):
    #Filtra os números primos
    return [num for num in lista if eh_primo(num)]

#Função principal
def main():
    #Solicita ao usuário para inserir os números
    entrada = input("Digite uma lista de números separados por espaço: ")
    
    #Converte o input em uma lista de inteiros
    numeros = list(map(int, entrada.split()))
    
    #Filtra os números primos
    primos = filtrar_primos(numeros)
    
    #Exibe a lista de números primos
    print("Os números primos são:", primos)

#Executa a função principal
if __name__ == "__main__":
    main()
# 3. Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.
def diferenca_simetrica(lista1, lista2):
    #Converte as listas em conjuntos e encontra a diferença simétrica
    return list(set(lista1).symmetric_difference(set(lista2)))

def main():
    #Solicita ao usuário para inserir os números da primeira lista, separados por espaço
    entrada1 = input("Digite os elementos da primeira lista separados por espaço: ")
    
    #Solicita ao usuário para inserir os números da segunda lista, separados por espaço
    entrada2 = input("Digite os elementos da segunda lista separados por espaço: ")
    
    #Converte as entradas em listas de inteiros
    lista1 = list(map(int, entrada1.split()))
    lista2 = list(map(int, entrada2.split()))
    
    #Calcula a diferença simétrica
    resultado = diferenca_simetrica(lista1, lista2)
    
    #Exibe a lista principal
    print("Elementos presentes em apenas uma das listas:", resultado)

#Executa a função principal
if __name__ == "__main__":
    main()

# 4. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.
def segundo_maior(lista):
    #Remove duplicatas e ordena a lista em ordem decrescente
    lista_unica = list(set(lista))
    lista_unica.sort(reverse=True)
    
    #Verifica se há pelo menos dois elementos na lista
    if len(lista_unica) < 2:
        raise ValueError("A lista deve conter pelo menos dois valores únicos.")
    
    #Retorna o segundo maior valor
    return lista_unica[1]

#Função principal para testar
def main():
    #Solicita ao usuário para inserir os números da lista, separados por espaço
    entrada = input("Digite uma lista de números inteiros separados por espaço: ")
    
    #Converte a entrada em uma lista de inteiros
    lista = [int(num) for num in entrada.split()]
    
    try:
        #Encontra e exibe o segundo maior valor
        resultado = segundo_maior(lista)
        print("O segundo maior valor é:", resultado)
    except ValueError as e:
        print(e)

#Executa a função principal
if __name__ == "__main__":
    main()

# 5. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.
def ordenar_por_nome(lista):
    #Ordena a lista de tuplas pelo nome (primeiro elemento da tupla)
    return sorted(lista, key=lambda x: x[0])

#Função principal para testar
def main():
    #Exemplo de lista de tuplas com nomes e idades
    pessoas = [("Ana", 23), ("João", 35), ("Beatriz", 29), ("Carlos", 19)]
    
    #Ordena a lista por nome
    lista_ordenada = ordenar_por_nome(pessoas)
    
    #Exibe a lista ordenada
    print("Lista ordenada por nome:")
    for pessoa in lista_ordenada:
        print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]}")

if __name__ == "__main__":
    main()

# 6. Observe os espaços sublinhados e complete o código.
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), layout="constrained")
for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5), transform=axs[row, col].transAxes, ha='center', va='center', fontsize=18, color='darkgrey')
fig.suptitle('plt.subplots()')

# 7. Observe os espaços sublinhados e complete o código.
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)