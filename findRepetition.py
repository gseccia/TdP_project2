import os
import hashlib


def find_repetition(dir: str):
    SHAbuckets = {}
    for file in os.listdir(dir):
        f = open(dir + "/" + file, "rb")
        sha = hashlib.sha256(f.read())
        sha = sha.hexdigest()
        f.close()
        if SHAbuckets.get(sha) is None:
            SHAbuckets[sha] = []
        SHAbuckets.get(sha).append(f.name)
    file_replied = []
    for bucket in SHAbuckets:
        if len(SHAbuckets[bucket]) > 1:
            file_replied.append(SHAbuckets[bucket])
    return file_replied


print(find_repetition('./tests/copy'))
