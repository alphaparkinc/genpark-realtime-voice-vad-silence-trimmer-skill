import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import RealtimeVoiceVadSilenceTrimmerClient

def main():
    client = RealtimeVoiceVadSilenceTrimmerClient()
    res = client.trim_speech_silence()
    print("=== Realtime Voice VAD Silence Trimmer Output ===")
    print(f"Speech Detected: {res['speech_detected']} | Peak Energy: {res['clean_speech_energy_peak']}")
    print(f"Frames: {res['original_frames_count']} -> {res['trimmed_frames_count']} (Latency Saved: {res['total_latency_saved_ms']}ms)")
    print(f"STT Payload Reduction: {res['stt_payload_reduction_pct']}")

if __name__ == '__main__':
    main()
