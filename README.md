
# 🤖 Deep Research Agent (with FastAPI + MCP + Selenium + LLM)

本專案是一個整合多工具的生成式 AI 深度研究助手，透過 FastAPI 提供 MCP 工具註冊、Selenium 自動操作 NotebookLM、OpenAI API 生成結構化摘要，實現自動化的研究整合與分析。

---

## 📁 專案結構

```
.
├── mcp_server.py          # MCP 工具伺服器
├── mcp_client.py          # 啟動 LangGraph + MCP 多工具 Agent
├── .env                   # 儲存 OpenAI API Key（已被 .gitignore 忽略）
├── pyproject.toml
├── README.md              # 本說明文件
```

---

## 🧑‍💻 安裝方式（建議使用 [`uv`](https://github.com/astral-sh/uv)）

```bash
# 安裝依賴（建議使用 uv）
uv pip install -r pyproject.toml
# 或使用 install 命令
uv pip install .
# 或使用 requirements.txt（如果你有產生的話）
uv pip install -r requirements.txt
```

---

## 🚀 啟動方式

### 使用 uv run 啟動 MCP 服務

```bash
uv run mcp_client.py
```

---

## 🧠 功能說明

### ✅ MCP 工具列表（由 mcp_server.py 提供）

| 工具名稱       | 功能說明           | 範例 |
|----------------|--------------------|------|
| `add`          | 加總兩個數字       | `add(a=3, b=5) → 8` |
| `multiply`     | 相乘兩個數字       | `multiply(a=4, b=6) → 24` |
| `get_weather`  | 查詢地點的天氣     | `get_weather(location="Taipei") → {"location": "Taipei", "temperature": "22°C", "condition": "Sunny"}` |

---

## 🔐 .env 設定
建立 `.env` 檔案，內容如下：

```env
OPENAI_API_KEY=your_key_here
```

或直接在 CLI 中執行：
```bash
export OPENAI_API_KEY=your_key_here
```
---

## 📜 License

MIT License

## 聯絡作者
Steve Wang | 2025