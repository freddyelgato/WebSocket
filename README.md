
# WebHook - Python Web Application

This project is a simple WebSocket service built using Pyhton and Docker. You can run it locally or in a Docker container and test it using cURL or Postman.

## Requirements
- **Docker**: [Install Docker](https://www.docker.com/get-started) if you don’t have it yet.
- **Python**: [Install Python](https://www.python.org/downloads/) if you plan to run the server locally.


## Installation Instructions

1. **Clone this repository**:
   ```bash
   git clone https://github.com/freddyelgato/WebSocket.git
   cd WebHook
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Build and run the application with Docker**:
   ```bash
   docker image build -t websocketconpython:latest .
   docker run -d -p 5000:5000 websocketconpython:latest
   ```

4. **Access the WebHook**:
   URL:
   - **WebHook Endpoint**: [http://localhost:5000](http://localhost:5000)



## Screenshots

### WebSocket Client Connect:
[![Client Connected](https://i.postimg.cc/QtSHFmWK/Cliente-Conectado.png)](https://postimg.cc/QtSHFmWK)

### WebSocket Client Disconnected:
[![Client Disconnected](https://i.postimg.cc/qqRgyK8b/Cliente-Desconectado.png)](https://postimg.cc/qqRgyK8b)


### Connect to the repository:

- For any questions, here is the [WebHook GitHub repository](https://github.com/freddyelgato/WebSocket) where you can find more details to guide you through the project.

- You can find the Docker image for this project here: [WebHook Docker Image](https://hub.docker.com/r/2424833f/websocket)
