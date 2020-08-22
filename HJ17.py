# -*- coding: utf-8 -*-

# Note: a = int("1A") this will trigger the ValueError

import os, sys

if __name__ == "__main__":
    moves = input().strip().split(";")
    
    x, y, dist = 0, 0, 0
    for move in moves:
        if len(move) and move[0] not in ["A", "D", "S", "W"]: continue
        try: dist = int(move[1:])
        except: continue
            
        if move[0] == "A":   x -= dist
        elif move[0] == "D": x += dist
        elif move[0] == "W": y += dist
        else: y -= dist
        
    print(x, ",", y, sep="")
            