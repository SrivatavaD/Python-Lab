# asyncio examples
import asyncio


async def say_hello():
    # async functions do not run immediately when called.
    # They return a coroutine, which must be awaited or scheduled.
    print("Example 1: Hello")
    await asyncio.sleep(1)  # pause this function for 1 second
    print("Example 1: Done\n")


async def task(name, seconds):
    # This function behaves like a task that takes some time.
    print(f"{name} started")
    await asyncio.sleep(seconds)  # while waiting, other async tasks can run
    print(f"{name} completed")


async def download_file(filename, seconds):
    # This example returns a value after waiting.
    print(f"Downloading {filename}...")
    await asyncio.sleep(seconds)
    return f"{filename} downloaded"


async def main():
    print("Running one async function with await")
    await say_hello()

    print("Running multiple tasks together using asyncio.gather")
    await asyncio.gather(
        task("task1", 4),
        task("task2", 2),
        task("task3", 1),
    )
    print()

    print("Collecting return values from async functions")
    results = await asyncio.gather(
        download_file("photo.png", 3),
        download_file("music.mp3", 2),
        download_file("notes.txt", 1),
    )
    print(results)
    print()

    print("Creating a task manually using asyncio.create_task")
    background_task = asyncio.create_task(task("background task", 2))

    # This line runs immediately after creating the task.
    # The background task is already running while this message prints.
    print("Main function is doing other work...")

    # We await the task later so the program waits for it to finish.
    await background_task


asyncio.run(main())
