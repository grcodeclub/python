# Ο κώδικας χειρίζεται σφάλματα που μπορεί να συμβούν κατά την αποστολή ενός HTTP αιτήματος με την requests

import requests  # Εισάγουμε τη βιβλιοθήκη requests για να κάνουμε HTTP αιτήματα

try:
    # Στέλνουμε το αίτημα GET στην URL
    response = requests.get('https://api.github.com/invalid-url')
    
    # Αν η απόκριση περιέχει σφάλμα (π.χ. 404), προκαλείται εξαίρεση
    response.raise_for_status()  # Θα προκαλέσει εξαίρεση για HTTP σφάλματα
except requests.exceptions.HTTPError as err:
    # Αν προκύψει σφάλμα τύπου HTTP (π.χ. 404 ή 500), το διαχειριζόμαστε εδώ
    print(f'HTTP error occurred: {err}')
except Exception as err:
    # Για οποιοδήποτε άλλο είδος σφάλματος (π.χ. πρόβλημα σύνδεσης), το διαχειριζόμαστε εδώ
    print(f'Other error occurred: {err}')
else:
    # Αν δεν προκύψουν σφάλματα, εκτυπώνουμε την επιτυχία και τα δεδομένα της απόκρισης
    print('Success!')
    print(response.json())  # Εκτυπώνουμε τα δεδομένα της απόκρισης σε μορφή JSON
