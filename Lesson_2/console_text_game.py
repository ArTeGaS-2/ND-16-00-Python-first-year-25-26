import random
import player, enemy

while player.health >= 0 or enemy.enemy_health_global >= 0:
    player.DoDamage(player.name,
                    enemy.enemy_name,
                    enemy.enemy_health_global,
                    player.level)
    enemy.DoDamage(enemy.enemy_name,
                player.name,
                player.health,
                enemy.enemy_level)


