import random

def get_sample(lista_numeros, n):
    if n > len(lista_numeros):
        return lista_numeros, []
    result = random.sample(lista_numeros, n)
    
    for item in result:
        lista_numeros.remove(item)
    
    return result, lista_numeros

def main():
    num_pessoas = int(input("Digite o número de pessoas: "))
    num_questoes = int(input("Digite o número de questões: "))
    
    lista_numeros = [i for i in range(1, num_questoes + 1)]
    min_questoes = num_questoes // num_pessoas
    questoes_por_pessoa = [min_questoes] * num_pessoas
    questoes_restantes = num_questoes - sum(questoes_por_pessoa)

    i = 0
    while questoes_restantes > 0:
        questoes_por_pessoa[i] += 1
        questoes_restantes -= 1
        i = (i + 1) % num_pessoas
        
    for num_questoes_pessoa in questoes_por_pessoa:
        sample, lista_numeros = get_sample(lista_numeros, num_questoes_pessoa)
        print(sample)

main()