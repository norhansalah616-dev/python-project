import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class LabApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.lbl_title = Label(text="مساعد التحاليل الطبية", font_size='22sp', size_hint_y=0.2)
        layout.add_widget(self.lbl_title)
        
        self.input_text = TextInput(hint_text="اكتب اسم التحليل هنا (مثلاً: FBS, Vitamin D)", size_hint_y=0.2)
        layout.add_widget(self.input_text)
        
        btn = Button(text="فحص التعليمات", size_hint_y=0.2, background_color=(0.2, 0.6, 0.8, 1))
        btn.bind(on_press=self.check_test)
        layout.add_widget(btn)
        
        self.lbl_result = Label(text="التعليمات ستظهر هنا...", font_size='16sp', size_hint_y=0.4)
        layout.add_widget(self.lbl_result)
        return layout

    def check_test(self, instance):
        test = self.input_text.text.strip().upper()
        if "FBS" in test:
            self.lbl_result.text = "FBS: يشترط الصيام من 8 إلى 12 ساعة."
        elif "VITAMIN D" in test:
            self.lbl_result.text = "Vitamin D: يفضل عدم إجراؤه أثناء الدورة الشهرية للنساء."
        else:
            self.lbl_result.text = f"تم إدخال: {test}\nلا توجد شروط خاصة إضافية مسجلة."

if __name__ == '__main__':
    LabApp().run()
