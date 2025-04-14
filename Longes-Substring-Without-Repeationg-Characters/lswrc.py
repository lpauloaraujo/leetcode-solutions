def longest_substring(string):
    longest_substring = ""
    actual_substring = ""
    for index, char in enumerate(string):
        if index == 0:
            actual_substring += char
        else:
            if char not in actual_substring:
                actual_substring += char
            else:
                longest_substring = max(longest_substring, actual_substring, key=len)
                actual_substring = char
    return longest_substring

def main():
    string = input("String: ")
    resultado = longest_substring(string)
    print(f"Longest substring without repeating: {resultado}\nLength: {len(resultado)}")

if __name__ == "__main__":
    main()
    