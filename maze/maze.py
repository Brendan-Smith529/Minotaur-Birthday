import multiprocessing as mp, time

# Solution
# Chosen One:
#   Everytime you see a missing cupcake: increment by 1
#   Whenever you don't: do nothing
#   Eat cupcake during first run (req if needed), don't afterwards
#
# Not Chosen:
#   If you see a cupcake missing: do not eat even if you haven't eaten
#   If cupcake is there:
#       If you have eaten: leave
#       If you have not eaten: eat the cupcake; don't replace afterwards

N_THREADS = 100


# If the cupcake isn't there and this guest hasn't eaten they will:
# have it replaced, eat it, then replace it again. Omitting unnecessary computation
def chosen_maze(lock, cupcake_there, complete):
    num_empty = 0

    # This user eats cupcake on their first attempt as their replacement doesn't matter
    while not complete.value:
        with lock:
            if not cupcake_there.value:
                num_empty += 1
                cupcake_there.value = True

            if num_empty == N_THREADS - 1:
                complete.value = True

def regular_maze(lock, cupcake_there, complete):
    eaten = False

    while not complete.value:
        with lock:
            if not eaten and cupcake_there.value:
                eaten = True
                cupcake_there.value = False

if __name__ == "__main__":
    threads = []

    start_time = time.time()

    with mp.Manager() as manager:
        cupcake_there = manager.Value('b', True)
        complete = manager.Value('b', False)
        lock = manager.Lock()

        # Spawns thread for guest chosen to count
        chosen_guest = mp.Process(target=chosen_maze, args=(lock, cupcake_there, complete))
        chosen_guest.start()
        threads.append(chosen_guest)

        # Spawns regular guest threads and starts them
        for _ in range(1, N_THREADS):
            thread = mp.Process(target=regular_maze, args=(lock, cupcake_there, complete))
            thread.start()
            threads.append(thread)

        # Joins threads
        for thread in threads:
            thread.join()

    elapsed_time = time.time() - start_time
    print(f'Maze complete in {elapsed_time:.2f} seconds')

