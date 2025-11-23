from google.adk.agents import Agent
from google.adk.tools import google_search
root_agent = Agent(
    name = "ai_news_google_search_agent",
    model = "gemini-2.5-flash-native-audio-preview-09-2025",
    instruction = "You are an AI News Assistant. Use Google Search to find recent AI News.",
    tools = [google_search]
)