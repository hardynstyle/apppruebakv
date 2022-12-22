# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 15:46:07 2022

@author: hardyn
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 08:29:57 2022

@author: hardyn
"""

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.slider.slider import MDSlider
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarIconListItem
# from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty, StringProperty



from kivy.uix.camera import Camera

from kivy.uix.image import Image
from kivy.clock import Clock

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:set text_color get_color_from_hex("#090909")
#:set focus_color get_color_from_hex("#85c4be")
#:set ripple_color get_color_from_hex("#c5bdd2")
#:set bg_color get_color_from_hex("#faffff")
#:set selected_color get_color_from_hex("#0c6c4d")
#: set colores  (89, 0, 0, 125, 255, 255)  # Blue


<Content>
    orientation: "vertical"
    spacing: "20dp"
    size_hint_y: None   
    height: "300dp"
    
    MDLabel:
       
        text: "Tonalidad Minima"
        font_style:"Overline"
        
    MySlider:
        id: ton_minima
        min: 0
        max: 255
        value: colores[0]
        hint: True
        color: (0,1,0,1) 
        on_touch_up: app.printval()
    
    MDLabel:
        font_style:"Overline"
        text: "Saturacion Minima"
    MDSlider:
        id:saturacion_minima
        min: 0
        max: 255
        value: colores[1]
        hint: True
        color: app.theme_cls.accent_color  
        on_touch_up: app.printval()        
    MDLabel:
        font_style:"Overline"
        text: "luminucidad Minima"
    MDSlider:
        id:luz_minima
        min: 0
        max: 255
        value: colores[2]
        hint: True
        on_touch_up: app.printval()  
    MDLabel:
       
        text: "Tonalidad Maxima"
        font_style:"Overline"
        
       
    MDSlider:
        id:tonalidad_maxima
        min: 0
        max: 255
        value: colores[3]
        hint: True
        color: (0,1,0,1) 
        on_touch_up: app.printval()    
    MDLabel:
        font_style:"Overline"
        text: "Saturacion Maxima"
    MDSlider:
        id:saturacion_maxima
        min: 0
        max: 255
        value: colores[4]
        hint: True
        color: app.theme_cls.accent_color  
        on_touch_up: app.printval()        
    MDLabel:
        font_style:"Overline"
        text: "luminucidad Maxima"
    MDSlider:
        id:luz_maxima
        min: 0
        max: 255
        value: colores[5]
        hint: True  
        on_touch_up: app.printval()
                
<ItemConfirm>
    on_release: root.set_icon(check)

    CheckboxLeftWidget:
        id: check
        group: "check"
     
        
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: focus_color
    unfocus_color: bg_color
    text_color: text_color
    icon_color: text_color
    ripple_color: ripple_color
    selected_color: selected_color


<DrawerLabelItem@MDNavigationDrawerItem>
    bg_color: bg_color
    text_color: text_color
    icon_color: text_color
    _no_ripple_effect: True
    
MDScreen:
  
    
    MDBottomNavigation:
        panel_color: get_color_from_hex("#eeeaea")
        selected_color_background: get_color_from_hex("#97ecf8")
        text_color_active: 0, 0, 0, 1


            
  
        MDBottomNavigationItem:
            id:imagenes
            name: 'screen 1'
            text: 'fotos'
            icon: 'image-multiple'
            # badge_icon: None
            MDLabel:
                text: 'fotos'
                halign: 'center'  
            MDBoxLayout:
            
                MDBoxLayout:
                    id:camara
                    padding: "24dp"


        MDBottomNavigationItem:
            id: reproductor
            name: 'screen 2'
            text: 'videos'
            icon: 'movie-play'
            badge_icon: "numeric-5"

            MDLabel:
                text: 'videos'
                halign: 'center' 
    MDFloatingActionButtonSpeedDial:
  
        data: app.data     
        # hint_animation: True
        # bg_hint_color: app.theme_cls.primary_light
        bg_color_root_button:(0,0,0,1)
        bg_color_stack_button:(0,0,0,1)
        bg_hint_color:(1,1,1,1)   
        color_icon_root_button:(1,0,0,1)
        color_icon_stack_button:(1,1,0,1)         
        callback: app.callback    
            
                
    MDNavigationLayout:
        ScreenManager:

            MDScreen:
                MDToolbar:
                    id:toolbar
                   
                    elevation: 10
                    pos_hint: {"top": 1}
                    md_bg_color: get_color_from_hex("#12b9d3")
                    specific_text_color:(1,1,1,1)
                    left_action_items:
                        [  [ 'menu',lambda x: app.nav_drawer_open()] ,['account'],['magnify']]
                    right_action_items:[['share-circle'],['cog',lambda x: app.show_confirmation_dialog()],["dots-vertical",lambda x: app.show_slider()]]
                   
                    # left_action_items: [['menu', lambda x: x],['home'],['share-variant'],['cog'],['account'],['information'],['share-circle']]
             
                     
                 
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0) if self.anchor == "left" else (16, 0, 0, 16)
            md_bg_color: bg_color

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    source: "personas/hardyn.png"
                    title: "Usuario:"
                    text: "ray.huanca.16@unsch.edu.pe"
                    
                    spacing: "4dp"
                    padding: "12dp", "12dp", 0, "56dp"
        

                MDNavigationDrawerLabel:
                    text: "Mail"

                DrawerClickableItem:
                    icon: "gmail"
                    right_text: "+99"
                    text_right_color: text_color
                    text: "Inbox"

                DrawerClickableItem:
                    icon: "send"
                    text: "Outbox"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "bases"

                DrawerClickableItem:
                    icon: "information"
                    text: "info"
                DrawerClickableItem:
                    icon: "tooltip-plus"
                    text: "extensiones"
                    on_press: app.adds_menu_inferior()
                DrawerClickableItem:
                    icon: "exit-to-app"
                    text: "exit"
                    # on_press: quit()
                
'''
class MySlider(MDSlider):
    sound = ObjectProperty(None)
      

        
    def on_touch_up(self, touch):
        if touch.grab_current == self:
            # call super method and save its return
            ret_val = super(MySlider, self).on_touch_up(touch)
            return ret_val
        else:
            return super(MySlider, self).on_touch_up(touch)
     
class Content(BoxLayout):
    pass




class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        global filtro_selecionado
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        
        for cont,check in enumerate(check_list):
    
            if check ==instance_check:
                filtro_selecionado=cont
                
     
            if check != instance_check:
                check.active = False
        print("filtro_selecionado:",filtro_selecionado)
      


        
class KivyCamera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        


    def update(self, dt):

        pass
            
            
            
            
                
class Hardyn(MDApp):
    global filtro_selecionado
    global tonalidad_minima,saturacion_minima,luz_minima,tonalidad_maxima,saturacion_maxima,luz_maxima
    filtro_selecionado=0
    dialogo_check = None
    dialogo_slider=None
    # icol = (36, 202, 59, 71, 255, 255)    # Green
    #icol = (18, 0, 196, 36, 255, 255)  # Yellow
    icol = (89, 0, 0, 125, 255, 255)  # Blue
    # icol = (0, 100, 80, 10, 255, 255)   # Red
    (tonalidad_minima,saturacion_minima,luz_minima,tonalidad_maxima,saturacion_maxima,luz_maxima)=icol
    data = {
        'fotos': 'image-multiple',
        'videos': 'movie-play',
        'musica': 'music-note-plus',
        'archivos': 'folder-open',
        'camara': 'camera-plus',
        
    }    
    def build(self):
       
        return Builder.load_string(KV)
    
# lambda x:   nav_drawer.set_state("open")  if nav_drawer.state == "close" else                             nav_drawer.set_state("close")  
    def nav_drawer_open(self):
        if self.root.ids.nav_drawer.set_state == "open":
            self.root.ids.nav_drawer.set_state("close")

        else:
            self.root.ids.nav_drawer.set_state("open")
            # self.root.ids.rail.add_widget(MDRoundFlatButton(    text= "adds",text_color= (0, 0, 0, 1) ))
            
            
    def on_start(self):

        return True
        
    def on_stop(self):
        #without this, app will not exit even if the window is closed
        self.capture.release()

    def callback(self, instance):
        print(instance.icon)  
        if instance.icon=="camera-plus":
            pass
            
        elif instance.icon=="music-note-plus":
            pass
            # codigo_principal.juego_de_circulos(self)
            # self.capture = cv2.VideoCapture(0)
            # self.my_camera = KivyCamera(capture=self.capture, fps=30)
            
            # self.root.ids.imagenes.add_widget(self.my_camera)
        elif instance.icon=="folder-open":
            Hardyn.file_manager_open(self) 
        else:
            pass
            
    def file_manager_open(self):
        self.manager_open = False
        self.file_manager = MDFileManager(
        exit_manager=self.exit_manager,
        select_path=self.select_path,preview=True,)
            
        
        
        self.file_manager.show('/')  # Directorio
        self.manager_open = True
        # self.file_manager.show_disks()
        

    def select_path(self, path):
        '''Se llamará cuando haga clic en el nombre del archivo
        o el botón de selección de catálogo.

        :escriba la ruta: str;
        :param ruta: ruta al directorio o archivo seleccionado;
        '''

        self.exit_manager()
        print("ruta:")
        print(path)
        toast(path)
        self.root.ids.reproductor.add_widget(VideoPlayer(source=path,state='stop'))
        

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()
        
    def callback_for_menu_items(self, *args):
        toast(args[0])          
    def adds_menu_inferior(self):
        
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Facebook": "facebook",
            "YouTube": "youtube",
            "Twitter": "twitter",
            "Da Cloud": "cloud-upload",
            "Camera": "camera",
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()  
        
    def closed_check_dialogo(self,obj):
        self.dialogo_check.dismiss()
               
    def show_confirmation_dialog(self):
        global filtro_selecionado
        # filtro_calido,filtro_helido,filtro_gotham,filtro_calido_griss,filtro_dibujo_lapiz,filtro_dibujo_esterilizado,filtro_carton1,filtro_carton2

        if not self.dialogo_check:
            self.dialogo_check = MDDialog(
                title="Tipo de filtros:",
                type="confirmation",
                items=[
                    ItemConfirm(text="Ninguno 0"),
                    ItemConfirm(text="RedMagic 1"),
                    ItemConfirm(text="Draw_fake 2"),
                    ItemConfirm(text="UltraUV 3"),
                    ItemConfirm(text="BlackRose 4"),
                    ItemConfirm(text="Acuarela 5"),
                    ItemConfirm(text="GreenRose 6"),
                    ItemConfirm(text="Sirena 7"),
                    ItemConfirm(text="Grenhsv 8"),
                    ItemConfirm(text="Griss4k 9"),
                    ItemConfirm(text="Magic 10"),
                    ItemConfirm(text="Belico 11"),
                    ItemConfirm(text="delows 12"),
                    ItemConfirm(text="GreenDayer 13"),
                    ItemConfirm(text="GrapheHSV 14"),
                    ItemConfirm(text="Venuss 15"),
                    ItemConfirm(text="BlackGraphe 16"),
                    ItemConfirm(text="duoacuamat 17"),
                    ItemConfirm(text="BlueBasic 18"),
                    ItemConfirm(text="Byredwhite 19"),
                    ItemConfirm(text="behavior 20"),
                    ItemConfirm(text="Filtro6kextremo 21"),
                    ItemConfirm(text="filtro_calido"),
                    ItemConfirm(text="filtro_helido"),
                    ItemConfirm(text="filtro_gotham"),
                    ItemConfirm(text="filtro_calido_griss"),
                    ItemConfirm(text="filtro_db_lapiz"),
                    ItemConfirm(text="filtro_db_esterilizado"),
                    ItemConfirm(text="filtro_carton1"),
                    ItemConfirm(text="filtro_carton2"),
                ],
                buttons=[
                    MDFlatButton(
                        text="CANCEL",on_release=self.closed_check_dialogo,
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,                       
                       
                    ),
                    MDFlatButton(
                        text="OK",on_release=self.closed_check_dialogo,
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialogo_check.open()
         

         
    def printval(self):
        global tonalidad_minima,saturacion_minima,luz_minima,tonalidad_maxima,saturacion_maxima,luz_maxima
  
        tonalidad_minima=int(self.dialogo_slider.content_cls.ids.ton_minima.value)         
        saturacion_minima=int(self.dialogo_slider.content_cls.ids.saturacion_minima.value )
        luz_minima=int(self.dialogo_slider.content_cls.ids.luz_minima.value)
        tonalidad_maxima=int(self.dialogo_slider.content_cls.ids.tonalidad_maxima.value )   
        saturacion_maxima=int(self.dialogo_slider.content_cls.ids.saturacion_maxima.value )
        luz_maxima=int(self.dialogo_slider.content_cls.ids.luz_maxima.value )
        valores=(tonalidad_minima,saturacion_minima,luz_minima,tonalidad_maxima,saturacion_maxima,luz_maxima)
        print("Valores de rango de colores:")
        print(valores)
    def closed_slider_dialogo(self,obj):      
        self.dialogo_slider.dismiss()   
        
    def show_slider(self):
        
        if not self.dialogo_slider:
            self.dialogo_slider = MDDialog(
                title="Tipo de filtros:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",on_release=self.closed_slider_dialogo,
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,                       
                       
                    ),
                    MDFlatButton(
                        text="OK",on_release=self.closed_slider_dialogo,
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialogo_slider.open()
        
        
        
        
        
        
class codigo_principal():
    def programa_de_deteccion_de_rostros(self):
        pass
        
    
        
        
Hardyn().run()



















