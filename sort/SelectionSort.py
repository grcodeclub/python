array =  ["Δημήτρης", "Ευγενία", "Ναταλία", "Ρένια", "Αλέξανδρος"]
 # Ένα παράδειγμα ενός πίνακα αριθμών
# array = [7, 2, 5, 1, 9, 3]
print("Πίνακας:", array)

# Εφαρμογή του αλγορίθμου ταξινόμησης με εισαγωγή
n = len(array)
for i in range(n-1): # range(0, N–1, 1)
    for j in range(n-1,i,-1): # μέχρι και i–1
        if array[j] < array[j-1] :
            array[j] , array[j-1] = array[j-1] , array[j]
            print("i:",i,"j:",j,"πίνακας:",array)

print("Ο ταξινομημένος πίνακας:", array)
