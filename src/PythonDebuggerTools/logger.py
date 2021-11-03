import inspect

def logger(important_params=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            values = [arg for arg in args]
            params = inspect.getfullargspec(func)[0]
            result = func(*args, **kwargs)

            curframe = inspect.currentframe()
            calframe = inspect.getouterframes(curframe, 2)
            
            if important_params:
                param_list = []
                if important_params:
                    for param in important_params:
                        for i, p in enumerate(params):
                            if str(p) == param:
                                param_list.append(str(param + "=" + str(values[i])))
                param_list = ', '.join(param_list)
                print("Executing function: [" + func.__name__ + "] Called by: [" + calframe[1][3] + "] Selected Args: " + param_list + " - Result: " + str(result))
            else:
                print("Executing function: [" + func.__name__ + "] Called by: [" + calframe[1][3] + "]" + "- Result: " + str(result))
            return result
        return inner
    return wrapper