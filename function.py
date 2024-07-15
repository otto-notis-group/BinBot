import random
from types import Callable
from typing import Any
key: str = open("key.txt").read()
def send_msg(text:str)
    "操你妈不会写"
    raise NotImplementedError
def record(func:Callable,*args:Any):
    "记录器"
    #open()
    try:
        return func(*args)
    except Exception as e:
        send_msg(f"错误{e}")
@record
def random_num(min:int,max:int):
    "哈人随机"
    if min < max:
        if min<8000 and max >9000:
            return random.randint(min,max) if round(random.uniform(0.0,1.0),2) != 0.24 else 9000 - 17*2
        return random.randint(min,max)
    raise SyntaxError
@record
def ture_misuc_random_select():
    "神曲选择器"
    song="Speculation (https://b23.tv/lGN2FVp)","THE CANNONBALLER (https://b23.tv/HJNhBTV)"
    return random.choice(song)
