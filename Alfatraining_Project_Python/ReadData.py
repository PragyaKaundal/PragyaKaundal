import csv  # Modul zum Lesen und Schreiben tabellarischer Daten ins CSV -Format
import os  # Betriebssystem
from tkinter import filedialog, messagebox  # Modul für die Pop-Up-Dialoge


class Readdata():
    """
    Das ist die Klasse zum Lesen der Daten von der CVS-Datei.
    """

    def __init__(self):
        """
        # initialisieren der Instanzvariablen
        """
        self.alter = []
        self.geschlecht = []
        self.ausbildung = []
        self.nutzung = []
        self.fitness = []
        self.einkommen = []
        self.wegstrecke = []

    def readValues(self):
        """
        Das ist die Funktion zum Lesen der Daten von der CVS-Datei
        """
        # Öffnen des Dialogs Datei, um die Datei auszuwählen, die geplottet werden soll
        filename = filedialog.askopenfilename(initialdir="C:/Users/Alfa/PycharmProjects/kurs", title="Datei öffnen",
                                              filetypes=(
                                                  ("csv files", "*.csv"), ("all files", "*.*")))
        s_name, s_ext = os.path.splitext(filename)
        # Wenn die Datei eine CSV-Datei ist, dann soll die Datei gelesen werden, andernfalls gib eine Fehlermeldung aus.
        if s_ext == ".csv":
            with open("CardioGoodFitness.csv") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')  # Lesen der CSV-Datei
                line_count = 0
                for row in csv_reader:
                    print(row)
                    if line_count == 0:
                        print(f"\tSpaltennamen sind {', '.join(row).title()}")
                    else:
                        try:
                            # Alter, Geschlecht, Ausbildung, Nutzung, Fitness, Einkommen, Wegstrecke
                            self.alter.append(int(row[1]))
                            self.geschlecht.append(row[2])
                            self.ausbildung.append(int(row[3]))
                            self.nutzung.append(int(row[5]))
                            self.fitness.append(int(row[6]))
                            self.einkommen.append(int(row[7]))
                            self.wegstrecke.append(float(row[8]))
                        except:
                            messagebox.showerror("Achtung!", "Kein gültiges Dateiformat gefunden!.")
                    line_count += 1
        else:
            messagebox.showerror("Achtung!", "Kein gültiges Dateiformat gefunden!.")

    def getValues(self):
        """
        Diese Funktion gibt die Werte zurück, die geplottet werden sollen
        """
        return self.alter, self.geschlecht, self.ausbildung, self.nutzung, self.fitness, self.einkommen, self.wegstrecke
