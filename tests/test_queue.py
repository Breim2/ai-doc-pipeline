# tests/test_queue.py
import asyncio
import pytest
from app.utils.queue_manager import JobQueue

@pytest.mark.asyncio
async def test_jobqueue_enqueue_and_process():
    queue = JobQueue()
    results = []

    async def dummy_processor(job_id, file_path):
        results.append((job_id, file_path))

    # Add jobs
    await queue.add_job("job1", "file1.jpg")
    await queue.add_job("job2", "file2.jpg")

    # Run queue processor
    processor_task = asyncio.create_task(queue.start(dummy_processor))

    # Wait for processing
    await processor_task

    # Assert both jobs were processed
    assert len(results) == 2
    assert results == [("job1", "file1.jpg"), ("job2", "file2.jpg")]
