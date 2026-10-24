import json, sys
from client import RealtimeVoiceVadSilenceTrimmerClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "vad-silence-trimmer", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "trim_speech_silence", "description": "Detects speech boundaries and trims silence to reduce voice agent latency."}]}}
    elif method == "tools/call":
        client = RealtimeVoiceVadSilenceTrimmerClient()
        res = client.trim_speech_silence()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = RealtimeVoiceVadSilenceTrimmerClient()
        print(json.dumps(client.trim_speech_silence(), indent=2))
