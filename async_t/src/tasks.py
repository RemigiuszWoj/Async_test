#!/usr/bin/env python3

import asyncio

from contextlib import suppress

async def main(f: asyncio.Future):
    await asyncio.sleep(1)
    try:
        f.set_result("Zakonczone")
    except RuntimeError as e:
        print("nie dziala")
    f.cancel()

loop = asyncio.get_event_loop()
fut = asyncio.Task(asyncio.sleep(1_000_000))
print(fut.done())

loop.create_task(main(f=fut))

with suppress(asyncio.CancelledError):
    loop.run_until_complete(fut)

print(fut.done())

print(fut.cancelled())