from firebase_config import db

def store_output(session_id, agent_name, output):
    doc_ref = db.collection("sessions").document(session_id)
    doc_ref.set({f"{agent_name}_output": output}, merge=True)

def retrieve_output(session_id, agent_name):
    doc_ref = db.collection("sessions").document(session_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict().get(f"{agent_name}_output", {})
    return {}
