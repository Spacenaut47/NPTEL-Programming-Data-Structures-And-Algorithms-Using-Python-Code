def primepartition(m):
    primelist = []
    if m < 0:
        return False
    else:
        for i in range(2, m + 1):
            for p in range(2, i):
                if (i % p) == 0:
                    break
            else:
                primelist.append(i)

        for x in primelist:
            y = m - x
            if y in primelist:
                return True
        return False


def matched(s):
    brackets_counter = 0
    i = 0
    while brackets_counter >= 0 and i < len(s):
        if s[i] == '(':
            brackets_counter += 1
        elif s[i] == ')':
            brackets_counter -= 1
        i += 1
    if brackets_counter == 0:
        return True
    else:
        return False


def rotatelist(l, k):
    output_list = []
    k = k % len(l)

    for item in range(k, len(l)):
        output_list.append(l[item])

    for item in range(0, k):
        output_list.append(l[item])

    return output_list
