import tkinter as tk  # tkinter -Modul für GUI (graphical user interface) widget-Set für Python

import matplotlib.pyplot as plt  # Zum Plotten
import mplcursors  # mplcursors stellt interaktive Datenauswahl-Cursors für Matplotlib zur Verfügung
import seaborn as sns  # Seaborn ist eine Python Datenvisualiserungsbibliothek, die auf matplotlib basiert.
from matplotlib.backend_bases import key_press_handler  # Implementierung der Standard Matplotlib Shortcuts
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk  # matplotlib Navigation-Toolbar
from pandas import DataFrame  # 2-dimensional, Größenanpassung, heterogene tabellarische Daten


class Plotwindow():
    """
    Das ist die Klasse zum Plotten der Daten, die wir mit Hilfe des ReadData-Moduls gelesen haben
    """

    def __init__(self, masterframe, size, val):
        """
        Diese Funktion ist zum Initialisieren des Plot-Fensters
        :param size: Größe des Fensters
        :param val: entscheidet, ob wir das Diagramm dreidimensional oder zweidimensional zeigen
        """
        (w, h) = size
        self.figure = plt.Figure(size)  # Erzeuge ein neu figure
        # # Hinzufügen eines subplot in erster Zeile und erster Spalte.
        if (val):
            self.axes = self.figure.add_subplot(111)  # Für den ersten und zweiten Graph zeige die standard geradlinige Projektion
        else:
            self.axes = self.figure.add_subplot(111, projection="3d")  # Für den dritten Graphen zeige die dritte Projektion
        # Erzeuge canvas als matplotlib Zeichenbereich
        self.c1 = FigureCanvasTkAgg(self.figure, master=masterframe)
        self.c1.get_tk_widget().grid(column=0, row=0, columnspan=4,
                                     sticky=tk.N + tk.S + tk.E + tk.W)  # # Skalierung und Positionierung des Canvas
        self.c1.mpl_connect("key_press_event",
                            key_press_handler)  # Verbinden von key press event mit der key_press_handler callback -Funktion
        toolbar = NavigationToolbar2Tk(self.c1, masterframe, pack_toolbar=False)  # matplotlib Navigation-Toolbar
        toolbar.grid(column=0, row=1, sticky=tk.W) # Scalierung und Positionierung der Toolbar
        toolbar.update()

    def fitnessNutzungGeschlecht(self, fitness, nutzung, geschlecht):
        """
        Mit dieser Funktion werden die Daten der Nutzung in Abhängigkeit von Fitness / Kondition und dem Geschlecht geplottet
        :param fitness: um Fitness zu plotten
        :param nutzung: um Nutzung pro Woche zu plotten
        :param geschlecht: um Geschlecht zu plotten
        """
        data1 = {'Fitness/Kondition': fitness,
                 'Nutzung pro Woche': nutzung,
                 'Geschlecht': geschlecht,
                 }
        df1 = DataFrame(data1, columns=['Fitness/Kondition', 'Nutzung pro Woche',
                                        'Geschlecht'])  # 2-dimensional, Größenanpassung, heterogene tabellarische Daten
        sns.barplot(x="Fitness/Kondition", y="Nutzung pro Woche", hue="Geschlecht", data=df1, ax=self.axes)  # Plot als Zwei-Balken-Plot
        self.axes.set_title('Nutzung in Abhängigkeit von Fitness and Geschlecht') # Titel festlegen
        self.c1.draw()

    def nutzungEinkommenAusbildung(self, nutzung, einkommen, ausbildung):
        """
        Dies ist eine Funktion, um die Daten der Nutzung in Abhängigkeit vom Jahreseinkommen zu plotten
        :param ausbildung: um Ausbildung in Jahren zu plotten
        :param einkommen: um Jahreseinkommen zu plotten
        :param nutzung: um die Nutzung pro Woche zu plotten
        """
        ein = [val / 1000 for val in einkommen]
        data2 = {'Jahreseinkommen (in Tausend)': ein,
                 'Ausbildung (in Jahre)': ausbildung
                 }
        df2 = DataFrame(data2, columns=['Jahreseinkommen (in Tausend)',
                                        'Ausbildung (in Jahre)']) # 2-dimensional, Größenanpassung, heterogene tabellarische Daten
        df2 = df2[['Jahreseinkommen (in Tausend)', 'Ausbildung (in Jahre)']].groupby('Jahreseinkommen (in Tausend)').mean()
        lines = df2.plot(kind='line', legend=True, ax=self.axes, color='r', marker='o',
                         fontsize=10)  # Erzeugen eines 2D-Linien-Plots aus DataFrame
        mplcursors.cursor(lines) # Ein Cursor zum Auswählen von Matplotlib artists
        self.axes.set_title('Nutzung in Abhängigkeit vom Jahreseinkommen und Ausbildung') # Titel festlegen
        self.axes.set_ylabel('Ausbildung (in Jahre)') # Festlegung der Bezeichnung auf der y-Achse
        for i in range(0, len(nutzung)):
            if (nutzung[i] != 3 and nutzung[i] != 4):
                # Beschriftung des Punktes xy mit Text
                self.axes.annotate(str(nutzung[i]), (ein[i], ausbildung[i]), ha="left", va="bottom",
                                   textcoords="offset points", xytext=(4, 4), zorder=i, fontsize=8)
        self.c1.draw()

    def alterWegstreckeFitnessNutzung(self, alter, wegstrecke, fitness, nutzung):
        """
        Diese Funktion dient zum Plotten der Daten Nutzung in Abhängigkeit vom Alter, der Wegstrecke und der Fitness
        :param alter: um Alter zu plotten
        :param wegstrecke: um Meilen zu plotten
        :param fitness: um Fitness zu plotten
        :param nutzung: um Nutzung pro Woche zu plotten
        """
        import matplotlib.colors
        cmap = plt.cm.rainbow
        norm = matplotlib.colors.Normalize(vmin=min(nutzung), vmax=max(nutzung)) # normalisiert Daten linear in das maximale und minimale Intervall
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm) # Rückgabe der RGBA Farben aus der colormap
        sm.set_array([])  # nur für matplotlib < 3.1 benötigt
        self.figure.colorbar(sm, orientation='horizontal', label='Nutzung pro Woche') # Erzeugung des Farbbalkens (colorbar)
        self.axes.scatter3D(alter, fitness, wegstrecke, color=cmap(norm(nutzung)))
        self.axes.legend(['Nutzung pro Woche'])
        self.axes.set_xlabel('Alter')
        self.axes.set_ylabel('Fitness/Kondition')
        self.axes.set_zlabel('Wegstrecke (in Meilen)')
        self.axes.set_title('Nutzung in Abhängigkeit vom Alter, Fitness und Wegstrecke')
        self.c1.draw()

    def clearplot(self):
        """
        Funktion zum Zurücksetzen des Plots
        """
        self.axes.cla()  # Zurücksetzen der Achsen
        self.c1.draw()
