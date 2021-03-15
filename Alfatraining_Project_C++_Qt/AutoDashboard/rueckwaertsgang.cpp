#include "rueckwaertsgang.h"

Rueckwaertsgang::Rueckwaertsgang(QObject *parent) : QObject(parent), mRF(false)
{

}

bool Rueckwaertsgang::rueckwaertsfahren(bool space, int v){
    if(space && v<=0) {
        mRF = true;
    } else {
        mRF = false;
    }
return mRF;

}
