n = int(input())
texts = []
for i in range(n):
    text = input()
    texts.append(text)
for text in texts:
    if text == "".join(reversed(text)):
        print(0)
    else:
        for j in range(len(text)//2):
            if text[j] == text[len(text)-j-1]:
                continue
            else:
                temp1 = text[:j] + text[j+1:]
                temp2 = text[:len(text) - j-1] + text[len(text) - j:]
                if temp1 == "".join(reversed(temp1)) or temp2 == "".join(reversed(temp2)):
                    print(1)
                    break
                else:
                    print(2)
                    break
