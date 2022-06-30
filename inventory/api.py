from controller import controller

def api():
    response = {
        "msg": "Hi this is the api for the inventory",
        "code": 200
    }
    controller()
    print(response)


if __name__ == "__main__":
    api()