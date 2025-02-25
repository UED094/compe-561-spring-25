def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


def check_access_token():
    def wrapper(func):
        def inner_wrapper():
            print("Checking access token")
            func()

        return inner_wrapper


@check_access_token
def make_request():
    print("Request is made")


make_request()
