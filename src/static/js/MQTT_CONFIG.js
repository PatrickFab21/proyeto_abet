var display = document.getElementById("display")


var clientId = 'client_id_' + Math.floor((Math.random() * 100000) + 1)

var hostname = "ioticos.org";
var port = 8094; //Correspondiente a web sockets (WSS)
clientId += new Date().getUTCMilliseconds();;
var username = "muRiUdRvIVz8EFe";
var password = "jAkcIP17Rra1BqL";
var subscription = "TMfL59ZWFISeQwT/#"; //Suscripcion al Topico publicacion

mqttClient = new Paho.MQTT.Client(hostname, Number(port), clientId);

mqttClient.onMessageArrived = MessageArrived;
mqttClient.onConnectionLost = ConnectionLost;

Connect();

/*Initiates a connection to the MQTT broker*/
function Connect() {
    mqttClient.connect({
        onSuccess: Connected,
        onFailure: ConnectionFailed,
        keepAliveInterval: 10,
        userName: username,
        useSSL: true,
        password: password
    });
}


/*Callback for successful MQTT connection */
function Connected() {
    console.log("Connected");
    mqttClient.subscribe(subscription);
    $("#status").html("Conexion exitosa al Broker")
}


/*Callback for incoming message processing */
function MessageArrived(message) {
    console.log(message.destinationName + " : " + message.payloadString);
    // display.innerHTML += message.destinationName +" : " + message.payloadString + "<br>";
    if (message.destinationName == "TMfL59ZWFISeQwT/output/temperatura") {
        $("#CambiarTemperatura").html(message.payloadString + "°C")
    }
}

/*Callback for failed connection*/
function ConnectionFailed(res) {
    console.log("Connect failed:" + res.errorMessage);
}

/*Callback for lost connection*/
function ConnectionLost(res) {
    if (res.errorCode !== 0) {
        console.log("Connection lost:" + res.errorMessage);
        Connect();
    }
}


function estadoLED() {
    var luminosidad = document.getElementById('luminosidad').value

    var data = 'Luminosidad ' + luminosidad;

    console.log(data)
    mensaje = new Paho.MQTT.Message(String(luminosidad));
    mensaje.destinationName = "TMfL59ZWFISeQwT/input/led";
    mqttClient.send(mensaje);
}


if (1 == '1') {

}


var a = 10
a = 'HOLA'
a = true