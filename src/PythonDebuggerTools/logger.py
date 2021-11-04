import inspect

class Debug:
    def logger(self, important_params=None, output_file=None):
        def wrapper(func):
            def inner(*args, **kwargs):
                values = [arg for arg in args]
                params = inspect.getfullargspec(func)[0]
                result = func(*args, **kwargs)

                curframe = inspect.currentframe()
                calframe = inspect.getouterframes(curframe, 2)
                output_line = ""

                if important_params:
                    param_list = []
                    if important_params:
                        for param in important_params:
                            for i, p in enumerate(params):
                                if str(p) == param:
                                    param_list.append(str(param + "=" + str(values[i])))
                    param_list = ', '.join(param_list)
                    output_line = "Executing function: [" + func.__name__ + "] Called by: [" + calframe[1][3] + "] Selected Args: " + param_list + " - Result: " + str(result)
                else:
                    output_line = "Executing function: [" + func.__name__ + "] Called by: [" + calframe[1][3] + "]" + "- Result: " + str(result)
                
                if self.DEBUG:
                    print(output_line)
                
                return result
            return inner
        return wrapper

class Log:    
    def __init__(self):
        self.DEBUG = True

    def log(self, *args):
        if self.DEBUG:
            output_line = ' '.join([str(arg) for arg in args])
            print(output_line)