# app/utils/queue_manager.py

import asyncio
from collections import deque
from app.utils.logger import get_logger

logger = get_logger("queue")

class JobQueue:
    def __init__(self):
        self.queue = deque()
        self.processing = False

    async def add_job(self, job_id: str, file_path: str):
        """Add a job to the queue asynchronously."""
        self.queue.append((job_id, file_path))
        logger.info(f"Queued job: {job_id} (file: {file_path})")

    async def start(self, processor_func):
        """Start processing jobs in the queue using the given async processor function."""
        if self.processing:
            return
        self.processing = True
        while self.queue:
            job_id, file_path = self.queue.popleft()
            logger.info(f"→ START job {job_id}")
            await processor_func(job_id, file_path)
            logger.info(f"✓ DONE job {job_id}")
        self.processing = False
