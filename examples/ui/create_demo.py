import zoof
from zoof import ui

def keep_alive():
    __iep__.process_commands()
    ui.call_later(0.1, keep_alive)



class MyApp(ui.App):
    
    _config = ui.App.Config(title='Zoof test app', size=(400, 300),
                            icon='https://assets-cdn.github.com/favicon.ico')
               
    def init(self):
        
        with ui.HBox(self):
                
            with ui.VBox():
                
                with ui.HBox(flex=0):
                    ui.Button(text='Box A', flex=0)
                    ui.Button(text='Box B', flex=0)
                    ui.Button(text='Box C is a bit longer', flex=0)
                
                with ui.HBox(flex=0):
                    ui.Button(text='Box A', flex=1)
                    ui.Button(text='Box B', flex=1)
                    ui.Button(text='Box C is a bit longer', flex=1)
                
                with ui.HBox(flex=0):
                    ui.Button(text='Box A', flex=1)
                    ui.Button(text='Box B', flex=0)
                    ui.Button(text='Box C is a bit longer', flex=2)
                
                with ui.HBox(flex=1, spacing=10) as self.hbox2:
                    ui.Button(text='Box A', flex=1)
                    ui.Button(text='Box B', flex=2)
                    ui.Button(text='Box C is a bit longer', flex=3)
            
            with ui.VBox():
                
                with ui.HBox(flex=0):
                    ui.Button(text='Box A', flex=0)
                    ui.Button(text='Box B', flex=0)
                    ui.Button(text='Box C is a bit longer', flex=0)
                
                with ui.HBox(flex=0):
                    ui.Button(text='Box A', flex=1)
                    ui.Button(text='Box B', flex=1)
                    ui.Button(text='Box C is a bit longer', flex=1)
                
                with ui.HBox(flex=0):
                    ui.Button(text='Box A', flex=1)
                    ui.Button(text='Box B', flex=0)
                    ui.Button(text='Box C is a bit longer', flex=2)
                
                with ui.HBox(flex=1, spacing=10) as self.hbox2:
                    ui.Button(text='Box A', flex=1)
                    ui.Button(text='Box B', flex=2)
                    ui.Button(text='Box C is a bit longer', flex=3)
            
    
        #self.win = ui.Window(self, 'A new window!')
        
# class MyApp2(ui.App):
#     def init(self):
#         self.b = ui.Button(self, 'Hello world')

app = MyApp()
keep_alive()
ui.run(runtime='xul')
