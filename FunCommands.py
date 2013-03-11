from __future__ import division

from Helper import color
from Helper import sudo


import random

import org.bukkit as bukkit

from org.bukkit.potion import PotionEffectType
from org.bukkit.potion import PotionEffect

itemnamewhitelist = "1234567890abcdeflmnok"
mushroomeffects = ["SLOW", "CONFUSION", "BLINDNESS"]
mushroomsayings = ["You feel a tad off", "Melons...Oh god melons!", "Hmm..  needs more salt", "You don't feel your best", "You shouldn't be that color...", "You feel dizzy..."]
cakeeffects = ["SPEED", "JUMP", "NIGHT_VISION"]
cakesayings = ["So nommy!", "You want another!", "Mmmmmmmmmm"]
foodlistitem = [' 260', ' 282',        ' 297',         ' 319',    ' 349',' 354',' 357',  ' 360',          ' 364', ' 365',   ' 391',  ' 392',  ' 400']
foodlistname = ['apple','bowl of soup','loaf of bread','porkchop','fish','cake','cookie','slice of melon','steak','chicken','carrot','potato','pie']


#food fight
@hook.command("foodfight", description="A polite mealtime activity")
def onCommandFoodfight(sender,args):
    if len(args) == 0:
        sender.sendMessage("You must specify who you are to throw food at")
        return False
    food = random.randint(1,len(foodlistitem))
    receiver=bukkit.Bukkit.getPlayer(args[0])
    if receiver == 'null':
        sender.sendMessage(color('c')+'No such player.')
        return False
    sudo("give "+args[0]+foodlistitem[food]+" 1")
    if food == 1:
        bukkit.Bukkit.broadcastMessage(color("6")+sender+color("c")+" threw an"+color("6")+" apple"+color("c")+" at"+color("6")+args[0])
    else:
        bukkit.Bukkit.broadcastMessage(color("6")+sender+color("c")+" threw a"+color("6")+foodlistname[food]+color("c")+" at"+color("6")+args[0])
    if random.randint(1,5) == 1:
        receiver.addPotionEffect(PotionEffect(PotionEffectType.BLINDNESS, 30, 2, True))
        bukkit.Bukkit.broadcastMessage(color("5")+"Headshot!")
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
        return Truesender.addPotionEffect(PotionEffect(PotionEffectType.BLINDNESS, 30, 2, True))
    
    if len(args) == 3 and args[0].isdigit() == True and args[1].isdigit() == True and args[2].isdigit() == True:
        precision = 10 % int(args[2])
        sender.sendMessage(str((random.randint(precision*int(args[0]),precision*int(args[1])))/precision))
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
    
    if len(args) == 0:
        sender.sendMessage(color("c")+"You must have an argument -"+color("6")+" /eff [effect] [power] [duration]"+color("c")+" you can also use 'rem' and 'list' as effects, for special functions")
        return False
    
    if args[0] == "rem":
        if len(args) < 2:
            for effect in sender.getActivePotionEffects():
                sender.removePotionEffect(effect.getType())
            return True
        elif int(args[1]) < sender.getActivePotionEffects():
            effect = sender.getActivePotionEffects()[int(args[1])]
            sender.removePotionEffect(effect.getType())
            return True
    if args[0] == "list" and len(args) > 0:
        
        if len(args) < 2:
            bukkit.Bukkit.dispatchCommand(sender,"e")
        
        else:
            bukkit.Bukkit.dispatchCommand(sender,"e "+args[1])
        return True
    
    if len(args) < 3:
        sender.sendMessage(color("c")+"You must have the correct amount of arguments -"+color("6")+" /eff [effect] [power] [duration]")
        return False
    
    for i in range(1,2):
        if args[i].isdigit() == False:
            sender.sendMessage(color("c")+"Your potion duration and power must be integers -"+color("6")+" /eff [Effect] [Power] [Duration]")
            return False

    args[0] = args[0].upper()
    args[0] = args[0].replace(" ","")
    args[0] = args[0].replace(".","")
    
    sender.addPotionEffect(PotionEffect(eval("PotionEffectType."+args[0]), int(args[2]), (int(args[1])-1)))
    
    return True

#fast
@hook.command("fast", description="Cheat at races! :D")	
def onCommandFast(sender, args):

    bukkit.Bukkit.dispatchCommand(sender,"eff rem")
    
    sender.addPotionEffect(PotionEffect(PotionEffectType.SPEED, 50000, 50, True))
    sender.addPotionEffect(PotionEffect(PotionEffectType.JUMP, 50000, 9, True))
    sender.addPotionEffect(PotionEffect(PotionEffectType.BLINDNESS, 30, 2, True))

    sender.sendMessage(color("5")+color("l")+"SUPER"+color("6")+" speed! :D")
    
    return True
        
#love
@hook.command("love", description="<3")
def onCommandLove(sender, args):
    
    if len(args) == 0:
        bukkit.Bukkit.broadcastMessage(color("d")+sender.getName()+color("4")+color("l")+" <3 "+color("d")+"RSW")
        return True
    
    else:
        bukkit.Bukkit.broadcastMessage(color("d")+sender.getName()+color("4")+color("l")+" <3 "+color("d")+args[0])
        return True
        
#hate
@hook.command("hate", description="D:")
def onCommandHate(sender, args):
    
    if len(args) == 0:
        bukkit.Bukkit.broadcastMessage(color("a")+sender.getName()+color("2")+color("l")+" hates "+color("a")+"redgame")
        return True
    
    else:
        bukkit.Bukkit.broadcastMessage(color("a")+sender.getName()+color("2")+color("l")+" hates "+color("a")+args[0])
        return True

#hug
@hook.command("hug", description="A special command for someone you love")
def onCommandHug(sender, args):
    
    if len(args) == 0:
        sender.sendMessage(color("c")+"You must have an argument -"+color("6")+" /hug [thing]")
        return False
    
    sender.sendMessage(color("d")+"You hugged "+args[0])
    bukkit.Bukkit.broadcastMessage(color(str(hex(random.randint(1,15)))[2])+color(str(hex(random.randint(1,15)))[2])+sender.getName()+color(str(hex(random.randint(1,15)))[2])+" hugged "+color(str(hex(random.randint(1,15)))[2])+args[0])
    
    return True

#fixme
@hook.command("fixme", description="removes potion effects")
def onCommandFixme(sender, args):

    bukkit.Bukkit.dispatchCommand(sender,"eff rem")
    sender.sendMessage("Removed potion effects")

    return True

#mushroom
@hook.command("mushroom", description="???")
def onCommandMushroom(sender, args):

    bukkit.Bukkit.dispatchCommand(sender,"eff rem")
    
    sender.sendMessage(color("a")+"You find some mushrooms on the floor ... mmm"+color("2")+" tasty")
    sender.sendMessage(color(str(random.randint(1,3)))+random.choice(mushroomsayings))
    sender.addPotionEffect(PotionEffect(eval("PotionEffectType."+random.choice(mushroomeffects)), 300, 3, True))

    return True

#cake
@hook.command("cake", description="A tasty treat!")
def onCommandCake(sender, args):

    bukkit.Bukkit.dispatchCommand(sender,"eff rem")
    
    sender.sendMessage(color("9")+"You take a slice of cake - it looks so"+color("6")+" soft and moist")
    sender.sendMessage(color(str(random.randint(4,6)))+random.choice(cakesayings))
    sender.addPotionEffect(PotionEffect(eval("PotionEffectType."+random.choice(cakeeffects)), 300, 3, True))

    return True
    
#quick
@hook.command("quick",description="A version of /fast, made for buliding")
def onCommandQuick(sender, args):

    bukkit.Bukkit.dispatchCommand(sender,"eff rem")
    
    sender.addPotionEffect(PotionEffect(PotionEffectType.SPEED, 50000, 3, True))
    sender.addPotionEffect(PotionEffect(PotionEffectType.JUMP, 50000, 2, True))
    sender.addPotionEffect(PotionEffect(PotionEffectType.NIGHT_VISION, 50000, 2, True))
    sender.addPotionEffect(PotionEffect(PotionEffectType.INCREASE_DAMAGE, 50000, 2, True))

    sender.sendMessage(color("9")+"Super powers!")

    return True
    

