import json
from getpass import getpass

def main():
    print("=== Minecraft Discord Botu Kurulum ===")
    token = getpass("Discord Bot Token: ")
    prefix = input("Komut prefix (örn !): ") or "!"
    guild_id = input("Minecraft sunucu ID (örn 1234567890): ") or ""
    config = {"token": token, "prefix": prefix, "guild_id": guild_id}

    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    print("\nKurulum tamamlandı. `python bot.py` ile botu başlatabilirsiniz.")

if __name__ == "__main__":
    main()
