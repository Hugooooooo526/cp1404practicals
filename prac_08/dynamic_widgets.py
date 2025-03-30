"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create labels based on a list of names
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # 创建名称列表 - 这是程序的数据（模型）
        self.names = ["张三", "李四", "王五", "赵六", "钱七", "孙八", "周九"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "动态标签"
        self.root = Builder.load_file('prac_08/dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from data and add them to the GUI."""
        # 清空现有标签
        self.root.ids.entries_box.clear_widgets()
        # 为每个名称创建标签
        for name in self.names:
            # 创建标签小部件
            temp_label = Label(text=name)
            # 将标签添加到布局中
            self.root.ids.entries_box.add_widget(temp_label)


DynamicWidgetsApp().run()
