masa = int(input("podaj swoja mase w kg "))
wzrost_w_centymetrach = int(input("podaj wzrost w cm "))

wzrost_w_metrach = wzrost_w_centymetrach / 100

bmi = masa / (wzrost_w_metrach**2)

if bmi < 18.50:
  print("masz niedowage")

if bmi >= 18.50 and bmi < 25:
  print("optimum")

if bmi >= 25 and bmi < 30:
  print("masz nadwaga")
  
if bmi > 30:
  print("otylosc")

print(bmi)
