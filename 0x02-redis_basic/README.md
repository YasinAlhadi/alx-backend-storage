# 0x02. Redis basic
0. Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes, int or float.<br />
1. Reading from Redis and recovering original type. <br />
2. Incrementing values <br />
3. Storing lists <br />
4. Retrieving lists <br />