#Este programa sirve para determinar el número más alto y la media de los
#números que ha puesto la persona en el programa
def programa_1():
    max_num=input("Introduce un número: ")
    sum_nums=max_num
    i=1
    while(i<=10):
        num=input("Introduce otro número ")
        sum_nums=sum_nums+num
        if num>max_num:
            max_num=num
        i=i+1
    print("The largest number is: "+str(max_num))
    print("The average is: "+str(float(sum_nums)/10))
programa_1()
