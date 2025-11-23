from google.adk.agents import Agent
from google.adk.tools import google_search
root_agent = Agent(
    name = "ai_news_google_search_text_agent",
    model = "gemini-3-pro-preview",
    instruction = "You are an AI News Assistant. Use Google Search to find and summarize recent AI News.",
    tools = [google_search]
)