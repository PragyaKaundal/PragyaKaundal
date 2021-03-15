#ifndef START_H
#define START_H

#include <QObject>
#include <QKeyEvent>
#include <QDebug>

/* Diese Klasse gibt uns zurück, ob das Auto gestartet wurde. */
class Start : public QObject
{
    Q_OBJECT
    bool mStart;
public:
    explicit Start(QObject *parent = nullptr);
    /*Diese Funktion nimmt die Rückmeldung der Tastertur auf und passt die Variable mstart entsprechend an. */
    void starten(bool);
    /*Diese Funktion gibt uns zurück, ob das Auto gestartet wurde. */
    bool getStart() const;
};

#endif // START_H
