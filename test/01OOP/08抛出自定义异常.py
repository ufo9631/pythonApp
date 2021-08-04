class ShortInputException(Exception):
    #自定义异常类
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


try:
    raise ShortInputException("sdf","自定义异常") #raise主动抛出异常

except ShortInputException:
    print("抛出自定义异常")
