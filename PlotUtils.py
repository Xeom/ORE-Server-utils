import org.bukkit.Location as Location

@hook.command('plotwarp', description='Warp to a particular plot')
def onCommaandpwarp(sender, args):
    if len(args) == 0:
        sender.sendMessage(''.join([colour('c'),'/plotwarp [X] [Y]']))
        return False
    try:
        X = int(args[0], 16)
        Z = int(args[1], 16)
    except:
        sender.sendMessage(''.join([colour('c'),'Coords must be two hex values']))
        return False
    if X and Z:
        if X > 0:
            X = X - 128
        else:
            X = X + 128
        if Z > 0:
            Z = Z - 128
        else:
            Z = Z + 128
        V = Location(sender.getWorld(),X,18,Z)
        sender.teleport(V)
        return True
