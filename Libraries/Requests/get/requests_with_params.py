# Ο κώδικας που παραθέτεις στέλνει ένα αίτημα GET σε μια URL, προσθέτοντας παραμέτρους στο URL με τη μορφή query string. 
# Οι παράμετροι μεταφέρονται μέσω του params και είναι προσυσκευασμένες αυτόματα στην URL από τη βιβλιοθήκη requests.

import requests  # Εισάγουμε τη βιβλιοθήκη requests για να κάνουμε HTTP αιτήματα

# Ορίζουμε τις παραμέτρους που θέλουμε να στείλουμε με το αίτημα
params = {'param1': 'value1', 'param2': 'value2'}

# Στέλνουμε το αίτημα GET στην URL με τις παραμέτρους
response = requests.get('https://grcodeclub.gr/get', params=params)

# Εκτυπώνουμε τον κωδικό κατάστασης της απάντησης (π.χ. 200 για επιτυχία)
print(response.status_code)

# Αν η απάντηση είναι σε μορφή JSON, την εκτυπώνουμε ως Python dict
print(response.json())
