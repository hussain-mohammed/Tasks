def checking_the_multiple(index):
    def validator(func):
        def wrapper(*args, **kwargs):
            if args[index] > 0:
                return func(*args, **kwargs)
            raise ValueError(f'Argument {index} must be non-negative')
        return wrapper
    return validator


@checking_the_multiple(1)
def multiple_string(string, multiple):
    return string * multiple

#
# print(multiple_string('ahmed', 10))