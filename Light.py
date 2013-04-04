import org.bukkit as b

FLAMING_SHARD = i(Material.GOLD_NUGGET, 1, 1)
M = FLAMING_SHARD.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"dFlaming Shard"]))
FLAMING_SHARD.addUnsafeEnchantment(ench.FIRE_ASPECT, 4)
FLAMING_SHARD.setItemMeta(M)

l = []
pl = []
sl = []
tl = []

def intLoc(loc):
    return [int(loc.getX()),int(loc.getY()),int(loc.getZ())]
def rLoc(loc,p,i):
    return b.Location(p.getWorld(),loc.getX(),loc.getY()+sl[i],loc.getZ())

@hook.command("light", description="Toggles a nice light!")
def onCommandLight(sender,args):
    if sender in pl:
        i = pl.index(sender)
        sender.sendBlockChange(rLoc(l[i][1],sender,i),l[i][0].getTypeId(),0)
        pl.pop(i)
        sl.pop(i)
        tl.pop(i)
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
        tl.append(True)
        l.append([rLoc(sender.getLocation(),sender,i).getBlock(), sender.getLocation()])
        sender.sendBlockChange(rLoc(sender.getLocation(),sender,i),50,0)
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
            if tl[i]:
                b = 51
            else:
                b = 50
            p.sendBlockChange(rLoc(p.getLocation(),p,i),b,0)
            

@hook.event("player.PlayerItemHeldEvent","Monitor")
def onPlayerClick(event):
    ep = event.getPlayer()
    if ep.getItemInHand() == FLAMING_SHARD:
        i=len(pl)
        pl.append(sender)
        sl.append(3)
        tl.append(False)
        l.append([rLoc(ep.getLocation(),ep,i).getBlock(), ep.getLocation()])
        ep.sendBlockChange(rLoc(p.getLocation(),ep,i),51,0)
    elif ep in pl:
        if not tl[pl.index(pl)]:
            i = pl.index(ep)
            ep.sendBlockChange(rLoc(l[i][1],ep,i),l[i][0].getTypeId(),0)
            pl.pop(i)
            sl.pop(i)
            tl.pop(i)
