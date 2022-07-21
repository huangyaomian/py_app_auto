# -*- coding: utf-8 -*-
from base.action import ElementActions
from lib.pages.set import ProductPages as p
from base.verify import NotFoundTextError
from base.utils import log


# 测试用例demo，pytest框架自动加载执行


class Test_demo():

    def test_home(self, action: ElementActions):

        # up.登录页.login(action,'13550234762','tmhrush2233')

        action.click(p.首页.進入搜索頁按鈕)

        # 因为调用action的大部分公用方法是返回self，所以可以一条语句执行多次不同方法
        action.text(p.搜索首頁.搜索输入框, "mika").click(p.搜索首頁.搜索按钮)

        action.click(p.搜索后列表页.遊戲譯名)

        # 循环下拉，检查是否有对应关键字，找到后终止
        # for count in range(20):
        #     if action.swip_down().is_text_displayed("遊戲"):
        #         break
        # 没有对应关键字抛出错误
        if action.is_text_displayed("mika"):
            raise NotFoundTextError

        action.sleep(1)
