# AI Voice Agent Using OpenAI and Python

A Python-based AI Voice Assistant designed for real-time, natural voice conversations using **OpenAI, LiveKit, FastAPI, and React**.

The project combines a Python AI agent, a backend API, and a web interface to support interactive voice-based communication.

## Project Overview

The goal of this project is to build an AI-powered voice assistant that can receive spoken questions, process requests using OpenAI models, and generate spoken responses.

The application uses LiveKit for real-time audio communication and a Python backend to securely manage connections.


## Technology Stack

| Technology | Purpose |
|---|---|
| Python | AI agent and backend development |
| OpenAI API | Speech processing and AI responses |
| LiveKit | Real-time audio communication |
| FastAPI | Backend API |
| React | Frontend user interface |
| JavaScript | Frontend functionality |
| Python-dotenv | Environment variable management |

## Features

The project is designed to support:

- Real-time voice interaction
- AI-generated conversational responses
- Speech recognition and speech synthesis
- Browser-based microphone interaction
- LiveKit audio sessions
- Secure server-side API credentials
- Extensible Python agent architecture

Additional integrations, such as weather information, external APIs, conversation history, and custom commands, can be developed in future versions.

## Project Structure

```text
AI-Voice-Agent-using-OpenAI-Python/
├── backend/
│   ├── agent.py
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── package.json
│   └── src/
├── .gitignore
├── README.md
└── LICENSE
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/jagjitkaur0000/AI-Voice-Agent-using-OpenAI-Python.git
cd AI-Voice-Agent-using-OpenAI-Python
```

### 2. Set up the Python backend

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file inside the `backend` directory using `.env.example` as a template.

```dotenv
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
OPENAI_API_KEY=your_openai_api_key
```


## Application Architecture

```text
User (Microphone)
       |
       v
React Frontend
       |
       v
FastAPI Backend (Session Token)
       |
       v
LiveKit Real-Time Audio
       |
       v
Python AI Agent
       |
       v
OpenAI API
       |
       v
Spoken AI Response
```

## Deployment

The application can be deployed using:

- **Vercel:** React frontend
- **Render or Railway:** FastAPI backend
- **LiveKit Cloud or worker hosting:** AI voice agent
- **OpenAI API:** AI processing

Deployment requires appropriate environment variables and a running voice agent. Public production deployment should also include authentication, rate limiting, and usage controls.


## Future Improvements

- Conversation history and persistent storage
- User authentication
- Additional AI tools and external API integrations
- Multilingual voice interaction
- Improved error handling and automated tests
- Mobile-responsive user interface
- Usage monitoring and rate limiting
- Public demonstration mode

## Author

**Jagjit Kaur**

GitHub: https://github.com/jagjitkaur0000

## License

This project is licensed under the MIT License. 
