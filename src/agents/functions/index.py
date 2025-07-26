from flask import Flask, request, jsonify
from planner import plan
from executor import execute
from memory import store_output

app = Flask(__name__)

@app.route('/session-analyst', methods=['POST'])
def session_analyst():
    data = request.get_json()

    session_id = data.get("session_id")
    company_context = data.get("company_context")

    if not session_id or not company_context:
        return jsonify({"error": "Missing session_id or company_context"}), 400

    tasks = plan("session-analyst")
    results = {}

    for task in tasks:
        prompt = f"{task}\n\nCompany context:\n{company_context}"
        result = execute(prompt)
        results[task] = result

    store_output(session_id, "session-analyst", results)

    return jsonify({
        "status": "success",
        "agent": "session-analyst",
        "output": results
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
