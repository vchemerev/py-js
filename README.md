# py-js
Transfer a variable from Python to JavaScript using web sockects

**On the server-side (Python):**

import asyncio
import websockets

# Define the variable value to be transferred
my_variable = "Hello from Python!"

async def send_variable(websocket, path):
    # Send the variable value to the client
    await websocket.send(my_variable)

start_server = websockets.serve(send_variable, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

**On the client-side (JavaScript):**

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


