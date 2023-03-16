def main():
    str = changevowels(input())
    print (str)               



def changevowels(string):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for vowel in vowels:
        if vowel in string:
            string = string.replace(vowel, "")
    return string

main()