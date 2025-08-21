import platform  # Εισαγωγή της βιβλιοθήκης platform
#pip install psutil 
import psutil  # Εισαγωγή της βιβλιοθήκης psutil

# Δημιουργία ενός λεξικού με πληροφορίες συστήματος
system_info = {
    'System': platform.system(),
    'Node Name': platform.node(),
    'Release': platform.release(),
    'Version': platform.version(),
    'Machine': platform.machine(),
    'Processor': platform.processor(),
    'Total RAM': f'{psutil.virtual_memory().total / (1024 ** 3):.2f} GB',  # Συνολική διαθέσιμη μνήμη RAM σε GB
    'Available RAM': f'{psutil.virtual_memory().available / (1024 ** 3):.2f} GB',  # Διαθέσιμη μνήμη RAM σε GB
    'Used RAM': f'{psutil.virtual_memory().used / (1024 ** 3):.2f} GB',  # Χρησιμοποιούμενη μνήμη RAM σε GB
    'CPU Usage': f'{psutil.cpu_percent()}%'  # Ποσοστό χρήσης της CPU
}

# Εκτύπωση των πληροφοριών συστήματος
for key, value in system_info.items():
    print(f'{key}: {value}')    
