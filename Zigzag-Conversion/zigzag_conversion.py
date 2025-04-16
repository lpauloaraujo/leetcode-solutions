def turn_into_zigzag(string, rows):
    matrix = [[] for _ in range(rows)]
    row = 0
    column = 0
    char_index = 0
    while char_index < len(string):
        if row == rows:
            row -= 1
            while column < rows - 2 and char_index < len(string):
                column += 1
                row -= 1
                for line in matrix:
                    if line == matrix[row]:
                        if char_index >= len(string):
                            break
                        line.append(f"{string[char_index]}")
                        char_index += 1
                    else:
                        line.append(" ")
            row = 0
            column = 0
        else:
            matrix[row].append(f"{string[char_index]}")
            char_index += 1
            row += 1
    return matrix

def string_zigzag(matrix):
    printed_zigzag = ""
    read_zigzag = ""
    for row in matrix:
        for index, column in enumerate(row):
            if column != " ":
                read_zigzag += column
            if index == len(row) - 1:
                printed_zigzag += f" {column} \n"
            else:
                printed_zigzag += f" {column} "
    return printed_zigzag, read_zigzag

def main():
    string = input("String: ")
    rows = int(input("Number of rows: "))
    zigzag = turn_into_zigzag(string, rows)
    str_zigzag, output = string_zigzag(zigzag)
    print(f"Zigzag:\n{str_zigzag}")
    print(f"Output: {output}")

if __name__ == "__main__":
    main()
