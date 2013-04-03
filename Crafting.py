GRINDSTONE = ItemStack(Material.FLINT, 1, 2)
M = GRINDSTONE.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','rGrindstone']))
GRINDSTONE.setItemMeta(M)

GOLD_DUST = ItemStack(Material.GLOWSTONE_DUST, 1, 1)
M = GOLD_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bGold Dust']))
GOLD_DUST.setItemMeta(M)

IRON_DUST = ItemStack(Material.SUGAR, 1, 1)
M = IRON_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bIron Dust']))
IRON_DUST.setItemMeta(M)

NETHER_DUST = ItemStack(Material.REDSTONE, 1, 1)
M = NETHER_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bNether Dust']))
NETHER_DUST.setItemMeta(M)

METAL_DUST = ItemStack(Material.SULPHUR, 1, 1)
M = METAL_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bMetal Dust']))
METAL_DUST.setItemMeta(M)

STONE_DUST = ItemStack(Material.SULPHUR, 1, 2)
M = STONE_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bStone Dust']))
STONE_DUST.setItemMeta(M)

EARTHEN_DUST = ItemStack(Material.SULPHUR, 1, 3)
M = EARTHEN_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bEarthen Dust']))
EARTHEN_DUST.setItemMeta(M)

FIREY_DUST = ItemStack(Material.REDSTONE, 1, 2)
M = FIREY_DUST.getItemMeta()
M.setDisplayName(''.join([u'\u00A7','bFirey Dust']))
FIREY_DUST.setItemMeta(M)

MAGICIANS_POWDER = ItemStack(Material.REDSTONE, 1, 3)
M = MAGICIANS_POWDER.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"bMagician's Powder"]))
MAGICIANS_POWDER.setItemMeta(M)

SPELLBOOK = ItemStack(Material.ENCHANTED_BOOK, 1, 1)
M = SPELLBOOK.getItemMeta()
M.setDisplayName(''.join([u'\u00A7',"dSpellbook"]))
SPELLBOOK.setItemMeta(M)

R = ShapelessRecipe(GRINDSTONE)
R.addIngredient(Material.FLINT, 0)
R.addIngredient(Material.COBBLESTONE, 0)
getServer().addRecipe(R)

R = ShapelessRecipe(GOLD_DUST)
R.addIngredient(Material.FLINT, 1)
R.addIngredient(Material.GOLD_INGOT, 0)
getServer().addRecipe(R)

R = ShapelessRecipe(IRON_DUST)
R.addIngredient(Material.FLINT, 1)
R.addIngredient(Material.GOLD_INGOT, 0)
getServer().addRecipe(R)

