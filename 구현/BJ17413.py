text = input()
result = ""
if "<" in text:
    cnt = 1
    text = text.split('>')
    for mini_text in text:
        close = mini_text.find('<')
        if close == 0:
            result += mini_text+">"
        elif close == -1:
            result += mini_text[::-1]+" "
        else:
            first = mini_text[:close]
            first = first.split()
            for tmp in first:
                result += tmp[::-1]+" "
            result = result[:-1]
            second = mini_text[close:]
            result += (second+">")
    print(result[:-1])
else:
    text = text.split()
    for mini_text in text:
        result += mini_text[::-1]+' '
    print(result[:-1])
