from platform import uname
dchk=uname().machine.lower()
if "aarch" in dchk:
    dchk="aarch"
    print(' \033[1;32m\nYou can fuck Qsr\033[1;37m')
else:
    print(" \n\033[1;31mSorry bro you can't fuck Qsr (32bit device)\033[1;31m")
    exit()
import fuck
