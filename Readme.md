# BakaBot

基于 [tencent-connect/botpy](https://github.com/tencent-connect/botpy) 的QQ机器人

<div align="center">

*Working In Progress*

</div>

## 安装

### 依赖

必须安装的依赖：
```
Python 3.12.3 或更高版本
```
在Python安装成功后可以通过
```
pip install -r requirements.txt
```
安装其他依赖

(没搞虚拟环境，也还没删改，如果装了会多出很多没用的库，目前不建议用)

### 配置

先决条件：
在官方的开放平台创建好机器人账号，并完成基本配置，获取BotID和Secret码。

将获取到的BotID和Secret填入 [config.yaml](./config.yaml) 

## 功能

（见[feature.py](./feature.py)）

---
### Terrible Random Number - 哈人随机数

#### 功能介绍

在7000-9000之间随机抽取一个数字

### Ture Music Random Selecter - 神曲随机

#### 功能介绍

在 [神曲链接表](./ture_music_list.scv) 中抽取一个链接

*你也可以按照格式自行添加链接，然后进行Pull Request*

---
（剩下的以后再写）
