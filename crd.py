import sys
import time

json = {}


def create(key, name, phone_no, timeout=0):
    if key not in json:
        if len(json) < (1024 * 1020 * 1024) and sys.getsizeof(name) + sys.getsizeof(phone_no) <= (16 * 1024 * 1024):
            if timeout == 0:
                l = [name, phone_no, timeout]
            else:
                l = [name, phone_no, time.time() + timeout]
            if len(key) <= 32:
                json[key] = l
                print("successfully created")
        else:
            print("error: Memory limit exceeded!! ")

    else:
        print("error: this key already exists")


def read(key):
    if key not in json:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b = json[key]
        if b[2] != 0:
            if time.time() < b[2]:
                string = "{" + "Name" + ":" + str(b[0]) + "," + "Phoneno" + ":" + str(
                    b[1]) + "}"
                return string
            else:
                print("error: time-to-live of", key, "has expired")
        else:
            string = "{" + "Name" + ":" + str(b[0]) + "," + "Phoneno" + ":" + str(b[1]) + "}"
            return string


def delete(key):
    if key not in json:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b = json[key]
        if b[2] != 0:
            if time.time() < b[2]:
                del json[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of", key, "has expired")
        else:
            del json[key]
            print("key is successfully deleted")