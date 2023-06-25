const socket = new WebSocket('ws://localhost:8765');

socket.onmessage = function(event) {
  var myVariable = event.data;
  console.log(myVariable);
};

socket.onopen = function(event) {
  // Connection is established, you can perform any necessary actions
  // For example, you can send a message to the server
  // socket.send('Client is ready');
};
