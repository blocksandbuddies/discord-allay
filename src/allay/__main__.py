from __future__ import annotations

import sys
import os

import discord
import dotenv

from allay.bot import Allay


dotenv.load_dotenv()


def main() -> None:
    token = os.getenv("TOKEN")

    if not token:
        raise ValueError("TOKEN is missing")

    bot = Allay()

    try:
        bot.run(token)
        return
    except KeyboardInterrupt:
        return
    except Exception:
        raise


if __name__ == "__main__":
    main()
