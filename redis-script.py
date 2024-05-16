import redis


def connect_to_redis(host='localhost', port=6379, db=0):
    try:
        client = redis.Redis(host=host, port=port, db=db)
        client.ping()
        print("Connected to Redis")

        return client
    except redis.ConnectionError as e:
        print(f"Could not connect to Redis: {e}")
        return None


def main():
    client = connect_to_redis()

    if client:
        client.set('my_key', 'Hello, Redis!')

        value = client.get('my_key')
        print(f"Value for 'my_key': {value.decode('utf-8')}")


if __name__ == "__main__":
    main()
