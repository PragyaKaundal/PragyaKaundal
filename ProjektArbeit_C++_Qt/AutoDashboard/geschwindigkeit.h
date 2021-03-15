#ifndef GESCHWINDIGKEIT_H
#define GESCHWINDIGKEIT_H

#include <QObject>
#include <QDebug>

/* Diese Klasse wird benötigt, um die berechenten Werte an das UI zu übergeben */
class Geschwindigkeit : public QObject
{
    Q_OBJECT
    const double mAcc = 2.1;
    const double mDcc = 1.5;

    double mV = 0.0;
    double mDZ = 1;
    double mStrecke = 0.0;
    double mTankLevel = 0.9;
    int mGang = 0;
    bool mBeschleunigen = false;
    double mTime = 0.0;

    /* Diese Funktion berechnet die Geschwindigkeit. */
    void kmh();
    /* Diese Funktion berechnet die gesamt gefahrene Strecke. */
    void strecke();
    /* Diese Funktion berechnet den Kartstoffverbrauch. */
    void verbrauch();
    /* Diese Funktion berechnet die Drehzahl. */
    void rpm();
    /* Diese Funktion berechnet den Gang. */
    void schalten();

public:
    explicit Geschwindigkeit(QObject *parent = nullptr);
    /* Diese Funktion ruft andere Funktionen auf und setzt die Variable mBeschleunigen. */
    void beschleunigen(int, bool);
    /* Diese Funktion gibt die Geschwindigkeit zurück. */
    int getKMH() const;
    /* Diese Funktion gibt die gesamt gefahrene Strecke zurück. */
    QString getStrecke() const;
    /* Diese Funktion gibt den Kartstoffverbrauch zurück. */
    double getVerbrauch() const;
     /* Diese Funktion gibt die Drehzahl zurück. */
    double getDrehZahl() const;
    /* Diese Funktion gibt den Gang zurück. */
    QString getGang() const;
    /* Diese Funktion setzt die Werte zurück wenn das Auto ausgeschaltet wird */
    void ausschalten();
};

#endif // GESCHWINDIGKEIT_H
