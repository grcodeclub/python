# Ο κώδικας εκτελεί ένα HTTP GET αίτημα στην ιστοσελίδα "http://www.grcodeclub.gr" 
# και στη συνέχεια εκτυπώνει το περιεχόμενο της σελίδας (σε μορφή HTML) μέσω της r.text.

import requests  # Εισάγουμε τη βιβλιοθήκη requests για να κάνουμε HTTP αιτήματα

# Στέλνουμε ένα GET αίτημα στην ιστοσελίδα
r = requests.get('http://www.grcodeclub.gr')

# Εκτυπώνουμε το περιεχόμενο της σελίδας (σε μορφή HTML)
print(r.text)
