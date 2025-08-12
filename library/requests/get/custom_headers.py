#  Στέλνουμε ένα αίτημα HTTP GET στην ιστοσελίδα https://grcodeclub.gr/headers με προσαρμοσμένα headers, 
#  Συγκεκριμένα το User-Agent. Το User-Agent χρησιμοποιείται για να δηλώσει ποια εφαρμογή (ή πρόγραμμα περιήγησης) κάνει το αίτημα.
import requests  # Εισάγουμε τη βιβλιοθήκη requests για να κάνουμε HTTP αιτήματα

# Ορίζουμε τη διεύθυνση URL στην οποία θέλουμε να στείλουμε το αίτημα
url = 'https://grcodeclub.gr/headers'

# Ορίζουμε τα headers που θα στείλουμε μαζί με το αίτημα (για παράδειγμα, το User-Agent)
headers = {'User-Agent': 'my-app'}

# Στέλνουμε το αίτημα GET στην καθορισμένη URL με τα προσαρμοσμένα headers
response = requests.get(url, headers=headers)

# Εκτυπώνουμε τον κωδικό κατάστασης του αιτήματος (π.χ. 200 για επιτυχία)
print(response.status_code)

# Αν η απάντηση είναι σε μορφή JSON, την εκτυπώνουμε ως Python dict
print(response.json())
