# YKRPG-Python
自分用なので可読性とか考えてないですW

# うさげ
```py
import ykrpg


# エンティティインスタンスの作成
player = ykrpg.Player()
enemy = ykrpg.Enemy()

# HPの確認
print(f"player health: {player.health}")
print(f"enemy health: {enemy.health}")

# playerがenemyに攻撃
player.attack_to(enemy)
print(f"player attack -> enemy")

print(f"enemy health: {enemy.health}")

# enemyがplayerに攻撃
enemy.attack_to(player)
print(f"enemy attack -> player")

print(f"player health: {player.health}")
```
