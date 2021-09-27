from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('design.kv')

class MainScreen(Screen):
    def go_to_pressure_head(self):
        self.manager.transition.direction = "left"
        self.manager.current = "pressure_head_screen"
    def go_to_horizontal_volume(self):
        self.manager.transition.direction = "left"
        self.manager.current = "horizontal_volume_screen"
    def go_to_vertical_volume(self):
        self.manager.transition.direction = "left"
        self.manager.current = "vertical_volume_screen"
    def go_to_sphere_volume(self):
        self.manager.transition.direction = "left"
        self.manager.current = "sphere_volume_screen"
    def go_to_other_conversions(self):
        self.manager.transition.direction = "left"
        self.manager.current = "other_conversions_screen"


class PressureHeadScreen(Screen):
    def go_to_home(self):
        self.manager.transition.direction = "right"
        self.manager.current = "main_screen"     
    def convert_to_head(self, sg, pressurehead):
        try:
            sg=float(sg)
            pressurehead=float(pressurehead)
            
            if float(sg)>0:
                head = float(pressurehead) * 2.31 / float(sg)
                self.ids.p_h_output.text = "Head = " + str(round(head, 2)) + " ft"
                self.ids.h_p_output.text = ""
            elif float(sg)<=0:
                self.ids.p_h_output.text = "Enter a SG greater than 0!"
                self.ids.h_p_output.text = ""
            else:
                self.ids.p_h_output.text = "Don't leave inputs blank"
                self.ids.h_p_output.text = ""
        except ValueError:
            self.ids.p_h_output.text = "Input was not a number"
            self.ids.h_p_output.text = ""
    def convert_to_pressure(self, sg, pressurehead):
        try:    
            sg=float(sg)
            pressurehead=float(pressurehead)
            
            if float(sg)>0:
                pressure = sg * pressurehead / 2.31
                self.ids.h_p_output.text = "Pressure = " + str(round(pressure, 2)) + " psig"
                self.ids.p_h_output.text = ""
            elif float(sg)<=0:
                self.ids.h_p_output.text = "Enter a SG greater than 0!"
                self.ids.p_h_output.text = ""
            else:
                self.ids.h_p_output.text = "Don't leave inputs blank"
                self.ids.p_h_output.text = ""
        except ValueError:
            self.ids.h_p_output.text = "Input was not a number"
            self.ids.p_h_output.text = ""

class HorizontalVolumeScreen(Screen):
    def go_to_home(self):
        self.manager.transition.direction = "right"
        self.manager.current = "main_screen"     
    def horizontal(self,x,y,h,D,L):
        try:
            x=float(x)
            y=float(y)
            h=float(h)
            D=float(D)
            L=float(L)
            b=D/4 #semi-ellipsoidal head 2:1
            K=2*b/D
            H1=(x+y*(h/100 - 0.5))/12 #inch
            Ze=H1/D
            Zc=H1/D
            fZe= 0.0093665092*Ze**4 - 2.0209811828*Ze**3 + 3.0148766410*Ze**2 - 0.0033697820*Ze + 0.0000898677
            fZc= -0.0049216462*Zc**4 - 1.0839030424*Zc**3 + 1.6340572990*Zc**2 + 0.4703929912*Ze - 0.0079299847
            volume = 0.17810760667*(1/6*3.14*K*D**3 * fZe    +  0.25*3.14*D**2*L*fZc) #cuft to barrels
            self.ids.HorizontalVolume.text = "Partial volume = " + str(round(volume, 2)) + " bbl"
   
            totalvolume=0.17810760667*(1/6*3.14*K*D**3   +  0.25*3.14*D**2*L) #cuft to barrels
            self.ids.HorizontalTotalVolume.text = "Total volume = " + str(round(totalvolume, 2)) + " bbl"
            
            remainingvolume=totalvolume - volume
            self.ids.HorizontalRemainingVolume.text = "Remaining volume = " + str(round(remainingvolume, 2)) + " bbl"        
        except ValueError:
            self.ids.HorizontalTotalVolume.text = "Input was not a number" #this is the middle of the page, so chose this ID
 

class VerticalVolumeScreen(Screen):
    def go_to_home(self):
        self.manager.transition.direction = "right"
        self.manager.current = "main_screen"     
    def vertical(self,x,y,h,D,L):
        try:
            x=float(x)
            y=float(y)
            h=float(h)
            D=float(D)
            L=float(L)
            b=D/4 #semi-ellipsoidal head 2:1
            K=2*b/D
            H1=(x+y*(h/100 - 0.5))/12 #inch
            H3=(x-(y/2*(50-h)/50))/12-H1
            Ze=(H1+H3)/(K*D)
            fZe= 0.0093665092*Ze**4 - 2.0209811828*Ze**3 + 3.0148766410*Ze**2 - 0.0033697820*Ze + 0.0000898677
            volume = 0.17810760667*(1/6*3.14*K*D**3 * fZe    +  0.25*3.14*D**2*H3) #cuft to barrels
            self.ids.VerticalVolume.text = "Partial volume = " + str(round(volume, 2)) + " bbl"
   
            totalvolume=0.17810760667*(1/6*3.14*K*D**3   +  0.25*3.14*D**2*L) #cuft to barrels
            self.ids.VerticalTotalVolume.text = "Total volume = " + str(round(totalvolume, 2)) + " bbl"
            
            remainingvolume=totalvolume - volume
            self.ids.VerticalRemainingVolume.text = "Remaining volume = " + str(round(remainingvolume, 2)) + " bbl"        
        except ValueError:
            self.ids.VerticalTotalVolume.text = "Input was not a number" #this is the middle of the page, so chose this ID               

class SphereVolumeScreen(Screen):
    def go_to_home(self):
        self.manager.transition.direction = "right"
        self.manager.current = "main_screen"     
    def sphere(self,x,y,h,D):
        try:
            x=float(x)
            y=float(y)
            h=float(h)
            D=float(D)
            H=(x-((50-h)/50)*(y/2))/12
            volume = 0.17810760667*(3.14/3*H**2*(1.5*D-H)) #cuft to barrels
            self.ids.SphereVolume.text = "Partial volume = " + str(round(volume, 2)) + " bbl"
   
            totalvolume=0.17810760667*(1/6*3.14*D**3) #cuft to barrels
            self.ids.SphereTotalVolume.text = "Total volume = " + str(round(totalvolume, 2)) + " bbl"
            
            remainingvolume=totalvolume - volume
            self.ids.SphereRemainingVolume.text = "Remaining volume = " + str(round(remainingvolume, 2)) + " bbl"        
        except ValueError:
            self.ids.SphereTotalVolume.text = "Input was not a number" #this is the middle of the page, so chose this ID 
    
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()