#include "geschwindigkeit.h"

Geschwindigkeit::Geschwindigkeit(QObject *parent) : QObject(parent)
{
}

void Geschwindigkeit::kmh(){
    double v{0.0};
    if(mBeschleunigen) {
        v = mAcc*mTime + mV;
    } else {
        v = mV - mDcc*mTime;
    }
    mV = v;
}

void Geschwindigkeit::strecke(){
    double s = 0.5*mAcc*mTime*mTime + mV*mTime + mStrecke;
    mStrecke = s;
}

void Geschwindigkeit::verbrauch(){
    double t = mTankLevel - 0.00008*mStrecke;
    mTankLevel = t;
}

void Geschwindigkeit::beschleunigen(int t, bool b){
    mTime = (t/1000 + (t%1000)*0.001)*10;
    mBeschleunigen = b;
    kmh();
    strecke();
    verbrauch();
    schalten();
    rpm();
}

void Geschwindigkeit::rpm(){
    int v = getKMH();
    double dz;
    if (v == 0) {
        dz = 0.8;
    } else if (v <= 10) {
        dz = 1.5;
    } else if (v <= 20) {
        dz = 3;
    } else if (v <= 30) {
        dz = 5;
    } else if (v <= 40) {
        dz = 1.5;
    } else if (v <= 50) {
        dz = 3;
    } else if (v <= 60) {
        dz = 5.5;
    } else if (v <= 70) {
        dz = 1.5;
    } else if (v <= 80) {
        dz = 3;
    } else if (v <= 90) {
        dz = 4;
    } else if (v <= 100) {
        dz = 5.5;
    } else if (v <= 110) {
        dz = 1.5;
    } else if (v <= 120) {
        dz = 2.5;
    } else if (v <= 130) {
        dz = 3.5;
    } else if (v <= 140) {
        dz = 6;
    } else if (v <= 150) {
        dz = 1.5;
    } else if (v <= 160) {
        dz = 2.5;
    } else if (v <= 180) {
        dz = 5;
    } else if (v <= 190) {
        dz = 6;
    } else if (v <= 200) {
        dz = 6.8;
    } else {
        dz = 7.5;
    }
    mDZ = dz;
}

void Geschwindigkeit::schalten(){
    int v = static_cast<int>(mV*3.6);
    if (v == 0) {
        mGang = 0;
    } else if (v <= 30) {
        mGang = 1;
    } else if (v <= 60) {
        mGang = 2;
    } else if (v <= 100) {
        mGang = 3;
    } else if (v <= 140) {
        mGang = 4;
    } else if (v <= 180){
        mGang = 5;
    } else {
        mGang = 6;
    }
}

int Geschwindigkeit::getKMH() const {
    int v = static_cast<int>(mV*3.6);
    return v;
}

QString Geschwindigkeit::getStrecke()const {
    int s = static_cast<int>(mStrecke);
    int strecke = static_cast<int>(s/100 + (s%1000)*0.001);
    return QString().setNum(strecke);
}

double Geschwindigkeit::getVerbrauch()const {
    return mTankLevel;
}

double Geschwindigkeit::getDrehZahl() const {
    return mDZ;
}

QString Geschwindigkeit::getGang() const{
    if(mGang == 0) {
        return "P";
    } else {
        QString gang = QString().setNum(mGang);
        return gang;
    }
}

void Geschwindigkeit::ausschalten(){
    mV = 0;
    mDZ = 1;
    mGang = 0;
    mBeschleunigen = false;
    mTime = 0;
}
