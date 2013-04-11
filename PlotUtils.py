import org.bukkit.Location as Location
from Helper import color
from Helper import sudo
import pickle
import time.ctime as ctime
import org.bukkit.block.Block.setTypeIdAndData as setBlock
import org.bukkit.Bukkit.getWorld as getWorld
import org.bukkit.World.getBlockAt as getBlock
import org.bukkit.block.Sign.setLine as setLine

config = open('Plots.config')

Conf = {'MiddleLayerEdge' : [155, 2],
        'BaseLayerFiller' : [155, 0],
        'XLineEdgeFiller' : [155, 0],
        'ZLineEdgeFiller' : [155, 0],
        'XCenteralFiller' : [155, 0],
        'ZCenteralFiller' : [155, 0],
        'IsClaimedBottom' : [152, 0],
        'IsClaimedSymbol' : [124, 0],
        'UnclaimedBottom' : [0,   0],
        'UnclaimedSymbol' : [123, 0],
        'SymbolXEdgeLine' : [155, 3],
        'SymbolZEdgeLine' : [155, 4],
        'MapSymbolCorner' : [155, 1],
        'PlotMapPosition' : [0,30,0],
        'PlotEdgeLengths' : [256   ],
        }

for i in config.readlines():
    if i.find('#') != -1:
        i = i[:i.find('#')]
    l = i.replace('\n','').split()
    if len(l) > 1:
        n = l.pop(0)
        if n in Conf:
            c = []
            for p in l:
                try:
                    c.append(int(p))
                except:
                    c.append(0)
                    print 'Error while reading config!'
                    print i
                else:
                    Conf[n] = c

Xpos = Conf['PlotMapPosition'][0]
Ypos = Conf['PlotMapPosition'][1]
Zpos = Conf['PlotMapPosition'][2]
PlotSize = Conf['PlotEdgeLengths'][0]

#Loading xeodata files
plots = pickle.load(open("build/Plots.xeodata", "rb"))
players = pickle.load(open("build/Players.xeodata", "rb"))
    
#Loading op files
opfile = open('build/ops.txt')
ops = []

for i in opfile.readlines():
    ops.append(i.replace('\n',''))

opfile.close()

def infreturn(i, sender):
    sender.sendMessage(''.join([color('6'),i]))

def redreturn(i, sender):
    sender.sendMessage(''.join([color('c'),i]))

def getMapRelative(sender):
    loc = sender.getLocation()
    X = int(loc.getX())
    Z = int(loc.getZ())
    X-=Xpos
    Z-=Zpos+1
    if X > 0:
        X-=1
    else:
        X+=1
    if Z > 0:
        Z-=1
    else:
        Z+=1
    return (X//3,Z//3)

def getMapReverse(X,Z):
    X = X*3
    Z = Z*3
    if X < 0:
        X-=1
    else:
        X+=1
    if Z < 0:
        Z-=1
    else:
        Z+=1
    return (X+Xpos+2,Z+Zpos+2)

def getlocdual(sender):
    if getMapRelative(sender) in plots:
        return getMapRelative(sender)
    if getloc(sender) in plots:
        return getloc(sender)
    return False

def getloc(sender):
    loc = sender.getLocation()
    X = int(loc.getX())
    Z = int(loc.getZ())
    return (X//PlotSize,Z//PlotSize)

def mapgen(Xa,Za,C,E):
    V = getMapReverse(Xa,Za)
    X = V[0]
    Z = V[1]
    if C:
        Cb = Conf['IsClaimedBottom'][0]
        Cd = Conf['IsClaimedBottom'][1]
    else:
        Cb = Conf['UnclaimedBottom'][0]
        Cd = Conf['UnclaimedBottom'][1]
    for x in range(-1,1):
        for z in range(-1,1):
            getWorld('build').getBlockAt(X+x,Ypos-1,Z+z).setTypeIdAndData(Cb, Cd, False)
    if C:
        Cb = Conf['IsClaimedSymbol'][0]
        Cd = Conf['IsClaimedSymbol'][1]
    else:
        Cb = Conf['UnclaimedSymbol'][0]
        Cd = Conf['UnclaimedSymbol'][1]
    for x in range(-1,1):
        for z in range(-1,1):
            getWorld('build').getBlockAt(X+x,Ypos,Z+z).setTypeIdAndData(Cb, Cd, False)
    for x in range(-1,1):
        getWorld('build').getBlockAt(X+x,Ypos,Z+1).setTypeIdAndData(Conf['SymbolXEdgeLine'][0], Conf['SymbolXEdgeLine'][1], False)
    for z in range(-1,1):
        getWorld('build').getBlockAt(X+1,Ypos,Z+z).setTypeIdAndData(Conf['SymbolZEdgeLine'][0], Conf['SymbolZEdgeLine'][1], False)
    if E:
        for x in range(-1,1):
            getWorld('build').getBlockAt(X+x,Ypos,Z-2).setTypeIdAndData(Conf['SymbolXEdgeLine'][0], Conf['SymbolXEdgeLine'][1], False)
        for z in range(-1,1):
            getWorld('build').getBlockAt(X-2,Ypos,Z+z).setTypeIdAndData(Conf['SymbolZEdgeLine'][0], Conf['SymbolZEdgeLine'][1], False)
    getWorld('build').getBlockAt(X+1,Ypos,Z+1).setTypeIdAndData(Conf['MapSymbolCorner'][0], Conf['MapSymbolCorner'][1], False)
    if E:
        getWorld('build').getBlockAt(X+1,Ypos,Z-2).setTypeIdAndData(Conf['MapSymbolCorner'][0], Conf['MapSymbolCorner'][1], False)
        getWorld('build').getBlockAt(X-2,Ypos,Z+1).setTypeIdAndData(Conf['MapSymbolCorner'][0], Conf['MapSymbolCorner'][1], False)
        getWorld('build').getBlockAt(X-2,Ypos,Z-2).setTypeIdAndData(Conf['MapSymbolCorner'][0], Conf['MapSymbolCorner'][1], False)

def mapLines(D):
    for x in range(-2-(3*D),(3*D)+3):
        getWorld('build').getBlockAt(Xpos+x,Ypos,Zpos).setTypeIdAndData(Conf['XCenteralFiller'][0], Conf['XCenteralFiller'][1], False)
        getWorld('build').getBlockAt(Xpos+x,Ypos,Zpos+2+(3*D)).setTypeIdAndData(Conf['XLineEdgeFiller'][0], Conf['XLineEdgeFiller'][1], False)
        getWorld('build').getBlockAt(Xpos+x,Ypos,Zpos-2-(3*D)).setTypeIdAndData(Conf['XLineEdgeFiller'][0], Conf['XLineEdgeFiller'][1], False)
        getWorld('build').getBlockAt(Xpos+x,Ypos-1,Zpos+2+(3*D)).setTypeIdAndData(Conf['MiddleLayerEdge'][0], Conf['MiddleLayerEdge'][1], False)
        getWorld('build').getBlockAt(Xpos+x,Ypos-1,Zpos-2-(3*D)).setTypeIdAndData(Conf['MiddleLayerEdge'][0], Conf['MiddleLayerEdge'][1], False)
    for z in range(-2-(3*D),(3*D)+3):
        getWorld('build').getBlockAt(Xpos,Ypos,Zpos+z).setTypeIdAndData(Conf['ZCenteralFiller'][0], Conf['ZCenteralFiller'][1], False)
        getWorld('build').getBlockAt(Xpos+2+(3*D),Ypos,Zpos+z).setTypeIdAndData(Conf['ZLineEdgeFiller'][0], Conf['ZLineEdgeFiller'][1], False)
        getWorld('build').getBlockAt(Xpos-2-(3*D),Ypos,Zpos+z).setTypeIdAndData(Conf['ZLineEdgeFiller'][0], Conf['ZLineEdgeFiller'][1], False)
        getWorld('build').getBlockAt(Xpos+2+(3*D),Ypos-1,Zpos+z).setTypeIdAndData(Conf['MiddleLayerEdge'][0], Conf['MiddleLayerEdge'][1], False)
        getWorld('build').getBlockAt(Xpos-2-(3*D),Ypos-1,Zpos+z).setTypeIdAndData(Conf['MiddleLayerEdge'][0], Conf['MiddleLayerEdge'][1], False)
        for x in range(-2-(3*D),(3*D)+3):
            getWorld('build').getBlockAt(Xpos+x,Ypos-2,Zpos+z).setTypeIdAndData(Conf['BaseLayerFiller'][0], Conf['BaseLayerFiller'][1], False)

###Start of commands###

@hook.command('ploc', description='Find the plot you are on')
def onCommandsPloc(sender, args):
    l = getlocdual(sender)
    if l:
        infreturn(''.join([color('e'),str(l)]),sender)
        if plots[l][0] == False:
            infreturn('Unclaimed',sender)
        else:
            infreturn(''.join(['Claimed by ',plots[l][0]]),sender)
        return True
    redreturn('No such plot',sender)
    return False

    
@hook.command('pwarp', description='Warp to a particular plot')
def onCommandpwarp(sender, args):
    X = 0
    Y = 0
    if len(args) == 0:
        if getMapRelative(sender) in plots:
            X = getMapRelative(sender)[0]
            Z = getMapRelative(sender)[1]
        else:
            redreturn('/pwarp [X] [Z] OR /pwarp [player]', sender)
            return False
    elif args[0] in players:
        if len(args) == 2:
            if args[1].replace('-','').isdigit():
                try:
                    C = players[args[0]][0][int(args[1])-1]
                    X = C[0]
                    Z = C[1]
                except:
                    infreturn('No such plot', sender)
                    return False
        else:
            C = players[args[0]][0][0]
            X = C[0]
            Z = C[1]
    elif len(args) == 2:
        try:
            X = int(args[0])
            Z = int(args[1])
        except:
            redreturn('Coords must be two values', sender)
            return False
    O = plots.get((X,Z))
    if O == None:
        infreturn('No such plot', sender)
        return False
    V = Location(sender.getWorld(),(X * PlotSize) + (PlotSize/2),18,(Z * PlotSize) + (PlotSize/2))
    if O[0] != False:
        infreturn(''.join(['Teleporting to ',O[0],"'s plot #",str(plots[(X,Z)][1]),'; ',str(X),',',str(Z)]), sender)
    else:
        infreturn(''.join(['Teleporting to plot ',str(X),',',str(Z),' - Unclaimed']), sender)
    sender.teleport(V)
    return True

@hook.command('pclaim', description='Claim a particular plot')
def onCommandClaim(sender, args):
    global plots, players
    if not len(args):
        l = getlocdual(sender)
        if l:
            args.append(str(l[0]))
            args.append(str(l[1]))
        else:
            redreturn('/punclaim [X] [Z]', sender)
            return False
    try:
        X = int(args[0])
        Z = int(args[1])
    except:
        redreturn('/claim [X] [Z]', sender)
        return False
    if (X,Z) in plots:
        if plots[(X,Z)][0] == False:
            n = sender.getName()
            if not n in players:
                players[n] = [[(X,Z)],1]
                plots[(X,Z)] = [n,1,ctime()]
                T = ctime().split()
                mapgen(X,Z,True,False)
                infreturn('New user defined, and given a plot', sender)
                saveall()
                return True
            else:
                p = players[n]
                if len(p[0]) < p[1]:
                    p[0].append((X,Z))
                    plots[(X,Z)] = [n,len(p[0]),ctime()]
                    infreturn('Plot claimed', sender)
                    T = ctime().split()
                    mapgen(X,Z,True,False)
                    saveall()
                    return True
                infreturn('You cannot claim another plot', sender)
                return False
        infreturn('That plot is claimed, or something, I dunno..', sender)
        return False
    infreturn('That plot does not exist yet', sender)
    return False


@hook.command('pgenerate', description='Generate new plots')
def onCommandGenerate(sender, args):
    global plots, players
    if not sender.getName() in ops:
        redreturn('No permission', sender)
        return False
    if len(args) == 0:
        infreturn('/generate [diameter]', sender)
        return False
    if args[0].isdigit():
        d = int(args[0])
        i = 0
        for x in range(-d,d):
            for z in range(-d,d):
                if plots.get((x,z)) == None:
                    plots[(x,z)] = [False,0,'']
                    if x == -d or x == d-1 or z == -d or z == d-1 or x == 0 or z == 0:
                        E = True
                    else:
                        E = False
                    mapgen(x,z,False,E)
                    mapLines(d)
                    i+=1
        saveall()
        infreturn(''.join(['Generated ',str(i),'. plots']), sender)
        return True

@hook.command('pgive', description='Give someone an extra plot')
def onCommandGiveplot(sender, args):
    global players
    if not sender.getName() in ops:
        redreturn('No permission', sender)
        return False
    if len(args) == 0:
        redreturn('/pgive [player]', sender)
    n = args[0]
    if n in players:
        players[n][1] += 1
        saveall()
        return True
    infreturn('Not a valid player', sender)
    return False

@hook.command('ptake', description='Take away the ability to claim an extra plot')
def onCommandGiveplot(sender, args):
    global players
    if not sender.getName() in ops:
        redreturn('No permission', sender)
        return False
    if len(args) == 0:
        redreturn('/ptake [player]', sender)
    n = args[0]
    if n in players:
        if len(players[n][0]) == players[n][1]:
            redreturn('That player must have a plot unclaimed first', sender)
            return False
        players[n][1] -= 1
        saveall()
        infreturn(''.join([n,' now can have ',str(players[n][1]),' plots']), sender)
        return True
    infreturn('Not a valid player', sender)
    return False

@hook.command('punclaim', description='Unclaim a plot')
def onCommandUnclaim(sender, args):
    global players, plots
    if not len(args):
        l = getlocdual(sender)
        if l:
            args.append(str(l[0]))
            args.append(str(l[1]))
        else:
            redreturn('/punclaim [X] [Z]', sender)
            return False
    if len(args) == 2:
        if args[0].replace('-','').isdigit() and args[1].replace('-','').isdigit():
            X = int(args[0])
            Z = int(args[1])
            if (X,Z) in plots:
                if plots[(X,Z)][0] != False:
                    if plots[(X,Z)][0] == sender.getName() or sender.getName() in ops:
                        players[plots[(X,Z)][0]][0].remove((X,Z))
                        plots[(X,Z)] = [False,0,'']
                        mapgen(X,Z,False,False)
                        saveall()
                        infreturn('Plot unclaimed', sender)
                        return True
                    redreturn('You do not own that plot', sender)
                    return False
            redreturn('No such plot', sender)
            return False
        redreturn('Your coords must be integers', sender)
        return False
    redreturn('/punclaim [X] [Z]', sender)
    return False

@hook.command('psearch', description='Search for a user or plot')
def onCommandPsearch(sender, args):
    if not len(args):
        l = getlocdual(sender)
        if l:
            args.append(str(l[0]))
            args.append(str(l[1]))
        else:
            redreturn('/psearch [X] [Z] OR [Name] OR [Partial]', sender)
    if args[0] in players:
        p = players[args[0]]
        for i, v in enumerate(p[0]):
            infreturn(''.join(['Plot #',color('e'),str(i)]), sender)
            infreturn(''.join([color('e'),str(v)]), sender)
            infreturn(''.join(['Claimed ',color('e'),' '.join(plots[v][2].split())]), sender)
        return True
    if len(args) == 1:
        for i in players:
            if i.lower().find(args[0].lower()) != -1:
                infreturn(''.join([color('e'),'']), sender)
                for a, v in enumerate(players[i][0]):
                    infreturn(i, sender)
                    infreturn(''.join([color('6'),'Plot #',color('e'),str(a+1)]), sender)
                    infreturn(''.join([color('e'),str(v)]), sender)
                    infreturn(''.join([color('6'),'Claimed ',color('e'),' '.join(plots[v][2].split())]), sender)
        return True
    if len(args) == 2:
        if args[0].replace('-','').isdigit() and args[1].replace('-','').isdigit():
            if (int(args[0]),int(args[1])) in plots:
                p = plots[(int(args[0]),int(args[1]))]
                if p[0] != False:
                    infreturn(''.join([color('6'),'Claimed by ',color('e'),p[0]]), sender)
                    infreturn(''.join([color('6'),'Claimed ',color('e'),' '.join(p[2].split())]), sender)
                    return True
                else:
                    infreturn('Unclaimed', sender)
                    return True
            redreturn('Plot not generated', sender)
            return False
        redreturn('Your coords must be numeric', sender)
        return False
    redreturn('/psearch [Criteria]', sender)
    return False

        
@hook.command('pusers', description='Lists all users')
def userlist(sender, args):
    t = list(players)
    t.sort()
    infreturn(', '.join(t), sender)
    return True

def saveall():
    pickle.dump(plots, open("build/Plots.xeodata", "wb"))
    pickle.dump(players, open("build/Players.xeodata", "wb"))
    return
