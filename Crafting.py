import org.bukkit.Material as Material
import org.bukkit.inventory.ItemStack as i
import org.bukkit.inventory.ShapelessRecipe as s
import org.bukkit.inventory.ShapedRecipe as sh
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
METAL_DUST.addUnsafeEnchantment(ench.DIG_SPEED, 1)

STONE_DUST = i(Material.SULPHUR, 1, 2)
M = STONE_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bStone Dust']))
STONE_DUST.setItemMeta(M)

EARTHEN_DUST = i(Material.SULPHUR, 1, 3)
M = EARTHEN_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bEarthen Dust']))
EARTHEN_DUST.setItemMeta(M)
EARTHEN_DUST.addUnsafeEnchantment(ench.DIG_SPEED, 4)

FIREY_DUST = i(Material.REDSTONE, 1, 2)
M = FIREY_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bFirey Dust']))
FIREY_DUST.setItemMeta(M)
FIREY_DUST.addUnsafeEnchantment(ench.FIRE_ASPECT, 3)

MAGICIANS_POWDER = i(Material.SUGAR, 1, 2)
M = MAGICIANS_POWDER.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"bMagician's Powder"]))
MAGICIANS_POWDER.setItemMeta(M)
MAGICIANS_POWDER.addUnsafeEnchantment(ench.KNOCKBACK, 1)

SPELLBOOK = i(Material.ENCHANTED_BOOK, 1, 1)
M = SPELLBOOK.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"dSpellbook"]))
SPELLBOOK.setItemMeta(M)

FIREY_INGOT = i(Material.CLAY_BRICK, 1, 1)
M = FIREY_INGOT.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"bFirey Ingot"]))
FIREY_INGOT.setItemMeta(M)
FIREY_INGOT.addUnsafeEnchantment(ench.FIRE_ASPECT, 1)

MAGICIANS_INGOT = i(Material.IRON_INGOT, 1, 1)
M = MAGICIANS_INGOT.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"bMagician's Ingot"]))
MAGICIANS_INGOT.setItemMeta(M)
MAGICIANS_INGOT.addUnsafeEnchantment(ench.LOOT_BONUS_MOBS, 1)

FLAMING_SHARD = i(Material.GOLD_NUGGET, 1, 1)
M = FLAMING_SHARD.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"dFlaming Shard"]))
FLAMING_SHARD.addUnsafeEnchantment(ench.FIRE_ASPECT, 4)
FLAMING_SHARD.addUnsafeEnchantment(ench.DAMAGE_ALL, 10)
FLAMING_SHARD.setItemMeta(M)

MAGICIANS_BLADE = i(Material.GOLD_SWORD, 1, 0)
M = MAGICIANS_BLADE.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"dMagician's Blade"]))
MAGICIANS_BLADE.setItemMeta(M)
MAGICIANS_BLADE.addUnsafeEnchantment(ench.DAMAGE_ALL, 10)
MAGICIANS_BLADE.addUnsafeEnchantment(ench.LOOT_BONUS_MOBS, 4)
MAGICIANS_BLADE.addUnsafeEnchantment(ench.DURABILITY, 10)

DARK_INGOT = i(Material.NETHER_BRICK_ITEM, 1, 1)
M = DARK_INGOT.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"dDark Ingot"]))
DARK_INGOT.setItemMeta(M)
DARK_INGOT.addUnsafeEnchantment(ench.DAMAGE_UNDEAD, 1)
###THING###

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

R = s(MAGICIANS_INGOT)
R.addIngredient(Material.SUGAR, 2)
R.addIngredient(Material.SUGAR, 2)
R.addIngredient(Material.SUGAR, 2)
R.addIngredient(Material.SUGAR, 2)
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

R = s(i(Material.GLOWSTONE_DUST, 4, 0))
R.addIngredient(Material.GLOWSTONE, 1)
R.addIngredient(Material.FLINT, 1)
getServer().addRecipe(R)

R = sh(FLAMING_SHARD)
R.shape('pip','imi','pip')
R.setIngredient('p',Material.REDSTONE,2)
R.setIngredient('i',Material.CLAY_BRICK,1)
R.setIngredient('m',Material.GOLDEN_APPLE,1)
getServer().addRecipe(R)

R = sh(MAGICIANS_BLADE)
R.shape('pap','pap','psp')
R.setIngredient('p',Material.SUGAR,2)
R.setIngredient('a',Material.GOLDEN_APPLE,1)
R.setIngredient('s',Material.STICK,0)
getServer().addRecipe(R)

R = s(DARK_INGOT)
R.addIngredient(Material.CLAY_BRICK, 1)
R.addIngredient(Material.SULHUR, 3)
getServer().addRecipe(R)

R = s(FIREY_INGOT)
R.addIngredient(Material.NETHER_BRICK_ITEM, 1)
R.addIngredient(Material.REDSTONE, 2)
getServer().addRecipe(R)
