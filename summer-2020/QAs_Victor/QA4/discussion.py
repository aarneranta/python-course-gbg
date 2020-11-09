def discussion_2():
    #a
    print(s2.upper()[:2])
    #b
    print(s1+s2)
    #c
    print(((s1.capitalize()+" "+s2.capitalize()).ljust(10)*3).rstrip())
    #d
    print(s1)
    #e
    print(s1.split('a'))
    #f
    print("".join(s1.split('a')))
    #f alt
    print(s1[:2] + s1[3:])
