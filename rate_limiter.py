import time

requests = {}

def check_rate_limit(client_ip):
    current_time = time.time()

    if client_ip not in requests:
        requests[client_ip] = []

    # keep only last 60 seconds
    requests[client_ip] = [
        t for t in requests[client_ip] if current_time - t < 60
    ]

    # max 5 requests per minute
    if len(requests[client_ip]) >= 5:
        return False

    requests[client_ip].append(current_time)
    return True