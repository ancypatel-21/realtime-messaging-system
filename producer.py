import time
import random

def create_message(msg_id):
    return {
        "id": msg_id,
        "created_at": time.time()
    }

def producer(name, count, message_queue):
    for i in range(count):
        msg = create_message(f"{name}-{i}")
        message_queue.put(msg)
        print(f"[Producer {name}] Produced {msg['id']}")
        time.sleep(random.uniform(0.05, 0.2))