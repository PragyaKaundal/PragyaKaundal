import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4

Window {
    id: root
    visible: true
    width: 1024
    height: 600
    property bool imageVisible: false
    property bool rectVisible: false
    property real kph_alt: 0
    property real kph_neu: 0
    property real fuel_alt: 0.9
    property real fuel_neu: 0.9
    property real rpm_alt: 0
    property real rpm_neu : 0
    property string fehler: ""
    color: "#161616"
    title: "Dashboard"

    Image {
        id: background
        source: "rueckwaertsbild.png"
        visible: imageVisible
        sourceSize.width: 1500
        sourceSize.height: 800
    }

    Connections {
        target: auto
        onRueckwaertsfahren: {
            root.imageVisible = rF
        }
        onFehlerMessage: {
            if(stop) {
                rect.color = "lightyellow";
                label_fehler.color = "black";
            }
                rect.visible = true;
                label_fehler.text = msg;
        }

        onGetWerte: {
            rect.visible = false;
            label_fehler.text = qsTr("");
            label_gang.text = gang;
            label_gesamtKm.text = strecke;
            root.kph_alt = root.kph_neu;
            root.kph_neu = kmh;
            root.fuel_alt = root.fuel_neu;
            root.fuel_neu = verbrauch;
            root.rpm_alt = root.rpm_neu;
            root.rpm_neu = drehZahl;
            pa.restart();
            if(verbrauch < 0.2) {
                rect.visible = true;
                label_fehler.text = qsTr("Bitte tanken");
            }
            if(drehZahl > 7) {
                rect.visible = true;
                label_fehler.text = qsTr("Hohe Drehzahl. Bitte langsamer!");
            }
        }
    }

    Item {
        focus: true
        objectName: "it"
    }

    ParallelAnimation {
        id: pa
        NumberAnimation {
            id: nx
            target: speedometer
            property: "value"
            from: root.kph_alt
            to: root.kph_neu
            duration: 6000
        }
        NumberAnimation {
            id: ny
            target: fuelGauge
            property: "value"
            from: root.fuel_alt
            to: root.fuel_neu
            duration: 3000
        }
        NumberAnimation {
            id: nz
            target: tachometer
            property: "value"
            from: root.rpm_alt
            to: root.rpm_neu
            duration: 3000
        }
    }

    // Dashboards are typically in a landscape orientation, so we need to ensure
    // our height is never greater than our width.
    Item {
        id: container
        width: root.width
        height: Math.min(root.width, root.height)
        anchors.centerIn: parent
        visible: !imageVisible

        Row {
            id: gaugeRow
            spacing: container.width * 0.02
            anchors.centerIn: parent

                Item {
                width: height
                height: container.height * 0.25 - gaugeRow.spacing
                anchors.verticalCenter: parent.verticalCenter

                    CircularGauge {
                        id: fuelGauge
                        value: 0.9
                        maximumValue: 1
                        y: parent.height / 2 - height / 2 - container.height * 0.01
                        width: parent.width
                        height: parent.height * 0.7

                        style: IconGaugeStyle {
                            id: fuelGaugeStyle

                            icon: "qrc:/fuel-icon.png"
                            minWarningColor: Qt.rgba(0.5, 0, 0, 1)

                            tickmarkLabel: Text {
                                color: "white"
                                visible: styleData.value === 0 || styleData.value === 1
                                font.pixelSize: fuelGaugeStyle.toPixels(0.225)
                                text: styleData.value === 0 ? "E" : (styleData.value === 1 ? "F" : "")
                            }
                        }
                    }

                    Rectangle {
                        id: rect_gesamtKm
                        width: parent.width * 0.8
                        height: parent.height * 0.2
                        y: parent.height * 0.7 //+ parent.height * 0.02
                        anchors.horizontalCenter: parent.horizontalCenter
                        color: '#696969'
                        radius: 5

                        Label {
                            id: label_gesamtKm
                            width: parent.width
                            height: parent.height
                            y: rect_gesamtKm.height * 0.15
                            x: 7
                            text: qsTr("0")
                            font.pixelSize: 18
                            color: "White"
                            }

                        Label {
                            id: label_km
                            width: parent.width * 0.3
                            height: parent.height
                            y: rect_gesamtKm.height * 0.15
                            x: parent.width * 0.7
                            text: qsTr("km")
                            font.pixelSize: 18
                            color: "White"
                            }
                    }
                }


                Item {
                width: height
                height: container.height * 0.54 - gaugeRow.spacing

                anchors.verticalCenter: parent.verticalCenter

                    CircularGauge {
                        id: speedometer
                        anchors.verticalCenter: parent.verticalCenter
                        maximumValue: 280
                        // We set the width to the height, because the height will always be
                        // the more limited factor. Also, all circular controls letterbox
                        // their contents to ensure that they remain circular. However, we
                        // don't want to extra space on the left and right of our gauges,
                        // because they're laid out horizontally, and that would create
                        // large horizontal gaps between gauges on wide screens.
                        width: height
                        height: container.height * 0.5

                        style: DashboardGaugeStyle {}
                    }

                    Rectangle {
                        id: rect
                        visible: false
                        width: parent.width
                        height: parent.height * 0.1//3
                        y: parent.height + parent.height * 0.02
                        color: '#b22222'
                        radius: 10

                        Label {
                            id: label_fehler
                            width: parent.width
                            height: parent.height
                            y: parent.height * 0.2
                            x: 7
                            text: ""
                            font.pixelSize: 18
                            color: "White"
                            }
                    }
                }

                Item {
                width: height
                height: container.height * 0.25 - gaugeRow.spacing
                anchors.verticalCenter: parent.verticalCenter
                    CircularGauge {
                        id: tachometer
                        width: height
                        height: container.height * 0.25 - gaugeRow.spacing
                        maximumValue: 8
                        anchors.verticalCenter: parent.verticalCenter

                        style: TachometerStyle {}
                    }
                }

            Item {
                width: height
                height: container.height * 0.25 - gaugeRow.spacing
                anchors.verticalCenter: parent.verticalCenter

                Label {
                    id: label_gang
                    anchors.verticalCenter: parent.verticalCenter
                    width: height
                    height: container.height * 0.1 - gaugeRow.spacing
                    text: qsTr("P")
                    font.pixelSize: 30
                    color: "White"
                }

                Label {
                    id: label_gang2
                    y: parent.height * 0.2// + parent.height * 0.02
                    width: height
                    height: container.height * 0.1 - gaugeRow.spacing
                    text: qsTr("Gang")
                    font.pixelSize: 15
                    color: "White"
                    }
            }

        }
    }
}
