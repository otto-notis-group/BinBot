import random
import processer
import csv
from typing import Callable
from typing import Any
from botpy import logging

_log = logging.get_logger()

def record(func:Callable,*args:Any):
    "记录器"
    #open()
    try:
        return func(*args)
    except Exception as e:
        return(f"错误：{e}")
@record
def ture_music_random_select():
    "神曲选择器"
    csvfile = "./ture_music_list.csv"
    reader = list(csv.reader(open(csvfile)))
    random_result = random.choice(reader)
    return " : ".join(random_result[1:])
@record
def random_num(min:int,max:int):
    "哈人随机"
    if min < max:
        if min<8000 and max >9000:
            return random.randint(min,max) if round(random.uniform(0.0,1.0),2) != 0.24 else 9000 - 17*2
        return random.randint(min,max)
    raise SyntaxError("The Min is Bigger than Max.")
@record
def is_that_ao():
    "I make Touhou otomad, is that okay?"
    yes_or_no = ["不！我无法忍受你的行为","ao"]
    return random.choice(yes_or_no)