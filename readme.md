# 简易telegram代理机器人

喜欢就点个stars吧～

配置见 config.py 文件

## 安装&运行
```bash
git clone https://github.com/heinu123/proxy-bot.git && cd proxybot
pip3 install -r requirements.txt
python3 mian.py
```

## 命令列表

```bash
help - 帮助
proxy - 获取v2ray代理(带clash订阅转换)
tgproxy - 获取telegram直连(mtproxy)代理
sign - 签到
info - 获取当前积分
list - 获取当前代理池数量
add - 向代理池添加代理[admin]
rm - 删除代理池的某个代理[admin]
getlist - 获取代理池全部内容[admin]
add_integral - 增加某个用户的积分[admin]
deduct_integral - 扣除某个用户的积分[admin]
```

**管理员**

**/getlist**命令
获取[v2ray/mtproxy]代理池全部内容(已文件形式发送)
例：
```bash
/getlist [v2ray/mtproxy]
```

**/add**命令
向[v2ray/mtproxy]代理池添加代理
例：
```bash
/add [v2ray/mtproxy] 代理内容
```

**/rm**命令
删除[v2ray/mtproxy]代理池的某个代理
例：
```bash
/rm [v2ray/mtproxy] 代理内容
```

**/add_integral**命令
增加某个用户的积分
例：
```bash
/add_integral [telegram id] [增加的积分数量]
```

**/deduct_integral**命令
扣除某个用户的积分
例：
```bash
/deduct_integral [telegram id] [扣除的积分数量]
```

ps：来订阅我的tg频道喵 https://t.me/heinuhome
