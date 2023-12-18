# ZbrozekFinal
# Programmer: Mike Zbrozek
# Email: MZbrozek1@cnm.edu
# Purpose: Metronone GUI - read in song list from dictionary to count time for songs I like. 
#Files associated with this assignment - metronome.py, spotify.py, metronome_songs.txt
# Spotify.py uses Spotipy library to call various spotify api endpoints, grabs a playlist, gets track ID from the playlist, queries the audio analysis endpoint for tempo and time_signature data.
# and writes to txt file.



from tkinter import *
from tkinter import ttk
import winsound
from winsound import Beep
import os
import ast

# Create metronome class, and it's corresponding methods
class Metronome:
    def __init__(self, tk, beats, songList):
        
        self.tk = tk
        self.beats = beats
        self.songList = songList
        
        self.start = False
        self.bpm = 0
        self.count = 1
        self.beat = 0
        self.time = 0

        self.string_var = StringVar()
        self.int_var = IntVar()
        self.string_var.set(self.count)

        self.interface()

    def interface(self):
        '''tkinter interface'''
       # Interface for the metronome app.
        frame = Frame(background="SkyBlue3")
        frame.pack()

        entry = Entry(frame, width=8, justify="center")
        entry.insert(0, "60")
        entry.grid(row=0, column=0, padx=10, sticky="E")

        r1 = Radiobutton(frame, background="SkyBlue3", text="clave", variable=self.int_var, value=1, command=self.sound)
        r1.grid(row = 0, column=2, padx=5, pady=5, sticky = "E")    

        r2 = Radiobutton(frame, background="SkyBlue3", text="beep", variable=self.int_var, value=2, command=self.sound)
        r2.grid(row = 0, column=3, padx=5, pady=5, sticky = "E")

        spinbox = Spinbox(frame, width=5, values=self.beats, wrap=True)
        spinbox.grid(row = 0, column=1, padx=5, pady=5, sticky = "E")

        bpm_label = Label(frame, background="SkyBlue3",text = "BPM:")
        bpm_label.grid(row=0, column=0, sticky = "W")

        time_label = Label(frame,background="SkyBlue3", text = "Time:")
        time_label.grid(row=0, column=1, padx =5, sticky = "W")

        song_select_label = Label(frame, background="SkyBlue3", text = "Select a song from the options below: ")
        song_select_label.grid(row=1, column=0, padx =5, sticky = "W")

        song_select_dd = ttk.Combobox(frame, state='readonly', values= self.songList, width = 75)
        song_select_dd.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

        count_label = Label(frame, textvariable = self.string_var, font=("Sans Serif Collection", 48))
        count_label.grid(row=3, column=0, columnspan=3, padx=20, pady=5)

        start_button = Button(frame, text="Start", width=10, height=2, command = lambda: self.start_counter(entry, spinbox, song_select_dd))
        start_button.grid(row=4, column=0, padx = 10, sticky= "W")

        stop_button = Button(frame, text="Stop", width=10, height=2, command = lambda: self.stop_counter(song_select_dd))
        stop_button.grid(row=4, column=1, padx=10, sticky="E")
    

    def sound(self):
        '''checks to see if the radio buttons are selected.
        Default is a beep'''
        if (self.int_var.get() == 1):
            return winsound.PlaySound("Clave.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
        else:
            return Beep(500, 100)
    
    def start_counter(self, entry, spinbox, song_select_dd):
        '''Start counter if self.start is False
        Check to see if a song was selected from the comboBox selector, sets self.bpm object and runs counter method '''
        
        if not self.start:
            if str(song_select_dd.get()):
                try:
                    newString = (song_select_dd.get())
                    data = newString.split(" ")
                    self.bpm = float((data[len(data) -2]))
                    print(f"song bpm = {self.bpm}")
                except ValueError:
                    self.bpm = 60
            else:
                try:
                    self.bpm = int(entry.get())
                except ValueError:
                    self.bpm = 60
        else:
            # bpm cannot exceed 300
            if self.bpm > 300:
                self.bpm = 300

        self.start = True
        self.counter(spinbox, song_select_dd)

    def stop_counter(self, song_select_dd):
        '''clears the comboBox selection, sets self.start to False'''
        song_select_dd.set('')
        self.start = False
    
    def counter(self, spinbox, song_select_dd):
        '''Start counter if self.start is True
        Check to see if a song was selected from the comboBox selector, sets self.time object and calculates metronome delay values.
         
          Controls timing of sounds and increments the counter. '''
        if self.start:
            if (song_select_dd.get()):
               newString = (song_select_dd.get())
               data = newString.split(" ")
               self.beat = int((data[len(data) -1])[0])
               print(f"song time = {self.beat}")

            else: self.beat = int(spinbox.get()[0])

            if self.beat == 6: # 6/8 time signature
                self.time = int((60 / (self.bpm / .5) - 0.1) * 1000)
            else: 
                self.time = int((60 / self.bpm - 0.1) * 1000) # Calculate delay in ms

            self.count += 1
            self.string_var.set(self.count)

            if self.count == 1:
                Beep(900, 100) 
            elif self.count >= self.beat:
                self.count = 0
            else:
                self.sound()

            self.tk.after(self.time, lambda: self.counter(spinbox, song_select_dd))

    def open_songs_file():
        '''Populate the dropdown menu with songs from .txt file'''
        f = open("metronome_songs.txt", "r")
        data = []
        songList = []
        while True:
            line = f.readline().strip()
            if not line: break
            list = ast.literal_eval(line)
            data.append(list)
        print(data)
        for val in data: 
             resultlist = [*val.values()]
             songList.append(resultlist)
        return songList

            
                

def main():
    '''Runs the main method, instantiates the Metronome object'''
    tk = Tk()
    tk.title("Metronome")

    beats = ["4/4", "6/8", "2/4", "3/4"]
    sounds = []
    
    songList = Metronome.open_songs_file()
    Metronome(tk, beats, songList)
    print(songList)
    tk.mainloop()

if __name__ == "__main__":
    main()