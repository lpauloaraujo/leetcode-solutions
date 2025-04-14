def is_palindromic(substring):
    if substring == substring[::-1]:
        return True
    else:
        return False

def longest_substring(string):
    lps = ""
    for index in range(len(string)):
        current_lps = ""
        for char in string[index:]:
            current_lps += char
            if is_palindromic(current_lps) and len(current_lps) > len(lps):
                lps = current_lps
    return lps

def main():
    string = input("String:")
    lps = longest_substring(string)
    print(f"Longest Palindromic Substring in {string}: {lps}")

if __name__ == "__main__":
    main()
