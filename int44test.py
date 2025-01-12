import speedtest
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox


def ping_host(host):
    """
    Wykonuje polecenie `ping` na podanym hoście i zwraca średni czas RTT w ms.
    """
    try:
        result = subprocess.run(["ping", "-n", "4", host], stdout=subprocess.PIPE, text=True)
        output = result.stdout
        lines = output.splitlines()
        for line in lines:
            if "Average" in line:
                avg_ping = line.split("Average = ")[1].replace("ms", "").strip()
                return float(avg_ping)
        return None
    except Exception as e:
        return f"Error: {e}"


def test_speed(progress_var, progress_label):
    """
    Przeprowadza test szybkości internetu oraz mierzy dokładny ping za pomocą `ping`.
    """
    try:
        # Aktualizacja paska postępu
        progress_var.set(20)
        progress_label.config(text="Łączenie z serwerem...")
        root.update_idletasks()

        # Inicjalizacja klienta Speedtest
        st = speedtest.Speedtest()

        # Pobranie listy serwerów i wybór najlepszego
        servers = st.get_servers()
        best_server = st.get_best_server()

        progress_var.set(50)
        progress_label.config(text="Testowanie prędkości pobierania...")
        root.update_idletasks()

        # Testowanie prędkości pobierania
        download_speed = st.download() / 1_000_000  # Konwersja na Mbps

        progress_var.set(70)
        progress_label.config(text="Testowanie prędkości wysyłania...")
        root.update_idletasks()

        # Testowanie prędkości wysyłania
        upload_speed = st.upload() / 1_000_000  # Konwersja na Mbps

        progress_var.set(90)
        progress_label.config(text="Pomiar pinga...")
        root.update_idletasks()

        # Dokładny ping z konsoli
        exact_ping = ping_host(best_server['host'].split(':')[0])

        progress_var.set(100)
        progress_label.config(text="Test zakończony!")
        root.update_idletasks()

        return {
            "server": f"{best_server['host']} ({best_server['name']}, {best_server['country']})",
            "download_speed": round(download_speed, 2),  # Mbps
            "upload_speed": round(upload_speed, 2),  # Mbps
            "ping": round(exact_ping, 2) if exact_ping is not None else "Błąd pinga",
        }

    except Exception as e:
        return {"error": str(e)}


def start_test():
    """
    Funkcja uruchamiająca test szybkości internetu i aktualizująca wyniki w GUI.
    """
    # Resetowanie paska postępu
    progress_var.set(0)
    progress_label.config(text="Rozpoczynam test...")
    result_label.config(text="", fg="black")

    result = test_speed(progress_var, progress_label)

    if "error" in result:
        messagebox.showerror("Błąd", f"Nie udało się przeprowadzić testu:\n{result['error']}")
        progress_label.config(text="Błąd podczas testu.")
    else:
        # Dynamiczne kolorowanie wyników
        download_color = "green" if result['download_speed'] > 100 else "orange"
        upload_color = "green" if result['upload_speed'] > 50 else "orange"
        ping_color = "green" if result['ping'] < 20 else "red"

        result_label.config(
            text=(
                f"Serwer: {result['server']}\n"
                f"Prędkość pobierania: {result['download_speed']} Mbps\n"
                f"Prędkość wysyłania: {result['upload_speed']} Mbps\n"
                f"Ping: {result['ping']} ms"
            ),
            fg="black"
        )
        download_label.config(text=f"Download: {result['download_speed']} Mbps", fg=download_color)
        upload_label.config(text=f"Upload: {result['upload_speed']} Mbps", fg=upload_color)
        ping_label.config(text=f"Ping: {result['ping']} ms", fg=ping_color)


# Tworzenie głównego okna
root = tk.Tk()
root.title("Speed Test")
root.geometry("600x400")

# Nagłówek
header_label = tk.Label(root, text="Test szybkości internetu", font=("Arial", 16), pady=10)
header_label.pack()

# Pasek postępu
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate", variable=progress_var)
progress_bar.pack(pady=10)

progress_label = tk.Label(root, text="Oczekiwanie na rozpoczęcie testu...", font=("Arial", 12))
progress_label.pack()

# Wyniki testu
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=550, justify="left")
result_label.pack(pady=10)

download_label = tk.Label(root, text="Download: -", font=("Arial", 12))
download_label.pack()

upload_label = tk.Label(root, text="Upload: -", font=("Arial", 12))
upload_label.pack()

ping_label = tk.Label(root, text="Ping: -", font=("Arial", 12))
ping_label.pack()

# Przyciski
start_button = tk.Button(root, text="Rozpocznij test", font=("Arial", 14), command=start_test)
start_button.pack(pady=10)

# Start aplikacji
root.mainloop()
