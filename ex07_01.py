fh = open('mbox-short.txt')

for lx in fh :
    #. rstrio은 개행문자(빈열)을 지워주는 역할
    ly = lx.rstrip()
    print(ly.upper())