const webcamVideo = document.getElementById("webcamVideo");

navigator.mediaDevices.getUserMedia({video: true}).then((stream)=>{
    webcamVideo.srcObject = stream;

}).catch((error)=>{
    console.error(error);
})