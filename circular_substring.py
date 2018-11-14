from TdP_collections.text.find_kmp import find_kmp


def circular_substring(p, t):
    m = len(p)
    t += t[0:m - 1]
    return True if find_kmp(t, p) >= 0 else False


print(circular_substring("ingco", "commostring"))
