from src.input import *
import os
from colorama import Fore, Back, Style
import time
from playsound import playsound
import math
from datetime import datetime, timedelta
import json

data = {}
with open('replays/replay.json') as json_file:
    data = json.load(json_file)

id = len(data)
data[id] = []

# ----------------------------------------------------------------------------------------------------------------------

class Building:
    def __init__(self, width, height, char, startr, startc):
        self.width = width
        self.height = height
        self.char = char
        self.alive = True

    def set_map(self, map):
        map.set_map(self.startr, self.startc, self.height, self.width, self.char)
        map.set_color(self.startr, self.startc, self.height, self.width, 1)
        map.set_attack_map(self.startr, self.startc, self.height, self.width, self)
    
    def attacked(self,damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
        # print("self.health:" + str(self.health))
        return self.health
    
    def attacked_color(self,damage):
        health = self.attacked(damage)
        if health>=self.heath_max/2:
            map.set_color(self.startr, self.startc, self.height, self.width, 1)
        elif health>=self.heath_max/5:
            map.set_color(self.startr, self.startc, self.height, self.width, 3)
        elif health>0:
            map.set_color(self.startr, self.startc, self.height, self.width, 4)
        else:
            map.set_color(self.startr, self.startc, self.height, self.width, 0)
            map.set_map(self.startr, self.startc, self.height, self.width, 0)
            map.set_attack_map(self.startr, self.startc, self.height, self.width, -1)
            self.alive = False
    


class Town(Building):
    def __init__(self, char, startr, startc):
        self.width = 3
        self.height = 4
        self.char = char
        self.startr = startr
        self.startc = startc
        self.health = 600
        self.heath_max = 600
        self.centre_c = startc + 1
        self.centre_r = startr + 1
        Building.__init__(self, self.width, self.height, char, startr, startc)


class Hut(Building):
    def __init__(self, char, startr, startc):
        self.width = 2
        self.height = 2
        self.char = char
        self.startr = startr
        self.startc = startc
        self.health = 100
        self.heath_max = 100
        self.centre_c = startc
        self.centre_r = startr
        Building.__init__(self, self.width, self.height, char, startr, startc)


class Wall(Building):
    def __init__(self, char, startr, startc):
        self.width = 1
        self.height = 1
        self.char = char
        self.startr = startr
        self.startc = startc
        self.centre_c = startc
        self.centre_r = startr
        self.health = 100
        self.heath_max = 100
        Building.__init__(self, self.width, self.height, char, startr, startc)


class Canon(Building):
    def __init__(self, char, startr, startc, damage):
        self.width = 2
        self.height = 1
        self.char = "C"
        self.startr = startr
        self.startc = startc
        self.range = 6
        self.damage = damage
        self.health = 500
        self.heath_max = 500
        self.centre_c = startc + 1
        self.centre_r = startr
        Building.__init__(self, self.width, self.height, char, startr, startc)

    def attack(self,map):
        if(self.alive):
            for y in range(self.startc -2, self.startc+2):
                for x in range(self.startr -2, self.startr+2):
                    if x>=0 and x<map.height and y>=0 and y<map.width:
                        if map.get_attack_map(x,y) != -1:
                            obj = map.get_attack_map(x,y)
                            if(obj.char == "K>" or obj.char == "B" or obj.char == "K^" or obj.char == "Kv" or obj.char == "<K" or obj.char == "A" or obj.char == "Q>" or obj.char == "Q^" or obj.char == "Qv" or obj.char == "<Q"):
                                # file = './src/canonshot.wav'
                                # os.system("afplay " + file)
                                # print("canon shot")
                                # print("damage: " + str(self.damage))
                                # print("obj health: " + str(obj.health))

                                obj.attacked(self.damage)
                    
class WizardTower(Building):
    def __init__(self, char, startr, startc, damage):
        self.width = 2
        self.height = 3
        self.char = char
        self.startr = startr
        self.startc = startc
        self.range = 6
        self.damage = damage
        self.health = 500
        self.heath_max = 500
        self.centre_c = startc + 1
        self.centre_r = startr
        Building.__init__(self, self.width, self.height, char, startr, startc)

    def attack(self,map):
        # print("wizard tower attack")

        if(self.alive):
            for y in range(self.startc -2, self.startc+4):
                for x in range(self.startr -2, self.startr+5):
                    if x>=0 and x<map.height and y>=0 and y<map.width:
                        if map.get_attack_map(x,y) != -1 and map.get_attack_map(x,y) != self:
                            obj = map.get_attack_map(x,y)
                            # ch = input()
                            # print("ola: " + str(obj))
                            # print("attacking!")
                            # print(obj.char +" "+ str(obj))
                            if(obj.char == "K>" or obj.char == "B" or obj.char == "K^" or obj.char == "Kv" or obj.char == "<K" or obj.char == "A" or obj.char == "✈" or obj.char == "Q>" or obj.char == "Q^" or obj.char == "Qv" or obj.char == "<Q"):
                                obj.attacked(self.damage)
                                # print(obj.char +" "+ str(obj))
                                # print("damage: " + str(obj.health))
                                for j in range(obj.curr_c -3, obj.curr_c +3):
                                    # print("j: " + str(j))
                                    # print(obj.char +" "+ str(obj))
                                    for i in range(obj.curr_r -3, obj.curr_r+3):
                                        # print(obj.char +" "+ str(obj))
                                        # print("i: " + str(i))
                                        if i>=0 and i<map.height and j>=0 and j<map.width:
                                            if map.get_attack_map(i,j) != -1:
                                                obj1 = map.get_attack_map(i,j)
                                                # print("exit1")
                                                if(obj1.char == "K>" or obj1.char == "B" or obj1.char == "K^" or obj1.char == "Kv" or obj1.char == "<K" or obj1.char == "A" or obj1.char == "✈" ):
                                                    obj1.attacked(self.damage)
                                                    # print(f"{obj1.char} {obj1.health}")
                            #                     print("exit2")
                            #                 print("exit3")
                            # print("exit4")
                        

# ----------------------------------------------------------------------------------------------------------------------
# Characters

class Character:

    def __init__(self, health, damage, startr, startc, char,speed):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.startr = startr
        self.startc = startc
        self.curr_c = startc
        self.curr_r = startr
        self.char = char
        self.alive = True
        self.head = 'd'
        self.heath_max = health
    
    def check_health(self):
        health = self.health
        if health>=self.heath_max/2:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 6)
        elif health>=self.heath_max/5:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 3)
        elif health>0:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 4)
        else:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 0)
            map.set_map(self.curr_r, self.curr_c, 1, 1, 0)
            map.set_attack_map(self.curr_r, self.curr_c, 1, 1, -1)
            self.alive = False

    def Kmove(self, direction, map):

        map.set_map(self.curr_r, self.curr_c, 1, 1, 0)
        map.set_color(self.curr_r, self.curr_c, 1, 1, 0)
        map.set_attack_map(self.curr_r, self.curr_c, 1, 1, -1)

        if direction == "w":
            if self.curr_r > 0 and map.map[self.curr_r - self.speed][self.curr_c] == 0:
                self.curr_r -= self.speed
                self.head = 'w'
                self.char = "K^"
        elif direction == "s"and self.curr_r < map.height - self.speed and map.map[self.curr_r + self.speed][self.curr_c] == 0:
                self.curr_r += self.speed
                self.head = 's'
                self.char = "Kv"
        elif direction == "a" and map.map[self.curr_r][self.curr_c - self.speed] == 0:
            if self.curr_c > 0:
                self.curr_c -= self.speed
                self.head = 'a'
                self.char = "<K"
        elif direction == "d" and self.curr_c < map.width - self.speed and map.map[self.curr_r][self.curr_c + self.speed] == 0:
                self.curr_c += self.speed
                self.head = 'd'
                self.char = "K>"
        
        map.set_map(self.curr_r, self.curr_c, 1, 1, self.char)
        self.check_health()
        map.set_attack_map(self.curr_r, self.curr_c, 1, 1, self)
    
    def Qmove(self, direction, map):

        map.set_map(self.curr_r, self.curr_c, 1, 1, 0)
        map.set_color(self.curr_r, self.curr_c, 1, 1, 0)
        map.set_attack_map(self.curr_r, self.curr_c, 1, 1, -1)

        if direction == "w":
            if self.curr_r > 0 and map.map[self.curr_r - self.speed][self.curr_c] == 0:
                self.curr_r -= self.speed
                self.head = 'w'
                self.char = "Q^"
        elif direction == "s"and self.curr_r < map.height - self.speed and map.map[self.curr_r + self.speed][self.curr_c] == 0:
                self.curr_r += self.speed
                self.head = 's'
                self.char = "Qv"
        elif direction == "a" and map.map[self.curr_r][self.curr_c - self.speed] == 0:
            if self.curr_c > 0:
                self.curr_c -= self.speed
                self.head = 'a'
                self.char = "<Q"
        elif direction == "d" and self.curr_c < map.width - self.speed and map.map[self.curr_r][self.curr_c + self.speed] == 0:
                self.curr_c += self.speed
                self.head = 'd'
                self.char = "Q>"
        # print(f"{self.curr_r} {self.curr_c}")
        # ch = input()
        map.set_map(self.curr_r, self.curr_c, 1, 1, self.char)
        self.check_health()
        map.set_attack_map(self.curr_r, self.curr_c, 1, 1, self)

    def BalloonMove(self, direction, map):

        if(map.map[self.curr_r][self.curr_c] == "✈"):
            map.set_map(self.curr_r, self.curr_c, 1, 1, 0)
            map.set_color(self.curr_r, self.curr_c, 1, 1, 0)
        if(map.attack_map[self.curr_r][self.curr_c] == self):
            map.set_attack_map(self.curr_r, self.curr_c, 1, 1, -1)
        if direction == "w":
            if self.curr_r > 0:
                self.curr_r -= self.speed
                self.head = 'w'
        elif direction == "a":
            if self.curr_c > 0:
                self.curr_c -= self.speed
                self.head = 'a'
        elif direction == "s":
                self.curr_r += self.speed
                self.head = 's'
        elif direction == "d":
                self.curr_c += self.speed
                self.head = 'd'
        # print(map.map[self.curr_r][self.curr_c])
        # print(map.attack_map[self.curr_r][self.curr_c])
        if(map.map[self.curr_r][self.curr_c] == 0):
            # print("changed")
            map.set_map(self.curr_r, self.curr_c, 1, 1, self.char)
        self.check_health()
        if(map.attack_map[self.curr_r][self.curr_c] == -1):
            # print("changed")
            map.set_attack_map(self.curr_r, self.curr_c, 1, 1, self)
        # map.set_attack_map(self.curr_r, self.curr_c, 1, 1, self)
        # map.set_attack_map(self.curr_r, self.curr_c, 1, 1, self.char)
                
    def Bmove(self, direction, map):

        map.set_map(self.curr_r, self.curr_c, 1, 1, 0)
        map.set_color(self.curr_r, self.curr_c, 1, 1, 0)
        map.set_attack_map(self.curr_r, self.curr_c, 1, 1, -1)
        
        if direction == "w":
            if self.curr_r > 0 and map.map[self.curr_r - self.speed][self.curr_c] == 0:
                self.curr_r -= self.speed
                self.head = 'w'
        elif direction == "s"and self.curr_r < map.height - self.speed and map.map[self.curr_r + self.speed][self.curr_c] == 0:
                self.curr_r += self.speed
                self.head = 's'
        elif direction == "a" and map.map[self.curr_r][self.curr_c - self.speed] == 0:
            if self.curr_c > 0:
                self.curr_c -= self.speed
                self.head = 'a'
        elif direction == "d" and self.curr_c < map.width - self.speed and map.map[self.curr_r][self.curr_c + self.speed] == 0:
                self.curr_c += self.speed
                self.head = 'd'

        map.set_map(self.curr_r, self.curr_c, 1, 1, self.char)
        self.check_health()
        map.set_attack_map(self.curr_r, self.curr_c, 1, 1, self)
    
    def attack(self,map):
        if self.head == 'w' and map.map[self.curr_r - 1][self.curr_c] != 0:
            obj = map.get_attack_map(self.curr_r - 1, self.curr_c)
            if(obj!=-1):
                obj.attacked_color(self.damage)
        elif self.head == 's'and map.map[self.curr_r + 1][self.curr_c] != 0:
            obj = map.get_attack_map(self.curr_r + 1, self.curr_c)
            if(obj!=-1):
                obj.attacked_color(self.damage)
        elif self.head == 'a' and map.map[self.curr_r][self.curr_c - 1] != 0:
            # map.set_color(self.curr_r, self.curr_c - 1, 1, 1, 3)
            obj = map.get_attack_map(self.curr_r, self.curr_c - 1)
            if(obj!=-1):
                obj.attacked_color(self.damage)
        elif self.head == 'd' and map.map[self.curr_r][self.curr_c + 1] != 0:
            obj = map.get_attack_map(self.curr_r, self.curr_c + 1)
            if(obj!=-1):
                obj.attacked_color(self.damage)
    

class King(Character):
    def __init__(self, health, damage, startr, startc,speed):
        Character.__init__(self, health, damage, startr, startc, 'K',speed)
        self.char = "K>"
        self.alive = True
        self.head = 'd'
        self.speed = speed
        self.range = 1
        self.damage = damage
        self.health = 1000
        self.max_health = 1000
    
    def check_health(self):
        health = self.health
        if health>=self.heath_max/2:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 6)
        elif health>=self.heath_max/5:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 3)
        elif health>0:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 4)
        else:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 0)
            map.set_map(self.curr_r, self.curr_c, 1, 1, 0)
            map.set_attack_map(self.curr_r, self.curr_c, 1, 1, -1)
            self.alive = False

    def attacked(self, damage):
        self.health -= damage
        self.check_health()

    def move(self, direction, map):
        if self.alive:
            Character.Kmove(self, direction, map)

    def attack(self, map):
        if self.alive:
            Character.attack(self, map)

    def attackLettivian(self, map):
        if self.alive:
            attack_r = self.curr_r
            attack_c = self.curr_c
    
            # loop across a 5x5 arear whose centre is attack_r and attack_c
            attacked_obj = []
            for i in range(attack_r - 1, attack_r + 2):
                for j in range(attack_c - 1, attack_c + 2):
                    if i>=0 and i<map.height and j>=0 and j<map.width:
                        if map.get_attack_map(i,j)!= -1:
                            obj = map.get_attack_map(i, j)
                        # print(f"{obj}, {i}, {j}")    
                            if(obj!=self) and not (obj in attacked_obj) and not(obj.char == "K>" or obj.char == "B" or obj.char == "K^" or obj.char == "Kv" or obj.char == "<K" or obj.char == "A" or obj.char == "K" or obj.char == "✈" or obj.char == "Q>" or obj.char == "Q^" or obj.char == "Qv" or obj.char == "<Q"):
                                # print(obj)
                                obj.attacked_color(self.damage)
                                attacked_obj.append(obj)
    
    def set_map(self, map):
        map.set_map(self.startr, self.startc, 1, 1, self.char)
        map.set_color(self.startr, self.startc, 1, 1, 2)
        map.set_attack_map(self.startr, self.startc, 1, 1, self)

class Queen(Character):
    def __init__(self, health, damage, startr, startc,speed):
        Character.__init__(self, health, damage, startr, startc, 'Q',speed)
        self.char = "Q>"
        self.alive = True
        self.head = 'd'
        self.speed = speed
        self.range = 1
        self.damage = damage
        self.health = 1000
        self.max_health = 1000
    
    def check_health(self):
        health = self.health
        if health>=self.heath_max/2:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 6)
        elif health>=self.heath_max/5:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 3)
        elif health>0:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 4)
        else:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 0)
            map.set_map(self.curr_r, self.curr_c, 1, 1, 0)
            map.set_attack_map(self.curr_r, self.curr_c, 1, 1, -1)
            self.alive = False

    def attacked(self, damage):
        self.health -= damage
        self.check_health()

    def move(self, direction, map):
        if self.alive:
            Character.Qmove(self, direction, map)

    def attack(self, map):
        if self.alive:
            attack_r = self.curr_r
            attack_c = self.curr_c
            if self.head == 'w':
                attack_r = self.curr_r - 8
                attack_c = self.curr_c
                # obj = map.get_attack_map(self.curr_r - 1, self.curr_c)
                # if(obj!=-1):
                #     obj.attacked_color(self.damage)
            elif self.head == 's':
                attack_r = self.curr_r + 8
                attack_c = self.curr_c
            elif self.head == 'a':
                attack_r = self.curr_r
                attack_c = self.curr_c - 8
            elif self.head == 'd':
                attack_r = self.curr_r
                attack_c = self.curr_c + 8
            
            # loop across a 5x5 arear whose centre is attack_r and attack_c
            attacked_obj = []
            for i in range(attack_r - 2, attack_r + 3):
                for j in range(attack_c - 2, attack_c + 3):
                    if i>=0 and i<map.height and j>=0 and j<map.width:
                        if map.get_attack_map(i,j)!= -1:
                            obj = map.get_attack_map(i, j)
                                
                            if(obj!=self) and not (obj in attacked_obj) and not(obj.char == "K>" or obj.char == "B" or obj.char == "K^" or obj.char == "Kv" or obj.char == "<K" or obj.char == "A" or obj.char == "K" or obj.char == "✈"):
                                # print(obj)
                                obj.attacked_color(self.damage)
                                attacked_obj.append(obj)
            
    
    def attackEagle(self, map):
        if self.alive:
            attack_r = self.curr_r
            attack_c = self.curr_c
            if self.head == 'w':
                attack_r = self.curr_r - 16
                attack_c = self.curr_c
                # obj = map.get_attack_map(self.curr_r - 1, self.curr_c)
                # if(obj!=-1):
                #     obj.attacked_color(self.damage)
            elif self.head == 's':
                attack_r = self.curr_r + 16
                attack_c = self.curr_c
            elif self.head == 'a':
                attack_r = self.curr_r
                attack_c = self.curr_c - 16
            elif self.head == 'd':
                attack_r = self.curr_r
                attack_c = self.curr_c + 16
            
            # loop across a 5x5 arear whose centre is attack_r and attack_c
            attacked_obj = []
            for i in range(attack_r - 4, attack_r + 5):
                for j in range(attack_c - 4, attack_c + 5):
                    if i>=0 and i<map.height and j>=0 and j<map.width:
                        if map.get_attack_map(i,j)!= -1:
                            obj = map.get_attack_map(i, j)
                                
                            if(obj!=self) and not (obj in attacked_obj) and not(obj.char == "K>" or obj.char == "B" or obj.char == "K^" or obj.char == "Kv" or obj.char == "<K" or obj.char == "A" or obj.char == "K" or obj.char == "✈"):
                                # print(obj)
                                obj.attacked_color(self.damage)
                                attacked_obj.append(obj)
            # ch=input()

    def set_map(self, map):
            map.set_map(self.startr, self.startc, 1, 1, self.char)
            map.set_color(self.startr, self.startc, 1, 1, 2)
            map.set_attack_map(self.startr, self.startc, 1, 1, self)

class Barbarian(Character):
    def __init__(self, health, damage, startr, startc,speed):
        Character.__init__(self, health, damage, startr, startc, 'B',speed)
        self.char = 'B'
        self.alive = True
        self.head = 'd'
        self.speed = speed
        self.damage = damage
        self.nearest_building = None


    def check_health(self):
        health = self.health
        if health>=self.heath_max/2:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 6)
        elif health>=self.heath_max/5:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 3)
        elif health>0:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 4)
        else:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 0)
            map.set_map(self.curr_r, self.curr_c, 1, 1, 0)
            map.set_attack_map(self.curr_r, self.curr_c, 1, 1, -1)
            self.alive = False

    def attacked(self, damage):
        self.health -= damage
        self.check_health()

    def move(self, map, buildings):
        if(self.alive):
            # calculate minimum euclidian distance and nearest buoiulding
            won = True
            min_distance = 100000
            for building in buildings:
                if building.alive:
                    dist = math.sqrt((self.curr_r - building.centre_r)**2 + (self.curr_c - building.centre_c)**2)
                    if dist < min_distance:
                        min_distance = dist
                        self.nearest_building = building
                    won = False
            
            if(won):
                print("LEVEL WONNNN!!!!\nClick on any button to proceed.")
                ch = input()
                if(map.level == 3):
                    print("GAME WON! ALL LEVELS CLEARED")
                    exit()
                main1(map.KQ, map.level + 1)


            
            # move towards nearest buoiulding
            if self.nearest_building.centre_r > self.curr_r:
                Character.Bmove(self,'s', map)
            elif self.nearest_building.centre_r < self.curr_r:
                Character.Bmove(self,'w', map)
            elif self.nearest_building.centre_c > self.curr_c:
                Character.Bmove(self,'d', map)
            elif self.nearest_building.centre_c < self.curr_c:
                Character.Bmove(self,'a', map)

            # print(str(self.curr_c) + "," + str(self.curr_r) + "," + str(self.nearest_building.centre_r)+ "," + str(self.nearest_building.centre_c) )
            # ch = input()
            # attack nearest buoiulding
            
            self.found = False
            # print(str(self.curr_r) + "," + str(self.curr_c + 1))
            # print(map.get_attack_map(self.curr_r, self.curr_c + 1))
            # print(str(self.curr_r) + "," + str(self.curr_c - 1))
            # print(map.get_attack_map(self.curr_r, self.curr_c - 1))
            # print(str(self.curr_r+1) + "," + str(self.curr_c ))
            # print(map.get_attack_map(self.curr_r + 1, self.curr_c))
            # print(str(self.curr_r-1) + "," + str(self.curr_c))
            # print(map.get_attack_map(self.curr_r - 1, self.curr_c))
            # print(str(self.curr_r+1) + "," + str(self.curr_c + 1))
            # print(map.get_attack_map(self.curr_r+1, self.curr_c + 1))
            # print(str(self.curr_r-1) + "," + str(self.curr_c + 1))
            # print(map.get_attack_map(self.curr_r-1, self.curr_c + 1))
            # print(str(self.curr_r+1) + "," + str(self.curr_c - 1))
            # print(map.get_attack_map(self.curr_r+1, self.curr_c - 1))
            # print(str(self.curr_r - 1) + "," + str(self.curr_c - 1))
            # print(map.get_attack_map(self.curr_r-1, self.curr_c - 1))
            
            # check if nearest building is around current position
            try:
                if(map.get_attack_map(self.curr_r, self.curr_c + 1) != -1):
                    self.found = map.get_attack_map(self.curr_r, self.curr_c + 1)
                    
                elif(map.get_attack_map(self.curr_r, self.curr_c - 1) != -1):
                    self.found = map.get_attack_map(self.curr_r, self.curr_c - 1)
                    
                elif (map.get_attack_map(self.curr_r + 1, self.curr_c) != -1):
                    self.found = map.get_attack_map(self.curr_r + 1, self.curr_c)
                    
                elif(map.get_attack_map(self.curr_r - 1, self.curr_c) != -1):
                    self.found = map.get_attack_map(self.curr_r - 1, self.curr_c)
                    
                elif(map.get_attack_map(self.curr_r+1, self.curr_c + 1) != -1):
                    self.found = map.get_attack_map(self.curr_r+1, self.curr_c + 1)
                    
                elif(map.get_attack_map(self.curr_r-1, self.curr_c + 1) != -1):
                    self.found = map.get_attack_map(self.curr_r-1, self.curr_c + 1)
                    
                elif(map.get_attack_map(self.curr_r+1, self.curr_c-1) != -1):
                    self.found = map.get_attack_map(self.curr_r+1, self.curr_c-1)
                
                elif(map.get_attack_map(self.curr_r-1, self.curr_c-1) != -1):
                    self.found = map.get_attack_map(self.curr_r-1, self.curr_c-1)
                    

                # print(str(self.nearest_building) + "," + str(self.found))
                # ch = input()
                if(self.found):
                    self.found.attacked_color(self.damage)
            except:
                pass


    def attack(self, map):
        Character.attack(self, map)
    
    def set_map(self, map):
        map.set_map(self.startr, self.startc, 1, 1, self.char)
        map.set_color(self.startr, self.startc, 1, 1, 6)

class Archer(Character):
    def __init__(self, health, damage, startr, startc,speed):
        Character.__init__(self, health, damage, startr, startc, 'A',speed)
        self.char = 'A'
        self.alive = True
        self.head = 'd'
        self.speed = speed
        self.damage = damage
        self.nearest_building = None


    def check_health(self):
        health = self.health
        if health>=self.heath_max/2:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 6)
        elif health>=self.heath_max/5:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 3)
        elif health>0:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 4)
        else:
            map.set_color(self.curr_r, self.curr_c, 1, 1, 0)
            map.set_map(self.curr_r, self.curr_c, 1, 1, 0)
            map.set_attack_map(self.curr_r, self.curr_c, 1, 1, -1)
            self.alive = False

    def attacked(self, damage):
        self.health -= damage
        self.check_health()

    def move(self, map, buildings):
        if(self.alive):
            # calculate minimum euclidian distance and nearest buoiulding
            won = True
            min_distance = 100000
            for building in buildings:
                if building.alive:
                    dist = math.sqrt((self.curr_r - building.centre_r)**2 + (self.curr_c - building.centre_c)**2)
                    if dist < min_distance:
                        min_distance = dist
                        self.nearest_building = building
                    won = False
            
            
            if(won):
                print("LEVEL WONNNN!!!!\nClick on any button to proceed.")
                ch = input()
                if(map.level == 3):
                    print("GAME WON! ALL LEVELS CLEARED")
                    exit()
                main1(map.KQ, map.level + 1)

                # level += 1
                # main1(KQ, level)

            
            # move towards nearest buoiulding
            if self.nearest_building.centre_r > self.curr_r:
                Character.Bmove(self,'s', map)
            elif self.nearest_building.centre_r < self.curr_r:
                Character.Bmove(self,'w', map)
            elif self.nearest_building.centre_c > self.curr_c:
                Character.Bmove(self,'d', map)
            elif self.nearest_building.centre_c < self.curr_c:
                Character.Bmove(self,'a', map)

            # print(str(self.curr_c) + "," + str(self.curr_r) + "," + str(self.nearest_building.centre_r)+ "," + str(self.nearest_building.centre_c) )
            # print(self.nearest_building)
            # ch = input()
            # attack nearest buoiulding
            # print(str(self.curr_r) + "," + str(self.curr_c + 1))
            # print(map.get_attack_map(self.curr_r, self.curr_c + 1))
            # print(str(self.curr_r) + "," + str(self.curr_c - 1))
            # print(map.get_attack_map(self.curr_r, self.curr_c - 1))
            # print(str(self.curr_r+1) + "," + str(self.curr_c ))
            # print(map.get_attack_map(self.curr_r + 1, self.curr_c))
            # print(str(self.curr_r-1) + "," + str(self.curr_c))
            # print(map.get_attack_map(self.curr_r - 1, self.curr_c))
            # print(str(self.curr_r+1) + "," + str(self.curr_c + 1))
            # print(map.get_attack_map(self.curr_r+1, self.curr_c + 1))
            # print(str(self.curr_r-1) + "," + str(self.curr_c + 1))
            # print(map.get_attack_map(self.curr_r-1, self.curr_c + 1))
            # print(str(self.curr_r+1) + "," + str(self.curr_c - 1))
            # print(map.get_attack_map(self.curr_r+1, self.curr_c - 1))
            # print(str(self.curr_r - 1) + "," + str(self.curr_c - 1))
            # print(map.get_attack_map(self.curr_r-1, self.curr_c - 1))
            
            # check if nearest building is around current position
            attacked_obj = []
            try:
                for y in range(self.curr_c -4, self.curr_c+4):
                    for x in range(self.curr_r -4, self.curr_r +4):
                        # print(str(x)+ "," + str(y) + "," + str(map.get_attack_map(x,y)))
                        if x>=0 and x<map.height and y>=0 and y<map.width:
                            if map.get_attack_map(x,y)!= -1:
                                obj = map.get_attack_map(x,y)
                                    # file = './src/canonshot.wav'
                                    # os.system("afplay " + file)
                                    # print("canon shot")
                                    # print("damage: " + str(self.damage))
                                # print("obj health: " + str(obj.health))
                                # print(obj)
                                # print(map.attack_map)
                                # if(obj.startc):
                                #     print(obj.startc)
                                #     print(obj.startr)
                                    

                                
                                if(obj!=self) and not (obj in attacked_obj) and not(obj.char == "K>" or obj.char == "B" or obj.char == "K^" or obj.char == "Kv" or obj.char == "<K" or obj.char == "A" or obj.char == "K" or obj.char == "✈" or obj.char == "Q>" or obj.char == "Q^" or obj.char == "Qv" or obj.char == "<Q"):
                                    # print(obj)
                                    obj.attacked_color(self.damage)
                                    attacked_obj.append(obj)

                                # print(attacked_obj)   
                                # ch = input()
                                    
                                # ch = input()

                    # print(str(self.nearest_building) + "," + str(self.found))
            except Exception as er:
                pass
                # print(er)


    def attack(self, map):
        Character.attack(self, map)
    
    def set_map(self, map):
        map.set_map(self.startr, self.startc, 1, 1, self.char)
        map.set_color(self.startr, self.startc, 1, 1, 6)

class Balloon(Character):
    def __init__(self, health, damage, startr, startc,speed):
        Character.__init__(self, health, damage, startr, startc, 'A',speed)
        self.char = '✈'
        self.alive = True
        self.head = 'd'
        self.speed = speed
        self.damage = damage
        self.nearest_building = None
        self.prev_move = 'd'


    def check_health(self):
        health = self.health
        if(map.map[self.curr_r][self.curr_c] == "✈"):
            if health>=self.heath_max/2:
                map.set_color(self.curr_r, self.curr_c, 1, 1, 6)
            elif health>=self.heath_max/5:
                map.set_color(self.curr_r, self.curr_c, 1, 1, 3)
            elif health>0:
                map.set_color(self.curr_r, self.curr_c, 1, 1, 4)
            else:
                map.set_color(self.curr_r, self.curr_c, 1, 1, 0)
                map.set_map(self.curr_r, self.curr_c, 1, 1, 0)
                map.set_attack_map(self.curr_r, self.curr_c, 1, 1, -1)
                self.alive = False

    def attacked(self, damage):
        self.health -= damage
        self.check_health()

    def move(self, map, buildings):
        # print(f"{self.char} {self.curr_c} {self.curr_r} {self.health}")
        if(self.alive):
            # calculate minimum euclidian distance and nearest buoiulding
            won = True
            defensiveBuilding = []
            otherBuildings = []
            for building in buildings:
                if(building.alive):
                    char = building.char
                    if(char=="♔" or char=="C"):
                        defensiveBuilding.append(building)
                    elif(char!="W"):
                        otherBuildings.append(building)
            
            if(len(defensiveBuilding)>0):
                min_distance = 100000
                for building in defensiveBuilding:
                    if building.alive:
                        dist = math.sqrt((self.curr_r - building.centre_r)**2 + (self.curr_c - building.centre_c)**2)
                        if dist < min_distance:
                            min_distance = dist
                            self.nearest_building = building
                        won = False
            else:
                min_distance = 100000
                for building in otherBuildings:
                    if building.alive:
                        dist = math.sqrt((self.curr_r - building.centre_r)**2 + (self.curr_c - building.centre_c)**2)
                        if dist < min_distance:
                            min_distance = dist
                            self.nearest_building = building
                        won = False
            
            
            if(won):
                print("LEVEL WONNNN!!!! \nPress any button to continue!")
                ch = input()

            # print(self.nearest_building)
            # ch = input()

            # move towards nearest buoiulding
            # print("inside move")
            if self.nearest_building.centre_r > self.curr_r:
                Character.BalloonMove(self, 's', map)
                # print("s")
            elif self.nearest_building.centre_c < self.curr_c:
                Character.BalloonMove(self,'a', map)
                # print("a")
            elif self.nearest_building.centre_r < self.curr_r:
                Character.BalloonMove(self,'w', map)
                # print("w")
            elif self.nearest_building.centre_c > self.curr_c:
                Character.BalloonMove(self,'d', map)
                # print("d")
            
            # ch = input()
            
            

            # print(str(self.curr_c) + "," + str(self.curr_r) + "," + str(self.nearest_building.centre_r)+ "," + str(self.nearest_building.centre_c) )
            # print(self.nearest_building)
            # ch = input()
            # attack nearest buoiulding
            # print(str(self.curr_r) + "," + str(self.curr_c + 1))
            # print(map.get_attack_map(self.curr_r, self.curr_c + 1))
            # print(str(self.curr_r) + "," + str(self.curr_c - 1))
            # print(map.get_attack_map(self.curr_r, self.curr_c - 1))
            # print(str(self.curr_r+1) + "," + str(self.curr_c ))
            # print(map.get_attack_map(self.curr_r + 1, self.curr_c))
            # print(str(self.curr_r-1) + "," + str(self.curr_c))
            # print(map.get_attack_map(self.curr_r - 1, self.curr_c))
            # print(str(self.curr_r+1) + "," + str(self.curr_c + 1))
            # print(map.get_attack_map(self.curr_r+1, self.curr_c + 1))
            # print(str(self.curr_r-1) + "," + str(self.curr_c + 1))
            # print(map.get_attack_map(self.curr_r-1, self.curr_c + 1))
            # print(str(self.curr_r+1) + "," + str(self.curr_c - 1))
            # print(map.get_attack_map(self.curr_r+1, self.curr_c - 1))
            # print(str(self.curr_r - 1) + "," + str(self.curr_c - 1))
            # print(map.get_attack_map(self.curr_r-1, self.curr_c - 1))
            
            # check if nearest building is around current position
            try:
                for y in range(self.curr_c - self.speed, self.curr_c + self.speed):
                    for x in range(self.curr_r - self.speed, self.curr_r + self.speed):
                        # print(str(x)+ "," + str(y) + "," + str(map.get_attack_map(x,y)))
                        if x>=0 and x<map.height and y>=0 and y<map.width:
                            if map.get_attack_map(x,y)!= -1:
                                obj = map.get_attack_map(x,y)
                                    # file = './src/canonshot.wav'
                                    # os.system("afplay " + file)
                                    # print("canon shot")
                                    # print("damage: " + str(self.damage))
                                # print("obj health: " + str(obj.health))
                                # print(obj)
                                # print(map.attack_map)
                                # if(obj.startc):
                                #     print(obj.startc)
                                #     print(obj.startr)
                                    

                                
                                if(obj == self.nearest_building):
                                    obj.attacked_color(self.damage)

                                # print(attacked_obj)   
                                # ch = input()
                                    
                                # ch = input()

                    # print(str(self.nearest_building) + "," + str(self.found))
                    # ch = input()
            except Exception as er:
                pass
                # print(er)
                # ch = input()
            
            # print(f"{self.char} {self.curr_c} {self.curr_r} {self.health}")
            # ch = input()


    def attack(self, map):
        Character.attack(self, map)
    
    def set_map(self, map):
        map.set_map(self.startr, self.startc, 1, 1, self.char)
        map.set_color(self.startr, self.startc, 1, 1, 6)  
# ----------------------------------------------------------------------------------------------------------------------
# Map

class Map:
    def __init__(self, width, height, KQ, level):
        self.KQ = KQ
        self.level = level
        self.width = width
        self.height = height
        self.map = [[0 for x in range(width)] for y in range(height)]
        self.color = [[0 for x in range(width)] for y in range(height)]
        self.attack_map = [[-1 for x in range(width)] for y in range(height)]

    def set_map(self, startr, startc, height, width, char):
        for y in range(startr, startr + height):
            for x in range(startc, startc + width):
                self.map[y][x] = char

    def set_color(self, startr, startc, height, width, char):
        for y in range(startr, startr + height):
            for x in range(startc, startc + width):
                self.color[y][x] = char
    
    def set_attack_map(self, startr, startc, height, width, char):
        for y in range(startr, startr + height):
            for x in range(startc, startc + width):
                self.attack_map[y][x] = char
            

    def set_tile(self, x, y, value):
        self.map[y][x] = value

    def get_attack_map(self, y, x):
        return self.attack_map[y][x]
    
    def get_map(self, y, x):
        return self.map[y][x]

    def print_map(self):
        print("*" * (self.width*2 + 2))

        for y in range(self.height):
            print("*", end="")
            for x in range(self.width):
                if self.color[y][x] == 1 and self.map[y][x] != 0:
                    print(Fore.GREEN + self.map[y][x] + Style.RESET_ALL, end="")
                elif self.color[y][x] == 0:
                    print(".", end="")
                elif self.color[y][x] == 2 and self.map[y][x] != 0:
                    print(Fore.BLUE + self.map[y][x] + Style.RESET_ALL, end="")
                elif self.color[y][x] == 3 and self.map[y][x] != 0:
                    print(Fore.YELLOW + self.map[y][x] + Style.RESET_ALL, end="")
                elif self.color[y][x] == 4 and self.map[y][x] != 0:
                    print(Fore.RED + self.map[y][x] + Style.RESET_ALL, end="")
                elif self.color[y][x] == 6 and self.map[y][x] != 0:
                    print(Style.DIM + Fore.GREEN + self.map[y][x] + Style.RESET_ALL, end="")
                
                obj = self.get_attack_map(y, x)
                if obj != -1:
                   if not (obj.char == "K>" or obj.char == "K^" or obj.char == "Kv" or obj.char == "<K" or obj.char == "Q>" or obj.char == "Q^" or obj.char == "Qv" or obj.char == "<Q"):
                      print(" ", end="") 
                
                else:
                    print(" ", end="")
            print("*")

        print("*" * (self.width*2 + 2))
    
    def sprintmap(self):
        printm = ""
        printm+= "*" * (self.width*2 + 2) + "\n"

        for y in range(self.height):
            printm+= "*"
            for x in range(self.width):
                if self.color[y][x] == 1 and self.map[y][x] != 0:
                    printm+= Fore.GREEN + self.map[y][x] + Style.RESET_ALL
                elif self.color[y][x] == 0:
                    printm+= "."
                elif self.color[y][x] == 2 and self.map[y][x] != 0:
                    printm+= Fore.BLUE + self.map[y][x] + Style.RESET_ALL
                elif self.color[y][x] == 3 and self.map[y][x] != 0:
                    printm+= Fore.YELLOW + self.map[y][x] + Style.RESET_ALL
                elif self.color[y][x] == 4 and self.map[y][x] != 0:
                    printm+= Fore.RED + self.map[y][x] + Style.RESET_ALL
                elif self.color[y][x] == 6 and self.map[y][x] != 0:
                    printm+= Style.DIM + Fore.GREEN + self.map[y][x] + Style.RESET_ALL
                
                obj = self.get_attack_map(y, x)
                if obj != -1:
                   if not (obj.char == "K>" or obj.char == "K^" or obj.char == "Kv" or obj.char == "<K" or obj.char == "Q>" or obj.char == "Q^" or obj.char == "Qv" or obj.char == "<Q"):
                      printm+= " "
                
                else:
                    printm+= " "
            printm+= "*\n"

        printm+= "*" * (self.width*2 + 2)   
        return printm  

map = Map(30, 14, "K", 1)
# -------------------------------

def rage(king,Balive):
    print("Rage")
    ch = input()
    king.damage*=2
    king.speed*=2

    for B in Balive:
        B.damage*=2
        B.speed*=2

def heal(king,Balive):
   print("Healead")
   ch = input()
   kh = king.health*2
   if(kh>king.max_health):
       kh = king.max_health
    
   king.health = kh
   print("ola")
   for B in Balive:
        bh = king.health*2
        if(bh>king.max_health):
            bh = king.max_health
            
        king.health = bh

def check_lost(king,Balive):
    if(king.alive):
        return False

    for B in Balive:
        if(B.alive):
            return False 
              
    return True  
# ----------------------------------------------------------------------------------------------------------------------

def replay():
    print("Do you want to see replay? (y/n)")
    ch = input()
    if(ch == "y"):
        for i in range(len(replay_list)):
            print(replay_list[i])


def main1(player, level):
    map.KQ = player
    map.level = level
    map.map = [[0 for x in range(map.width)] for y in range(map.height)]
    map.color = [[0 for x in range(map.width)] for y in range(map.height)]
    map.attack_map = [[-1 for x in range(map. width)] for y in range(map.height)]
    buildingArray = []
    noBarbariansLeft = 20
    noArchersLeft = 20
    noBalloonsLeft = 9


    town = Town("T", 5, 13)
    town.set_map(map)
    buildingArray.append(town)


    hutarray = []
    hut1 = Hut("H", 10, 20)
    hut1.set_map(map)
    hutarray.append(hut1)

    hut2 = Hut("H", 5, 25)
    hut2.set_map(map)
    hutarray.append(hut2)

    hut3 = Hut("H", 1, 5)
    hut3.set_map(map)
    hutarray.append(hut3)

    hut4 = Hut("H", 1, 12)
    hut4.set_map(map)
    hutarray.append(hut4)

    hut5 = Hut("H", 12, 8)
    hut5.set_map(map)
    hutarray.append(hut5)

    buildingArray+= hutarray

    wallarray = []
    wall1 = Wall("W", 5, 12)
    wall1.set_map(map)
    wallarray.append(wall1)

    wall2 = Wall("W", 6, 12)
    wall2.set_map(map)
    wallarray.append(wall2)

    wall3 = Wall("W", 7, 12)
    wall3.set_map(map)
    wallarray.append(wall3)

    wall4 = Wall("W", 8,12)
    wall4.set_map(map)
    wallarray.append(wall4)

    wall1 = Wall("W", 9, 12)
    wall1.set_map(map)
    wallarray.append(wall1)

    wall1.set_map(map)
    wallarray.append(wall1)

    wall1 = Wall("W", 4, 12)
    wall1.set_map(map)
    wallarray.append(wall1)

    wall1 = Wall("W", 4, 13)
    wall1.set_map(map)
    wallarray.append(wall1)

    wall1 = Wall("W", 4, 14)
    wall1.set_map(map)
    wallarray.append(wall1)

    wall1 = Wall("W", 4, 15)
    wall1.set_map(map)
    wallarray.append(wall1)

    wall1 = Wall("W", 4, 16)
    wall1.set_map(map)
    wallarray.append(wall1)

    wall1 = Wall("W", 5, 16)
    wall1.set_map(map)
    wallarray.append(wall1)

    wall2 = Wall("W", 6, 16)
    wall2.set_map(map)
    wallarray.append(wall2)

    wall3 = Wall("W", 7, 16)
    wall3.set_map(map)
    wallarray.append(wall3)

    wall4 = Wall("W", 8,16)
    wall4.set_map(map)
    wallarray.append(wall4)

    wall1 = Wall("W", 9, 16)
    wall1.set_map(map)
    wallarray.append(wall1)

    wall2 = Wall("W", 4, 13)
    wall2.set_map(map)
    wallarray.append(wall2)

    wall3 = Wall("W", 4, 14)
    wall3.set_map(map)
    wallarray.append(wall3)

    wall4 = Wall("W", 9, 15)
    wall4.set_map(map)
    wallarray.append(wall4)

    wall2 = Wall("W", 9, 13)
    wall2.set_map(map)
    wallarray.append(wall2)

    wall3 = Wall("W", 9, 14)
    wall3.set_map(map)
    wallarray.append(wall3)

    wall4 = Wall("W", 9, 15)
    wall4.set_map(map)
    wallarray.append(wall4)

    wall4 = Wall("W", 12,3)
    wall4.set_map(map)
    wallarray.append(wall4)
    wall4 = Wall("W", 12,4)
    wall4.set_map(map)
    wallarray.append(wall4)
    wall4 = Wall("W", 11,4)
    wall4.set_map(map)
    wallarray.append(wall4)

    # buildingArray+= wallarray

    defensiveBuilding = []
    
    cannon1 = Canon("C", 2, 2, 10)
    cannon1.set_map(map)
    buildingArray.append(cannon1)
    defensiveBuilding.append(cannon1)

    cannon2 = Canon("C", 10, 25, 5)
    cannon2.set_map(map)
    buildingArray.append(cannon2)
    defensiveBuilding.append(cannon2)

    if(level >= 2):
        cannon3 = Canon("C", 8, 27, 5)
        cannon3.set_map(map)
        buildingArray.append(cannon3)
        defensiveBuilding.append(cannon3)
    
    if(level == 3):
        cannon4 = Canon("C", 4, 2, 5)
        cannon4.set_map(map)
        buildingArray.append(cannon4)
        defensiveBuilding.append(cannon4)

    wizardTower1 = WizardTower("♔", 6, 4, 10)
    wizardTower1.set_map(map)
    buildingArray.append(wizardTower1)
    defensiveBuilding.append(wizardTower1)

    wizardTower2 = WizardTower("♔", 1, 25, 5)
    wizardTower2.set_map(map)
    buildingArray.append(wizardTower2)
    defensiveBuilding.append(wizardTower2)

    if(level >= 2):
        wizardTower3 = WizardTower("♔", 6, 7, 5)
        wizardTower3.set_map(map)
        buildingArray.append(wizardTower3)
        defensiveBuilding.append(wizardTower3)
    
    if(level == 3):
        wizardTower4 = WizardTower("♔", 1, 27, 5)
        wizardTower4.set_map(map)
        buildingArray.append(wizardTower4)
        defensiveBuilding.append(wizardTower4)


    if player=="K":
        king = King(100,10, 0, 0, 1)
    else:
        king = Queen(100,7, 0, 0, 1)
    king.set_map(map)


    os.system("clear")
    print(Style.DIM + "*" * (30 + 2))
    print(Fore.BLUE + "Welcome to the game!")
    print(Style.RESET_ALL)
    print(Style.DIM + "*" * (30 + 2))
    print(Style.RESET_ALL)
    map.print_map()
    print(Fore.BLUE + "Health: " + str(king.health))
    print(Style.RESET_ALL)

    Balive = []
    replay_list = []

    time_e = -1

    while True:

        if time_e <= time.time() and player == "Q" and time_e != -1:
            print("Queen Eagle Attack Mode Activated!")
            # ch = input()
            king.attackEagle(map)
            time_e = -1
            

        if(check_lost(king,Balive)):
            print("GAME LOST!")
            exit()
        
        for defense in defensiveBuilding:
            defense.attack(map)

        os.system("clear")
        map.print_map()
        print(Fore.BLUE + "Health: " + str(king.health))
        print(Style.RESET_ALL)

        key_pressed = input_to()
        replay_list.append(key_pressed)
        for B1 in Balive:
            B1.move(map, buildingArray)
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)
    
        if key_pressed == "1" and noBarbariansLeft > 0:
            B1 = Barbarian(100, 10, 0,1,1)
            # B1 = Barbarian(100, 10, 6,8,1)
            B1.set_map(map)
            Balive.append(B1)
            noBarbariansLeft -= 1
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)
        elif key_pressed == "2" and noBarbariansLeft > 0:
            B2 = Barbarian(100, 10,0,15,1)
            B2.set_map(map)
            Balive.append(B2)
            noBarbariansLeft -= 1
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)
        elif key_pressed == "3" and noBarbariansLeft > 0:
            B3 = Barbarian(100, 10, 0,24,1)
            B3.set_map(map)
            Balive.append(B3)
            noBarbariansLeft -= 1
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)
        
        elif key_pressed == "4" and noArchersLeft > 0:
            A1 = Archer(50, 5, 13,20,2)
            A1.set_map(map)
            Balive.append(A1)
            noArchersLeft -= 1
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)

        elif key_pressed == "5" and noArchersLeft > 0:
            A1 = Archer(50, 5, 12,0,2)
            A1.set_map(map)
            Balive.append(A1)
            noArchersLeft -= 1
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)

        elif key_pressed == "6" and noArchersLeft > 0:
            A1 = Archer(50, 5, 8,0,2)
            A1.set_map(map)
            Balive.append(A1)
            noArchersLeft -= 1
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)
        
        elif key_pressed == "7" and noBalloonsLeft > 0:
            A1 = Balloon(100, 10,8,24,2)
            A1.set_map(map)
            Balive.append(A1)
            noBalloonsLeft -= 1
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)
        
        elif key_pressed == "8" and noBalloonsLeft > 0:
            A1 = Balloon(100, 10,9,24,2)
            A1.set_map(map)
            Balive.append(A1)
            noBalloonsLeft -= 1
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)
        
        elif key_pressed == "9" and noBalloonsLeft > 0:
            A1 = Balloon(100, 10,9,24,2)
            A1.set_map(map)
            Balive.append(A1)
            noBalloonsLeft -= 1
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)

        elif key_pressed == "q":
            exit()
        elif key_pressed == "s":
            king.move('s',map)
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)
        elif key_pressed == "a":
            king.move('a',map)
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)
        elif key_pressed == "d":
            king.move('d',map)
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)
        elif key_pressed == "w":
            king.move('w',map)
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)
        elif key_pressed == " ":
            king.attack(map)
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)
        elif key_pressed == "p":
            print("paused")
            ch = input()
        elif key_pressed == "r":
            rage(king,Balive)
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)
        elif key_pressed == "h":
            heal(king,Balive)
            os.system("clear")
            map.print_map()
            print(Fore.BLUE + "Health: " + str(king.health))
            print(Style.RESET_ALL)
        elif key_pressed == "e" and player == "Q":
            time_e = time.time() + 1
            print("Queen Eagle Attack will be activated after 1 second!")
            # ch = input()
        elif key_pressed == "l" and player == "K":
            king.attackLettivian(map)

        printm = map.sprintmap()
        printm += "\n" + Fore.BLUE + "Health: " + str(king.health) + Style.RESET_ALL
        data[id].append(printm)
        # write data to json
        with open('replays/replay.json', 'w') as f:
            json.dump(data, f)
        # time.sleep(0.1)


def main():





    print("""
    ╭╮╭━┳╮╱╱╱╱╱╱╱╱╭╮╱╭╮╱╱╱╭━┳━━━┳╮╱╱╱╭━╮╱╭╮
    ┃┃┃╭┫┃╱╱╱╱╱╱╱╱┃┃╱┃┃╱╱╱┃╭┫╭━╮┃┃╱╱╱┃┃╰╮┃┃
    ┃╰╯╯┃┃╱╱╭━━┳━━┫╰━╯┣━━┳╯╰┫┃╱╰┫┃╭━━┫╭╮╰╯┣━━╮
    ┃╭╮┃┃┃╱╭┫╭╮┃━━┫╭━╮┃╭╮┣╮╭┫┃╱╭┫┃┃╭╮┃┃╰╮┃┃━━┫
    ┃┃┃╰┫╰━╯┃╭╮┣━━┃┃╱┃┃╰╯┃┃┃┃╰━╯┃╰┫╭╮┃┃╱┃┃┣━━┃
    ╰╯╰━┻━━━┻╯╰┻━━┻╯╱╰┻━━╯╰╯╰━━━┻━┻╯╰┻╯╱╰━┻━━╯""")
    print(f"\n\tGame ID: {id}")

    # print(
    #     """
    #     Select Your Level:
    #     ➊➋➌➊➋➌➊➋➌➊➋➌➊➋➌➊➋➌➊➋➌➊➋➌➊➋➌➊➋➌➊➋
    #     1. EasyPeasy
    #     2. NormalIsUnderated
    #     3. HardAsABrick
    #     """
        
    # )

    ch = input("Which game do you want to replay? (Enter GameID or N for not replaying anything): ")
    if ch == "N":
        print(
            """
            Select Your Player:
            K♔ King
            Q♕ Archer Queen
            """
        )
        ch = input("Which player are you ready to take on? (K/Q)")

        if(ch=="K"):
            main1("K",1)
        elif(ch=="Q"):
            main1("Q",1)
    
    elif ch.isdigit() and int(ch) in range(0,len(data)):
        for map in data[ch]:
            print(map)
            time.sleep
            os.system("clear")
            
        main()


main()