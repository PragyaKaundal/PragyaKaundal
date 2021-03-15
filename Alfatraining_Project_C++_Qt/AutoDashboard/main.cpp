#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlComponent>
#include <QQuickItem>
#include <QQmlContext>
#include "auto.h"

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    QQmlApplicationEngine engine;
    QQmlComponent component(&engine,
            QUrl(QStringLiteral("qrc:/main.qml")));
    QQmlContext* ctx = engine.rootContext();
    Auto a;
    ctx->setContextProperty("auto", &a);
    QObject* window = component.create();
    QQuickItem* rect = window->findChild<QQuickItem*>("it");
    rect->installEventFilter(&a);
    return app.exec();
}
