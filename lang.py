print("This program will work for only 9 language. Which are ->\n English, Danish, Dutch, French, German, Italian, Norway, Spanish and Swiss\n")

fname = input("Insert a .txt format file: ")
words = list()

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0

if len(fname) < 1:
    fname = "data_file.txt"
fopen = open(fname)

for line in fopen:
    a = line.replace(",", "")
    b = a.replace("!", "")
    data = b.replace(".", "")
    #print(data)
    old_data = data.strip()
    new_data = old_data.split()
    for word_list in new_data:
        if word_list not in words:
            words.append(word_list)
#print(words)

for word in words:
    print("The word '", word, "' belongs to ->")
    with open("english.txt") as en_f:
        en_lst = [line.rstrip('\n') for line in en_f]
        for fs in en_lst:
            if word == fs:
                print("English")
                count1 = count1 + 1

    with open("danish.txt") as dn_f:
        dn_lst = [line.rstrip('\n') for line in dn_f]
        for se in dn_lst:
            if word == se:
                print("Danish")
                count2 = count2 + 1


    with open("dutch.txt") as du_f:
        du_lst = [line.rstrip('\n') for line in du_f]
        for th in du_lst:
            if word == th:
                print("Dutch")
                count3 = count3 + 1

    with open("french.txt") as fr_f:
        fr_lst = [line.rstrip('\n') for line in fr_f]
        for fo in fr_lst:
            if word == fo:
                print("French")
                count4 = count4 + 1

    with open("german.txt") as ge_f:
        ge_lst = [line.rstrip('\n') for line in ge_f]
        for fi in ge_lst:
            if word == fi:
                print("German")
                count5 = count5 + 1

    with open("italian.txt") as it_f:
        it_lst = [line.rstrip('\n') for line in it_f]
        for si in it_lst:
            if word == si:
                print("Italian")
                count6 = count6 + 1

    with open("norway.txt") as no_f:
        no_lst = [line.rstrip('\n') for line in no_f]
        for sev in dn_lst:
            if word == sev:
                print("Norway")
                count7 = count7 + 1

    with open("spanish.txt") as sp_f:
        sp_lst = [line.rstrip('\n') for line in sp_f]
        for ei in dn_lst:
            if word == ei:
                print("Spanish")
                count8 = count8 + 1

    with open("swiss.txt") as sw_f:
        sw_lst = [line.rstrip('\n') for line in sw_f]
        for ni in sw_lst:
            if word == ni:
                print("Swiss")
                count9 = count9 + 1

    print("...................NEXT WORD........................\n")

var = {count1 : "English", count2 : "Danish", count3 : "Dutch", count4 : "French", count5 : "German", count6 : "Italian", count7 : "Norway", count8 : "Spanish", count9 : "Swiss"}
#print(count1, count2, count3, count4, count5, count6, count7, count8, count9)
doc_type = var.get(max(var))

print("This document is mostly '", doc_type , "' Language")