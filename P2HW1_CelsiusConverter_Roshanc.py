# C and F calculator
# 09/12/2018
# CTI-110 P2HW1 - Celsius Fahrenheit Converter 
# Roshan Chandrasekara
#row to enter C value
c=float(input('Enter Temperature in celsius: '))
#f conversion formula
f=c*9/5+32.0
#conversion

print('conversion in Fahrenheit: ',f)
#row to enter F value
f=float(input('Enter Temperature in Fahrenheit: '))
# c conversion formula
c=(f-32)*(5/9)
#conversion

print('Conversion in Celsius: ',format(c,'.2f'))

print('Thank you for using the program ! python programming by Roshan Chan')

input() 
