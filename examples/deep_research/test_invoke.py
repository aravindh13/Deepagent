import asyncio
import os
from agent import agent

async def main():
    try:
        async for event in agent.astream({"messages": [("user", "What is the capital of France?")]}):
            print(event)
    except Exception as e:
        import traceback
        traceback.print_exc()

asyncio.run(main())
