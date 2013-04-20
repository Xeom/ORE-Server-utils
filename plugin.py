from Helper import color

import FunAliases
import Aliases
import FunCommands

import Light

import Derps
import BindCommand

import NameSystem
import OnlinePlayers

import usefulCommands
import PlotUtils

import Crafting

@hook.enable
def onEnable():
    Derps.load_derps("OREUtilsFiles/derps.txt")
    return True

@hook.disable
def onDisable():
    PlotUtils.saveall()
    for i in range(0, 100):
        print 'CATS'
    return True



