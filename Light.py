import org.bukkit as b

l = []
pl = []
sl = []

def intLoc(loc):
    return [int(loc.getX()),int(loc.getY()),int(loc.getZ())]
def rLoc(loc,p,i):
    return b.Location(p.getWorld(),loc.getX(),loc.getY()+sl[i],loc.getZ())

@hook.command("light", description="Toggles a nice light!")
def onCommandLight(sender,args):
    if sender in pl:
        i = pl.index(sender)
        sender.sendBlockChange(rLoc(l[i][1],sender,i),l[i][0].getTypeId(),0)
        pl[i]=None
        sl[i]=None
        sender.sendMessage("You turned off your light.")
        return True
    if len(args)!=1:
        sender.sendMessage("This command requires 1 argument: Height of lamp in blocks")
        return False
    else:
        try:
            q=int(args[0])
        except:
            sender.sendMessage("Your argument should be a number.")
            return False
        i=len(pl)
        pl.append(sender)
        sl.append(q)
        l.append([rLoc(sender.getLocation(),sender,i).getBlock(), sender.getLocation()])
        sender.sendBlockChange(rLoc(sender.getLocation(),sender,i),89,0)
        sender.sendMessage("You got a light!")
    return True

@hook.event("player.PlayerMoveEvent","Monitor")
def onPlayerMove(event):
    p=event.getPlayer()
    if p in pl:
        i=pl.index(p)
        if intLoc(p.getLocation()) != intLoc(l[i][1]):
            p.sendBlockChange(rLoc(l[i][1],p,i),l[i][0].getTypeId(),0)
            rLoc(l[i][1],p,i).getBlock().getState().update()
            l[i]=[rLoc(p.getLocation(),p,i).getBlock(), p.getLocation()]
            p.sendBlockChange(rLoc(p.getLocation(),p,i),89,0)
            
