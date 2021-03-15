#include "start.h"

Start::Start(QObject *parent) : QObject(parent), mStart(false)
{

}

void Start::starten(bool start){
    mStart = start;
}

bool Start::getStart() const {
    return mStart;
}


