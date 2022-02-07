#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    # Implement the VendingMachine here
    item_coins = 0
    num_items = 0
    
    def __init__(self, num_items, item_coins):
        self.num_items = num_items
        self.item_coins = item_coins
    
    def buy(self, num_items, num_coins):
        total = 0;
        balance = 0
        if(num_items > self.num_items):
            return 'Not enough items in the machine'
        
        total = self.item_coins * num_items
        if(num_coins < total):
            return 'Not enough coins'
        
        if(self.num_items >= num_items):
            balance =  num_coins - total
            self.num_items -= num_items
            return balance
        
        
    
    pass
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()
