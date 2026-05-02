import threading

class Metrics:
    def __init__(self):
        self.latencies = []
        self.processing_times = []
        self.lock = threading.Lock()

    def record(self, latency, processing_time):
        with self.lock:
            self.latencies.append(latency)
            self.processing_times.append(processing_time)

    def summary(self, total_time):
        total_messages = len(self.latencies)
        avg_latency = sum(self.latencies) / total_messages if total_messages else 0
        avg_processing = sum(self.processing_times) / total_messages if total_messages else 0
        throughput = total_messages / total_time if total_time > 0 else 0

        return {
            "total_messages": total_messages,
            "avg_latency": avg_latency,
            "avg_processing": avg_processing,
            "throughput": throughput
        }