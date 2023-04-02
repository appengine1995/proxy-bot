import telebot
import user
import config
import proxys
from telebot import types
from urllib import parse
global proxylist, tgproxylist


bot = telebot.TeleBot(config.token)
proxys.init()

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.send_message(message.chat.id, "我是属于 @heinuhome 的代理机器人👋\n命令列表:\n/help - 帮助\n/proxy - 获取v2ray代理(带clash订阅转换)\n/tgproxy - 获取telegram直连(mtproxy)代理\n/sign - 签到\n/info - 获取当前积分\n/list - 获取当前代理池数量\n/add - 向代理池添加代理[admin]\n/rm - 删除代理池的某个代理[admin]\n/getlist - 获取代理池全部内容[admin]\n/add_integral - 增加某个用户的积分[admin]\n/deduct_integral - 扣除某个用户的积分[admin]")

@bot.message_handler(commands=["sign"])
def send_welcome(message):
    global signmsg_id
    markup = types.InlineKeyboardMarkup()
    sign = types.InlineKeyboardButton("点我签到", callback_data='sign')
    markup.add(sign)
    signmsg_id = bot.send_message(message.chat.id, "点击按钮完成签到", reply_markup=markup).message_id


@bot.message_handler(commands=["info"])
def send_welcome(message):
    bot.send_message(message.chat.id, user.get_deduct(message.chat.id))

@bot.message_handler(commands=["list"])
def send_welcome(message):
    bot.send_message(message.chat.id, proxys.get_proxylist())

@bot.message_handler(commands=["proxy"])
def send_welcome(message):
    deduct = user.deduct_points(message.chat.id)
    if deduct:
        proxy = proxys.get_proxy()
        URL = proxys.subconvert(proxy)
        markup = types.InlineKeyboardMarkup()
        subconverts = types.InlineKeyboardButton("订阅转换", url=URL)
        btn2 = types.InlineKeyboardButton("倾城极速", url="https://qcjs.pro")
        btn3 = types.InlineKeyboardButton("新生机场", url="https://hs114514.tech")
        markup.add(subconverts, btn2, btn3)
        bot.send_message(message.chat.id, proxy, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "积分不足！")
 
@bot.message_handler(commands=["tgproxy"])
def send_welcome(message):
    deduct = user.deduct_points(message.chat.id)
    if deduct:
        proxy = proxys.get_tgproxy()
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton("倾城极速", url="https://qcjs.pro")
        btn3 = types.InlineKeyboardButton("新生机场", url="https://hs114514.tech")
        markup.add(btn2, btn3)
        bot.send_message(message.chat.id, proxy, reply_markup=markup) 
    else:
        bot.send_message(message.chat.id, "积分不足！")

@bot.message_handler(commands=["add_integral"])
def send_welcome(message):
    for uid in config.adminlist:
        if message.chat.id == uid:
            isadmin = True
    if isadmin:
        bot.send_message(message.chat.id, user.add_integral(message.text.split(" ")[1], message.text.split(" ")[2]))
    else:
        bot.send_message(message.chat.id, "你不是管理员\n无法使用该命令!")

@bot.message_handler(commands=["deduct_integral"])
def send_welcome(message):
    for uid in config.adminlist:
        if message.chat.id == uid:
            isadmin = True
    if isadmin:
        bot.send_message(message.chat.id, user.deduct_integral(message.text.split(" ")[1], message.text.split(" ")[2]))
    else:
        bot.send_message(message.chat.id, "你不是管理员\n无法使用该命令!")

@bot.message_handler(commands=["add"])
def send_welcome(message):
    for uid in config.adminlist:
        if message.chat.id == uid:
            isadmin = True
    if isadmin:
        module = message.text.split(" ")[1]
        text = message.text.split(" ")[2]
        msg_id = bot.send_message(message.chat.id, "添加中..").message_id
        if module == "mtproxy":
            files = config.TGPROXY_FILE
        elif module == "v2ray":
            files = config.PROXY_FILE
        else:
            bot.edit_message_text("代理类型不存在", message.chat.id, msg_id)
            return
        with open(files, "a") as file:
            file.write(text)
        proxys.init()
        bot.edit_message_text("以下代理已添加:\n" + text, message.chat.id, msg_id)
    else:
        bot.send_message(message.chat.id, "你不是管理员\n无法使用该命令!")

 
@bot.message_handler(commands=["rm"])
def send_welcome(message):
    for uid in config.adminlist:
        if message.chat.id == uid:
            isadmin = True
    if isadmin:
        module = message.text.split(" ")[1]
        text = message.text.split(" ")[2]
        msg_id = bot.send_message(message.chat.id, "删除中..").message_id
        if module == "mtproxy":
            files = config.TGPROXY_FILE
        elif module == "v2ray":
            files = config.PROXY_FILE
        else:
            bot.edit_message_text("代理类型不存在", message.chat.id, msg_id)
            return
        with open(files, "r") as file:
            new_contents = []
            for line in file:
                if text not in line:
                    new_contents.append(line)
        with open(files, "w") as file:
            for line in new_contents:
                file.write(line)
        proxys.init()
        bot.edit_message_text("以下代理已删除:\n" + text, message.chat.id, msg_id)
    else:
        bot.send_message(message.chat.id, "你不是管理员\n无法使用该命令!")

@bot.message_handler(commands=["getlist"])
def send_welcome(message):
    for uid in config.adminlist:
        if message.chat.id == uid:
            isadmin = True
    if isadmin:
        module = message.text.split(" ")[1]
        if module == "mtproxy":
            files = config.TGPROXY_FILE
        elif module == "v2ray":
            files = config.PROXY_FILE
        else:
            bot.edit_message_text("代理类型不存在", message.chat.id, msg_id)
            return
        file = open(files, "rb")
        bot.send_document(message.chat.id, file)
        bot.send_document(message.chat.id, "FILEID")
    else:
        bot.send_message(message.chat.id, "你不是管理员\n无法使用该命令!")

@bot.callback_query_handler(func=lambda call: True)
def callback_handle(call):
    if call.data == "sign":
        bot.delete_message(call.message.chat.id, signmsg_id)
        bot.send_message(call.message.chat.id, "@" + call.message.chat.username + " " + user.sign_in(call.message.chat.id) + "\n" + user.get_deduct(call.message.chat.id))



bot.infinity_polling()