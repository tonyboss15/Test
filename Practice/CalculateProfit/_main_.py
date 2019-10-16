import numpy as np
from .dict import cost_dict

def profit(cost_dict):
    return (cost_dict[sell_price]-cost_dict[cost_price])/cost_dict[inventory]
