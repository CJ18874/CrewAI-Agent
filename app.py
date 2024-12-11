# Entry point for running the application (e.g., Flask server).

from flask import Flask, request, jsonify
from crewai.agent import CrewAIAgent

app = Flask(__name__)
agent = CrewAIAgent()

@app.route("/analyze", methods=["POST"])
def analyze():
    input_data = request.json
    response = agent.analyze(input_data)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
