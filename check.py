import sfml as sf

def check(tab):
    i = 0
    for line in tab:
        if len(tab[0]) != len(tab[i]):
            return(1)
        i = i + 1
    return(0)