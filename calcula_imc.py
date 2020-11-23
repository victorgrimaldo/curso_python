try:

    estatura = float(input("Ingresa tu estatura en m: "))
    peso = float(input("Ingresa tu peso en kg: "))

    imc = peso / (estatura**2)

    if imc < 18.50:
        print("Tu imc es: " + str(round(imc,2)) + ", estás por debajo de tu peso")
    else:
        if 18.51 <= imc <= 24.99:
            print("Tu imc es: " + str(round(imc,2)) + ", estás en tu peso ideal")
        else: 
            if 25.00 <= imc <=  29.99:
                print("Tu imc es: " + str(round(imc,2)) + ", estás con sobrepeso")
            else:
                print("Tu imc es: " + str(round(imc,2)) + ", estás con obesidad")
except:
    print("No ingresaste un número")
