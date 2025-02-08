def split(string, delimiters):
    result = []
    current = ""
    i = 0

    while i < len(string):
        match = False
        for delimiter in delimiters:
            print(string[i:i + (len(delimiter))], delimiter)
            print(string[i:i + len(delimiter)] == delimiter)
            if string[i:i + len(delimiter)] == delimiter:
                result.append(current)
                current = ""
                i += len(delimiter) - 1
                match = True
                break
        if not match:
            current += string[i]
        i += 1

    result.append(current)
    return result


def untion(stringValue):
    caracter_especial = "|"
    delimeters = []
    pos_caracter_especial = 0
    if stringValue:
      for i in range(0, len(stringValue)):
        if stringValue[i] == caracter_especial:
            delimeters.append(stringValue[pos_caracter_especial:i])
            pos_caracter_especial = i+1
    return delimeters


strinbSomeValue = "The quick brown fox jumps over the lazy dog. However, the fox was surprised to find a umdoistrêsquatrohidden treasure in the middle of the forest. The treasure was guarded by a fierce dragon, but the fox was clever and managed to outsmart the dragon. In the end, the fox shared the treasure with its friends, and they all lived happily ever after."

delimeters = untion("um|dois|três|quatro|")
print(split(strinbSomeValue, delimeters))