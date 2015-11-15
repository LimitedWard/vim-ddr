import pygame
import sys
import time
import math
import os


def calculateMS(startTime):
	return math.trunc((time.time() - startTime) * 1000)

def writeToFile(sumNum, timeTaken, file):
	file.write("[" + str(sumNum) + "," + str(timeTaken) + "]," + "\n")


def main():

    pygame.init()
    BLACK = (0,0,0)
    RED = (255,255,255)
    WIDTH = 1280
    HEIGHT = 1024
    windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    startTime = 0
    currentTime = 0
    started = True
    windowSurface.fill(BLACK)
    fName = 'notes.txt'
    pygame.mixer.music.load('./public/assets/harder_better_faster_stronger.ogg')

    f = open(fName, 'w')

    gameLoop = True
    started = True
    f.write("var arrayLevel = [")
    while gameLoop:
        if(started):
            pygame.mixer.music.play(-1,0)
            startTime = time.time()
            started = False

        events = pygame.event.get()
        for event in events:
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_h):
                    writeToFile(1, calculateMS(startTime), f)
                elif(event.key == pygame.K_j):
                    writeToFile(2, calculateMS(startTime), f)
                elif(event.key == pygame.K_k):
                    writeToFile(4, calculateMS(startTime), f)
                elif(event.key == pygame.K_l):
                    writeToFile(8, calculateMS(startTime), f)
                elif(event.key == pygame.K_h and event.key == pygame.K_j):
                    writeToFile(3, calculateMS(startTime), f)
                elif(event.key == pygame.K_h and event.key == pygame.K_k):
                    writeToFile(5, calculateMS(startTime), f)
                elif(event.key == pygame.K_h and event.key == pygame.K_l):
                    writeToFile(9, calculateMS(startTime), f)
                elif(event.key == pygame.K_j and event.key == pygame.K_k):
                    writeToFile(6, calculateMS(startTime), f)
                elif(event.key == pygame.K_j and event.key == pygame.K_l):
                    writeToFile(10, calculateMS(startTime), f)
                elif(event.key == pygame.K_k and event.key == pygame.K_l):
                    writeToFile(12, calculateMS(startTime),f)
                elif(event.key == pygame.K_h and event.key == pygame.K_j and event.key == pygame.K_k):
                    writeToFile(7, calculateMS(startTime), f)
                elif(event.key == pygame.K_h and event.key == pygame.K_j and event.key == pygame.K_l):
                    writeToFile(11, calculateMS(startTime), f)
                elif(event.key == pygame.K_h and event.key == pygame.K_k and event.key == pygame.K_l):
                    writeToFile(13, calculateMS(startTime), f)
                elif(event.key == pygame.K_j and event.key == pygame.K_k and event.key == pygame.K_l):
                    writeToFile(14, calculateMS(startTime), f)
                elif(event.key == pygame.K_h and event.key == pygame.K_j and event.key == pygame.K_k and event.key == pygame.K_l):
                    writeToFile(15, calculateMS(startTime), f)
                elif(event.key == pygame.K_c):
                    gameLoop = False

    f.write("];\nmodule.exports.arrayLevel = arrayLevel;")
    f.close()


    files = os.listdir(os.curdir)
    for file in files:
        if '.txt' in file:
            if(os.path.isfile(fName[:-4] + '.js')):
                os.remove(os.curdir + '/notes.js')
            newfile = file.replace('.txt', '.js')
            os.rename(file, newfile)
            break
                
main()

