# Chat Room Project

**A Client-Server Chat Application**  
Lucio Baiocchi, June 13, 2024

---

## Project Overview

This project implements a client-server chat room system using Python's socket programming capabilities. The server manages multiple clients concurrently, enabling real-time message exchange in a shared chat room environment. The client application allows users to connect to the server, send messages, and receive messages from other users.

---

## Features

### Server:
- Accepts multiple client connections.
- Handles message broadcasting to all connected clients.
- Manages a list of clients and their nicknames.

### Client:
- Connects to the server using a unique nickname.
- Sends and receives messages in real-time.
- Provides a user-friendly graphical interface for chat interactions.

---

## Technologies Used

- **Programming Language:** Python
- **Libraries:**
  - `socket` for network communication.
  - `threading` for handling concurrent connections.
  - `tkinter` for the graphical user interface (client-side).

---

## Setup and Usage

### Prerequisites
1. Python 3.x installed on your system.

### Steps to Run:
1. **Start the Server:**
   ```bash
   python server.py
   ```
2. **Run the Client:**
   ```bash
   python client.py
   ```
3. On starting the client, you will be prompted to enter a nickname to join the chat room.

---

## Code Architecture

### Server
The server performs the following tasks:
1. Listens for incoming client connections.
2. Receives messages from clients and broadcasts them to all others.
3. Maintains a list of connected clients and their nicknames.

**Key Methods:**
- `handle_client(client)`: Handles messages from a specific client.
- `broadcast(message, client)`: Sends a message to all connected clients except the sender.

### Client
The client application:
1. Connects to the server using a socket.
2. Uses a GUI for user interaction.
3. Handles sending and receiving messages in separate threads to ensure responsiveness.

**Key Components:**
- `ChatClient`: Main class implementing the GUI and network interaction.
- `receive_messages()`: Listens for messages from the server.
- `send_message()`: Sends user input to the server.

---

## Optimizations

### Enhancements for Performance and Scalability:
- **Threading:** Both server and client use threads to handle message sending/receiving without blocking the interface or other operations.
- **Buffering:** A buffer size of 1024 bytes is used to optimize data transmission.
- **Exception Handling:** Improved handling for client disconnections and network errors.
- **Scalable Architecture:** Designed to support multiple clients simultaneously with minimal performance degradation.

---

## Future Enhancements
- **User Authentication:** Implement user login and registration.
- **Message Encryption:** Secure communication with encryption protocols.
- **Enhanced UI:** Add features like themes, user statuses, and chat history.

---
