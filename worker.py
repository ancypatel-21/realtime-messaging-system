import time
import random
import queue as queue_module

def worker(name, message_queue, metrics):
    while True:
        try:
            msg = message_queue.get(timeout=2)

            start_process = time.time()
            queue_delay = start_process - msg["created_at"]

            print(f"[Worker {name}] Processing {msg['id']} | Queue delay: {queue_delay:.4f}s")
            time.sleep(random.uniform(0.1, 0.3))

            processing_time = time.time() - start_process
            metrics.record(queue_delay, processing_time)

            message_queue.task_done()

        except queue_module.Empty:
            break