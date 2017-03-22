import time
import json


def log_duration(function):

    def show_execution_time(*args, **kwargs):
        ts = time.time()
        result = function(*args, **kwargs)
        te = time.time()
        print('Time elapsed for function: {0} - {1:2.6f} sec'.format(function.__name__, te-ts))
        return result

    return show_execution_time


@log_duration
def test_list():
    return [i for i in range(10000)]


def to_json(function):

    def code_to_json(*args, **kwargs):
        if isinstance(function(*args, **kwargs), dict):
            return json.dumps(function(*args, **kwargs))
        else:
            return function(*args, **kwargs)
    return code_to_json


@to_json
def test_dict():
    return {"1":1, "2":2}


@to_json
def test_not_dict():
    return [1, 2, 3]


def ignore_exceptions(*exceptions):
    def decorator(function):
        def ignore_exception():
            try:
                function()
            except exceptions:
                return None
        return ignore_exception
    return decorator


@ignore_exceptions(ZeroDivisionError, TypeError)
def test_error():
    print(1/0)
    print("Lol")
    return 1


if __name__ == '__main__':
    print(test_list())

    testing_dictionary = test_dict()
    print(testing_dictionary)
    print(type(testing_dictionary))
    testing_not_dictionary = test_not_dict()
    print(testing_not_dictionary)
    print(type(testing_not_dictionary))

    print(test_error())