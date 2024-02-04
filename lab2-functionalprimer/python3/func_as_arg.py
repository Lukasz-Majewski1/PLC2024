def listFunc(a, b):
    return [i for i in range(a, b + 1)]

def applicatorFunc(inpFunc, a, b, s):
    if s =='s':
        return sum(inpFunc(a, b))
    else:
        return sum(inpFunc(a, b)) / (b - a + 1)

print(applicatorFunc(listFunc, 1, 5, 'a'))