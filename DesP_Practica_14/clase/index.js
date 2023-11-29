var admin = require("firebase-admin");

var serviceAccount = require("./desarrollo-3ecbf-firebase-adminsdk-yqr4l-dd62ed8c4e.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://desarrollo-3ecbf-default-rtdb.firebaseio.com"
});

var db = admin.database();
var ref = db.ref("server/data");
var userRef = ref.child("node_js");  
userRef.set({
    productos: {
        nombre: "takis",
        precio: "3",
        tamano: 2
    }
});
