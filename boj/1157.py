string = input()
alphabets = dict()
for char in string:
    if 65 <= ord(char) <= 90: 
        if alphabets.get(char):
            alphabets[char] += 1
        else:
            alphabets[char] = 1
    else:
        if alphabets.get(chr(ord(char)-32)):
            alphabets[chr(ord(char)-32)] += 1
        else:
            alphabets[chr(ord(char)-32)] = 1

Max = max(alphabets.values())
answer = ''
for key, value in alphabets.items():
    if value == Max:
        answer += key

print(answer if len(answer)==1 else '?')