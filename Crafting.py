import org.bukkit.Material as Material
import org.bukkit.inventory.ItemStack as i
import org.bukkit.inventory.ShapelessRecipe as s
import org.bukkit.Bukkit.getServer as getServer
import org.bukkit.enchantments.Enchantment as ench

GRINDSTONE = i(Material.FLINT, 5, 1)
M = GRINDSTONE.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','rGrindstone']))
GRINDSTONE.setItemMeta(M)

GOLD_DUST = i(Material.GLOWSTONE_DUST, 1, 1)
M = GOLD_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bGold Dust']))
GOLD_DUST.setItemMeta(M)

IRON_DUST = i(Material.SUGAR, 1, 1)
M = IRON_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bIron Dust']))
IRON_DUST.setItemMeta(M)

NETHER_DUST = i(Material.REDSTONE, 1, 1)
M = NETHER_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bNether Dust']))
NETHER_DUST.setItemMeta(M)

METAL_DUST = i(Material.SULPHUR, 1, 1)
M = METAL_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bMetal Dust']))
METAL_DUST.setItemMeta(M)

STONE_DUST = i(Material.SULPHUR, 1, 2)
M = STONE_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bStone Dust']))
STONE_DUST.setItemMeta(M)

EARTHEN_DUST = i(Material.SULPHUR, 1, 3)
M = EARTHEN_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bEarthen Dust']))
EARTHEN_DUST.setItemMeta(M)

FIREY_DUST = i(Material.REDSTONE, 1, 2)
M = FIREY_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bFirey Dust']))
M.setLore(['A burning powder'])
FIREY_DUST.addEnchantment(ench.FIRE_ASPECT, 1)
FIREY_DUST.setItemMeta(M)

MAGICIANS_POWDER = i(Material.SUGAR, 1, 2)
M = MAGICIANS_POWDER.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"bMagician's Powder"]))
MAGICIANS_POWDER.setItemMeta(M)

SPELLBOOK = i(Material.ENCHANTED_BOOK, 1, 1)
M = SPELLBOOK.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"dSpellbook"]))
SPELLBOOK.setItemMeta(M)

FIREY_INGOT = i(Material.BRICK, 1, 1)
M = FIREY_INGOT.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"bFirey Ingot"]))
FIREY_INGOT.setItemMeta(M)

MAGICIANS_INGOT = i(Material.IRON_INGOT, 1, 1)
M = MAGICIANS_INGOT.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"bMagician's Ingot"]))
MAGICIANS_INGOT.setItemMeta(M)

R = s(GRINDSTONE)
R.addIngredient(Material.FLINT, 0)
R.addIngredient(Material.COBBLESTONE, 0)
getServer().addRecipe(R)

R = s(GOLD_DUST)
R.addIngredient(Material.FLINT, 1)
R.addIngredient(Material.GOLD_INGOT, 0)
getServer().addRecipe(R)

R = s(IRON_DUST)
R.addIngredient(Material.FLINT, 1)
R.addIngredient(Material.IRON_INGOT, 0)
getServer().addRecipe(R)

R = s(NETHER_DUST)
R.addIngredient(Material.FLINT, 1)
R.addIngredient(Material.NETHERRACK, 0)
getServer().addRecipe(R)

R = s(METAL_DUST)
R.addIngredient(Material.SUGAR, 1)
R.addIngredient(Material.GLOWSTONE_DUST, 1)
getServer().addRecipe(R)

R = s(STONE_DUST)
R.addIngredient(Material.FLINT, 1)
R.addIngredient(Material.STONE, 0)
getServer().addRecipe(R)

R = s(EARTHEN_DUST)
R.addIngredient(Material.SULPHUR, 2)
R.addIngredient(Material.SULPHUR, 1)
getServer().addRecipe(R)

R = s(FIREY_DUST)
R.addIngredient(Material.SULPHUR, 0)
R.addIngredient(Material.REDSTONE, 1)
getServer().addRecipe(R)

R = s(MAGICIANS_POWDER)
R.addIngredient(Material.GLOWSTONE_DUST, 0)
R.addIngredient(Material.REDSTONE, 0)
R.addIngredient(Material.REDSTONE, 2)
R.addIngredient(Material.SULPHUR, 1)
getServer().addRecipe(R)

R = s(SPELLBOOK)
R.addIngredient(Material.BOOK, 0)
R.addIngredient(Material.SUGAR, 2)
getServer().addRecipe(R)
	
R = s(FIREY_INGOT)
R.addIngredient(Material.SULPHUR, 1)
R.addIngredient(Material.IRON_INGOT, 1)
R.addIngredient(Material.REDSTONE, 2)
getServer().addRecipe(R)

R = s(i(Material.IRON_INGOT, 4, 0))
R.addIngredient(Material.SUGAR, 1)
R.addIngredient(Material.SUGAR, 1)
R.addIngredient(Material.SUGAR, 1)
R.addIngredient(Material.GLOWSTONE_DUST, 1)
R.addIngredient(Material.REDSTONE, 0)
getServer().addRecipe(R)

R = s(i(Material.GOLD_INGOT, 4, 0))
R.addIngredient(Material.SUGAR, 1)
R.addIngredient(Material.GLOWSTONE_DUST, 1)
R.addIngredient(Material.GLOWSTONE_DUST, 1)
R.addIngredient(Material.GLOWSTONE_DUST, 1)
R.addIngredient(Material.REDSTONE, 0)
getServer().addRecipe(R)
