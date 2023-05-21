from tkinter import *
import tkinter as tk
from tkinter import filedialog
import tkinter
from tkinter.tix import IMAGETEXT
import PIL
from pygame import mixer
import pygame
import customtkinter


class MP:
    def __init__(self, win):
        # Create Tkinter window
        self.root = win
        win.geometry('600x400')
        win.title('Music Player')
        win.resizable(0, 0)
        self.root.configure(background='gray')

        #Menubar
        self.menubar = Menu(self.root)
        self.root.configure(menu = self.menubar)

         #Menu
        self.submenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = 'File', menu=self.submenu)
        self.submenu.add_command(label = 'Open', command=self.load)
        self.submenu.add_command(label = 'Exit', command=self.root.destroy)

        #about function
        def about():
            tkinter.messagebox.showinfo('About us', 'Created by Sudhanshu Agnihotri')


        self.submenu2 = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = 'Help', menu=self.submenu2)
        self.submenu2.add_command(label = 'About',command=about)

        # StringVar to change button text later
        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        self.play_restart.set('Play')
        self.pause_resume.set('Pause')

        #image .jpg
        self.photo=PIL.ImageTk.PhotoImage(file='C:/Users/agnih/OneDrive/Desktop/desktop folder/apple-music-note-image3.jpg')
        photo=Label(self.root,image=self.photo,bg='gray').place(x=250,y=50)

        self.photo_p=PIL.ImageTk.PhotoImage(file='C:/Users/agnih/OneDrive/Desktop/desktop folder/play .jpg')
        photo_p=Button(self.root,image=self.photo_p,bd=0, command=self.play).place(x=22,y=51)

        self.photo_p1=PIL.ImageTk.PhotoImage(file='C:/Users/agnih/OneDrive/Desktop/desktop folder/pause .jpg')
        photo_p1=Button(self.root,image=self.photo_p1,bd=0, command=self.pause).place(x=21,y=91)

        self.photo_s=PIL.ImageTk.PhotoImage(file="C:/Users/agnih/OneDrive/Desktop/desktop folder/Stopbutton.jpg")
        photo_s=Button(self.root,image=self.photo_s, command=self.stop).place(x=20,y=131)
 

        self.photo_mute=PIL.ImageTk.PhotoImage(file='C:/Users/agnih/OneDrive/Desktop/desktop folder/speaker2.jpg')
        photo_mute=Button(self.root,image=self.photo_mute,bd=0,bg='gray').place(x=16,y=175)


       


        #label 
        self.label1=Label(self.root,text="MP3",bg='white',fg='black',font=22)
        self.label1.pack(side="bottom",fill=X)

        def volume(value):
            pygame.mixer.music.set_volume(value)


        play_button = Button(win, textvariable=self.play_restart, width=10, font=('Arial', 20), command=self.play,bg='gray')
        play_button.place(x=150, y=80, anchor='center')

        pause_button = Button(win, textvariable=self.pause_resume, width=10, font=('Arial', 20), command=self.pause,bg='gray')
        pause_button.place(x=150, y=120, anchor='center')

        stop_button = Button(win, text='Stop', width=10, font=('Arial', 20), command=self.stop,bg='gray')
        stop_button.place(x=150, y=160, anchor='center')

        slider = customtkinter.CTkSlider(win,width=160,height=16,border_width=5.5,command=volume)
        slider.place(x=150, y=200,anchor='center')

        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()
        print("Loaded: ", self.music_file)
        self.play_restart.set('Play')

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(str(self.music_file))
            mixer.music.play()
            self.playing_state = False
            self.pause_resume.set('Pause')
            self.label1['text'] = 'Music Playing...'

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
            self.pause_resume.set('Resume')
            self.play_restart.set('Restart')
            self.label1['text'] = 'Music Paused'
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_resume.set('Pause')

    def stop(self):
        mixer.music.stop()
        self.label1['text'] = 'Music Stopped'


root = Tk()
MP(root)
root.mainloop()