import org.bukkit.Bukkit as Bukkit

from java.util.logging import Level

def color(color):
    return u'\u00A7' + color

# Execute a command with root permissions
def sudo(command):
    Bukkit.dispatchCommand(Bukkit.getConsoleSender(), command)

def info(message):
    Bukkit.getServer().getLogger().log(Level.INFO, message)

def severe(message):
    Bukkit.getServer().getLogger().log(Level.SEVERE, message)
