
import os
import uuid
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from livekit import api

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(title="AI Voice Assistant API", lifespan=lifespan)
origins = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173").split(",")
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=False,
                   allow_methods=["GET", "POST"], allow_headers=["Content-Type"])

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/session")
async def create_session():
    url = os.getenv("LIVEKIT_URL")
    key = os.getenv("LIVEKIT_API_KEY")
    secret = os.getenv("LIVEKIT_API_SECRET")
    if not all([url, key, secret]):
        raise HTTPException(500, "LiveKit environment variables are missing")
    room = f"voice-{uuid.uuid4().hex}"
    identity = f"guest-{uuid.uuid4().hex[:12]}"
    token = (
        api.AccessToken(key, secret)
        .with_identity(identity)
        .with_name("Guest")
        .with_ttl(__import__("datetime").timedelta(minutes=15))
        .with_grants(api.VideoGrants(room_join=True, room=room, can_publish=True,
                                     can_subscribe=True, can_publish_data=True))
        .to_jwt()
    )
    lk = api.LiveKitAPI()
    try:
        await lk.agent_dispatch.create_dispatch(
            api.CreateAgentDispatchRequest(agent_name="voice-assistant", room=room)
        )
    except Exception as exc:
        raise HTTPException(502, "Could not start voice worker; check LiveKit configuration") from exc
    finally:
        await lk.aclose()
    return {"serverUrl": url, "token": token, "room": room}
