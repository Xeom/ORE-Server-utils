from Helper import color
import org.bukkit as bukkit

FullString = []
ResetAllPending = []
WritingNames = []
WritingLines = []

@hook.command('mb')
def onCommandMb(sender,args):
    ops = open('plugins/ThunderUtils.py.dir/RandomFiles/ops.txt')
    if ops.readlines().count(''.join([sender.getName,'\n'])) == 0:
        ops.close()
        sender.sendMessage(''.join([color('c'),'You are not an op.']))
        return False
    ops.close()
    if args[0] == 'list':
        b = open('plugins/ThunderUtils.py.dir/RandomFiles/Binds.py',"r")
        for i in b.readlines():
            if i[0] == '#':
                sender.sendMessage(i[1:len(i)-2])
    if args[0] == 'deleteall':
        sender.sendMessage(''.join([color('4'),'Are you CERTAIN you want to delete ALL MB commands?']))
        sender.sendMessage(''.join([color('4'),'Respond with /mb confirmdelete or /mb declinedelete']))
        if ResetAllPending.count(sender.getName()) == 0:
            ResetAllPending.append(sender.getName())
            return True
        return False
    if args[0] == 'confirmdelete':
        if ResetAllPending.count(sender.getName()) == 1:
            b = open('plugins/ThunderUtils.py.dir/RandomFiles/Binds.py','w')
            c = open('plugins/ThunderUtils.py.dir/RandomFiles/Template.txt')
            b.writelines(c.readlines())
            c.close()
            b.close()
            sender.sendMesage(''.join([color('a'),'Deleted']))
            return True
        sender.sendMesage(''.join([color('c'),'You have no pending deletion requests']))
        return False
    if args[0] == 'declinedelete':
        if ResetAllPending.count(sender.getName()) == 1:
            ResetAllPending.remove(sender.getName())
            sender.sendMesage(''.join([color('a'),'Not deleted']))
            return True
        sender.sendMesage(''.join([color('c'),'You have no pending deletion requests']))
        return False
    if args[0] == 'write':
        args.pop(0)
        if WritingNames.count(sender.getName()) == 0:
            WritingNames.append(sender.getName())
            WritingLines.append(args)
            sender.sendMesage(''.join([color('a'),'New command started, and written to']))
            return True
        WritingLines[WritingNames.index(sender.getName())].append(args)
        sender.sendMesage(''.join([color('a'),'Command written to']))
        return True
    if args[0] == 'done':
        if WritingNames.count(sender.getName()) == 1:
            Written = WritingLines.pop(WritingNames.index(sender.getName()))
            if complie(sender, Written = WritingLines.pop(WritingNames.index(sender.getName()))):
                WritingNames.remove(sender.getName())
                sender.sendMesage(''.join([color('a'),'Successfully written into a command']))
                return True
            WritingNames.remove(sender.getName)
            return False
        sender.sendMessage(''.join([color('c'),'You do not have anything being written']))
        return False
    if args[0] == 'new':
        args.pop(0)
        if complie(sender,args):
            sender.sendMessage(''.join([color('a'),'Successfully written into a command']))
            return True
        return False
    if args[0] == 'cancel':
        if WritingNames.count(sender.getName()) == 1:
            WritingLines.pop(WritingNames.index(sender.getName))
            WritingNames.remove(sender.getName)
            sender.sendMessage(''.join([color('a'),'Successfully cancelled']))
            return True
        sender.sendMessage(''.join([color('c'),'Nothing to cancel']))
        return False
    if args[0] == 'delete':
        b = open('plugins/ThunderUtils.py.dir/RandomFiles/Binds.py')
        if b.readlines().count(''.join(['#',args[0],'\n'])) != 0:
            delPos = b.readlines().index(''.join(['#',args[0],'\n']))
            delList = b.readlines()
            while True:
                if delList[delPos].replace('\n','') == '':
                    break
                delList.pop(delPos)
            return True
        sender.sendMessage('No such command')
        return False
    sender.sendMessage(''.join([color('a'),'List - lists all finished commands']))
    sender.sendMessage(''.join([color('a'),'ResetAll - Resets all commands (Leave it alone)']))
    sender.sendMessage(''.join([color('a'),'Write - Write a new command - This command will allow you to write more to any pending command']))
    sender.sendMessage(''.join([color('a'),'Done - Comfirm that the current "/mb write" command is done, and can be turned into code']))
    sender.sendMessage(''.join([color('a'),'New - Writes and creates a command in one command']))
    sender.sendMessage(''.join([color('a'),'Cancel - Cancels the writing of the current "/mb write" command']))
    sender.sendMessage(''.join([color('a'),'The following are flags, to be used when creating a command']))
    sender.sendMessage(''.join([color('a'),'/ - Start of a new line']))
    sender.sendMessage(''.join([color('a'),'#s Excecutes the current line as a comsole command']))
    sender.sendMessage(''.join([color('a'),'#c Writes the current line as a custom line of code']))
    sender.sendMessage(''.join([color('a'),'#b Broadcasts the current line to the server']))
    sender.sendMessage(''.join([color('a'),'The default setting is to exceute the line as a command by the sender']))
    sender.sendMessage(''.join([color('a'),'#t (only used woth #c) creates a tab']))
    sender.sendMessage(''.join([color('a'),'#p Name of the excecuter of the command']))
    sender.sendMessage(''.join([color('a'),'#n AutoCompleted name in the first argument']))
    sender.sendMessage(''.join([color('a'),'#[number] An argument of the player']))
    return True


def complie(sender,args):
    global FullString
    FullString = []
    b = open('plugins/ThunderUtils.py.dir/RandomFiles/Binds.py','r')
    if b.readlines().count(''.join(['#',CommandName,'\n'])) != 0:
        sender.sendMessage(''.join([color('c'),'That name is already in use'])) #Checks if command name is free
        b.close()
        return False
    b.close()
    if len(args) < 2:
        sender.sendMessage(''.join([color('c'),'You must have at least three arguments']))#Argument checking
        return False
    if (args[0])[0] != '/':
        sender.sendMessage(''.join([color('c'),'Your third argument must be a / or //']))
        return False
    for i in args:
        if compose(i) == False: #Split command into lines
            sender.sendMessage(''.join([color('c'),'You cannot bind a command to an MB']))
    CommandName = args.pop(0)
    CommandName = CommandName.replace('"',"") #Replace invalid characters in the name
    a = []
    b = open('plugins/ThunderUtils.py.dir/RandomFiles/Binds.py','a')
    b.write(''.join(['#',CommandName,'\n']))
    b.write(''.join(['@hook.command("'CommandName'",description="',CommandName,', by ',sender.getName,'")\n'
    b.write(''.join(['def onCommand',CommandName,'(sender,args):\n']) #Write 'introduction'
    b.close()
    argsNum = 0
    for i in FullString:
        form = 0
        if i.find("#s") != -1:
            form = 1
            i = i.replace("#s","") #Define form of line via flags
        if i.find("#b") != -1:
            form = 2
            i = i.replace("#b","")
        if i.find("#c") != -1:
            form = 3
            i = i.replace("#c","")
            i = i.replace("#t","{tab}")
            i = i.replace("#p",'sender.getName()') #Replace returning flags for custom code lines
            if i.find("#n") != -1:
                i = i.replace("#n",'(bukkit.Bukkit.getPlayer(args[0])).getName()')
                if argsNum == 0:
                    argsNum = 1
        else:
            i = i.replace('"',"") #Replace returning flags for normal lines, and get rid of invalid chars
            i = i.replace("{","")
            i = i.replace("}","")
            i = i.replace("#p",'",sender.getName(),"')
            if i.find("#n") != -1:
                i = i.replace("#n",'",(bukkit.Bukkit.getPlayer(args[0])).getName(),"')
                if argsNum == 0:
                    argsNum = 1
        i = i.replace("#","# ")
        i = i.replace("# f","#f ")
        l = i.split()
        while True:
            if l.count('#f') == 0:
                break
            if form == 3:
                l.insert(l.index("#f"),''.join(['color("',l[(l.index("#f")+1)][0],'")'])) #Replaces color flags
                l[(l.index("#f")+1)] = l[(l.index("#f")+1)][1:]
            else:
                l.insert(l.index("#f"),''.join(['",color("',l[(l.index("#f")+1)][0],'"),"']))
                l[(l.index("#f")+1)] = l[(l.index("#f")+1)][1:]
            l.remove("#f")
        while True:
            if l.count('#') == 0:
                break
            else:
                argsValue = int(l[(l.index("#")+1)])+1
                if argsValue.isdigit():
                    if argsNum < argsValue:
                        argsNum = argsValue
                    if form == 3:
                        l.insert(l.index("#f"),''.join(['args["',l[(l.index("#f")+1)][0],']'])) #Replaces argument flags
                        l[(l.index("#f")+1)] = l[(l.index("#f")+1)][1:]
                    else:
                        l.insert(l.index("#"),''.join(['",args[',l[(l.index("#")+1)][0],'],"']))
                        l[(l.index("#")+1)] = l[(l.index("#")+1)][1:]
                    l.remove("#")
                else:
                    sender.sendMessage(''.join([color('c'),'Invalid flags']))
                    delPos = b.readlines().index(''.join(['#',CommandName,'\n'])) #Deletes introductions to invalidated commands
                    delList = b.readlines()
                    while True:
                        if delList[delPos].replace('\n','') == '':
                            break
                        delList.pop(delPos)
                    return False
        i = ' '.join(l)
        if form == 1:
            a.append(''.join(['\u0009sudo("".join(["',i,'"]))\n']))
        elif form == 2:
            a.append(''.join(['\u0009bukkit.Bukkit.broadcastMessage("".join(["',i,'"]))\n']))#Appends full argument syntax
        elif form == 0:
            a.append(''.join(['\u0009bukkit.Bukkit.dispatchCommand(sender, "".join(["',i,'"]))\n']))
        elif form == 3:
            a.append(''.join([i.replace('{tab}','\u0009'),'\n']))
    a.append('\u0009return True\n')
    a.append('\n')
    b = open('plugins/ThunderUtils.py.dir/RandomFiles/Binds.py','a')
    if argsNum != 0:
        b.write(''.join(['\u0009if len(args) != ',str(argsNum),':\n']))
        b.write(''.join(['\u0009\u0009sender.sendMessage("You must have ',str(argsNum),' arguments")\n']))#Writes if statement for amount of arguments
        b.write('\u0009\u0009return False\n')
    for i in a:
        b.write(i) #Writes appends to command
    b.close()
    return True

def compose(argument):
    global FullString
    if argument[0] == '/': #Starts new lines
        FullString.append('')
        argument = argument[1:]
    FullString[(len(FullString)-1)] = ''.join([FullString[(len(FullString)-1)],argument,' ']) #Appends argument to string of line
    return True