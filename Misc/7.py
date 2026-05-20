# multiprocessing examples
import multiprocessing
import time


def task(name):
    # This function will run inside a separate process.
    print(f"{name} started")
    time.sleep(2)  # imagine this is some slow work
    print(f"{name} finished")


def square(n):
    # This function is used by Pool to calculate many values in parallel.
    return n * n


if __name__ == "__main__":
    # This line is important for multiprocessing.
    # It prevents child processes from creating more child processes again.

    print("Example 1: Creating processes manually")

    # Create two separate processes.
    # target=task means each process will run the task function.
    # args=("Process 1",) passes one argument to the task function.
    process1 = multiprocessing.Process(target=task, args=("Process 1",))
    process2 = multiprocessing.Process(target=task, args=("Process 2",))

    # start() begins running the processes.
    process1.start()
    process2.start()

    # join() waits until each process finishes.
    process1.join()
    process2.join()

    print("Both manual processes finished\n")

    print("Example 2: Using multiprocessing.Pool")

    numbers = [1, 2, 3, 4, 5]

    # Pool creates a group of worker processes.
    # pool.map(square, numbers) applies square() to every number.
    with multiprocessing.Pool() as pool:
        results = pool.map(square, numbers)

    print("Original numbers:", numbers)
    print("Squared numbers:", results)
