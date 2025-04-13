def receber_entrada():
    tamanho_l1 = int(input("Tamanho da lista 1:"))
    lista1 = [None] * tamanho_l1
    for num in range(tamanho_l1):
        lista1[num] = int(input(f"Número na {num + 1}° da lista 1:"))
    tamanho_l2 = int(input("Tamanho da lista 2:"))
    lista2 = [None] * tamanho_l2
    for num in range(tamanho_l2):
        lista2[num] = int(input(f"Número na {num + 1}° da lista 2:"))
    return lista1, lista2

def lista_para_numero(lista):
    numero_ao_contrario = "".join(map(str, lista))
    return int(numero_ao_contrario[::-1])

def addtwonumbers(lista1, lista2):
    numero1 = lista_para_numero(lista1)
    numero2 = lista_para_numero(lista2)
    soma = numero1 + numero2
    return [int(digito) for digito in str(soma)][::-1]

def main():
    lista1, lista2 = receber_entrada()
    resultado = addtwonumbers(lista1, lista2)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
