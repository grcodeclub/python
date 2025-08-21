# Εκτελεί ένα αίτημα GET σε μια URL που απαιτεί αυθεντικοποίηση (HTTP Basic Authentication). 
# Η αυθεντικοποίηση γίνεται με το χρήστη (user) και τον κωδικό πρόσβασης (pass).

import requests  # Εισάγουμε τη βιβλιοθήκη requests για να κάνουμε HTTP αιτήματα
from requests.auth import HTTPBasicAuth  # Εισάγουμε την κλάση HTTPBasicAuth για αυθεντικοποίηση

# Ορίζουμε τη διεύθυνση URL στην οποία θέλουμε να στείλουμε το αίτημα
url = 'https://grcodeclub.gr/basic-auth/user/pass'

# Στέλνουμε το αίτημα GET στην URL με βασική αυθεντικοποίηση χρησιμοποιώντας τα στοιχεία του χρήστη και του κωδικού
response = requests.get(url, auth=HTTPBasicAuth('user', 'pass'))

# Εκτυπώνουμε τον κωδικό κατάστασης του αιτήματος (π.χ. 200 για επιτυχία)
print(response.status_code)

# Αν η απάντηση είναι σε μορφή JSON, την εκτυπώνουμε ως Python dict
print(response.json())
