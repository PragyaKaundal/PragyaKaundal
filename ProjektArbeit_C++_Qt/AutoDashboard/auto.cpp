#include "auto.h"

Auto::Auto(QObject *parent) : QObject(parent)
{
    mRueckwaertsgang = new Rueckwaertsgang();
    mGeschwindigkeit = new Geschwindigkeit();
    mStart = new Start();
}

bool Auto::eventFilter(QObject *object, QEvent *event)
{
    if (event->type() == QEvent::KeyPress) {
        QKeyEvent *keyEvent = static_cast<QKeyEvent *>(event);
        if (keyEvent->key() == Qt::Key_Up && mStart->getStart()) {
            if(keyEvent->isAutoRepeat()) {
               mSpeedPress = true;
            } else {
               mSpeedPress = false;
               qDebug() << "speed up";
               mTimer = new QTime();
               mTimer->start();
            }
            emit rueckwaertsfahren(false);
            return true;
        } else if (keyEvent->key() == Qt::Key_Down  && mStart->getStart()) {
            if(keyEvent->isAutoRepeat()) {
               mSpeedPress = true;
            } else {
               mSpeedPress = false;
               qDebug() << "speed down";
               mTimer = new QTime();
               mTimer->start();
            }
            return true;
        }  else if (keyEvent->key() == Qt::Key_Space && mStart->getStart()) {
            bool rF = mRueckwaertsgang->rueckwaertsfahren(true, mGeschwindigkeit->getKMH());
            if(rF ==false) {
                emit fehlerMessage(false, "Rückwärtsgang nicht möglich");
            }
            emit rueckwaertsfahren(rF);
            return true;
        } else if (keyEvent->key() == Qt::Key_S) {
            qDebug() << "auto start";
            mStart->starten(true);
            emit getWerte(mGeschwindigkeit->getKMH(), mGeschwindigkeit->getStrecke(),
                          mGeschwindigkeit->getVerbrauch(), mGeschwindigkeit->getDrehZahl(),
                          mGeschwindigkeit->getGang());
            return true;
        } else if (keyEvent->key() == Qt::Key_A) {
            qDebug() << "auto stop";
            mStart->starten(false);
            mGeschwindigkeit->ausschalten();
            emit getWerte(0, "0",
                          0.9,0,
                          "P");
            emit fehlerMessage(true,"Auto ausgeschaltet");
            emit rueckwaertsfahren(false);
            return true;
        }
    } else if (event->type() == QEvent::KeyRelease) {
        QKeyEvent *keyEvent = static_cast<QKeyEvent *>(event);
        if (keyEvent->key() == Qt::Key_Up && mStart->getStart()) {
            if(!keyEvent->isAutoRepeat() && mSpeedPress) {
                mGeschwindigkeit->beschleunigen(mTimer->elapsed(), true);
                delete mTimer;
                mTimer = nullptr;
                emit getWerte(mGeschwindigkeit->getKMH(), mGeschwindigkeit->getStrecke(),
                              mGeschwindigkeit->getVerbrauch(), mGeschwindigkeit->getDrehZahl(),
                              mGeschwindigkeit->getGang());
                 qDebug() << "speed up release";
            }
            return true;
        } else if (keyEvent->key() == Qt::Key_Down && mStart->getStart()) {
            if(!keyEvent->isAutoRepeat() && mSpeedPress) {
                mGeschwindigkeit->beschleunigen(mTimer->elapsed(), false);
                delete mTimer;
                mTimer = nullptr;
                emit getWerte(mGeschwindigkeit->getKMH(), mGeschwindigkeit->getStrecke(),
                              mGeschwindigkeit->getVerbrauch(), mGeschwindigkeit->getDrehZahl(),
                              mGeschwindigkeit->getGang());
                 qDebug() << "speed down release";
            }
            return true;
        }
    }
    return QObject::eventFilter(object, event);
}

Auto::~Auto() {
    delete mRueckwaertsgang;
    mRueckwaertsgang = nullptr;
    delete mGeschwindigkeit;
    mGeschwindigkeit = nullptr;
    delete mStart;
    mStart = nullptr;
}
