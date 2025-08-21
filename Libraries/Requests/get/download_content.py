# Ο κώδικας κατεβάζει ένα αρχείο από την URL https://www.grcodeclub.gr/somefile.zip και το αποθηκεύει στον τοπικό υπολογιστή με το όνομα somefile.zip.

import requests  # Εισάγουμε τη βιβλιοθήκη requests για να κάνουμε HTTP αιτήματα

# Ορίζουμε τη διεύθυνση URL του αρχείου που θέλουμε να κατεβάσουμε
url = 'https://www.grcodeclub.gr/somefile.zip'

# Στέλνουμε το αίτημα GET για να κατεβάσουμε το αρχείο
response = requests.get(url)

# Ανοίγουμε το αρχείο στον τοπικό υπολογιστή σε λειτουργία εγγραφής δυαδικών δεδομένων ('wb')
with open('somefile.zip', 'wb') as file:
    # Εγγράφουμε το περιεχόμενο του αρχείου που λήφθηκε από το αίτημα
    file.write(response.content)
