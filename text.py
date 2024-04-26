# piles of text

# values when game start
"""
Keeps only one for convenience
[理智] = san;
[体力] = hp;
[魔法] = mp;
"""
default_dic = {
    "姓名": "伦道夫.卡特",
    "力量": 50, "敏捷": 50, "意志": 50, "智力": 50, "体质": 50, "外貌": 50, "教育": 50, "体型": 50,
    "理智": 99, "幸运": 50, "魔法": 10, "体力": 10, "会计": 5, "人类学": 1,
    "估价": 5, "考古学": 1, "取悦": 15, "魅惑": 15, "攀爬": 20, "计算机": 5, "计算机使用": 5, "电脑": 5,
    "信用评级": 0, "克苏鲁神话": 0, "乔装": 5, "闪避": 25, "汽车驾驶": 20, "电气维修": 10, "电子学": 1,
    "话术": 5, "斗殴": 25, "手枪": 20, "急救": 30, "历史": 5, "恐吓": 15, "跳跃": 20, "母语": 50, "法律": 5,
    "图书馆使用": 20, "聆听": 20, "开锁": 1, "撬锁": 1, "锁匠": 1, "机械维修": 10, "医学": 1, "博物学": 10,
    "自然学": 10, "领航": 10, "导航": 10, "神秘学": 5, "操作重型机械": 1, "说服": 10, "精神分析": 1, "心理学": 10,
    "骑术": 5, "妙手": 10, "侦查": 25, "潜行": 20, "生存": 10, "游泳": 20, "投掷": 20, "追踪": 10, "动物驯养": 5,
    "潜水": 1, "爆破": 1, "读唇": 1, "催眠": 1, "炮术": 1, "hp_og": 10, "san_og": 99, "mp_og": 10
    }

def translate_key(input_key):
    return key_map.get(input_key, input_key)

def description(character):
    """
    Get character descriptions based on attributes.
    
    :param character: Dictionary containing character attributes.
    :return: Dictionary with attribute descriptions.
    """
    desc = {}

    # 力量 (Strength)
    str_value = character["力量"]
    if str_value <= 0:
        desc["力量"] = ""
    elif str_value <= 15:
        desc["力量"] = "虚弱，孱弱"
    elif str_value <= 40:
        desc["力量"] = "力量弱小"
    elif str_value <= 60:
        desc["力量"] = "有正常人的力量"
    elif str_value <= 80:
        desc["力量"] = "超乎常人的力量"
    elif str_value < 100:
        desc["力量"] = "超乎超乎常人的力量"
    else:
        desc["力量"] = "你怕是个神话中的人物"

    # 体质 (Constitution)
    con_value = character["体质"]
    if con_value <= 0:
        desc["体质"] = ""
    elif con_value <= 20:
        desc["体质"] = "常年患病在身"
    elif con_value <= 40:
        desc["体质"] = "体弱多病"
    elif con_value <= 60:
        desc["体质"] = "不会生什么大毛病"
    elif con_value <= 80:
        desc["体质"] = "健硕，浑身湿透也不会感冒"
    elif con_value < 100:
        desc["体质"] = "身体素质极好，精神抖擞"
    else:
        desc["体质"] = "神一般的体质"

    # 体型 (Size)
    siz_value = character["体型"]
    if siz_value <= 0:
        desc["体型"] = ""
    elif siz_value <= 20:
        desc["体型"] = "孩童，身短体瘦"
    elif siz_value <= 40:
        desc["体型"] = "乙女身材"
    elif siz_value <= 60:
        desc["体型"] = "普遍身高155-175"
    elif siz_value <= 80:
        desc["体型"] = "不是高就是胖"
    elif siz_value <= 100:
        desc["体型"] = "大号的人"
    elif siz_value < 150:
        desc["体型"] = "听说你正在申请身高世界记录？"
    elif siz_value < 180:
        desc["体型"] = "你可能是一头牛"
    elif siz_value < 200:
        desc["体型"] = "你已经是历史上最重的人类了"
    else:
        desc["体型"] = "过分了喂！"

    # 敏捷 (Dexterity)
    dex_value = character["敏捷"]
    if dex_value <= 0:
        desc["敏捷"] = ""
    elif dex_value <= 20:
        desc["敏捷"] = "很不灵活"
    elif dex_value <= 40:
        desc["敏捷"] = "不是很灵活"
    elif dex_value <= 60:
        desc["敏捷"] = "普通人水平"
    elif dex_value <= 80:
        desc["敏捷"] = "是一位运动健将"
    elif dex_value < 100:
        desc["敏捷"] = "高速而灵活,可以达成超凡的技艺"
    else:
        desc["敏捷"] = "神级敏捷，超越人类极限"

    # 外貌 (Appearance)
    app_value = character["外貌"]
    if app_value <= 0:
        desc["外貌"] = ""
    elif app_value <= 20:
        desc["外貌"] = "用脸就能恐惧敌人...或队友"
    elif app_value <= 40:
        desc["外貌"] = "有些难看"
    elif app_value <= 60:
        desc["外貌"] = "人群之中谁也不会看你一眼之后就忘不掉你容颜"
    elif app_value <= 80:
        desc["外貌"] = "五官端正，仪表堂堂"
    elif app_value < 100:
        desc["外貌"] = "沉鱼落雁，闭月羞花"
    else:
        desc["外貌"] = "令人难以直视的美"

    # 智力 (Intelligence)
    int_value = character["智力"]
    if int_value <= 0:
        desc["智力"] = ""
    elif int_value <= 20:
        desc["智力"] = "脑子是个好东西，可惜。。。"
    elif int_value <= 40:
        desc["智力"] = "理解知识要耗费比普通人更多的时间"
    elif int_value <= 60:
        desc["智力"] = "有着普通人的灵光一现"
    elif int_value <= 80:
        desc["智力"] = "可以自主进行发明创造"
    elif int_value < 100:
        desc["智力"] = "天才级水准"
    else:
        desc["智力"] = "超凡脱俗，绝世智慧"

    # 意志 (Willpower)
    pow_value = character["意志"]
    if pow_value <= 0:
        desc["意志"] = ""
    elif pow_value <= 20:
        desc["意志"] = "尔不过玩物"
    elif pow_value <= 40:
        desc["意志"] = "痴愚盲目"
    elif pow_value <= 60:
        desc["意志"] = "如常人一般会有一定自制力"
    elif pow_value <= 80:
        desc["意志"] = "我心如铁，心坚石穿"
    elif pow_value < 100:
        desc["意志"] = "泰山崩于面而色不变"
    elif pow_value < 140:
        desc["意志"] = "钢铁之心，还能看见鬼"
    else:
        desc["意志"] = "你怕是个假人吧"

    # 教育 (Education)
    edu_value = character["教育"]
    if edu_value <= 0:
        desc["教育"] = ""
    elif edu_value <= 20:
        desc["教育"] = "目不识丁"
    elif edu_value <= 40:
        desc["教育"] = "小学毕业"
    elif edu_value <= 60:
        desc["教育"] = "高中毕业"
    elif edu_value <= 80:
        desc["教育"] = "是重点大学的学生，或是普通大学的研究生"
    elif edu_value < 100:
        desc["教育"] = "饱读诗书，满腹经纶"
    else:
        desc["教育"] = "博学之士，知无不言"

    # 幸运 (Luck)
    luck_value = character["幸运"]
    if luck_value <= 0:
        desc["幸运"] = ""
    elif luck_value <= 20:
        desc["幸运"] = "克夫克妻"
    elif luck_value <= 40:
        desc["幸运"] = "霉运连连"
    elif luck_value <= 60:
        desc["幸运"] = "命格平庸"
    elif luck_value <= 80:
        desc["幸运"] = "在马路边捡到100块"
    elif luck_value < 100:
        desc["幸运"] = "被幸运女神所眷顾"
    else:
        desc["幸运"] = "命运之子，天选之人"

    return desc



key_map = {
    "str": "力量", "力量": "力量", "力量": "力量",
    "dex": "敏捷", "敏捷": "敏捷", "敏捷": "敏捷",
    "pow": "意志", "意志": "意志", "意志": "意志",
    "con": "体质", "體質": "体质", "体质": "体质",
    "app": "外貌", "外貌": "外貌", "外貌": "外貌",
    "edu": "教育", "教育": "教育", "教育": "教育",
    "siz": "体型", "體型": "体型", "体型": "体型",
    "int": "智力", "靈感": "智力", "灵感": "智力", "智力": "智力",
    "san": "理智", "san值": "理智", "理智值": "理智", "理智": "理智",
    "luck": "幸运", "運氣": "幸运", "运气": "幸运", "幸運": "幸运", "幸运": "幸运",
    "mp": "魔法", "魔法": "魔法", "魔法": "魔法",
    "hp": "体力", "體力": "体力", "体力": "体力",
    "會計": "会计", "会计": "会计",
    "人類學": "人类学", "人类": "人类学", "人类学": "人类学",
    "估價": "估价", "估价": "估价",
    "考古學": "考古学", "考古": "考古学", "考古学": "考古学",
    "取悅": "取悦", "取悦": "取悦",
    "表演": "表演", "表演": "表演",
    "魅惑": "魅惑", "魅惑": "魅惑",
    "攀爬": "攀爬", "攀爬": "攀爬",
    "計算機": "计算机", "计算机使用": "计算机", "电脑": "计算机", "電腦": "计算机", "计算机": "计算机",
    "信用": "信用评级", "信譽": "信用评级", "信誉": "信用评级", "信用评级": "信用评级",
    "克蘇魯": "克苏鲁神话", "克苏鲁神话": "克苏鲁神话", "cm": "克苏鲁神话",
    "喬裝": "乔装", "乔装": "乔装",
    "閃避": "闪避", "闪避": "闪避",
    "汽车": "汽车驾驶", "汽車": "汽车驾驶", "駕駛": "汽车驾驶", "驾驶": "汽车驾驶", "汽车驾驶": "汽车驾驶",
    "電氣維修": "电气维修", "电气维修": "电气维修",
    "電子學": "电子学", "电子学": "电子学", "电子": "电子学",
    "話術": "话术", "话术": "话术",
    "鬥毆": "斗殴", "斗殴": "斗殴",
    "手槍": "手枪", "手枪": "手枪",
    "機關槍": "机枪", "机枪": "机枪",
    "衝鋒槍": "冲锋枪", "冲锋枪": "冲锋枪",
    "步槍": "步枪", "步枪": "步枪",
    "急救": "急救", "急救": "急救",
    "歷史": "历史", "历史": "历史",
    "恐嚇": "恐吓", "恐吓": "恐吓",
    "跳躍": "跳跃", "跳跃": "跳跃",
    "母語": "母语", "母语": "母语",
    "法律": "法律", "法律": "法律",
    "圖書館": "图书馆使用", "图书馆": "图书馆使用", "图书馆使用": "图书馆使用",
    "聽力": "聆听", "聆听": "聆听",
    "開鎖": "开锁", "撬锁": "开锁", "锁匠": "开锁", "鎖匠": "开锁", "开锁": "开锁",
    "機械維修": "机械维修", "機械": "机械维修", "机械": "机械维修", "机械维修": "机械维修",
    "醫學": "医学", "医生": "医学", "医学": "医学",
    "博物學": "博物学", "博物学": "博物学", "博物": "博物学",
    "自然學": "自然学", "自然": "自然学", "自然学": "自然学",
    "領航": "领航", "導航": "领航", "导航": "领航",
    "神秘學": "神秘学", "神秘学": "神秘学",
    "重型操作": "操作重型机械", "重型機械": "操作重型机械", "操作重型机械": "操作重型机械", "重型": "操作重型机械", "重型机械操作": "操作重型机械",
    "說服": "说服", "说服": "说服",
    "精神分析": "精神分析", "精神分析": "精神分析",
    "心理學": "心理学", "心理学": "心理学",
    "騎術": "骑术", "骑术": "骑术",
    "妙手": "妙手", "妙手": "妙手",
    "偵查": "侦查", "侦查": "侦查",
    "潛行": "潜行", "潜行": "潜行",
    "生存": "生存", "生存": "生存",
    "游泳": "游泳", "游泳": "游泳",
    "投擲": "投掷", "投掷": "投掷",
    "追蹤": "追踪", "追踪": "追踪",
    "動物馴養": "动物驯养", "动物": "动物驯养", "动物驯养": "动物驯养",
    "潛水": "潜水", "潜水": "潜水",
    "爆破": "爆破", "爆破": "爆破",
    "讀唇": "读唇", "读唇": "读唇",
    "催眠": "催眠", "催眠": "催眠",
    "炮術": "炮术", "炮术": "炮术"
}


