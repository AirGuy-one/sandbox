import asyncio
import os
import sys


async def another_function() -> str:
    return 'another func'

async def my_function():
    print("Start")
    await another_function()
    print("End")

coroutine1 = my_function()
print(coroutine1)
print(sys.argv)
print(sys.stdin, sys.stdout)
print(os.path)
str()
