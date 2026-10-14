import React, { useRef, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { Room, RoomEvent } from 'livekit-client';
import './style.css';

function App() {
  const [status, setStatus] = useState('Disconnected');
  const [error, setError] = useState('');
  const [connected, setConnected] = useState(false);
  const roomRef = useRef(null);
  const audioRef = useRef(null);
  const [muted, setMuted] = useState(false);

  async function start() {
    setError(''); setStatus('Requesting session...');
    try {
      const res = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/session`, {method: 'POST'});
      if (!res.ok) throw new Error(`Session request failed (${res.status})`);
      const { serverUrl, token } = await res.json();
      const room = new Room({adaptiveStream: true, dynacast: true});
      roomRef.current = room;
      room.on(RoomEvent.Disconnected, () => {setConnected(false); setStatus('Disconnected');});
      room.on(RoomEvent.TrackSubscribed, (track) => {
        if (track.kind === 'audio') {
          const el = track.attach();
          el.autoplay = true;
          document.body.appendChild(el);
        }
      });
      room.on(RoomEvent.TrackUnsubscribed, track => track.detach().forEach(el => el.remove()));
      await room.connect(serverUrl, token);
      await room.localParticipant.setMicrophoneEnabled(true);
      setMuted(false); setConnected(true); setStatus('Connected — speak now');
    } catch (e) {
      setError(e.message || 'Unable to connect');
      setStatus('Disconnected');
      roomRef.current?.disconnect(); roomRef.current = null;
    }
  }
  async function toggleMic() {
    if (!roomRef.current) return;
    const next = !muted;
    await roomRef.current.localParticipant.setMicrophoneEnabled(!next);
    setMuted(next);
  }
  function stop() {
    roomRef.current?.disconnect(); roomRef.current = null;
    document.querySelectorAll('audio').forEach(el => el.remove());
    setConnected(false); setStatus('Disconnected');
  }
  return <main className="shell">
    <div className="orb">🎙</div>
    <h1>AI Voice Assistant</h1>
    <p>Have a natural voice conversation powered by OpenAI and LiveKit.</p>
    <div className="status">{status}</div>
    {error && <p className="error" role="alert">{error}</p>}
    <div className="actions">
      {!connected ? <button onClick={start}>Start conversation</button> : <>
        <button onClick={toggleMic}>{muted ? 'Unmute microphone' : 'Mute microphone'}</button>
        <button className="stop" onClick={stop}>End conversation</button>
      </>}
    </div>
    <small>Allow microphone access when your browser asks. Use headphones to avoid echo.</small>
  </main>;
}

createRoot(document.getElementById('root')).render(<App/>);
