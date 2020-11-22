def single_char(regex, char):
    return regex in ('', '.', char)


def equal_length(regex, string):
    if not regex:
        return True
    elif not string:
        return regex[0] == "$"
    elif regex[0] == '\\':
        if regex[1] != string[0]:
            return False
        return equal_length(regex[2:], string[1:])
    else:
        if len(regex) >= 2:
            if regex[1] in ('?', '*', '+') and regex[0] != '\\':
                if regex[1] == '?':
                    return equal_length(regex[2:], string) or \
                        equal_length(regex[0] + regex[2:], string)
                elif regex[1] == '*':
                    return equal_length(regex[2:], string) or \
                        equal_length(regex, string[1:])
                elif regex[1] == '+':
                    return equal_length(regex[0] + regex[2:], string) or \
                        equal_length(regex, string[1:])
        if single_char(regex[0], string[0]):
            return equal_length(regex[1:], string[1:])
    return False


def diff_length(regex, string):
    if not string:
        return False
    elif equal_length(regex, string):
        return True
    else:
        return diff_length(regex, string[1:])


def edges(regex, string):
    if '^' in regex:
        return equal_length(regex[1:], string)
    elif '$' in regex:
        return diff_length(regex, string)
    else:
        if equal_length(regex, string):
            return True
        else:
            return diff_length(regex, string[1:])


print(edges(*(input().split('|'))))
