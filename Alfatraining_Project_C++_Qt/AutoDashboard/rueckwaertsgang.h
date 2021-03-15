#ifndef RUECKWAERTSGANG_H
#define RUECKWAERTSGANG_H

#include <QObject>
#include <QDebug>

/* Diese Klasse überprüft, ob der Rückwärtsgang aktiviert werden kann. */
class Rueckwaertsgang : public QObject
{
    Q_OBJECT
    bool mRF;
public:
    explicit Rueckwaertsgang(QObject *parent = nullptr);
   /* Diese Funktion überprüft, ob der Rückwärtsgang aktiviert werden kann. */
    bool rueckwaertsfahren(bool, int);
};

#endif // RUECKWAERTSGANG_H
