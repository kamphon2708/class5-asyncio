#solution
# Tue Aug  8 23:18:59 2023 hello 1 started
# Tue Aug  8 23:18:59 2023 hello 2 started
# Tue Aug  8 23:19:03 2023 hello 1 done
# Tue Aug  8 23:19:03 2023 hello 2 done
# Time: 4.01 sec

import asyncio
import time


async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")


async def main():
    task1 = asyncio.create_task(hello(1)) 

    task2 = asyncio.create_task(hello(2))
    await task1
    await task2


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')