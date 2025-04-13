def receber_entrada():
    tamanho_array = int(input("Tamanho do array:"))
    array = [None] * tamanho_array
    for num in range(tamanho_array):
        array[num] = int(input(f"Número na {num + 1}° do array:"))
    target = int(input("Target:"))
    return array, target

def twosum(array, target):
    for indice_x, numero_x in enumerate(array):
        x = numero_x
        for indice_y, numero_y in enumerate(array):
            if indice_y == indice_x:
                continue
            y = numero_y
            if x + y == target:
                return [indice_x, indice_y]
    return "Nenhum par encontrado"

def main():
    array, target = receber_entrada()
    resultado = twosum(array, target)
    print(f"Resultado: {resultado}")    

if __name__ == "__main__":
    main()
