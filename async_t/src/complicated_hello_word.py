#!/usr/bin/env python3

import asyncio
import time


async def main() -> None:
    print(f"{time.ctime()} Siema!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Elo!")


loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_until_complete(task)

pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
