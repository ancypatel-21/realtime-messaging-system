import queue
import time
import threading

from producer import producer
from worker import worker
from metrics import Metrics

message_queue = queue.Queue()
metrics = Metrics()

start_time = time.time()

producers = [
    threading.Thread(target=producer, args=("A", 5, message_queue)),
    threading.Thread(target=producer, args=("B", 5, message_queue)),
]

workers = [
    threading.Thread(target=worker, args=("1", message_queue, metrics)),
    threading.Thread(target=worker, args=("2", message_queue, metrics)),
]

for p in producers:
    p.start()

for w in workers:
    w.start()

for p in producers:
    p.join()

message_queue.join()

end_time = time.time()
total_time = end_time - start_time
summary = metrics.summary(total_time)

print("\n=== Metrics Summary ===")
print(f"Total messages processed: {summary['total_messages']}")
print(f"Average queue latency: {summary['avg_latency']:.4f}s")
print(f"Average processing time: {summary['avg_processing']:.4f}s")
print(f"Throughput: {summary['throughput']:.2f} messages/sec")
print("All messages processed!")