

def show_menu():
    print("")
    print("*" * 45)
    print("欢迎使用【名片管理系统】v1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 45)


business_cards = []

def new_card():
    # 新建名片
    print("-" * 45)
    print("功能：新建名片")
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    QQ = input("请输入QQ：")
    email = input("请输入邮件：")
    new_card = {"name": name, "phone": phone, "QQ": QQ, "email": email}
    # print(new_card)
    business_cards.append(new_card)
    print("已新建名片完成！")


def show_cards():
    print("-"*45)
    print("功能：显示全部")

    if len(business_cards) == 0:
        print("当前没有名片记录哦，请使用新增1功能添加名片~")
        # 特点：返回一个函数的执行结果、
        # 下方的代码不会被执行
        return
    # if len(business_cards) != 0:

    # 打印表头
    for name in ["name","phone","QQ","Email"]:
        print(name, end="\t\t")

    print("")
    print("="*45)

    for card_dict in business_cards:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["QQ"],
                                        card_dict["email"]))



def search_cards():
    """查找名片

    """
    print("-" * 45)
    print("功能：查询名片")
    check_name = str(input("请输入查询名片的姓名："))
    # print(check_name)
    for name_str in business_cards:
        if name_str["name"] == check_name:
            for name in ["name", "phone", "QQ", "Email"]:
                print(name, end="\t\t")

            print("")
            print("=" * 45)
            print("%s\t\t%s\t\t%s\t\t%s" % (name_str["name"],
                                            name_str["phone"],
                                            name_str["QQ"],
                                            name_str["email"]))

            #  针对找到的名片记录执行修改和删除的操作
            operate_card(name_str)

            break
    else:
        # if name_str["name"] != check_name:
        print("抱歉，您还未添加名片到管理系统，请返回首页输入1新建名片")


def operate_card(find_dict):
    """处理查找到的名字

    :param find_dict:查找的的名片
    """
    # print(find_dict)
    operation = str(input("请输入对名片的操作："
                          "[1] 修改 [2] 删除 [0] 返回上级菜单"))

    if operation == "1":
        print("-" * 45)
        print("功能：修改名片")

        find_dict["name"] = input_card_info(find_dict["name"],"请输入姓名[按回车跳过修改]：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "请输入电话[按回车跳过修改]：")
        find_dict["QQ"] = input_card_info(find_dict["QQ"], "请输入QQ[按回车跳过修改]：")
        find_dict["email"] = input_card_info(find_dict["email"], "请输入邮件[按回车跳过修改]：")
        print("修改名片成功！")

    if operation == "2":
        print("-" * 45)
        print("功能：删除名片")
        business_cards.remove(find_dict)
        print("删除 %s 成功" % find_dict["name"])

    if operation == "0":
        pass


def input_card_info(dict_value, tip_message):
    """输入名片信息

    :param dict_value: 名片字典中原有的值
    :param tip_message: 用户输入的提示文字
    :return: 如果用户输入了内容，就返回内容，否则则返回字典中的值
    """
    # 1. 提示用户输入内容
    result_str = input(tip_message)
    # 2. 针对用户输入的内容进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str

    # 3. 如果用户不输入内容，返回字典中的值
    if len(result_str) == 0:
        return dict_value


def quit_system():
    print("退出系统成功！")


