word = input("Insert a word: ")

with open("english.txt") as en_f:
    en_lst = [line.rstrip('\n') for line in en_f]
    for fs in en_lst:
        if word == fs:
            print("English")

with open("danish.txt") as dn_f:
    dn_lst = [line.rstrip('\n') for line in dn_f]
    for se in dn_lst:
        if word == se:
            print("Danish")

with open("dutch.txt") as du_f:
    du_lst = [line.rstrip('\n') for line in du_f]
    for th in du_lst:
        if word == th:
            print("Dutch")

with open("french.txt") as fr_f:
    fr_lst = [line.rstrip('\n') for line in fr_f]
    for fo in fr_lst:
        if word == fo:
            print("French")

with open("german.txt") as ge_f:
    ge_lst = [line.rstrip('\n') for line in ge_f]
    for fi in ge_lst:
        if word == fi:
            print("German")

with open("italian.txt") as it_f:
    it_lst = [line.rstrip('\n') for line in it_f]
    for si in it_lst:
        if word == si:
            print("Italian")

with open("norway.txt") as no_f:
    no_lst = [line.rstrip('\n') for line in no_f]
    for sev in dn_lst:
        if word == sev:
            print("Norway")

with open("spanish.txt") as sp_f:
    sp_lst = [line.rstrip('\n') for line in sp_f]
    for ei in dn_lst:
        if word == ei:
            print("Spanish")

with open("swiss.txt") as sw_f:
    sw_lst = [line.rstrip('\n') for line in sw_f]
    for ni in sw_lst:
        if word == ni:
            print("Swiss")