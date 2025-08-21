# Ο κώδικας δείχνει πώς να στείλεις δεδομένα σε κομμάτια (chunked) με τη χρήση του chunked transfer encoding. 
# Χρησιμοποιώντας τη βιβλιοθήκη requests, δημιουργεί μια Session που επιτρέπει την αποστολή δεδομένων σε κομμάτια μέσω του iter() και του HTTPAdapter.


import requests  # Εισάγουμε τη βιβλιοθήκη requests για να κάνουμε HTTP αιτήματα
from requests.adapters import HTTPAdapter  # Εισάγουμε το HTTPAdapter για να ρυθμίσουμε την προσαρμογή αιτημάτων
from requests.packages.urllib3.util.retry import Retry  # Εισάγουμε την κλάση Retry για επαναλήψεις σε αποτυχημένα αιτήματα

# Δημιουργία Session για να στείλουμε το αίτημα με chunked transfer encoding
session = requests.Session()

# Ορίζουμε μια στρατηγική επανεκκίνησης (retry strategy) για επαναλαμβανόμενα αιτήματα
adapter = HTTPAdapter(max_retries=Retry(total=3, backoff_factor=0.1))

# Συνδέουμε τον adapter με τα πρωτόκολλα HTTP και HTTPS
session.mount('http://', adapter)
session.mount('https://', adapter)

# Στέλνουμε το POST αίτημα με chunked δεδομένα
# Χρησιμοποιούμε την iter() για να στείλουμε τα δεδομένα σε κομμάτια (chunk1, chunk2)
response = session.post('https://httpbin.org/post', data=iter(['chunk1', 'chunk2']))

# Εκτυπώνουμε την απόκριση από το διακομιστή
print(response.status_code)  # Εκτυπώνουμε τον κωδικό κατάστασης
print(response.text)  # Εκτυπώνουμε το περιεχόμενο της απόκρισης
