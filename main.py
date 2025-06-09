import sqlite3
from kivymd.uix.list import ThreeLineAvatarIconListItem
import arabic_reshaper
from bidi.algorithm import get_display
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.label import Label
from kivymd.uix.button import MDIconButton, MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import pandas as pd
from kivy.core.window import Window
import webbrowser
Window.size = (270, 600)


file_path = "dictionary.csv"
df = pd.read_csv(file_path, encoding= "utf-8")
df.columns = df.columns.str.strip()
file_path = "verbs.csv"
vf = pd.read_csv(file_path, encoding= "utf-8")
vf.columns = vf.columns.str.strip()
file_path = "pronouns.csv"
pf = pd.read_csv(file_path, encoding= "utf-8")
pf.columns = pf.columns.str.strip()


class CustomThreeLineListItem(ThreeLineAvatarIconListItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids._lbl_primary.font_name = "Amiri-Regular.ttf"
        self.ids._lbl_secondary.font_name = "Amiri-Regular.ttf"
        self.ids._lbl_tertiary.font_name = "Amiri-Regular.ttf"

        self.ids._lbl_primary.pos_hint = {"center_x": 2.48, "center_y": 1}
        self.ids._lbl_secondary.pos_hint = {"center_x": 2.48, "center_y": 1}
        self.ids._lbl_tertiary.pos_hint = {"center_x": 2.48, "center_y": 1}

        self.ids._lbl_primary.size_hint_x = 5
        self.ids._lbl_secondary.size_hint_x = 5

        self.ids._lbl_primary.font_size = "15sp"
        self.ids._lbl_secondary.font_size = "15sp"
        self.ids._lbl_tertiary.font_size = "15sp"
        self.divider_color = 0.15, 0.22, 0.35, 1


class Ar_text(MDTextField):
    max_chars = NumericProperty(30)  # Maximum character allowed
    str = StringProperty()
    def __init__(self, **kwargs):
        super(Ar_text, self).__init__(**kwargs)
        self.text = get_display(arabic_reshaper.reshape("الكلمة بالعربيةً"))
        self.font_name = "Amiri-Regular.ttf"
        self.halign = "right"
        self.text_color_normal = 1, 1, 1, 0.4
    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.text) + len(substring) > self.max_chars):
            return
        self.str = self.str + substring
        self.text = get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(Ar_text, self).insert_text(substring, from_undo)
    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = get_display(arabic_reshaper.reshape(self.str))


class Ch_text(MDTextField):
    max_chars = NumericProperty(30)  # Maximum character allowed
    str = StringProperty()
    def __init__(self, **kwargs):
        super(Ch_text, self).__init__(**kwargs)
        self.text = get_display(arabic_reshaper.reshape("الترجمة بالشاوية"))
        self.size_hint = (None, None)  # Custom size
        self.width = 230  # Width of the rectangle
        self.height = 600  # Height of the rectangle
        self.font_name = "Amiri-Regular.ttf"
        self.halign = "right"
        self.line_color_normal = 1, 1, 1, 1
        self.text_color_normal = 1, 1, 1, 0.4
    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.text) + len(substring) > self.max_chars):
            return
        self.str = self.str + substring
        self.text = get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(Ch_text, self).insert_text(substring, from_undo)
    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = get_display(arabic_reshaper.reshape(self.str))


class Dic_text(MDTextField):
    max_chars = NumericProperty(30)  # Maximum character allowed
    str = StringProperty()
    def __init__(self, **kwargs):
        super(Dic_text, self).__init__(**kwargs)
        self.text = get_display(arabic_reshaper.reshape("إبحث هنا"))
        self.font_name = "Amiri-Regular.ttf"
        self.halign = "right"
        self.mode = "round"
        self.fill_color_normal = "#ffffff"
        self.pos_hint = {"center_x": 0.5, "center_y": 0.50}
    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.text) + len(substring) > self.max_chars):
            return
        self.str = self.str + substring
        self.text = get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(Dic_text, self).insert_text(substring, from_undo)
    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = get_display(arabic_reshaper.reshape(self.str))


class Ver_text(MDTextField):
    max_chars = NumericProperty(30)  # Maximum character allowed
    str = StringProperty()
    def __init__(self, **kwargs):
        super(Ver_text, self).__init__(**kwargs)
        self.text = get_display(arabic_reshaper.reshape("ادخل الفعل (في الماضي)"))
        self.font_name = "Amiri-Regular.ttf"
        self.halign = "right"
        self.mode = "round"
        self.pos_hint = {"center_x": 0.5, "center_y": 0.50}
    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.text) + len(substring) > self.max_chars):
            return
        self.str = self.str + substring
        self.text = get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(Ver_text, self).insert_text(substring, from_undo)
    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = get_display(arabic_reshaper.reshape(self.str))


class Pron_text(MDTextField):
    max_chars = NumericProperty(30)  # Maximum character allowed
    str = StringProperty()
    def __init__(self, **kwargs):
        super(Pron_text, self).__init__(**kwargs)
        self.text = get_display(arabic_reshaper.reshape("ادخل الفعل (في الماضي)"))
        self.font_name = "Amiri-Regular.ttf"
        self.halign = "right"
        self.mode = "round"
        self.pos_hint = {"center_x": 0.5, "center_y": 0.50}
        self.text_color_normal = 1, 1, 1, 0.4
    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.text) + len(substring) > self.max_chars):
            return
        self.str = self.str + substring
        self.text = get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(Pron_text, self).insert_text(substring, from_undo)
    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = get_display(arabic_reshaper.reshape(self.str))


class MainScreen(MDScreen):
    pass

class ContactUs(MDScreen):
    pass


class FavoriteScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db_name = "dictionary.db"
        self.create_table_favorite()

    def create_table_favorite(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                arabic_word TEXT NOT NULL,
                chaoui_word TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def add_word_to_database_favorite(self, word, meaning):
        if not self.word_exists_in_favorites(word):
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO favorites (arabic_word, chaoui_word) VALUES (?, ?)", (word, meaning))
            conn.commit()
            conn.close()

    def word_exists_in_favorites(self, arabic_word):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM favorites WHERE arabic_word = ?", (arabic_word,))
        exists = cursor.fetchone() is not None
        conn.close()
        return exists

    def get_all_words_favorite(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM favorites")
        words = cursor.fetchall()
        conn.close()
        return words

    def load_words_favorite(self):
        self.ids.favoritelist.clear_widgets()  # Clear existing items to avoid duplicates
        words = self.get_all_words_favorite()
        for word_id, arabic_word, chaoui_word in words:
            item = CustomThreeLineListItem(
                text=arabic_word,
                secondary_text=chaoui_word,
                tertiary_text="",
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
                secondary_theme_text_color="Custom",
                secondary_text_color=(0, 1, 1, 1)
            )
            delete_icon = MDIconButton(
                icon="delete",
                theme_icon_color="Custom",
                icon_color=(1, 1, 1, 1),
                icon_size="20dp",
                on_release=lambda x, word_id=word_id, item=item: self.show_delete_confirmation(word_id, item),
                # Use default argument
                pos_hint={"center_x": 0.08, "center_y": 0.55}
            )
            item.add_widget(delete_icon)
            self.ids.favoritelist.add_widget(item)

    def show_delete_confirmation(self, word_id, item):
        # Create a dialog for confirmation
        self.dialog = MDDialog(
            title="Alert",
            text="Are you sure you want to delete this item?",
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    on_release=self.close_dialog
                ),
                MDFlatButton(
                    text="Yes",
                    on_release=lambda x: self.delete_word_favorite(item, word_id)
                ),
            ],
        )
        self.dialog.open()
    def close_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()  # Close the dialog

    def delete_word_favorite(self, item, word_id):
        self.ids.favoritelist.remove_widget(item)  # Remove item from the UI
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM favorites WHERE id = ?", (word_id,))
        conn.commit()
        conn.close()
        self.close_dialog()

    def on_pre_enter(self, *args):
        self.load_words_favorite()  # Load words when entering the screen


def fix_arabic_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)
def create_label_dictionary(text):
    return Label(text=fix_arabic_text(text), font_name="Amiri-Regular.ttf", halign= "right")
def create_button_dictionary(text, on_press_action):
    button = MDRectangleFlatButton(text=fix_arabic_text(text), font_name="Amiri-Regular.ttf", size_hint=(0.5, 0.1), pos_hint= {"center_x": 0.5, "center_y": 0.5})
    button.bind(on_release=on_press_action)
    return button
def create_popup_dictionary():
    layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
    label = create_label_dictionary(" حتى تجد ماتبحث عنه يجب أن تكون: \n - الكلمة مكتوبة بشكل صحيح إملائيا \n - إحترام الهمزة مثل 'أرنب' و 'بئر'")
    close_button = create_button_dictionary("إغلاق", lambda instance: popup_dictionary.dismiss())
    layout.add_widget(label)
    layout.add_widget(close_button)
    global popup_dictionary
    popup_dictionary = Popup(title=fix_arabic_text("تنبيــــه"),
                  title_font="Amiri-Regular.ttf",  # هذا للسطر العلوي للنافذة
                  content=layout,
                  size_hint=(0.9, 0.5),
                  background='atlas://data/images/defaulttheme/button',
                  background_color=(60/255, 80/255, 140/255),
                  pos_hint={"center_x": 0.5, "center_y": 0.45},
                  auto_dismiss=False)
    popup_dictionary.open()
def create_popup_verb():
    layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
    label = create_label_dictionary(" حتى تجد ماتبحث عنه يجب أن يكون: \n - الفعل مكتوب في زمن الماضي \n - إحترام الهمزة مثل 'أكل' و 'سأل' \n - الفعل مكتوب بشكل صحيح إملائيا \n - التفريـق بين  'ي'  و  'ى'")
    close_button = create_button_dictionary("إغلاق", lambda instance: popup_verb.dismiss())
    layout.add_widget(label)
    layout.add_widget(close_button)
    global popup_verb
    popup_verb = Popup(title=fix_arabic_text("تنبيــــه"),
                  title_font="Amiri-Regular.ttf",  # هذا للسطر العلوي للنافذة
                  content=layout,
                  size_hint=(0.9, 0.5),
                  background='atlas://data/images/defaulttheme/button',
                  background_color=(60/255, 80/255, 140/255),
                  pos_hint={"center_x": 0.5, "center_y": 0.45},
                  auto_dismiss=False)
    popup_verb.open()
def create_popup_pronoun():
    layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
    label = create_label_dictionary(" حتى تجد ماتبحث عنه يجب أن يكون: \n - الفعل مكتوب في زمن الماضي \n - إحترام الهمزة مثل 'أكل' و 'سأل' \n - الفعل مكتوب بشكل صحيح إملائيا \n - التفريـق بين  'ي'  و  'ى'")
    close_button = create_button_dictionary("إغلاق", lambda instance: popup_pronoun.dismiss())
    layout.add_widget(label)
    layout.add_widget(close_button)
    global popup_pronoun
    popup_pronoun = Popup(title=fix_arabic_text("تنبيــــه"),
                  title_font="Amiri-Regular.ttf",  # هذا للسطر العلوي للنافذة
                  content=layout,
                  size_hint=(0.9, 0.5),
                  background='atlas://data/images/defaulttheme/button',
                  background_color=(60/255, 80/255, 140/255),
                  pos_hint={"center_x": 0.5, "center_y": 0.45},
                  auto_dismiss=False)
    popup_pronoun.open()


class ConnectedPronouns(MDScreen):
    def on_pre_enter(self, *args):
        global pf
        # إصلاح النص العربي (مرة واحدة فقط - انتبه أن لا تُكرر المعالجة)
        if 'arabic_fixed' not in pf.columns:
            # Ensure that we only apply the function to string values
            pf['verb'] = pf['verb'].apply(lambda x: fix_arabic_text(x) if isinstance(x, str) else x)
            pf['arabic_fixed'] = True  # نستخدم عمود وهمي لضمان المعالجة مرة واحدة
        self.ids.hint_label.text = fix_arabic_text("لتحسين الفهم، تم اعتماد تلوين مختلف لكل سطر\nبحسب محتواه كالتالي:\n- اللون الأصفر: هو الفعل الذي تريد البحث عنه\n- اللون الأخضر: يُشير إلى الضمير الذي يمثل الفاعل\n- اللون الأبيض: يُستخدم لتمثيل الضمائر التي تدل على\nالمفعول به.\n- اللون الأزرق: يُوضح طريقة نطق الكلمات بالشاوية\n- الأزمـنـة المـعـتـمـدة فـي الـتـصـريـف هـي:\n  الماضي/الحاضر/المستقبل، بهذا الترتيب.\nمثال توضيحي:\n- ضرب (الفعل)\n- ضربتُ (الفعل + تاء الفاعل)\n- ضربتكَ (الفعل + تاء الفاعل+ كاف المفعول به)\n بـمـعـنـى أنـا ضربـتـك أنـت")
        self.ids.pronoun_label.text = ""  # إفراغ النتائج السابقة إن وجدت
        self.ids.pronoun_input.str = ""
        self.ids.pronoun_input.focus = True
    def on_search_verb(self):
        search_term = self.ids.pronoun_input.text.strip()
        if not search_term:
            return
        results = pf[pf["verb"] == search_term]
        if not results.empty:
            self.ids.hint_label.text = ""
            result_text = ""
            # تعريف الألوان لكل سطر
            colors = {
                "verb": "#FFD700",          # أصفر باهت
                "tense": "#00CC66",         # أخضر باهت
                "pronunciation": "#4DBFBF", # أبيض رمادي
                "default": "#B4BEC8FF"        # سيان باهت (مخفف من السماوي)
            }
            lines = []
            for index, row in results.iterrows():
                lines.append(f"[color={colors['verb']}]الفعل: {fix_arabic_text(row['verb'])}[/color]")
                lines.append(f"[color={colors['tense']}]الضمير: {row['pronoun ana']}[/color]")
                lines.append(f"[color={colors['default']}]أنت: {row['anta']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinanta']}[/color]")
                lines.append(f"[color={colors['default']}]أنتي: {row['anti']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinanti']}[/color]")
                lines.append(f"[color={colors['default']}]أنتم: {row['antom']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinantom']}[/color]")
                lines.append(f"[color={colors['default']}]هو: {row['howa']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhowa']}[/color]")
                lines.append(f"[color={colors['default']}]هي: {row['hiya']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhiya']}[/color]")
                lines.append(f"[color={colors['default']}]هم: {row['hom']}[/color]")
                lines.append(f"[color={colors['tense']}]الضمير: {row['pronoun nahno']}[/color]")
                lines.append(f"[color={colors['default']}]أنت: {row['anta1']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinanta1']}[/color]")
                lines.append(f"[color={colors['default']}]أنتي: {row['anti1']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinanti1']}[/color]")
                lines.append(f"[color={colors['default']}]أنتم: {row['antom1']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinantom1']}[/color]")
                lines.append(f"[color={colors['default']}]هو: {row['howa1']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhowa1']}[/color]")
                lines.append(f"[color={colors['default']}]هي: {row['hiya1']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhiya1']}[/color]")
                lines.append(f"[color={colors['default']}]هم: {row['hom1']}[/color]")
                lines.append(f"[color={colors['tense']}]الضمير: {row['pronoun anta']}[/color]")
                lines.append(f"[color={colors['default']}]أنا: {row['ana2']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinana2']}[/color]")
                lines.append(f"[color={colors['default']}]نحن: {row['nahno2']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinnahno2']}[/color]")
                lines.append(f"[color={colors['default']}]هو: {row['howa2']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhowa2']}[/color]")
                lines.append(f"[color={colors['default']}]هي: {row['hiya2']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhiya2']}[/color]")
                lines.append(f"[color={colors['default']}]هم: {row['hom2']}[/color]")
                lines.append(f"[color={colors['tense']}]الضمير: {row['pronoun antom']}[/color]")
                lines.append(f"[color={colors['default']}]أنا: {row['ana3']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinana3']}[/color]")
                lines.append(f"[color={colors['default']}]نحن: {row['nahno3']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinnahno3']}[/color]")
                lines.append(f"[color={colors['default']}]هو: {row['howa3']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhowa3']}[/color]")
                lines.append(f"[color={colors['default']}]هي: {row['hiya3']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhiya3']}[/color]")
                lines.append(f"[color={colors['default']}]هم: {row['hom3']}[/color]")
                lines.append(f"[color={colors['tense']}]الضمير: {row['pronoun howa']}[/color]")
                lines.append(f"[color={colors['default']}]أنا: {row['ana4']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinana4']}[/color]")
                lines.append(f"[color={colors['default']}]نحن: {row['nahno4']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinnahno4']}[/color]")
                lines.append(f"[color={colors['default']}]أنت: {row['anta4']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinanta4']}[/color]")
                lines.append(f"[color={colors['default']}]أنتي: {row['anti4']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinanti4']}[/color]")
                lines.append(f"[color={colors['default']}]أنتم: {row['antom4']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinantom4']}[/color]")
                lines.append(f"[color={colors['default']}]هو: {row['howa4']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhowa4']}[/color]")
                lines.append(f"[color={colors['default']}]هي: {row['hiya4']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhiya4']}[/color]")
                lines.append(f"[color={colors['default']}]هم: {row['hom4']}[/color]")
                lines.append(f"[color={colors['tense']}]الضمير: {row['pronoun hiya']}[/color]")
                lines.append(f"[color={colors['default']}]أنا: {row['ana5']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinana5']}[/color]")
                lines.append(f"[color={colors['default']}]نحن: {row['nahno5']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinnahno5']}[/color]")
                lines.append(f"[color={colors['default']}]أنت: {row['anta5']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinanta5']}[/color]")
                lines.append(f"[color={colors['default']}]أنتي: {row['anti5']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinanti5']}[/color]")
                lines.append(f"[color={colors['default']}]أنتم: {row['antom5']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinantom5']}[/color]")
                lines.append(f"[color={colors['default']}]هو: {row['howa5']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhowa5']}[/color]")
                lines.append(f"[color={colors['default']}]هي: {row['hiya5']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhiya5']}[/color]")
                lines.append(f"[color={colors['default']}]هم: {row['hom5']}[/color]")
                lines.append(f"[color={colors['tense']}]الضمير: {row['pronoun hom']}[/color]")
                lines.append(f"[color={colors['default']}]أنا: {row['ana6']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinana6']}[/color]")
                lines.append(f"[color={colors['default']}]نحن: {row['nahno6']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinnahno6']}[/color]")
                lines.append(f"[color={colors['default']}]أنت: {row['anta6']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinanta6']}[/color]")
                lines.append(f"[color={colors['default']}]أنتي: {row['anti6']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinanti6']}[/color]")
                lines.append(f"[color={colors['default']}]أنتم: {row['antom6']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinantom6']}[/color]")
                lines.append(f"[color={colors['default']}]هو: {row['howa6']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhowa6']}[/color]")
                lines.append(f"[color={colors['default']}]هي: {row['hiya6']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhiya6']}[/color]")
                lines.append(f"[color={colors['default']}]هم: {row['hom6']}[/color]")
                lines.append("")
            for line in lines:
                result_text += arabic_reshaper.reshape(fix_arabic_text(line)) + '\n'
            self.ids.pronoun_label.text = result_text
            self.ids.pronoun_input.text = ""
            self.ids.pronoun_input.str = ""
        else:
            create_popup_pronoun()
            self.ids.pronoun_label.text = ""
        self.ids.pronoun_input.focus = True


class DictionaryScreen(MDScreen):
    def on_pre_enter(self, *args):
        global df
        if 'arabic_fixed' not in df.columns:
            df['arabic'] = df['arabic'].apply(lambda x: fix_arabic_text(x) if isinstance(x, str) else x)
            df['arabic_fixed'] = True
        self.ids.result_label.text = ""
        self.ids.dictionary_input.str = ""
        self.ids.dictionary_input.focus = True
        self.ids.favorite_button.icon = "heart-outline"
    def on_search(self):
        search_term = self.ids.dictionary_input.text.strip()
        if not search_term:
            return
        results = df[df["arabic"] == search_term]
        if not results.empty:
            result_text = ""
            for index, row in results.iterrows():
                result_text += arabic_reshaper.reshape(fix_arabic_text(
                    f"العربية: {(fix_arabic_text(row['arabic']))}\nالشاوية: {(row['amazigh'])}\nالنطق: {(row['latin'])}\nالجمع: {(row['plural'])}\nالنطق للجمع: {(row['latinplural'])}\nالمنطقة: {(row['origin'])}\n\n"))
            self.ids.result_label.text = result_text
            self.ids.dictionary_input.focus = True
            self.ids.dictionary_input.text = ""
            self.ids.dictionary_input.str = ""
            favorite_screen = self.manager.get_screen('favorite')
            if favorite_screen.word_exists_in_favorites(row['arabic']):
                self.ids.favorite_button.icon = "heart"  # قلب ممتلئ
            else:
                self.ids.favorite_button.icon = "heart-outline"
            self.ids.favorite_button.on_release = lambda: self.add_word_to_favorites(row['arabic'], fix_arabic_text(row['amazigh']))
        else:
            create_popup_dictionary()
        self.ids.dictionary_input.focus = True

    def add_word_to_favorites(self, arabic_word, chaoui_word):
        favorite_screen = self.manager.get_screen('favorite')  # تأكد من أن اسم الشاشة صحيح
        favorite_screen.add_word_to_database_favorite(arabic_word, chaoui_word)
        self.ids.favorite_button.icon = "heart"


class AddWordScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db_name = "dictionary.db"
        self.create_table()
    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS words (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                arabic_phrase TEXT NOT NULL,
                chaoui_phrase TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()
    def add_word_to_database(self, word, meaning):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO words (arabic_phrase, chaoui_phrase) VALUES (?, ?)", (word, meaning))
        conn.commit()
        conn.close()
    def get_all_words(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM words")
        words = cursor.fetchall()
        conn.close()
        return words
    def load_words(self):
        self.ids.mdlist.clear_widgets()  # Clear existing items to avoid duplicates
        words = self.get_all_words()
        for word_id, arabic_phrase, chaoui_phrase in words:
            item = CustomThreeLineListItem(
                text=arabic_phrase,
                secondary_text=chaoui_phrase,
                tertiary_text="",
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
                secondary_theme_text_color="Custom",
                secondary_text_color=(0, 1, 1, 1)
            )
            delete_icon = MDIconButton(
                icon="delete",
                theme_icon_color="Custom",
                icon_color=(1, 1, 1, 1),
                icon_size="20dp",
                on_release=lambda x, word_id=word_id, item=item: self.show_delete_confirmation(word_id, item),
                # Use default argument
                pos_hint={"center_x": 0.08, "center_y": 0.55}
            )
            item.add_widget(delete_icon)
            self.ids.mdlist.add_widget(item)
    def show_delete_confirmation(self, word_id, item):
        # Create a dialog for confirmation
        self.dialog = MDDialog(
            title="Alert",
            text="Are you sure you want to delete this item?",
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    on_release=self.close_dialog
                ),
                MDFlatButton(
                    text="Yes",
                    on_release=lambda x: self.delete_word(item, word_id)
                ),
            ],
        )
        self.dialog.open()
    def close_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()  # Close the dialog
    def delete_word(self, item, word_id):
        self.ids.mdlist.remove_widget(item)  # Remove item from the UI
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM words WHERE id = ?", (word_id,))
        conn.commit()
        conn.close()
        self.close_dialog()

    def on_pre_enter(self, *args):
        self.load_words()  # Load words when entering the screen


class UserInput(MDScreen):
    def save_word(self, word, meaning):
        if word and meaning:
            word = arabic_reshaper.reshape(word)
            meaning = arabic_reshaper.reshape(meaning)
            self.manager.get_screen("addword").add_word_to_database(word, meaning)
            self.ids.word_input.text= ""
            self.ids.meaning_input.text = ""
            self.manager.current = 'addword'
    def on_pre_enter(self, *args):
        self.ids.word_input.str = ""
        self.ids.meaning_input.str = ""


class VerbsScreen(MDScreen):
    def on_pre_enter(self, *args):
        global vf
        # إصلاح النص العربي (مرة واحدة فقط - انتبه أن لا تُكرر المعالجة)
        if 'arabic_fixed' not in vf.columns:
            # Ensure that we only apply the function to string values
            vf['verb'] = vf['verb'].apply(lambda x: fix_arabic_text(x) if isinstance(x, str) else x)
            vf['arabic_fixed'] = True  # نستخدم عمود وهمي لضمان المعالجة مرة واحدة
        self.ids.verb_label.text = ""
        self.ids.verb_input.str = ""
        self.ids.verb_input.focus = True
    def on_search_verb(self):
        search_term = self.ids.verb_input.text.strip()
        if not search_term:
            return
        results = vf[vf["verb"] == search_term]
        if not results.empty:
            result_text = ""
            # تعريف الألوان لكل سطر
            colors = {
                "verb": "#FFD700",          # أبيض
                "tense": "#00CC66",         # أخضر
                "pronunciation": "#4DBFBF", # أصفر
                "default": "#B4BEC8FF"        # سماوي
            }
            lines = []
            for index, row in results.iterrows():
                lines.append(f"[color={colors['verb']}]الفعل: {fix_arabic_text(row['verb'])}[/color]")
                lines.append(f"[color={colors['tense']}]الزمن: {row['tense']}[/color]")
                lines.append(f"[color={colors['default']}]أنا (نتش): {row['ana']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinana']} :النطق [/color]")
                lines.append(f"[color={colors['default']}]نحن (نشني): {row['nahno']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinnahno']} :النطق [/color]")
                lines.append(f"[color={colors['default']}]أنت (شك): {row['anta']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinanta']} :النطق [/color]")
                lines.append(f"[color={colors['default']}]أنتي (شم): {row['anti']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinanti']} :النطق [/color]")
                lines.append(f"[color={colors['default']}]أنتم (كميم): {row['antom']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinantom']} :النطق [/color]")
                lines.append(f"[color={colors['default']}]هو (نت): {row['howa']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhowa']} :النطق [/color]")
                lines.append(f"[color={colors['default']}]هي (نتاث): {row['hiya']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhiya']} :النطق [/color]")
                lines.append(f"[color={colors['default']}]هم (نهنين): {row['hom']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinhom']} :النطق [/color]")
                lines.append(f"[color={colors['tense']}]زمن الأمر: {row['order']}[/color]")
                lines.append(f"[color={colors['default']}]أنت/أنتي/أنتم: {row['pronouns']}[/color]")
                lines.append(f"[color={colors['pronunciation']}]{row['latinpro']} :النطق [/color]")
                lines.append("")  # لإضافة سطر فارغ بين النتائج
            # بناء نص النتيجة النهائي مع إعادة تشكيل النص العربي
            for line in lines:
                result_text += arabic_reshaper.reshape(fix_arabic_text(line)) + '\n'
            self.ids.verb_label.text = result_text
            self.ids.verb_input.text = ""
            self.ids.verb_input.str = ""
        else:
            create_popup_verb()
            self.ids.verb_label.text = ""
        self.ids.verb_input.focus = True


class MyApp(MDApp):
    def build(self):
        pass
    def get_arabic_text(self, text):
        return fix_arabic_text(text)

    def open_email(self):
        webbrowser.open("mailto:khaledaguaguena8@gmail.com")

    def open_whatsapp(self):
        webbrowser.open("https://wa.me/213796924032")

    def open_upwork(self):
        webbrowser.open("https://www.upwork.com/ab/account-security/login?redir=%2Fnx%2Ffind-work%2F")

    def open_phone(self):
        webbrowser.open("tel:+213796924032")
if __name__ == "__main__":
    MyApp().run()


