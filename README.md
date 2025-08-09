# Discord Bot Template

This repository contains a modular Discord bot built with `discord.py` 2.0+. The project features a structured layout with cogs, a SQLite database using SQLAlchemy, an APScheduler instance for background tasks, and a tiny aiohttp web server for health checks.

## Features
- Slash command only design
- Configurable via `config.yaml` and `.env`
- SQLite database with migrations
- Background scheduler
- Health check and metrics endpoints
- Example cogs for future expansion

## Setup
1. Clone the repository and enter the folder.
2. Copy `.env.example` to `.env` and fill in your `DISCORD_TOKEN` and optional `TEST_GUILD_ID`.
3. Copy `config.example.yaml` to `config.yaml` and adjust settings.
4. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
   pip install -r requirements.txt
   ```
5. Enable the required privileged intents (members and message content if needed) in the [Discord Developer Portal](https://discord.com/developers/applications).
6. Run the bot:
   ```bash
   python main.py
   ```

### Scripts
- `run.sh` – convenience launcher for Unix systems.
- `run.ps1` – convenience launcher for Windows PowerShell.

## Healthcheck
An aiohttp web server exposes two endpoints:
- `/healthz` – returns `{"status": "ok"}`
- `/metrics` – returns simple metrics like uptime and guild count

## Troubleshooting
- Ensure all intents are enabled in the Developer Portal.
- If commands do not appear, verify `TEST_GUILD_ID` or wait for global sync (up to 1 hour).
- Check the `logs/` directory for detailed log output.

This template is a starting point; extend the cogs to add real functionality.
