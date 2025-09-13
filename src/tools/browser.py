from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser
from src.config import Config


def get_browser_tools():
    """Initialize and return Playwright browser tools."""
    async_browser = create_async_playwright_browser(headless=Config.HEADLESS_MODE)
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
    return toolkit.get_tools()
