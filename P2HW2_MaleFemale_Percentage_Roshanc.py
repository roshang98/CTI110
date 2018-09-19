# Male Female Percentage calculation
# 09/12/2018
# CTI-110 P2HW2 - Male Female Percentage
# Roshan Chandrasekara
#enter no of males in the class
male=int(input('Enter no of male in the class: '))

#enter no of females in the class
female=int(input('Enter no of female in the class: '))

#calculate male,female percentage

maleper = float((male/(male+female))*100)
femaleper =float((female/(male+female))*100)

#display male,female percentage

print('Male Percentage: ',format(maleper,'.1f'))
print('Female Percentage: ',format(femaleper,'.1f'))
print('Thank You for using the program')
input()
