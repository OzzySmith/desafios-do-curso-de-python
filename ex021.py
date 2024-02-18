#Faça um programa em python que leia um arquivo mp3 e o reproduza.
import audioplayer
song = audioplayer.AudioPlayer('musica.mp3').play(loop = True, block = True)
