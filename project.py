# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:47:32 2019

@author: 25172
"""
import tkinter
import arcade
import easygui as e
from tkinter import messagebox
from tkinter import *

screenwidth=1280
screenheight=960
screentitle="escape space"
playermovementspeed=4
truepassword='888'
#use arcade and tiled to get the map
class mygame(arcade.Window):
    def __init__(self):
         super().__init__(screenwidth,screenheight,screentitle)
         self.playerlist=[]
         self.monsterlist=[]
         self.bomplist=[]
         self.walllist=[] 
         self.passwordlist=[]
         self.physics_engine=[]
         self.input_password = False
    def setup(self):
        #create sprite list
        self.playerlist=arcade.SpriteList()
        self.monsterlist=arcade.SpriteList()
        self.bomplist=arcade.SpriteList()
        self.walllist=arcade.SpriteList()
        self.passwordlist=arcade.SpriteList()
        #set the player, 1 means the scaling
        self.player=arcade.Sprite('human.jpg',1)
        self.player.center_x=660   #15*40+20
        self.player.center_y=900
        self.playerlist.append(self.player)
       
        #get the map,1 means the scaling
        my_map=arcade.tilemap.read_tmx('map1.tmx')
        self.walllist=arcade.tilemap.process_layer(my_map,'wall',1)
        self.bomplist=arcade.tilemap.process_layer(my_map,'bomp',1)
        self.monsterlist=arcade.tilemap.process_layer(my_map,'monster',1)
        self.groundlist=arcade.tilemap.process_layer(my_map,'ground',1)
        self.passwordlist=arcade.tilemap.process_layer(my_map,'password',1)
        #create the physics engine
        self.physics_engine=arcade.PhysicsEngineSimple(self.player,self.walllist)
        #self.doorphysics_engine=arcade.PhysicsEngineSimple(self.player,self.doorlist)
            
            
    def on_draw(self):
        arcade.start_render()
        #draw sprites
        self.walllist.draw()
        self.bomplist.draw()
        self.monsterlist.draw()
        self.playerlist.draw()
        self.groundlist.draw()
        self.passwordlist.draw()
    #set the key for moving:use up down right left to control
    def on_key_press(self,key,modifiers):
       if key == arcade.key.UP:
               self.player.change_y=playermovementspeed
               self.player.center_y-=self.player.change_y
       elif key==arcade.key.DOWN:
               self.player.change_y=-playermovementspeed
               self.player.center_y-=self.player.change_y
       elif key==arcade.key.LEFT:
               self.player.change_x=-playermovementspeed
               self.player.center_x-=self.player.change_x
       elif key==arcade.key.RIGHT:
               self.player.change_x=playermovementspeed
               self.player.center_x-=self.player.change_x
    def on_key_release(self,key,modifiers):
       if key == arcade.key.UP:
               self.player.change_y=0
       elif key==arcade.key.DOWN:
               self.player.change_y=0
       elif key==arcade.key.LEFT:
               self.player.change_x=0
       elif key==arcade.key.RIGHT:
               self.player.change_x=0
    
    def update(self,delta_time):
       self.physics_engine.update()
       
       #self.player.update()
       #collipse with bomp, we need to pick it
       bomphitlist=arcade.check_for_collision_with_list(self.player,self.bomplist)
       for bomp in bomphitlist:
           bomp.remove_from_sprite_lists()
           #if bomp.remove_from_sprite_lists()!=0:
       if len(self.bomplist)==0:
           monsterhitlist=arcade.check_for_collision_with_list(self.player,self.monsterlist)
           for monster in monsterhitlist:   
               monster.remove_from_sprite_lists()
       if len(self.monsterlist)==0:
           if arcade.check_for_collision_with_list(self.player,self.passwordlist):
               self.input_password=True
               arcade.close_window()
        
    
        
      
#    def pomp_window(self):
#        while 1:#len(self.bomplist)==0:
#            e.msgbox('now, you have entered the game, you need to beat the monster by the bomp')
#            break
def password_guess(truepassword):
    def password_input():
        try:
            
            guesspassword=text.get()
            if guesspassword==truepassword:
                #tkinter.messagebox.askokcancel(title=None, message=None, **options)
                print(messagebox.askokcancel("hint","you have escaped"))
                
            else:
                print(messagebox.askokcancel("hint","you need to guess the new password"))
                
        except:
            print(messagebox.showerror("hint","you did not input the logical number"))
    def password_again():
        guesspassword=text.get()
    tkwindow=tkinter.Tk()
    tkwindow.title('password')
    tkwindow.geometry('300x300')
    label=tkinter.Label(tkwindow, text="guess the password")
    label.grid(row = 0)
    text = StringVar()   #设置和接收输入框的内容
    text.set('')         #输入框的默认内容
    entry = Entry(tkwindow,bg = '#ff0000')
                                   #entry单行输入框,bg为输入框背景色,font文本字体
                                   #fg 文字颜色。值为颜色或为颜色代码，如：'red','#ff0000'
    entry['textvariable'] = text   #使用textvariable将变量与Entry绑定
    entry.grid(row = 0, column =5 ,ipadx=5,ipady=5)
    button1=tkinter.Button(tkwindow, text='yes', command=password_input)
    button1.grid(row=3, column=0)
    button2=tkinter.Button(tkwindow, text='guess again', command=password_again)
    button2.grid(row=3, column=1)                               

    
    tkwindow.mainloop()    
def main():
    window=mygame()
    window.setup()
#    window.pomp_window()
    arcade.run()
    if window.input_password:
        password_guess(truepassword)
    
if __name__=="__main__":
    main()   
#class death:
#    def enter(self):
#        print("you are died!")
#        
#class the_bridge:
#    def enter(self):
#        print("there is a Gothon and this is the scene to place the bomb")
#        
#class the_escape_pod:
#    def enter(self):
#        print("you have escaped!") 
#        return the_bridge().enter()
#    
#class laser_weapon_armory:
#    def password(self):
#        self.keypad= input("input four number,each number is from 0-9")
#    def enter(self):
#        print("""this is the place you could get the neutron bomb.but
#              it has the keypad,and you need guess the right number for. """)
#        print("you need to find the bridge")
#        self.password()
#        if self.keypad=='8888':
#            print("""you have found the bomb, and now you could escape to
#                  the escape pod and bomp the ship""" )
#            return the_escape_pod().enter()
#        else:
#            print("please input the password again:")
#            return self.password()
#            
#class central_corridor:
#    def enter(self):
#        print("""you have started the adventure, and you need to tell a joke
#              to the Gothon to defeat him.""")
#        print("you need to find the laser weapon armory scene")
#        playerdo=input("tell a joke or places the bomp")
#        if playerdo=='tell a joke':
#            print("the Gothon has been beated, and you could continue the adventure.")
#            return laser_weapon_armory().enter()
#        else:
#            print("you have beated by the Gathon.")
#            return death().enter()        
        

