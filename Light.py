import org.bukkit as b
import org.bukkit.inventory.ItemStack as ItemStack
import org.bukkit.Material as Material
import org.bukkit.enchantments.Enchantment as ench
import org.bukkit.event.block.Action as Action
import org.bukkit.potion.PotionEffectType as Effect
import org.bukkit.potion.PotionEffect as PotionEffect
import bukkit.Bukkit.broadcastMessage as broadcast

FLAMING_SHARD = ItemStack(Material.GOLD_NUGGET, 1, 1)
M = FLAMING_SHARD.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"dFlaming Shard"]))
FLAMING_SHARD.setItemMeta(M)
FLAMING_SHARD.addUnsafeEnchantment(ench.FIRE_ASPECT, 3)
FLAMING_SHARD.addUnsafeEnchantment(ench.DAMAGE_ALL, 5)

l = []
pl = []
sl = []
tl = []
lamps = False

opfile = open('build/ops.txt')
ops = []

def intLoc(loc):
    return [int(loc.getX()),int(loc.getY()),int(loc.getZ())]
def rLoc(loc,p,i):
    return b.Location(p.getWorld(),loc.getX(),loc.getY()+sl[i],loc.getZ())

@hook.command("lamps", description="See lamps!")
def onCommandLamps(sender,args):
    global lamps
    if sender.getName() in ops:
        lamps = not lamps
        if lamps:
            broadcast('Lamps have been temporarily disabled due to lag')
        else:
            broadcast('Lamps have been re-enabled')
        return True
    return False

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
    if not len(args):
        args.append('0')
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
                p.sendBlockChange(rLoc(p.getLocation(),p,i),50,0)
            else:
                p.sendBlockChange(rLoc(p.getLocation(),p,i),51,0)
            
@hook.event("block.BlockPhysicsEvent","High")
def blockChanged(event):
    if event.getBlock().getTypeId() in [123,124]:
        if lamps:
            event.setCancelled(True)


@hook.event("player.PlayerInteractEvent","Monitor")
def onPlayerClick(event):
    if event.getAction() == Action.RIGHT_CLICK_AIR:
        sender = event.getPlayer()
        if event.getItem() == FLAMING_SHARD:
            if sender in pl:
                sender.removePotionEffect(Effect.FIRE_RESISTANCE)
                i = pl.index(sender)
                sender.sendBlockChange(rLoc(l[i][1],sender,i),l[i][0].getTypeId(),0)
                pl.pop(i)
                sl.pop(i)
                tl.pop(i)
                return True
            else:
                sender.addPotionEffect(PotionEffect(Effect.FIRE_RESISTANCE, 10000, 0))
                i=len(pl)
                pl.append(sender)
                sl.append(1)
                tl.append(False)
                l.append([rLoc(sender.getLocation(),sender,i).getBlock(), sender.getLocation()])
                sender.sendBlockChange(rLoc(sender.getLocation(),sender,i),51,0)

        
