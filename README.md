# 迷宫逃脱游戏

## 项目简介
本项目是一个基于 pygame 的中型迷宫逃脱游戏，包含：
- 随机生成迷宫地图
- 玩家键盘控制移动
- 敌人AI巡逻和追击
- 道具系统（钥匙、药水等）
- 简单UI界面
- 胜利/失败判定

## 运行方法
1. 安装依赖：
   ```bash
   pip install pygame
   ```
2. 运行游戏：
   ```bash
   python main.py
   ```

## 目录结构
- main.py              # 游戏主入口
- maze.py              # 迷宫生成与地图逻辑
- player.py            # 玩家控制
- enemy.py             # 敌人AI
- item.py              # 道具系统
- settings.py          # 配置参数
- assets/              # 素材资源（图片、音效等）
