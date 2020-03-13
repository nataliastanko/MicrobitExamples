from microbit import *

spinner1 = Image("05790:"
                 "30000:"
                 "10000:"
                 "00000:"
                 "00000")

spinner2 = Image("03570:"
                 "10009:"
                 "00000:"
                 "00000:"
                 "00000")

spinner3 = Image("01350:"
                 "00007:"
                 "00009:"
                 "00000:"
                 "00000")

spinner4 = Image("00130:"
                 "00005:"
                 "00007:"
                 "00009:"
                 "00000")

spinner5 = Image("00010:"
                 "00003:"
                 "00005:"
                 "00007:"
                 "00090")

spinner6 = Image("00000:"
                 "00001:"
                 "00003:"
                 "00005:"
                 "00970")

spinner7 = Image("00000:"
                 "00000:"
                 "00001:"
                 "00003:"
                 "09750")

spinner8 = Image("00000:"
                 "00000:"
                 "00000:"
                 "90001:"
                 "07530")

spinner9 = Image("00000:"
                 "00000:"
                 "90000:"
                 "70000:"
                 "05310")

spinner10 = Image("00000:"
                 "90000:"
                 "70000:"
                 "50000:"
                 "03100")

spinner11 = Image("09000:"
                 "70000:"
                 "50000:"
                 "30000:"
                 "01000")

spinner12 = Image("07900:"
                 "50000:"
                 "30000:"
                 "10000:"
                 "00000")

spinner = [spinner1, spinner2, spinner3, spinner4, spinner5, spinner6, spinner7, spinner8, spinner9, spinner10, spinner11, spinner12]
display.show(spinner, delay=100, wait=False, loop=True)