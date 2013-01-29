import redis


class RedisHelp:
    """
    use the redis
    """
    def __init__(self, hosts=None):
        if hosts == None:
            self.hosts = "127.0.0.1"
        else:
            self.hosts = hosts
        self._r = redis.Redis(host=self.hosts)
            
    def set(self, key, value):
        self._r.set(key, value)

    def get(self, key):
        self._r.get(key)

