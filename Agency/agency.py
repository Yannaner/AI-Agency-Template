from agency_swarm import Agency
from Agent_1 import ContentManager
from Agent_2 import TrendAnalyzer

from agency_swarm.util import set_openai_key
import os
from dotenv import load_dotenv
load_dotenv()

set_openai_key(os.getenv("OPENAI_API_KEY"))

content_manager = ContentManager()
trend_analyzer = TrendAnalyzer()

# Create agency with communication flows
agency = Agency(
    [
        content_manager,  # Content Manager is the entry point
        [content_manager, trend_analyzer],  # Content Manager can communicate with Trend Analyzer

    ],
    shared_instructions="agency_shared_instruction.md",
    temperature=0.7,
    max_prompt_tokens=4000
)

if __name__ == "__main__":
    agency.run_demo() 