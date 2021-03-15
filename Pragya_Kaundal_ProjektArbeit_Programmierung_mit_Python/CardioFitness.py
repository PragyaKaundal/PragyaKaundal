import tkinter as tk  # tkinter -Modul für GUI (graphical user interface) widget-Set für Python
from tkinter import messagebox  # Modul für die Pop-Up -Dialoge

import matplotlib  # Import des gesamten matplotlib- Moduls für die Erstellung von Plots in Python
import matplotlib.pyplot as plt  # Um zu Plotten

matplotlib.use('TkAgg') #  Verwenden von Matplotlib mit tkinter (TkAgg)

from PlotWindow import Plotwindow  # Modul zum Plotten der Gesundheitsdaten
from ReadData import Readdata  # Modul zum Lesen der Gesundheitsdaten


def plotAlterWegstreckeFitnessNutzung():
    """
    Diese Funktion dient zum Plotten der Daten Nutzung in Abhängigkeit vom Alter, der Wegstrecke und der Fitness
    """
    plot_w.clearplot()
    # um die Werte vom ReadData-Modul zu erhalten
    alter, geschlecht, ausbildung, nutzung, fitness, einkommen, wegstrecke = datrd.getValues()
    # Anzeigen der Fehlermeldung, wenn keine Datei ausgewählt wurde
    if (len(nutzung) == 0):
        messagebox.showerror("Achtung!", "Bitte zuerst eine Datei öffnen, um zu Plotten!")
    else:
        # Plotten der Daten
        plot_w1 = Plotwindow(mainframe, (9, 8), False)
        plot_w1.alterWegstreckeFitnessNutzung(alter, wegstrecke, fitness, nutzung)


def plotNutzungEinkommenAusbildung():
    """
    Dies ist eine Funktion, um die Daten der Nutzung in Abhängigkeit vom Jahreseinkommen zu plotten
    """
    plot_w.clearplot()
    # um die Werte vom ReadData-Modul zu erhalten
    alter, geschlecht, ausbildung, nutzung, fitness, einkommen, wegstrecke = datrd.getValues()
    # Anzeigen der Fehlermeldung, wenn keine Datei ausgewählt wurde
    if (len(nutzung) == 0):
        messagebox.showerror("Achtung!", "Bitte zuerst eine Datei öffnen, um zu Plotten!")
    else:
        # Plotten der Daten
        plot_w2 = Plotwindow(mainframe, (9, 8), True)
        plot_w2.nutzungEinkommenAusbildung(nutzung, einkommen, ausbildung)


def plotFitnessNutzungGeschlecht():
    """
    Mit dieser Funktion werden die Daten der Nutzung in Abhängigkeit von Fitness/Kondition und dem Geschlecht
    """
    plot_w.clearplot()
    # um die Werte vom ReadData-Modul zu erhalten
    alter, geschlecht, ausbildung, nutzung, fitness, einkommen, wegstrecke = datrd.getValues()
    # Anzeigen der Fehlermeldung, wenn keine Datei ausgewählt wurde
    if (len(nutzung) == 0):
        messagebox.showerror("Achtung!", "Bitte zuerst eine Datei öffnen, um zu Plotten!")
    else:
        # Plotten der Daten
        plot_w3 = Plotwindow(mainframe, (9, 8), True)
        plot_w3.fitnessNutzungGeschlecht(fitness, nutzung, geschlecht)


def clear():
    """
    Mit dieser Funktion wird der Plott zurückgesetzt
    """
    plot_w.clearplot()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("CardioGoodFitness")  # Festlegen des Titels im Hauptfenster
    plt.style.use('seaborn')  # Verwendung von "Seaborn" als Style (Darstellung) in matplotlib.
    mainframe = tk.Frame(root)  # mainframe ist ein Container für andere Widgets (z.B. für Toolbar usw.)
    mainframe.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)  # Skalierung und Positionierung des mainframes
    datrd = Readdata()  # Erzeugung eines Objekts der Klasse Lesen zum Lesen der Datei, die geplotten werden soll
    plot_w = Plotwindow(mainframe, (9, 8), True)  # Erzeugung eines Objekts der Klasse Plotwindow zum Plotten des Fensters
    # Zum Erzeugen der Menüs und Untermenüs
    menu_widget = tk.Menu(mainframe)  # Erzeugung des drop-down -Menü (Auswahlliste)
    # Erzeugung der drop-down sub-Menüs
    submenu_widget = tk.Menu(menu_widget, tearoff=False)
    plotMenu = tk.Menu(mainframe, tearoff=False)
    menu_widget.add_cascade(label="Datei", menu=submenu_widget)
    submenu_widget.add_command(label="Öffnen",
                               command=datrd.readValues)
    submenu_widget.add_cascade(label="Plotten", menu=plotMenu)
    # Hinzufügen der Befehle, die ausgeführt werden sollen, wenn eine bestimmte Funktion ausgewählt wird
    # Die Funktion plotFitnessNutzungGeschlecht wird aufgerufen, wenn z.B. die Auswahl ""Nutzung in Abhängigkeit von Fitness and Geschlecht"
    # getroffen wird.
    plotMenu.add_command(label="Nutzung in Abhängigkeit von Fitness and Geschlecht",
                         command=plotFitnessNutzungGeschlecht)
    plotMenu.add_command(label="Nutzung in Abhängigkeit vom Jahreseinkommen und Ausbildung",
                         command=plotNutzungEinkommenAusbildung)
    plotMenu.add_command(label="Nutzung in Abhängigkeit vom Alter, Fitness und Wegstrecke",
                         command=plotAlterWegstreckeFitnessNutzung)
    submenu_widget.add_command(label="Schließen",
                               command=root.destroy)
    root.config(menu=menu_widget)
    root.mainloop()
