def wave(string):
    strings = []

    for idx, char in enumerate(string):
        # print(idx, char)
        if char == ' ':
            # print('skip')
            pass
        else:
            l_string = list(string)
            # print(l_string)
            l_string[idx] = l_string[idx].upper()

            l_string = ''.join(l_string)

            strings.append(l_string)
    return(strings)

print(wave(' the dog '))