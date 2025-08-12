import socket
import threading
import subprocess
import platform
from queue import Queue


# -------- ΡΥΘΜΙΣΕΙΣ --------
SUBNET = "192.168.1."
PORT_RANGE = range(1, 1025)
THREADS = 10

# -------- ΕΛΕΓΧΟΣ ΖΩΝΤΑΝΩΝ IP --------
def is_alive(ip):
    system_name = platform.system().lower()
    if system_name == "windows":
        cmd = ["ping", "-n", "1", ip]
        creationflags = subprocess.CREATE_NO_WINDOW
    else:
        cmd = ["ping", "-c", "1", ip]
        creationflags = 0

    try:
        output = subprocess.check_output(
            cmd,
            stderr=subprocess.DEVNULL,
            creationflags=creationflags,
            universal_newlines=True  # Επιστρέφει string αντί για bytes
        )
        if "ttl" in output.lower():
            return True
        else:
            return False
    except:
        return False


# -------- ΣΑΡΩΣΗ ΠΟΡΤΩΝ --------
def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip, port))
        print(f"[+] {ip}:{port} is OPEN")
        sock.close()
    except:
        pass

# -------- THREADING FUNCTION --------
def port_worker(ip):
    while True:
        port = port_queue.get()
        scan_port(ip, port)
        port_queue.task_done()

# -------- MAIN FUNCTION --------
def main():
    print(f"[*] Σάρωση για ενεργές συσκευές στο subnet {SUBNET}0/24...\n")
    alive_ips = []

    for i in range(1, 255):
        ip = SUBNET + str(i)
        if is_alive(ip):
            print(f"[✓] {ip} χρησιμοποιείται")
            alive_ips.append(ip)
        if not is_alive(ip):
            print(f"[✘] {ip} δεν χρησιμοποιείται")
            alive_ips.append(ip)

    if not alive_ips:
        print("[-] Δεν βρέθηκαν ενεργές IP.")
        return

    print("\n[*] Σάρωση θυρών για κάθε ενεργή IP...\n")

    for ip in alive_ips:
        print(f"\n--- Σάρωση IP: {ip} ---")
        global port_queue
        port_queue = Queue()

        for _ in range(THREADS):
            t = threading.Thread(target=port_worker, args=(ip,))
            t.daemon = True
            t.start()

        for port in PORT_RANGE:
            port_queue.put(port)

        port_queue.join()

if __name__ == "__main__":
    main()
