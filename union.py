def split(string, delimiters):
    result = []
    current = ""
    i = 0

    while i < len(string):
        match = False
        for delimiter in delimiters:
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


def union(stringValue):
    return [delimiter.strip() for delimiter in stringValue.split("|") if delimiter.strip()]


string = "banana maçã"
delimiters = union("na | ma")
print(delimiters)
print(split(string, delimiters))
