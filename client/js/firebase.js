var firebaseConfig = {
    apiKey: "AIzaSyAM_4YAXdIy2NcyhWux9r_z0tw-I6O-rYQ",
    authDomain: "mountain-b24ea.firebaseapp.com",
    databaseURL: "https://mountain-b24ea.firebaseio.com",
    projectId: "mountain-b24ea",
    storageBucket: "mountain-b24ea.appspot.com",
    messagingSenderId: "256636473257",
    appId: "1:256636473257:web:c43d6bd5e97ef6b5ef7eb8",
    measurementId: "G-BCL13PKBL3"
};

firebase.initializeApp(firebaseConfig);

var db = firebase.firestore();

function getSentiments(country) {

    var summaryRef = db.collection("summary").doc(country);

    return summaryRef.get()
        .then(function (doc) {
            if (doc.exists) {
                // console.log("Document data:", doc.data().sentiments);
                return doc.data().sentiments
            } else {
                // doc.data() will be undefined in this case
                // console.log("No document");
                return {}
            }
        }).catch(function (error) {
            console.log("Error getting document:", error);
        });
}



// window.onload(()getSentiments("CAN"));

