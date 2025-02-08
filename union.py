def split(string, delimiters):
    result = []
    current = ""
    i = 0

    while i < len(string):
        match = False
        for delimiter in delimiters:
            delim_length = len(delimiter)
            j = 0


            if delimiter == "\\d":
                if string[i].isdigit():
                    if current:
                        result.append(current)
                    result.append("")
                    current = ""
                    i += 1
                    match = True
                    break
            else:
                while j < delim_length and i + j < len(string) and string[i + j] == delimiter[j]:
                    j += 1

                if j == delim_length:
                    if current:
                        result.append(current)
                    result.append("") 
                    current = ""
                    i += delim_length
                    match = True
                    break
        
        if not match:
            current += string[i]
            i += 1

    if current:
        result.append(current)

    return result


def union(stringValue):
    delimiters = []
    current = ""
    i = 0

    while i < len(stringValue):
        if stringValue[i] == "|":
            if current:
                delimiters.append(current)
            current = ""
        else:
            current += stringValue[i]
        i += 1
    
    if current:
        delimiters.append(current)

    clean_delimiters = []
    for delim in delimiters:
        start = 0
        end = len(delim) - 1

        while start < len(delim) and delim[start] == " ":
            start += 1
        
        while end >= 0 and delim[end] == " ":
            end -= 1

        clean_delimiters.append(delim[start:end + 1])

    return clean_delimiters


string = "banana123 maçã456"
delimiters = union("na | ma | \\d")
print(delimiters)
print(split(string, delimiters))