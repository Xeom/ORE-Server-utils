from Helper import color
from Helper import sudo

import org.bukkit as bukkit

#Time Commands
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

    sender.sendMessage(color("5")+"T3h lagz, they be gone!")
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
    
    elif args[0] == "2":
        sender.sendMessage("06 - "+color("4")+"Heal")
        sender.sendMessage("07 - "+color("8")+"Harm")
        sender.sendMessage("08 - "+color("3")+"Jump")
        sender.sendMessage("09 - "+color("7")+"Confusion")
        sender.sendMessage("10 - "+color("d")+"Regeneration")
        sender.sendMessage(color("6")+"Page "+color("c")+"2 "+color("6")+"of "+color("c")+"4")
        return True
    
    elif args[0] == "3":
        sender.sendMessage("11 - "+color("5")+"Damage_Resistance")
        sender.sendMessage("12 - "+color("6")+"Fire_Resistance")
        sender.sendMessage("13 - "+color("3")+"Water_Breathing")
        sender.sendMessage("14 - "+color("8")+"Invisibility")
        sender.sendMessage("15 - "+color("8")+"Blindness")
        sender.sendMessage(color("6")+"Page "+color("c")+"3 "+color("6")+"of "+color("c")+"4")
        return True
    
    elif args[0] == "4":
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

