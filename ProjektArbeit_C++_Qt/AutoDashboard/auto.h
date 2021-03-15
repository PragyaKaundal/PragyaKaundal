#ifndef AUTO_H
#define AUTO_H

#include <QObject>
#include <QTime>
#include "geschwindigkeit.h"
#include "rueckwaertsgang.h"
#include "start.h"

/* Hauptklasse die mit dem UI kommuniziert */
class Auto : public QObject
{
    Q_OBJECT
    Geschwindigkeit* mGeschwindigkeit = nullptr;
    Rueckwaertsgang* mRueckwaertsgang = nullptr;
    Start* mStart = nullptr;
    QTime* mTimer = nullptr;
    bool mSpeedPress = false;

public:
    explicit Auto(QObject *parent = nullptr);
    ~Auto() override;

signals:
    /* Das Signal wird aufgerufen wenn die Space Taste gedrückt wird
        und die Geschwindigkeit 0 km/h beträgt */
    void rueckwaertsfahren(bool rF);
    /* Das Signal wird benutzt um all Werte an das Dashboard zurück zu geben. */
    void getWerte(int kmh, QString strecke, double verbrauch, double drehZahl, QString gang);
    /* Funktion um bestimmt Fehlermeldungen an den Benutzer zurückzugeben */
    void fehlerMessage(bool stop, QString msg);

protected:
    /*In diese Funktion werden alle Tastaturbelegungen definiert. */
    bool eventFilter(QObject *, QEvent *) override;
};

#endif // AUTO_H
