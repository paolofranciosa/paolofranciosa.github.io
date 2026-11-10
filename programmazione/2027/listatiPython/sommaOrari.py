def orario_finale(o_i, m_i, s_i, o_d, m_d, s_d):
    s_f = s_i + s_d
    m_riporto = 0
    if s_f >= 60:
        s_f = s_f-60
        m_riporto = 1
    m_f = m_i + m_d + m_riporto
    o_riporto = 0
    if m_f >= 60:
        m_f = m_f - 60
        o_riporto = 1
    o_f = o_i + o_d + o_riporto
    g_riporto = 0
    if o_f >= 24:
        o_f = o_f - 24
        g_riporto = 1
    return o_f, m_f, s_f, g_riporto

if __name__ == "__main__":
    oi, mi, si = input("scrivi ora inizio (hh:mm:ss) ").split(sep=":")
    oi = int(oi)
    mi = int(mi)
    si = int(si)
    od, md, sd = input("scrivi durata (hh:mm:ss) ").split(sep=":")
    od = int(od)
    md = int(md)
    sd = int(sd)
    of, mf, sf, grip = orario_finale(oi, mi, si, od, md, sd)
    print(f'termina alle {of:02d}:{mf:02d}:{sf:02d} del giorno ', end="")
    if grip == 0:
        print("stesso")
    else:
        print("successivo")