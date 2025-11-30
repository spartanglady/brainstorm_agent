import unittest
from unittest.mock import MagicMock, patch
import os
os.environ["GOOGLE_API_KEY"] = "TEST_KEY"

from brainstormer_agent.agent import InteractiveBrainstormerAgent
from brainstormer_agent.sub_agents.facilitator import MethodDecision

class TestInteractiveBrainstormerAgent(unittest.TestCase):
    @patch('brainstormer_agent.agent.ResearcherAgent')
    @patch('brainstormer_agent.agent.FacilitatorAgent')
    @patch('brainstormer_agent.agent.SpecialistAgent')
    def test_run_flow(self, MockSpecialist, MockFacilitator, MockResearcher):
        # Setup Mocks
        mock_researcher = MockResearcher.return_value
        mock_researcher.run.return_value = "Mock Context Brief"
        
        mock_facilitator = MockFacilitator.return_value
        mock_facilitator.run.return_value = MethodDecision(method="SCAMPER", reasoning="Mock Reasoning")
        
        mock_specialist = MockSpecialist.return_value
        mock_specialist.run.return_value = "Mock Ideas"
        
        # Initialize Agent
        agent = InteractiveBrainstormerAgent()
        
        # Run Agent
        ideas, method = agent.run("Test Problem")
        
        # Assertions
        mock_researcher.run.assert_called_once_with("Test Problem")
        mock_facilitator.run.assert_called_once()
        mock_specialist.run.assert_called_once_with(method="SCAMPER", context="Mock Context Brief", problem="Test Problem")
        
        self.assertEqual(ideas, "Mock Ideas")
        self.assertEqual(method, "SCAMPER")

if __name__ == '__main__':
    unittest.main()
