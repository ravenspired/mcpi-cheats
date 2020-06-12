from mcpi import minecraft
import time

mc = minecraft.Minecraft.create()

done = False


print("Minecraft Pi Cheat client Version 1")
playerName = input("Please enter player name:")
mc.postToChat("Cheats are now enabled.")
mc.postToChat("Use the terminal to send commands.")
mc.postToChat("Use /stop to stop client.")

def processCommand(command):
    splitted = []
    splitted = str.split(command, " ")
    return splitted
    
        

def parseCommand(splitted):
    #check for basic commands with no arguements
    if(splitted[0]=="stop"):
        sendChatMessage("Quitting...")
        sendChatMessage("Goodbye.")
        exit()
    if(splitted[0]=="help"):
        sendChatMessage("Available Commands:")
        sendChatMessage("stop - stops the client")
        sendChatMessage("help - shows these texts")
        sendChatMessage("kill - kills the player")
    if(splitted[0]=="kill"):
        mc.player.setPos(0, -42069, 0)
        
        sendChatMessage("Killed "+str(playerName))
        
    else:
        sendChatMessage("Invalid Command")
        
def sendChatMessage(msg):
    print(msg)
    mc.postToChat(msg)


while True:
    
    command = input("/")
    
    parseCommand(processCommand(command))
    
    