import cards_tools

#  *********************************************
#  欢迎使用【名片管理系统】v1.0
#
#  1. 新建名片
#  2. 显示全部
#  3. 查询名片
#
#  0. 退出系统
#
#  *********************************************



while 1:


    cards_tools.show_menu()

    action = int(input("请输入功能序号："))
    function_business_card = [0, 1, 2, 3]

    # for action in function_business_card:
    if action in function_business_card:

        if action == function_business_card[0]:
            #  退出系统
            cards_tools.quit_system()
            break

        if action == function_business_card[1]:
            # 1. 新建名片
            cards_tools.new_card()

        if action == function_business_card[2]:
            # 2. 显示所有名片
            cards_tools.show_cards()

        if action ==  function_business_card[3]:
            # 3. 查询名片信息
            cards_tools.search_cards()


    if action not in function_business_card:
        print("功能序号输入不对哦，请输入0~3的数字~")