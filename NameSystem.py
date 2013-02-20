from Helper import color
from Helper import sudo

@hook.command("nameformat", description="Nameformatting! Try: /nameformat d l")
def onCommandNameformat(sender, args):
    SName=sender.getName()
    Formatting=''
    rainbow=0
    ColourWhitelist='0123456789abcdef'
    FontWhitelist='olm'
    DoStuff=1
    if len(args)>=1:
        p=sender.getServer().getPlayer(args[0])
        if p!=None:
            DoStuff=0
            onCommandNameformat(p,args[1:len(args)])
            sender.sendMessage(''.join([color("e"),'You changed ',p.getName(),"'s name formatting."]))
        else:
            if args[0]=='multi':
    			Colours=''
				ResultName=''
				for i in range(1,len(args)):
					if ColourWhitelist.find(args[i][0:1])!=-1:
						Colours+=args[i][0:1]
					else:
						sender.sendMessage(''.join(args[i][0:1],' is not permitted! You need to use a valid colour.'))
				GSize=len(SName)/float(len(Colours))
				if GSize<=1:
				   for i in range(len(SName)):
						ResultName+='&'+Colours[i:i+1]+SName[i:i+1]
				else:
					j=0
					for i in range(len(SName)):
						if i==0:
							ResultName+='&'+Colours[j:j+1]+SName[i:i+1]
						else:
							if i-1 == int((j+1)*GSize):
								j+=1
								if j<len(Colours):
									ResultName+='&'+Colours[j:j+1]+SName[i:i+1]
								else:
									ResultName+=SName[i:i+1]
							else:
								ResultName+=SName[i:i+1]

				sender.sendMessage(''.join([color("e"),'Congrats, you got a multicoloured name! ',ResultName]))
				sudo(''.join(["nick ",SName," ",ResultName]))
				DoStuff=0
            else:
                for i in args:
                    if i=='rainbow':
                        rainbow=1
                    else:
                        if ColourWhitelist.find(i[0:1])!=-1 or FontWhitelist.find(i[0:1])!=-1:
                            Formatting+='&'+i[0:1]
                        else:
                            sender.sendMessage(''.join(i[0:1],' is not permitted!'))
                            return False
    
    if DoStuff==1:
        if rainbow==0:
            sudo(''.join(["nick ",SName," ",Formatting,SName]))
            sender.sendMessage(''.join([Formatting.replace('&',u'\u00A7'),'Your name now looks like this!']))
        else:
            ResultName=''
            Colours='4c6e23915dd'
            GSize=len(SName)/10.0
            if GSize<=1:
               for i in range(len(SName)):
                    ResultName+='&'+Colours[i:i+1]+SName[i:i+1]
            else:
                j=0
                for i in range(len(SName)):
                    if i==0:
                        ResultName+='&'+Colours[j:j+1]+SName[i:i+1]
                    if i-1 == int(j*GSize):
                        j+=1
                        ResultName+='&'+Colours[j:j+1]+SName[i:i+1]
            
            sender.sendMessage(''.join([color("e"),'Congratulations! You got a rainbow name!']))
            sudo(''.join(["nick ",SName," ",ResultName]))
    return True

@hook.command("tags", description="View the tags of the RDF")
def onCommandTags(sender, args):
    sender.sendMessage(''.join([color("c"), "M", color("f"), " - Moderator"]))
    sender.sendMessage(''.join([color("4"), "A", color("f"), " - Admin"]))
    sender.sendMessage(''.join([color("4"), "F", color("f"), " - Founder"]))
    sender.sendMessage(''.join([color("4"), "SA", color("f"), " - ServerAdmin"]))
    sender.sendMessage(''.join([color("2"), "D", color("f"), " - Donator ($7-$19.99)"]))
    sender.sendMessage(''.join([color("6"), "D", color("f"), " - Donator ($20-$49.99)"]))
    sender.sendMessage(''.join([color("5"), "W", color("f"), " - Writer"]))
    sender.sendMessage(''.join([color("7"), "H", color("f"), " - Helper"]))
    sender.sendMessage(''.join([color("2"), "S", color("f"), " - Sponsor ($50-$99.99)"]))
    sender.sendMessage(''.join([color("6"), "S", color("f"), " - Sponsor ($100-$150)"]))
    sender.sendMessage(''.join([color("1"), "S", color("f"), " - Sponsor ($150+)"]))

    return True

@hook.command("tag",description="Change a user's tags")
def onCommandTag(sender, args):
    if len(args) < 3:
        return False

    # TODO: Add error checking and better formatting

    sudo(''.join(["/pex user ", args[2], " group ", args[0], args[1]]))
    return True

@hook.command("skillup", description="Promote a user.")
def onCommandSkillup(sender, args):
    return True
        
@hook.command("skilldown", description="Demote a user.")
def onCommandSkilldown(sender,args):
    return True

@hook.command("fixname")
def onCommandFixname(sender, args):
    # WIP

    return True
