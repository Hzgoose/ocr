# -*- coding: utf-8 -*-
import hashlib


# hash data with type sha256
def hash_file(file):
    h = hashlib.sha256()
    h.update(file)
    rs_hash = h.hexdigest()
    return rs_hash


# save file with path
def save_file(file, path):
    f = open(path, "wb")
    f.write(file)
    f.close()
    return 1

