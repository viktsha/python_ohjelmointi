senttimetrit = int(input("Kalastaja, mikä on kuhan pituus?"))

if senttimetrit >= 37:
   print("Onnittelut!")

else:
    print("Laske kuha takaisin jarveen.")
    puuttuva = ( 37 - senttimetrit )
    print("Alimmasta sallitusta pyyntimitasta puuttuu", puuttuva)

