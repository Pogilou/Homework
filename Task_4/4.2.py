import string

def palindrome_check (line):
    string_with_letters_only = []
    line = line.lower()
    for i in line:
        if i in string.ascii_lowercase:
            string_with_letters_only ="".join(i)
    line = string_with_letters_only

    len_line=(len(line))//2

    for i in range(len_line):
        if line[i] != line [-1-i]:
            return (print("not palindrome"))

    return (print("palindrome"))

palindrome_check("Don't no/ * -* *-*d")