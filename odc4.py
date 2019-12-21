masa = input("podaj swoja mase w kg ")
masa = int(masa)

wzrost_w_centymetrach = input("podaj wzrost w cm ")
wzrost_w_centymetrach = int(wzrost_w_centymetrach)

wzrost_w_metrach = wzrost_w_centymetrach / 100

bmi = masa / (wzrost**2)

print(bmi)
