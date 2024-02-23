import multiprocessing as mp
import random, time

N_THREADS = 10

# Has the guests enter and look at vase
def enter(lock, available, seen):
    while not seen:
        with lock:
            if available:
                available.value = False
                seen = True

    # Minor amount of buffer time to somewhat simulate guest looking time
    # Can add time here if desired to do a more accurate simulation
    with available.get_lock():
        available.value = True

if __name__ == "__main__":
    threads = []

    start_time = time.time()

    with mp.Manager() as manager:
        available = mp.Value('b', True)
        lock = manager.Lock()

        # Spawns guest threads and starts them
        for _ in range(0, N_THREADS):
            seen = random.random() < 0.25 # 75% chance guest wants to see
            thread = mp.Process(target=enter, args=(lock, available, seen))
            thread.start()
            threads.append(thread)

        # Joins threads
        for thread in threads:
            thread.join()

    elapsed_time = time.time() - start_time
    print(f'All guests have viewed the vase in {elapsed_time:.2f} seconds')

