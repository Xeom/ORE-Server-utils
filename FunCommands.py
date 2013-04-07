from __future__ import division

from Helper import color
from Helper import sudo


import random

import org.bukkit.Bukkit as bukkit.Bukkit

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
        sender.sendMessage(''.join([color("c"),"You must specify who you are to throw food at."]))
        return False

    food = random.randint(1,(len(foodlistitem)-1))
    receiver = bukkit.Bukkit.getPlayer(args[0])

    if receiver == None:
        sender.sendMessage(''.join([color('c'),'No such player.']))
        return False

    sudo(''.join(["give ",args[0],foodlistitem[food]," 1"]))

    if food == 1:
        bukkit.Bukkit.broadcastMessage(''.join([color("5"),sender.getName(),color("c")," threw an ",color("6"),"apple",color("c")," at ",color("5"),receiver.getName()]))

    else:
        bukkit.Bukkit.broadcastMessage(''.join([color("5"),sender.getName(),color("c")," threw a ",color("6"),foodlistname[food],color("c")," at ",color("5"),receiver.getName()]))

    if random.randint(1,5) == 1:
        receiver.addPotionEffect(PotionEffect(PotionEffectType.BLINDNESS, 40, 1, True))
        bukkit.Bukkit.broadcastMessage(''.join([color("5"),"Headshot!"]))

    return True
        
    

# Random number
@hook.command("random", description="Produce a random number.")
def onCommandRandom(sender,args):
    
    if len(args) == 1 and args[0].isdigit():
        sender.sendMessage(str(random.randint(0,int(args[0]))))
        return True
    
    if len(args) == 2 and args[0].isdigit() and args[1].isdigit():
        
        if args[0] > args[1]:
            sender.sendMessage(str(random.randint(int(args[1]),int(args[0]))))
            return True
        
        sender.sendMessage(str(random.randint(int(args[0]),int(args[1]))))
        return True
    
    if len(args) == 3 and args[0].isdigit() and args[1].isdigit() and args[2].isdigit():
        precision = 10 % int(args[2])
        sender.sendMessage(str((random.randint(precision*int(args[0]),precision*int(args[1])))/precision))
        return True
    
    if len(args) == 0:
        sender.sendMessage(str(random.randint(0,10)))
        return True
    
    sender.sendMessage(''.join([color("c"),"Use the syntax ",color("6"),"/random [a] [b]"]))
    return False

#effect
@hook.command("eff", description="Get a custom potion effect!")
def onCommandItemname(sender,args):
    
    if len(args) == 0:
        sender.sendMessage(''.join([color("c"),"You must have an argument -",color("6")," /eff [effect] [power] [duration]",color("c")," you can also use 'rem' and 'list' as effects, for special functions"]))
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
            bukkit.Bukkit.dispatchCommand(sender,''.join(["e ",args[1]]))
        return True
    
    if len(args) < 3:
        sender.sendMessage(''.join([color("c"),"You must have the correct amount of arguments -",color("6")," /eff [effect] [power] [duration]"]))
        return False
    
    for i in range(1,2):
        if args[i].isdigit() == False:
            sender.sendMessage(''.join([color("c"),"Your power and duration must be integers -",color("6")," /eff [effect] [power] [duration]"]))
            return False

    args[0] = args[0].upper()
    args[0] = args[0].replace(" ","")
    args[0] = args[0].replace(".","")

    if len(args) == 4:
        receiver = bukkit.Bukkit.getPlayer(args[3])
        if receiver == None:
            sender.sendMessage(''.join([color("c"),"Invalid player"]))
            return False
    else:
        receiver = sender

    receiver.addPotionEffect(PotionEffect(eval(''.join(["PotionEffectType.",args[0]])), int(args[2]), (int(args[1])-1)))
    
    return True

#fast
@hook.command("fast", description="Cheat at races! :D")	
def onCommandFast(sender, args):

    bukkit.Bukkit.dispatchCommand(sender,"eff rem")
    
    sender.addPotionEffect(PotionEffect(PotionEffectType.SPEED, 50000, 50, True))
    sender.addPotionEffect(PotionEffect(PotionEffectType.JUMP, 50000, 9, True))
    sender.addPotionEffect(PotionEffect(PotionEffectType.BLINDNESS, 30, 2, True))

    sender.sendMessage(''.join([color("5"),color("l"),"SUPER",color("6")," speed! :D"]))
    return True


#cp
@hook.command("cp", description="...")	
def onCommandCp(sender, args):

    sender.sendMessage("OMG, Lag!")
    
    return True
        
#love
@hook.command("love", description="<3")
def onCommandLove(sender, args):

    loves = "RSW"

    if len(args) > 0:
        loves = ' '.join(args)

    bukkit.Bukkit.broadcastMessage(''.join([color("d"),sender.getName(),color("4"),color("l")," <3 ",color("d"),loves]))

    return True
        
#hate
@hook.command("hate", description="D:")
def onCommandHate(sender, args):

    hates = "Redgame"

    if len(args) > 0:
        hates = ' '.join(args)

    bukkit.Bukkit.broadcastMessage(''.join([color("a"),sender.getName(),color("2"),color("l")," hates ",color("a"),hates]))

    return True

#hug
@hook.command("hug", description="A special command for someone you love")
def onCommandHug(sender, args):
    
    if len(args) == 0:

        sender.sendMessage(''.join([color("c"),"You must have an argument -",color("6")," /hug [thing]"]))
        return False

    if bukkit.Bukkit.getPlayer(args[0]) != None:

        receiverPlayer = bukkit.Bukkit.getPlayer(args[0])
        receiverPlayer.sendMessage(''.join([color("d"),"You were hugged by ",sender.getName()]))
        receiver = receiverPlayer.getName()
        sender.sendMessage(''.join([color("d"),"You hugged ",receiver]))

    else:

        receiver = args[0]

    bukkit.Bukkit.broadcastMessage(''.join([color(str(hex(random.randint(1,15)))[2]),color(str(hex(random.randint(1,15)))[2]),sender.getName(),color(str(hex(random.randint(1,15)))[2])," hugged ",color(str(hex(random.randint(1,15)))[2]),receiver]))
    
    return True

#fixme
@hook.command("fixme", description="removes potion effects")
def onCommandFixme(sender, args):

    if len(args) == 1:
        receiver = bukkit.Bukkit.getPlayer(args[0])
    else:
        receiver = sender

    bukkit.Bukkit.dispatchCommand(receiver,"eff rem")

    receiver.sendMessage("Removed potion effects")
        
    return True

#mushroom
@hook.command("mushroom", description="???")
def onCommandMushroom(sender, args):

    bukkit.Bukkit.dispatchCommand(sender,"eff rem")
    
    sender.sendMessage(''.join([color("a"),"You find some mushrooms on the floor ... mmm",color("2")," tasty"]))
    sender.sendMessage(''.join([color(str(random.randint(1,3))),random.choice(mushroomsayings)]))
    sender.addPotionEffect(PotionEffect(eval(''.join(["PotionEffectType.",random.choice(mushroomeffects)])), 300, 3, True))

    return True

#cake
@hook.command("cake", description="A tasty treat!")
def onCommandCake(sender, args):

    bukkit.Bukkit.dispatchCommand(sender,"eff rem")
    
    sender.sendMessage(''.join([color("9"),"You take a slice of cake - it looks so",color("6")," soft and moist"]))
    sender.sendMessage(''.join([color(str(random.randint(4,6))),random.choice(cakesayings)]))
    sender.addPotionEffect(PotionEffect(eval(''.join(["PotionEffectType.",random.choice(cakeeffects)])), 300, 3, True))

    return True
    
#quick
@hook.command("quick",description="A version of /fast, made for buliding")
def onCommandQuick(sender, args):

    bukkit.Bukkit.dispatchCommand(sender,"eff rem")
    
    sender.addPotionEffect(PotionEffect(PotionEffectType.SPEED, 50000, 3, True))
    sender.addPotionEffect(PotionEffect(PotionEffectType.JUMP, 50000, 2, True))
    sender.addPotionEffect(PotionEffect(PotionEffectType.NIGHT_VISION, 50000, 2, True))
    sender.addPotionEffect(PotionEffect(PotionEffectType.INCREASE_DAMAGE, 50000, 2, True))

    sender.sendMessage(''.join([color("9"),"Super powers!"]))

    return True
    
#choice
@hook.command("choose",description="For those hard important decisions that you can't leave to chance")
def onCommandChoose(sender, args):

    if len(args) == 0:
        sender.sendMessage(''.join([color('c'),'You must have some things to choose between']))
        return False

    sender.sendMessage(''.join([color('5'),color('l'),'You roll your magic dice!']))
    sender.sendMessage(random.choice(args))

    return True

#lol
@hook.command("lol")
def onCommandLOL(sender, args):

    bukkit.Bukkit.broadcastMessage(''.join([color('6'),sender.getName(),color('e')," lol'd"]))

    return True

