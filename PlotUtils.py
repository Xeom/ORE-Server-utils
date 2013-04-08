import org.bukkit.Location as Location
from Helper import color
import pickle
import time.ctime as ctime

#Loading xeodata files
plots = pickle.load(open("Plots.xeodata", "rb"))
players = pickle.load(open("Players.xeodata", "rb"))

#Loading op files
opfile = open('plugins/ThunderUtils.py.dir/RandomFiles/ops.txt')
ops = []

#Generating List of ops
for i in opfile.readlines():
    ops.append(i.replace('\n',''))

def infreturn(i, sender):
    sender.sendMessage(i)

def redreturn(i, sender):
    sender.sendMessage(''.join([color('c'),i]))


@hook.command('pwarp', description='Warp to a particular plot')
def onCommandpwarp(sender, args):
    if len(args) == 0:
        redreturn('/pwarp [X] [Z] |OR| /pwarp [player]', sender)
        return False
    if args[0].lower() in players:
        if len(args) == 2:
            if args[1].isdigit():
                try:
                    C = players[args[0].lower()][0][int(args[1])]
                    X = C[0]
                    Z = C[1]
                except:
                    infreturn('No such plot', sender)
                    return False
        else:
            C = players[args[0].lower()][0][0]
            X = C[0]
            Z = C[1]
    else:
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
    V = Location(sender.getWorld(),(X * 256) + 128,18,(Z * 256) + 128)
    if O[0] != False:
        infreturn(''.join(['Teleporting to ',O[0],"'s plot #",str(plots[(X,Z)][1]),'; ',str(X),',',str(Z)]), sender)
    else:
        infreturn(''.join(['Teleporting to plot ',str(X),',',str(Z),' - Unclaimed']), sender)
    sender.teleport(V)
    return True

@hook.command('pclaim', description='Claim a particular plot')
def onCommandClaim(sender, args):
    if len(args) == 0:
        redreturn('/claim [X] [Z]', sender)
        return False
    try:
        X = int(args[0])
        Z = int(args[1])
    except:
        redreturn('Coords must be two values', sender)
        return False
    if (X,Z) in plots:
        if plots[(X,Z)][0] == False:
            n = sender.getName().lower()
            if not n in players:
                players[n] = [[(X,Z)],1]
                plots[(X,Z)] = [n,1,ctime()]
                T = ctime().split()
                mapgen(X,Z,True,[n,'Plot #1','Claimed:',' '.join([T[1],T[2],T[4]])])
                infreturn('New user defined, and given a plot', sender)
                pickle.dump(plots, open("Plots.xeodata", "wb"))
                pickle.dump(players, open("Players.xeodata", "wb"))
                return True
            else:
                p = players[n]
                if len(p[0]) < p[1]:
                    p[0].append((X,Z))
                    plots[(X,Z)] = [n,len(p[0]),ctime()]
                    infreturn('Plot claimed', sender)
                    pickle.dump(plots, open("Plots.xeodata", "wb"))
                    pickle.dump(players, open("Players.xeodata", "wb"))
                    return True
                infreturn('You cannot claim another plot', sender)
                return False
        infreturn('That plot is claimed, or something, I dunno..', sender)
        return False
    infreturn('That plot does not exist yet', sender)
    return False

@hook.command('pgenerate', description='Generate new plots')
def onCommandGenerate(sender, args):
    if not sender.getName() in ops:
        redreturn('No permission', sender)
        return False
    if len(args) == 0:
        infreturn('/generate [diameter]', sender)
        return False
    if args[0].isdigit():
        d = int(args[0])
        for x in range(-d,d):
            for z in range(-d,d):
                if plots.get((x,z)) == None:
                    plots[(x,z)] = [False,0,'']
                    mapgen(x,z,False,['Unclaimed'])
        pickle.dump(plots, open("Plots.xeodata", "wb"))
        infreturn(''.join(['Generated ',str((d ** 2)*4),'. plots']), sender)
        return True

@hook.command('pgive', description='Give someone an extra plot')
def onCommandGiveplot(sender, args):
    if not sender.getName() in ops:
        redreturn('No permission', sender)
        return False
    if len(args) == 0:
        redreturn('/giveplot [player]', sender)
    n = args[0].lower()
    if n in players:
        players[n][1] += 1
        pickle.dump(players, open("Players.xeodata", "wb"))
        infreturn(''.join([n,' now has ',str(players[n][1]),' plots']), sender)
        return True
    infreturn('Not a valid player', sender)
    return False

@hook.command('punclaim', description='Unclaim a plot')
def onCommandUnclaim(sender, args):
    if len(args) == 2:
        if args[0].isdigit() and args[1].isdigit():
            X = int(args[0])
            Z = int(args[1])
            if (X,Z) in plots:
                if plots[(X,Z)][0] != False:
                    if plots[(X,Z)][0] == sender.getName().lower():
                        players[plots[(X,Z)][0]][0].remove((X,Z))
                        plots[(X,Z)] = [False,0,'']
                        mapgen(X,Z,False,['Unclaimed'])
                        pickle.dump(plots, open("Plots.xeodata", "wb"))
                        pickle.dump(players, open("Players.xeodata", "wb"))
                        infreturn('Plot unclaimed', sender)
                        return True
            infreturn('No such plot', sender)
            return False
        infreturn('Your coords must be integers', sender)
        return False
    infreturn('/unclaimplot [X] [Z]', sender)
    return False

@hook.command('psearch', description='Search for a user or plot')
def onCommandPsearch(sender, args):
    if len(args) == 0:
        redreturn('/psearch [Criteria]', sender)
        return False
    if args[0].lower() in players:
        p = players[args[0].lower()]
        for i, v in enumerate(p[0]):
            infreturn(''.join([color('6'),'Plot #',color('e'),str(i)]), sender)
            infreturn(''.join([color('e'),str(v)]), sender)
            infreturn(' '.join([color('6'),'Claimed ',color('e'),''.join(plots[v][2].split())]), sender)
        return True
    if len(args) == 2:
        if args[0].isdigit() and args[1].isdigit():
            if (int(args[0]),int(args[1])) in plots:
                p = plots[(args[0],args[1])]
                if p[0] != False:
                    infreturn(''.join([color('6'),'Claimed by ',color('e'),p[0]]), sender)
                    infreturn(''.join([color('6'),'Claimed ',color('e'),''.join(p[2].split())]), sender)
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

def mapgen(X,Z,C,T): ###RED MAKE ME###
    print 'At X '+str(X)+'and Z '+str(Z)
    if C:
        print 'Lit'
    else:
        print 'Unlit'
    for I in T:
        print I

@hook.command('pusers', description='Lists all users')
def userlist(sender, args):
    t = list(players)
    t.sort()
    infreturn(', '.join(t), sender)
    return True
