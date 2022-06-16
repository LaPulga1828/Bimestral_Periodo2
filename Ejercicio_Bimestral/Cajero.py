print("-----------------------------")
print("-------Canjear Cheques-------")
print("-----------------------------")

#input
V_C=int(input("ingrese el valor de su cheque: "))

#Procesing
T_D=0
N_Trans=0
B_10000=0
B_2000=0
M_100=0
C_B_10000=0
C_B_2000=0
C_M_100=0

while V_C!=0:
    if V_C%100==0:
        V_C//10000
        B_10000 = V_C//10000
        B_2000 = (V_C%10000)//2000
        M_100 = ((V_C%10000)%2000)//100

        print("el cajero entrega:")
        print(B_10000,"billetes de 10000")
        print(B_2000,"billetes de 2000")
        print(M_100,"monedas de 100")

        C_B_10000= C_B_10000+B_10000
        C_B_2000= C_B_2000 + B_2000
        C_M_100= C_M_100 + M_100
        T_D=T_D+V_C
        N_Trans=N_Trans+1
    else:
        print("El valor no es aceptado")
    
    V_C=int(input("ingrese el valor de su cheque: "))
    
#output

print("Hoy se entregaron: ") 
print("Billetes de 10000: ",C_B_10000)
print("Billetes de 2000: ",C_B_2000)
print("Monedas de 100: ",C_M_100)
print("En total hoy se entregó: ",T_D)
print("En un total de ", N_Trans," transacciones")

print("Fin")