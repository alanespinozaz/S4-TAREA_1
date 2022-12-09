# Ejercicio 1 
texto ="afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood"
texto_invertido = ''.join(reversed(texto))
print(texto_invertido)
print("")

def palindromo(cadena):
    pos_left = 0
    pos_right= len(cadena) - 1
    
    while pos_right >= pos_left:
        if not cadena[pos_left] == cadena[pos_right]:
            return False
        
        pos_left += 1
        pos_right -= 1
        
    return True

print(palindromo("afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood"))

#Ejercicio 2
print()
print()
x=0
y=1
z=0
while True:
    n = int(input("digite un numero: "))
    if n>1:
        break

print("1", end=" ")
for i in range(0,n):
    z=x+y
    print(f" Numero de la serie: {z}" , end=" ".format(z))
    x=y
    y=z
print(" ")

def divisor(numero):
    resul = [divi for divi in range(1, numero +1 ) if numero % divi ==0]
    return  resul

print(f"El divisor de {z} es :", (divisor(z)))


