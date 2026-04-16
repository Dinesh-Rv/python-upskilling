import asyncio
import time

async def fetch_data(source, delay):
    print(f"Fetching from {source}...")
    await asyncio.sleep(delay)
    print(f"{source} data ready!")
    return f"{source} data"

async def main():
    start = time.time()

    db, cache, api = await asyncio.gather(
        fetch_data("Database", 2),
        fetch_data("Cache", 0.5),
        fetch_data("API", 1)
    )

    total = time.time() - start
    print(f"\nResults: {db}, {cache}, {api}")
    print(f"Total async Time: {total:.2f} seconds")
    print(f"Sequential would take: {2 + 0.5 + 1.5} seconds")

asyncio.run(main())

