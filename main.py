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
