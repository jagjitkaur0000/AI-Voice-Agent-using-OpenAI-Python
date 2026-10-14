"""LiveKit Agents 1.x voice worker. Run: python agent.py dev"""
import os
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession, RoomInputOptions
from livekit.plugins import openai, silero

load_dotenv()

INSTRUCTIONS = (
    "You are a helpful, concise AI voice assistant. "
    "Speak naturally, ask for clarification when needed, and never invent facts."
)

class VoiceAssistant(Agent):
    def __init__(self):
        super().__init__(instructions=INSTRUCTIONS)

server = agents.AgentServer()

@server.rtc_session(agent_name="voice-assistant")
async def voice_session(ctx: agents.JobContext):
    session = AgentSession(
        stt=openai.STT(model="gpt-4o-mini-transcribe"),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=openai.TTS(model="tts-1", voice="alloy"),
        vad=silero.VAD.load(),
    )
    await session.start(
        room=ctx.room,
        agent=VoiceAssistant(),
        room_input_options=RoomInputOptions(),
    )
    await session.generate_reply(instructions="Greet the user briefly and ask how you can help.")

if __name__ == "__main__":
    agents.cli.run_app(server)
