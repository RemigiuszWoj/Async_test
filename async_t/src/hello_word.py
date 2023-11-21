#!/usr/bin/env python3

import asyncio
import time


async def main() -> None:
    print(f"{time.ctime()} Siema!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Elo!")


asyncio.run(main())
