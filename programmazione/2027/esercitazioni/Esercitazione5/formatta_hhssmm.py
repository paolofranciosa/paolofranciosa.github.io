#!/usr/bin/env python3
def converti_secondi(secondi):
    ore     = secondi // 3600
    minuti  = secondi  % 3600 // 60
    secondi = secondi  % 3600 %  60
    return ore, minuti, secondi

def formatta_duecifre(numero):
    return '{:02d}'.format(numero)

def formatta_hhssmm(secondi):
    ore, minuti, secondi = converti_secondi(secondi)
    stringa_ore     = formatta_duecifre(ore)
    stringa_minuti  = formatta_duecifre(minuti)
    stringa_secondi = formatta_duecifre(secondi)
    return stringa_ore + ':' + stringa_minuti + ':' + stringa_secondi
