#Rust Gambling Sites
import os
import sys
import urllib

import chunk as chunk
import requests
from bs4 import BeautifulSoup
import csv
import json
import lxml

from urllib.request import urlopen
import ctypes

ruststake = '    127.0.0.1       ruststake.com'
rustdrop = '    127.0.0.1       rust-drop.com'
rustchance = '    127.0.0.1       rustchance.com'
rustypot = '    127.0.0.1       rustypot.com'
rustreaper = '    127.0.0.1       rustreaper.com'
banditcamp = '    127.0.0.1       bandit.camp'
rustignite = '    127.0.0.1       rustignite.com'
rustysaloon = '    127.0.0.1       rustysaloon.com'
rustmoment = '    127.0.0.1       rustmoment.com'
howl = '    127.0.0.1       howl.gg'
rustclash = '    127.0.0.1       rustclash.com'
rustcases = '    127.0.0.1       rustcases.com'
rustkingdom = '    127.0.0.1       rustkingdom.gg'
rustcase = '    127.0.0.1       rustcase.com'

#Trading Sites & Buying Sites
tradeit = '    127.0.0.1       tradeit.gg'
csdeals = '    127.0.0.1       cs.deals'
skinport = '    127.0.0.1       skinport.com'
gamerall = '    127.0.0.1       gamerall.com'
vmarket = '    127.0.0.1       vmarket.gg'
gameflip = '    127.0.0.1       gameflip.com'
bitskins = '    127.0.0.1       bitskins.com'
kinguin = '    127.0.0.1       kinguin.com'
swap = '    127.0.0.1       swap.gg'
lootfarm = '    127.0.0.1       loot.farm'

#Regular & CS:GO Sites
stake = '    127.0.0.1       stake.com'
gamdom = '    127.0.0.1       gamdom.com'
csgoempire = '    127.0.0.1       csgoempire.com'
wtfskins = '    127.0.0.1       wtfskins.com'
datdrop = '    127.0.0.1       datdrop.com'
hellcases = '    127.0.0.1       hellcases.com'
csgofast = '    127.0.0.1       csgofast.com'
csgoroll = '    127.0.0.1       csgoroll.com'
csgo500 = '    127.0.0.1       csgo500.com'
keydrop = '    127.0.0.1       key-drop.com'
csgopolygon = '    127.0.0.1       csgopolygon.com'
thunderpick = '    127.0.0.1       thunderpick.com'
skinbet = '    127.0.0.1       skinbet.gg'
hellstore = '    127.0.0.1       hellstore.net'
bounty = '    127.0.0.1       bounty.gg'

hosts = open("C:\Windows\System32\drivers\etc\hosts", "r")
readfile = hosts.read()
hostsappend = open("C:\Windows\System32\drivers\etc\hosts", "a")
hosts2 = "C:\Windows\System32\drivers\etc\hosts"


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    print("WIP")
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def yes_or_no(question):
    answer = input(question + "(y/n): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Input yes or no")
        answer = input(question + "(y/n):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False



if yes_or_no("Would you like to block regular gambling sites & CS:GO gambling sites?"):
    print("Now blocking gambling sites & CS:GO gambling sites.")
    if skinbet in readfile:
        print('SkinBet is already listed. ')
    else:
        hostsappend.write("\n" + skinbet)
        print('SkinBet has been blocked.')
    if thunderpick in readfile:
        print('ThunderPick is already listed. ')
    else:
        hostsappend.write("\n" + thunderpick)
        print('ThunderPick has been blocked.')
    if csgopolygon in readfile:
        print('CSGOPolygon is already listed. ')
    else:
        hostsappend.write("\n" + csgopolygon)
        print('CSGOPolygon has been blocked.')
    if keydrop in readfile:
        print('KeyDrop is already listed. ')
    else:
        hostsappend.write("\n" + keydrop)
        print('KeyDrop has been blocked.')
    if csgo500 in readfile:
        print('CSGO500 is already listed. ')
    else:
        hostsappend.write("\n" + csgo500)
        print('CSGO500 has been blocked.')
    if stake in readfile:
        print('Stake is already listed. ')
    else:
        hostsappend.write("\n" + stake)
        print('Stake has been blocked.')
    if gamdom in readfile:
        print('GamDom is already listed. ')
    else:
        hostsappend.write("\n" + gamdom)
        print('GamDom has been blocked.')
    if csgoempire in readfile:
        print('CsgoEmpire is already listed. ')
    else:
        hostsappend.write("\n" + csgoempire)
        print('CsgoEmpire has been blocked.')
    if wtfskins in readfile:
        print('WTFSkins is already listed. ')
    else:
        hostsappend.write("\n" + wtfskins)
        print('WTFSkins has been blocked.')
    if datdrop in readfile:
        print('DatDrop is already listed. ')
    else:
        hostsappend.write("\n" + datdrop)
        print('DatDrop has been blocked.')
    if hellcases in readfile:
        print('HellCases is already listed. ')
    else:
        hostsappend.write("\n" + hellcases)
        print('HellCases has been blocked.')
    if csgofast in readfile:
        print('CsgoFast is already listed. ')
    else:
        hostsappend.write("\n" + csgofast)
        print('CsgoFast has been blocked.')
    if csgoroll in readfile:
        print('CSGORoll is already listed. ')
    else:
        hostsappend.write("\n" + csgoroll)
        print('CSGORoll has been blocked.')
    if hellstore in readfile:
        print('HellStore is already listed. ')
    else:
        hostsappend.write("\n" + hellstore)
        print('HellStore has been blocked.')
    if bounty in readfile:
        print('Bounty is already listed. ')
    else:
        hostsappend.write("\n" + bounty)
        print('Bounty has been blocked.')
else:
    print("Regular gambling sites & CS:GO gambling sites were not blocked.")

if yes_or_no("Would you like to block skin-gambling sites?"):
    print("Now blocking skin-gambling sites.")
    if ruststake in readfile:
        print('RustStake is already listed. ')
    else:
        hostsappend.write("\n" + ruststake)
        print('RustStake has been blocked.')
    if rustdrop in readfile:
        print('Rust-Drop is already listed. ')
    else:
        hostsappend.write("\n" + rustdrop)
        print('Rust-Drop has been blocked.')
    if rustchance in readfile:
        print('RustChance is already listed. ')
    else:
        hostsappend.write("\n" + rustchance)
        print('RustChance has been blocked.')
    if rustypot in readfile:
        print('Rustypot is already listed. ')
    else:
        hostsappend.write("\n" + rustypot)
        print('Rustypot has been blocked.')
    if howl in readfile:
        print('Howl is already listed. ')
    else:
        hostsappend.write("\n" + howl)
        print('Howl has been blocked.')
    if rustclash in readfile:
        print('RustClash is already listed. ')
    else:
        hostsappend.write("\n" + rustclash)
        print('RustClash has been blocked.')
    if rustreaper in readfile:
        print('RustReaper is already listed. ')
    else:
        hostsappend.write("\n" + rustreaper)
        print('RustReaper has been blocked.')
    if banditcamp in readfile:
        print('BanditCamp is already listed. ')
    else:
        hostsappend.write("\n" + banditcamp)
        print('BanditCamp has been blocked.')
    if rustmoment in readfile:
        print('RustMoment is already listed. ')
    else:
        hostsappend.write("\n" + rustmoment)
        print('RustMoment has been blocked.')
    if rustignite in readfile:
        print('RustIgnite is already listed. ')
    else:
        hostsappend.write("\n" + rustignite)
        print('RustIgnite has been blocked.')
    if rustysaloon in readfile:
        print('RustySaloon is already listed. ')
    else:
        hostsappend.write("\n" + rustysaloon)
        print('RustySaloon has been blocked.')
    if rustkingdom in readfile:
        print('RustKingdom is already listed. ')
    else:
        hostsappend.write("\n" + rustkingdom)
        print('RustKingdom has been blocked.')
    if rustcase in readfile:
        print('RustCase is already listed. ')
    else:
        hostsappend.write("\n" + rustcase)
        print('RustCase has been blocked.')
    if rustcases in readfile:
        print('RustCases is already listed. ')
    else:
        hostsappend.write("\n" + rustcases)
        print('RustCases has been blocked.')
else:
    print("No skin-gambling sites were blocked.")

if yes_or_no("Would you like to block skin-purchasing sites?"):
    print("Now blocking skin-purchasing sites.")
    if tradeit in readfile:
        print('Tradeit is already listed. ')
    else:
        hostsappend.write("\n" + tradeit)
        print('Tradeit has been blocked.')
    if csdeals in readfile:
        print('CsDeals is already listed. ')
    else:
        hostsappend.write("\n" + csdeals)
        print('CsDeals has been blocked.')
    if gamerall in readfile:
        print('GamerAll is already listed. ')
    else:
        hostsappend.write("\n" + gamerall)
        print('GamerAll has been blocked.')
    if gameflip in readfile:
        print('GameFlip is already listed. ')
    else:
        hostsappend.write("\n" + gameflip)
        print('GameFlip has been blocked.')
    if skinport in readfile:
        print('SkinPort is already listed. ')
    else:
        hostsappend.write("\n" + skinport)
        print('SkinPort has been blocked.')
    if vmarket in readfile:
        print('Vmarket is already listed. ')
    else:
        hostsappend.write("\n" + vmarket)
        print('Vmarket has been blocked.')
    if bitskins in readfile:
        print('BitSkins is already listed. ')
    else:
        hostsappend.write("\n" + bitskins)
        print('BitSkins has been blocked.')
    if swap in readfile:
        print('Swap is already listed. ')
    else:
        hostsappend.write("\n" + swap)
        print('Swap has been blocked.')
    if lootfarm in readfile:
        print('LootFarm is already listed. ')
    else:
        hostsappend.write("\n" + lootfarm)
        print('LootFarm has been blocked.')
else:
    print("No skin-purchasing sites were blocked.")

if yes_or_no("Would you like to block Kinguin?"):
    print("Now blocking Kinguin.")
    if kinguin in readfile:
        print('Kinguin is already listed. ')
    else:
        hostsappend.write("\n" + kinguin)
        print('Kinguin has been blocked.')
else:
    print("Kinguin was not blocked.")

restart = input("Do you wish to restart the computer now in order to enact these changes? (yes/no): ")
if restart == 'no':
    exit()
elif restart == "yes":
    os.system("shutdown /r /t 1")
else:
    print("Invalid input- this input has been read as no!")



#file1 = open("../../Desktop/Anti-Gambling/hosts", "w")
#file1.write("\n")
#file1.write("    182.0.0.1 https://rustypot.com")
#file1 = open("../../Desktop/Anti-Gambling/hosts", "r")
#print("Output of Readlines after appending")
#print(file1.read())
#print()
#file1.close()