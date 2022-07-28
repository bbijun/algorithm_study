text = input()
result = ""
flag = False
tmp_text = ""
for char in text:
    if char == " ":
        if flag == True:
            result += (tmp_text+char)
            tmp_text = ""
        else:
            result += (tmp_text[::-1] + char)
            tmp_text = ""
    elif char == "<":
        result += tmp_text[::-1]
        tmp_text="<"
        flag = True

    elif char == ">":
        result += (tmp_text+">")
        tmp_text = ""
        flag = False
    else:
        tmp_text += char
result += tmp_text[::-1]
print(result)