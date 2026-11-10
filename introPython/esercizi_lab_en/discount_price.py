#!/usr/bin/env python3

def discount_price(prezzo, percentuale):
    if prezzo < 0 or percentuale < 0:
        return None
    return round(prezzo - prezzo/100 * percentuale, 1)
