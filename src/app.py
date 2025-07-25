from main import run_wedding_demo, run_fitness_demo, run_career_demo
from flask_cors import CORS
from flask import Flask, request, jsonify
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))


app = Flask(__name__)
CORS(app)


@app.route('/run-demo', methods=['POST'])
def handle_demo():
    data = request.get_json()
    choice = data.get('choice')
    results_data = {}

    # The print statements will still appear in your console, which is great for debugging
    if choice == '1':
        results_data = run_wedding_demo()
    elif choice == '2':
        results_data = run_fitness_demo()
    elif choice == '3':
        results_data = run_career_demo()
    else:
        return jsonify({"status": "error", "message": "Invalid choice"}), 400

    # We now embed the returned dictionary into our JSON response under the "results" key
    return jsonify({"status": "success", "results": results_data})


if __name__ == '__main__':
    app.run(port=5001, debug=True)
