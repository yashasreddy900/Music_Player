# Music player in python

from pygame import mixer

mixer.init()#mixer for loading and playing sounds
# --------------------------Path of your music
song="D://SONGS//JARVIS.mp3"

mixer.music.load(song)      #this wil lopad the file into player

mixer.music.set_volume(0.5) #can be any value between 0 to 1

mixer.music.play()          #this is the function to play the music



while True:
    print("Press 'p' to pause")  #if you press 'p', thrn music will pause
    
    print("Press 'r' to resume") #if you press 'p', thrn music will resume
    
    print("Press 'v' set volume") #if you press 'p', thrn music wiill set volume
    
    print("Press 'e' to exit")     #if you press 'p', thrn music will exit from player
    

    ch = input("['p','r','v','e']>>>")

    if ch == "p":
        mixer.music.pause()

        
    elif ch == "r":
        mixer.music.unpause()

        
    elif ch == "v":
        v = float(input("Enter volume(0 to 1): "))
        mixer.music.set_volume(v)

        
    elif ch == "e":
        mixer.music.stop()


        break   #break after all the processes

 
