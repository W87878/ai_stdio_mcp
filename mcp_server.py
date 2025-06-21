from mcp.server.fastmcp import FastMCP
import logging
import uvicorn
import json

# 配置日誌記錄器
logging.basicConfig(
    level=logging.INFO, # 設置日誌級別 INFO
    format='%(asctime)s - %(levelname)s - %(message)s' # 日誌格式
)

logger = logging.getLogger(__name__)

mcp = FastMCP("mcp Server", version="1.0.0")

@mcp.tool()
async def add(a: float, b: float) -> float:
    """Add two numbers."""
    logger.info(f"The add method is called: a={a}, b={b}")
    return a + b

@mcp.tool()
async def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    logger.info(f"The multiply method is called: a={a}, b={b}")
    return a * b

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather information for a specific location."""
    logger.info(f"The get_weather method is called: location={location}")
    # Simulate fetching weather data
    weather_data = {
        "location": location,
        "temperature": "22°C",
        "condition": "Sunny"
    }
    return json.dumps(weather_data)  # ✅ 回傳字串



if __name__ == "__main__":
    logging.info("Starting MCP Server") # 紀錄伺服器啟動日誌
    mcp.run(transport="stdio")  # 使用標準輸入輸出啟動伺服器
