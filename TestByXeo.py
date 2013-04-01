import org.bukkit.Material as Material
import org.bukkit.inventory.ItemStack as ItemStack
import org.bukkit.inventory.ShapedRecipe as ShapedRecipe
import org.bukkit.Bukkit.getServer() as getServer()

R = ShapedRecipe(ItemStack(Material.STICK, 1, 70)).shape("fse", "sss", "asw").setIngredient('f', Material.LAVA_BUCKET).setIngredient('e', Material.DIAMOND).setIngredient('s', Material.STICK).setIngredient('a', Material.FEATHER).setIngredient('w', Material.WATER_BUCKET)
getServer().addRecipe(R)
