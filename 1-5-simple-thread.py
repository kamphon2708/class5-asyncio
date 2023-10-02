#solution
# Task A: Computing 0+1
# Time: 0.00Task B: Computing 0+1

# Time: 0.01
# Task B: Computing 1+2
# Task A: Computing 1+2
# Time: 1.02
# Time: 1.02
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.04
# Task B: Sum = 6

# Time: 3.06 sec

import asyncio
import time
from concurrent.futures.thread import ThreadPoolExecutor

def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

async def sum(name, numbers):
    _executor = ThreadPoolExecutor(2)
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await loop.run_in_executor(_executor, sleep)
        total += number

    print(f'Task {name}: Sum = {total}\n')

start = time.time()

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')