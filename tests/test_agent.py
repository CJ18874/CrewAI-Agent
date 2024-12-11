# Write tests for your agent.

import unittest
from crewai.agent import CrewAIAgent
from app import app

class TestCrewAIAgent(unittest.TestCase):
    def setUp(self):
        """
        Set up resources before each test.
        """
        self.agent = CrewAIAgent()

    def test_analyze_success(self):
        """
        Test that the analyze method returns a success response.
        """
        input_data = {"sample_input": "test data"}
        result = self.agent.analyze(input_data)
        self.assertEqual(result["status"], "success")
        self.assertIn("data", result)

    def test_analyze_empty_input(self):
        """
        Test that the analyze method handles empty input gracefully.
        """
        input_data = {}
        result = self.agent.analyze(input_data)
        self.assertEqual(result["status"], "success")  # Adjust if failure is expected
        self.assertIn("data", result)

class TestCrewAIAgentAPI(unittest.TestCase):
    def setUp(self):
        """
        Set up Flask app for testing.
        """
        self.app = app.test_client()
        self.app.testing = True

    def test_analyze_endpoint_success(self):
        """
        Test the /analyze API endpoint with valid input.
        """
        input_data = {"data": "test input"}
        response = self.app.post("/analyze", json=input_data)
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertEqual(response_data["status"], "success")
        self.assertIn("data", response_data)

    def test_analyze_endpoint_missing_input(self):
        """
        Test the /analyze API endpoint with missing input.
        """
        response = self.app.post("/analyze", json={})
        self.assertEqual(response.status_code, 200)  # Adjust based on how you handle empty input
        response_data = response.get_json()
        self.assertEqual(response_data["status"], "success")  # Adjust if failure is expected
        self.assertIn("data", response_data)

    def test_analyze_endpoint_invalid_method(self):
        """
        Test the /analyze endpoint with an invalid HTTP method.
        """
        response = self.app.get("/analyze")  # GET is not allowed; only POST should work
        self.assertEqual(response.status_code, 405)  # Method Not Allowed

if __name__ == "__main__":
    unittest.main()
