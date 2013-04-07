import org.bukkit.Location as Location
from Helper import color
import pickle
import time.ctime as ctime

plots = pickle.load(open("Plots.xeodata", "rb"))
players = pickle.load(open("Players.xeodata", "rb"))

@hook.command('plotwarp', description='Warp to a particular plot')
def onCommandpwarp(sender, args):
    if len(args) == 0:
        sender.sendMessage(''.join([color('c'),'/plotwarp [X] [Z]']))
        return False
    if args[0] in players:
        if len(args) == 2:
            if args[1].isdigit():
                try:
                    X = players[args[0]][0][int(args[0])][0]
                    Z = players[args[0]][0][int(args[0])][1]
                except:
                    sender.sendMessage('No such plot')
                    return False
            else:
                X = players[args[0]][0][0][0]
                Z = players[args[0]][0][0][1]
    else:
        try:
            X = int(args[0], 16)
            Z = int(args[1], 16)
        except:
            sender.sendMessage(''.join([color('c'),'Coords must be two hex values']))
            return False
    X = (X * 256) + 128
    Z = (Z * 256) + 128
    V = Location(sender.getWorld(),X,18,Z)
    sender.teleport(V)
    return True

@hook.command('claim', description='Claim a particular plot')
def onCommandClaim(sender, args):
    if len(args) == 0:
        sender.sendMessage(''.join([color('c'),'/claim [X] [Z]']))
        return False
    try:
        X = int(args[0], 16)
        Z = int(args[1], 16)
    except:
        sender.sendMessage(''.join([color('c'),'Coords must be two hex values']))
        return False
    if (X,Z) in plots:
        if plots[(X,Z)][0] == False:
            n = sender.getName()
            if not n in players:
                players[n] = [[(X,Z)],1]
                plots[(X,Z)] = [n,1,ctime()]
                sender.sendMessage('New user defined, and given a plot')
                pickle.dump(plots, open("Plots.xeodata", "wb"))
                pickle.dump(players, open("Players.xeodata", "wb"))
                return True
            else:
                p = players[n]
                if len(p[0]) < p[1]:
                    p[0].append(X,Z)
                    plots[(X,Z)] = [n,len(p[0]),ctime()]
                    sender.sendMessage('Plot claimed')
                    pickle.dump(plots, open("Plots.xeodata", "wb"))
                    pickle.dump(players, open("Players.xeodata", "wb"))
                    return True
                sender.sendMessage('You cannot claim another plot')
                return False
        sender.sendMessage('That plot is claimed, or something, I dunno..')
        return False
    sender.sendMessage('That plot does not exist yet')
    return False

@hook.command('generate', description='Generate new plots')
def onCommandGenerate(sender, args):
    if len(args) == 0:
        sender.sendMessage('/generate [diameter]')
        return False
    if args[0].isdigit():
        d = int(args[0])
        for x in range(-d,d):
            for z in range(-d,d):
                plots[(x,z)] = [False,0,'']
        pickle.dump(plots, open("Plots.xeodata", "wb"))
        sender.sendMessage(''.join(['Generated ',str((d ** 2)*4),'. plots']))
        return True

@hook.command('giveplot', description='Give someone an extra plot')
def onCommandGiveplot(sender, args):
    if args[0] in players:
        players[args[0]][1] += 1
        pickle.dump(players, open("Players.xeodata", "wb"))
        sender.sendMessage(''.join([args[0],' now has ',players[args[0]][1],' plots']))
        return True
    sender.sendMessage('Not a valid player')
    return False

@hook.command('unclaimplot', description='Unclaim a plot')
def onCommandGiveplot(sender, args):
    if len(args) == 2:
        if args[0].isdigit() and args[1].isdigit():
            X = int(args[0])
            Z = int(args[1])
            if (X,Z) in plots:
                plots[(X,Z)] = [False,0,'']
                pickle.dump(plots, open("Plots.xeodata", "wb"))
                return True
            sender.sendMessage('No such plot')
            return False
        sender.sendMessage('Your coords must be integers')
        return False
    sender.sendMessage('/unclaimplot [X] [Z]')
    return False
