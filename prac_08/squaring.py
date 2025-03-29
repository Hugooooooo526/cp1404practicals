"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 200)  # 增加窗口大小以适应新的布局
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass
            
    def handle_increment(self, change):
        """
        处理上/下按钮点击，更新文本输入的值，然后调用计算函数
        :param change: 更改的数量
        """
        try:
            # 获取当前值，转换为浮点数，然后增加/减少
            value = float(self.root.ids.input_number.text) + change
            # 更新文本输入@
            self.root.ids.input_number.text = str(value)
            # 调用计算函数更新结果
            self.handle_calculate(self.root.ids.input_number.text)
        except ValueError:
            # 如果转换失败，设置为0
            self.root.ids.input_number.text = "0"
            self.handle_calculate("0")


SquareNumberApp().run()
