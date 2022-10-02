
def dominoPiling():
    M, N = map(int, input("Please enter two integers M and N — board sizes in squares (1≤M≤N≤16) with space between them: ").split())
    mult=M*N
    domino=mult//2
    print("The maximal number of dominoes, which can be placed are {}".format(domino))

dominoPiling()
