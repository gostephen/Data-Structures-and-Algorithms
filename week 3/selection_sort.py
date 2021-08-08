def selection_sort(l: list):
    for i in range(0, len(l) - 1):
        lowest = l[i]
        for j in range(i + 1, len(l)):
            store = l[i]
            if l[j] <= lowest:
                lowest = l[j]
                ind = j
        l[i] = lowest
        l[ind] = store
    return l
