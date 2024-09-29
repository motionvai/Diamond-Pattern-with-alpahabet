from string import ascii_lowercase as al



def print_rangoli(num):
    list_char=list(al[i] for i in range(num))
    width= 4*num -3
     # Handle the special case when num is 1
    if num == 1:
        print('a')
        return
    #for i in range (num):
        #list_char.append(al[i] )
        #print(list_char)
    for j in range(num-1,-1,-1):
        ulhd="-".join(list_char[j:(num)]).ljust(2*num-1,"-")
        #print(lhd)
        urhd="-".join(list_char[num:j:-1]).rjust(2*num-3,"-")
        #print(rhd)
        up=(urhd+("-"+ulhd if ulhd else "")).center(width, "-")
        print(up)
    for m in range(1,num):
        dlhd="-".join(list_char[m:(num)]).ljust(2*num-1,"-")
        drhd="-".join(list_char[num:m:-1]).rjust(2*num-3,"-")
        down=(drhd+("-"+dlhd if ulhd else "")).center(width, "-")
        print(down)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

"""num=int(input())
abc(num)
#print(list_char)"""