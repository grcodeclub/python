# Ο κώδικας που παραθέτεις στέλνει ένα αίτημα POST με δεδομένα σε μορφή JSON στην URL https://httpbin.org/post. 
# Χρησιμοποιεί την κεφαλίδα Content-Type: application/json για να δηλώσει ότι τα δεδομένα που αποστέλλονται είναι σε μορφή JSON.

import requests  # Εισάγουμε τη βιβλιοθήκη requests για να κάνουμε HTTP αιτήματα
import json  # Εισάγουμε τη βιβλιοθήκη json για να μετατρέψουμε τα δεδομένα σε μορφή JSON

# Ορίζουμε τη διεύθυνση URL στην οποία θέλουμε να στείλουμε το POST αίτημα
url = 'https://httpbin.org/post'

# Ορίζουμε τα headers για το αίτημα (δηλώνουμε ότι τα δεδομένα είναι σε μορφή JSON)
headers = {'Content-Type': 'application/json'}

# Ορίζουμε τα δεδομένα που θέλουμε να στείλουμε (σε μορφή Python dict)
json_data = {'key': 'value'}

# Στέλνουμε το αίτημα POST στην URL με τα δεδομένα και τις κεφαλίδες (headers)
response = requests.post(url, headers=headers, data=json.dumps(json_data))

# Εκτυπώνουμε τον κωδικό κατάστασης της απάντησης (π.χ. 200 για επιτυχία)
print(response.status_code)

# Εκτυπώνουμε τα δεδομένα της απάντησης σε μορφή JSON
print(response.json())
