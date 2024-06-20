from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel

class TwoPanelLayoutApp(MDApp):
    def build(self):
        Window.size = (900, 500)
        screen_manager = ScreenManager()
        screen = Screen()
        screen.add_widget(self._create_split_layout_panel())
        screen_manager.add_widget(screen)
        return screen_manager
        
    def _create_split_layout_panel(self):
        split_layout_panel = GridLayout(cols=2)
        # Add the navigation bar panel to split layout panel
        split_layout_panel.add_widget(self._create_navigation_bar_panel())
        # Add the content panel to split layout panel
        split_layout_panel.add_widget(self._create_content_panel())
        
        return split_layout_panel
    
    
    def _create_navigation_bar_panel(self):
        #Create a grid layout with 1 coloumn for navigation bar
        navigation_bar_panel = GridLayout(cols=1, spacing=20)
        navigation_bar_panel.size_hint_x = None
        navigation_bar_panel.width = 300
        
        #Create a label for the navigation bar panel title with bold text
        navigation_bar_panel_title= MDLabel(text="NavBar", size_hint=(1, 0.1), theme_text_color = "Secondary",
                                            font_style="H6")
        #Create a label for the navigation bar panel content with bold text
        navigation_bar_panel_content = MDLabel(text="Nav Bar Buttons", size_hint=(1, 0.9), theme_text_color= "Secondary",
                                               font_size="15sp", markup=True)
        navigation_bar_panel.add_widget(navigation_bar_panel_title)
        navigation_bar_panel.add_widget(navigation_bar_panel_content)
        return navigation_bar_panel
        
        
        
    def _create_content_panel(self):
        content_panel  = GridLayout(cols=1, spacing=20)
        content_panel.size_hint_x = None
        content_panel.width = 600
        
        #Create a label for the content panel title with bold text
        content_panel_title = MDLabel(text="Content Panel", size_hint=(1, 0.1), theme_text_color ="Secondary",
                                      font_style="H6")
        # Create a label for the content panel content with bold text
        content_panel_content = MDLabel(text="Content Space", size_hint=(1, 0.9), theme_text_color ="Secondary",
                                        font_size="15sp", markup=True)
        # Add the elements to the content panel
        content_panel.add_widget(content_panel_title)
        content_panel.add_widget(content_panel_content)
        
        return content_panel
    
    
#Create an instance of TwoPanelLayoutApp and run the app
TwoPanelLayoutApp().run()
        