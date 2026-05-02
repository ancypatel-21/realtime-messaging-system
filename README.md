# Real-Time Messaging System with Latency & Throughput Analysis

## Overview

This project simulates a real-time messaging pipeline similar to communication systems (e.g., Twilio). It models how messages are produced, queued, and processed concurrently while measuring latency and throughput.

---

## Features

* Multiple producers generating messages concurrently
* Multiple workers processing messages in parallel
* Queue latency tracking
* Processing time measurement
* Throughput calculation (messages/sec)
* Modular design (producer, worker, metrics)

---

## Project Structure

```
realtime-messaging-system/
│── main.py
│── producer.py
│── worker.py
│── metrics.py
│── README.md
```

---

## How It Works

### Message Production

Producers simulate incoming messages. Each message contains:

* `id`
* `created_at` timestamp

Messages are pushed into a shared queue.

---

### Queue System

A thread-safe queue (`queue.Queue`) acts as a buffer between producers and workers.

---

### Concurrent Processing

Workers:

* Pull messages from the queue
* Process them with simulated delays
* Record latency and processing time

---

### Metrics

The system tracks:

* Queue latency = processing start − creation time
* Processing time per message
* Throughput = total messages / total execution time

---

## Run the Project

```
python3 main.py
```

---

## Sample Output

```
[Producer A] Produced A-0
[Worker 1] Processing A-0 | Queue delay: 0.0021s

=== Metrics Summary ===
Total messages processed: 10
Average queue latency: 0.0431s
Average processing time: 0.1824s
Throughput: 7.85 messages/sec
All messages processed!
```

---

## Key Learnings

* Producer-consumer architecture using threads
* Real-time event processing concepts
* Measuring system performance (latency and throughput)
* Basics of distributed messaging systems

---

## Tech Stack

* Python
* threading
* queue
* time

---

## Future Improvements

* Message prioritization
* Failure handling and retry logic
* Integration with Redis/Kafka
* Metrics visualization

---

## Author

Ancy Patel
