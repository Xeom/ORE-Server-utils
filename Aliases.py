from Helper import color
from Helper import sudo
from __future__ import division

import random

import org.bukkit as bukkit

from org.bukkit.potion import PotionEffectType
from org.bukkit.potion import PotionEffect

itemnamewhitelist = "1234567890abcdeflmnok"

# Time Commands
@hook.command("day", description="Set your time to day.")
def onCommandDay(sender,args):
    
    sender.sendMessage("Your time was set to day.")
    sender.setPlayerTime(6000,0)
    
    return True

@hook.command("night", descriptoin="Set your time to night.")
def onCommandNight(sender,args):
    
    sender.sendMessage("Your time was set to night.")
    sender.setPlayerTime(18000,0)
    
    return True

# Fix lag
@hook.command("fixlag", description="Clears out minecarts,arrows,items, etc.")
def onCommandFixLag(sender, args):
    
    bukkit.Bukkit.dispatchCommand(sender, "rem items -1")
    bukkit.Bukkit.dispatchCommand(sender, "rem arrows -1")
    bukkit.Bukkit.dispatchCommand(sender, "rem boats -1")
    bukkit.Bukkit.dispatchCommand(sender, "rem xp -1")

    bukkit.Bukkit.dispatchCommand(sender, "butcher -f")

    sudo("save-all")

    sender.sendMessage("T3h lagz, they be gone!")
    return True
    
# Effects
@hook.command("e", description="List potion effect NBT values.")
def onCommandE(sender,args):
    
    if len(args) != 1:
        sender.sendMessage("01 - "+color("b")+"Speed")
        sender.sendMessage("02 - "+color("9")+"Slow")
        sender.sendMessage("03 - "+color("e")+"Fast_Digging")
        sender.sendMessage("04 - "+color("8")+"Slow_Digging")
        sender.sendMessage("05 - "+color("c")+"Increase_Damage")
        sender.sendMessage(color("6")+"Page "+color("c")+"1 "+color("6")+"of "+color("c")+"4")
        return True
    
    if args[0] == "2":
        sender.sendMessage("06 - "+color("4")+"Heal")
        sender.sendMessage("07 - "+color("8")+"Harm")
        sender.sendMessage("08 - "+color("3")+"Jump")
        sender.sendMessage("09 - "+color("7")+"Confusion")
        sender.sendMessage("10 - "+color("d")+"Regeneration")
        sender.sendMessage(color("6")+"Page "+color("c")+"2 "+color("6")+"of "+color("c")+"4")
        return True
    
    if args[0] == "3":
        sender.sendMessage("11 - "+color("5")+"Damage_Resistance")
        sender.sendMessage("12 - "+color("6")+"Fire_Resistance")
        sender.sendMessage("13 - "+color("3")+"Water_Breathing")
        sender.sendMessage("14 - "+color("8")+"Invisibility")
        sender.sendMessage("15 - "+color("8")+"Blindness")
        sender.sendMessage(color("6")+"Page "+color("c")+"3 "+color("6")+"of "+color("c")+"4")
        return True
    
    if args[0] == "4":
        sender.sendMessage("16 - "+color("1")+"Night_Vision")
        sender.sendMessage("17 - "+color("a")+"Hunger")
        sender.sendMessage("18 - "+color("8")+"Weakness")
        sender.sendMessage("19 - "+color("2")+"Poison")
        sender.sendMessage("20 - "+color("8")+"Wither")
        sender.sendMessage(color("6")+"Page "+color("c")+"4 "+color("6")+"of "+color("c")+"4")
        return True
    
    sender.sendMessage("01 - "+color("b")+"Speed")
    sender.sendMessage("02 - "+color("9")+"Slow")
    sender.sendMessage("03 - "+color("e")+"Fast_Digging")
    sender.sendMessage("04 - "+color("8")+"Slow_Digging")
    sender.sendMessage("05 - "+color("c")+"Increase_Damage")
    sender.sendMessage(color("6")+"Page "+color("c")+"1 "+color("6")+"of "+color("c")+"4")
    return True

# Show chat colors
@hook.command("c", description="Display each format with its respective character.")
def onCommandC(sender, args):
    
    sender.sendMessage(''.join([color("a"), "a ", color("b"), "b ", color("c"), "c ", color("d"), "d ", color("e"), "e ", color("f"), "f ", color("l"), "l ",color("r"),color("m"), "m",color("r")," ",color("n"), "n",color("r")," ",color("o"), "o "]))
    sender.sendMessage(''.join([color("0"), "0 ", color("1"), "1 ", color("2"), "2 ", color("3"), "3 ", color("4"), "4 ", color("5"), "5 ", color("6"), "6 ", color("7"), "7 ", color("8"), "8 ", color("9"), "9 "]))
    
    return True
    
# AFK
@hook.command("afk", description="Don't you dare.")
def onCommandAFK(sender, args):
    
    sender.sendMessage("Please do not go AFK, it wastes my bandwidth")
    sender.sendMessage("Instead, please log off the server")
    
    return True

# Save all
@hook.command("save", description="Saves the map.")
def onCommandSave(sender, args):                         
    
    sudo("save-all")
    
    return True

# Random number
@hook.command("random", description="Produce a random number.")
def onCommandRandom(sender,args):
    
    if len(args) == 1 and args[0].isdigit() == True:
        sender.sendMessage(str(random.randint(0,int(args[0]))))
        return True
    
    if len(args) == 2 and args[0].isdigit() == True and args[1].isdigit() == True:
        
        if args[0] > args[1]:
            sender.sendMessage(str(random.randint(int(args[1]),int(args[0]))))
            return True
        
        sender.sendMessage(str(random.randint(int(args[0]),int(args[1]))))
        return True
    
    if len(args) == 3 and args[0].isdigit() == True and args[1].isdigit() == True and args[2].isdigit() == True:
        sender.sendMessage(str(random.randint(int(args[2])*int(args[0]),int(args[2])*int(args[1]))/(10*int(args[2]))))
        return True
    
    if len(args) == 0:
        sender.sendMessage(str(random.randint(0,10)))
        return True
    
    sender.sendMessage(color("c")+"Use the syntax "+color("6")+"/random [a] [b]")
    return False
    
                           
# Item Renaming
@hook.command("itemname", description="Rename and recolour an item!")
def onCommandItemname(sender,args):
    
    if len(args) == 0:
        sender.sendMessage(color("c")+"You must have an argument -"+color("6")+" /itemname [name] [format1] [format2] etc.")
    addpos = 0
    namestring = list(args[0])
    
    for x in range(1,len(args)):
        addpos = addpos + 1
        for i in range(0, len(args[x])):
            
            if itemnamewhitelist.count((args[x])[i]) == 1:
                namestring.insert(addpos,color((args[x])[i]))
                addpos = addpos + 2
            
            else:
                sender.sendMessage(color("c")+"Sorry, the format "+color("6")+(args[x])[i],color("c")+"is not availible.")
    
    sender.sendMessage(str(namestring))
    
    return True

#effect
@hook.command("eff", description="Get a custom potion effect!")
def onCommandItemname(sender,args):
    
    if args[0] == "rem":
        for effect in sender.getActivePotionEffects():
            sender.removePotionEffect(effect.getType())
            return True
            
    if args[0] == "list":
        
        if len(args) < 2:
            bukkit.Bukkit.dispatchCommand(sender,"e")
        
        else:
            bukkit.Bukkit.dispatchCommand(sender,"e "+args[1])
        return True
    
    if len(args) < 3:
        sender.sendMessage(c
        return False
    
    for i in range(1,2):
        if args[i].isdigit() == False:
            sender.sendMessage(color("c")+"Your potion duration and power must be integers -"+color("6")+" /eff [Effect] [Power] [Duration]")
            return False
    
    args[0] = args[0].upper()
    args[0] = args[0].replace(" ","")
    args[0] = args[0].replace(".","")
    
    sender.addPotionEffect(PotionEffect(eval("PotionEffectType."+args[0]), int(args[2]), int(args[1])))
    
    return True
    
#fast
@hook.command("fast", description="Cheat at races! :D")	
def onCommandFast(sender, args):
    
    sender.addPotionEffect(PotionEffect(PotionEffectType.SPEED, 50000, 50, True))
    sender.addPotionEffect(PotionEffect(PotionEffectType.JUMP, 50000, 9, True))
    sender.addPotionEffect(PotionEffect(PotionEffectType.BLINDNESS, 30, 2, True))
    sender.sendMessage(color("5")+color("l")+"SUPER"+color("6")+" speed! :D")
    
    return True
        
#love
@hook.command("love")
def onCommandLove(sender, args):
    
    if len(args) == 0:
        bukkit.Bukkit.broadcastMessage(color("d")+sender.getName()+color("4")+color("l")+" <3 "+color("d")+"RSW")
        return True
    
    else:
        bukkit.Bukkit.broadcastMessage(color("d")+sender.getName()+color("4")+color("l")+" <3 "+color("d")+args[0])
        return True
        
#hate
@hook.command("hate")
def onCommandLove(sender, args):
    
    if len(args) == 0:
        bukkit.Bukkit.broadcastMessage(color("a")+sender.getName()+color("2")+color("l")+" hates "+color("a")+"chavs")
        return True
    
    else:
        bukkit.Bukkit.broadcastMessage(color("a")+sender.getName()+color("2")+color("l")+" hates "+color("a")+args[0])
        return True

#hug
@hook.command("hug")
def onCommandHug(sender, args):
    
    if len(args) == 0:
        sender.sendMessage(color("c")+"You must have an argument -"+color("6")+" /hug [player]")
        return False
    
    if Bukkit.getPlayer(args[0]) != "null":
        sender.sendMessage(color("d")+"You hugged "+args[0])
        Bukkit.getPlayer(args[0]).sendMessage(color("d")+sender.getName()+" hugged you!")
        return True
    
    else:
        
        return False
        
#brohug
@hook.command("hug")
def onCommandBrohug(sender, args):
    
    if len(args) == 0:
        sender.sendMessage(color("c")+"You must have an argument -"+color("6")+" /brohug [player]")
        return True
    
    if Bukkit.getPlayer(args[0]) != "null":
        sender.sendMessage(color("2")"You brohugged "+args[0])
        Bukkit.getPlayer(args[0]).sendMessage(color("2")+sender.getName()+" brohugged you!")
        return True
    
    else:
        
        return False
