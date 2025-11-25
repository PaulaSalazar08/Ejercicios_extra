#Este programa sirve para devolver el número más grande y el promedio de 10
#números
def programa_1():
    max_num=input("Introduce un número: ")
    sum_nums=max_num
    for i in range(9):
        num=input("Introduce otro número ")
        sum_nums=sum_nums+num
        if num>max_num:
            max_num=num
    print("The largest number is: "+str(max_num))
    print("The average is: "+str(float(sum_nums)/10))

programa_1()
