import os
import redis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
redis_client = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

def cache_get(key):
    return redis_client.get(key)

def cache_set(key, value, ex=300):
    redis_client.set(key, value, ex=ex)
