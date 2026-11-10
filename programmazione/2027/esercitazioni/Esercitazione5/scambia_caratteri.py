def scambia_caratteri(s, x, y):
    if not len(s) > x >= 0:
        return None    
    if not len(s) > y >= 0:
        return None
    t = x 
    x = min(x,y)
    y = max(t,y)
    r = s[:x] + s[y] + s[x+1:y] + s[x] + s[y+1:]
    return r
