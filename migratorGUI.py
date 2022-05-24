import os,glob,shutil
import json
import types
from kivy.config import Config 
Config.set('graphics','height','520')
Config.set('graphics','width','900')
Config.set('graphics','position','custom')
Config.set('graphics','top','200')
Config.set('graphics','left','510')
Config.set('graphics','resizable','0')


from kivy.utils import get_color_from_hex
from kivy.app import App
from kivy.uix.modalview import ModalView
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle,InstructionGroup,Rectangle
from kivy.properties import StringProperty,ColorProperty,ObjectProperty,ListProperty,NumericProperty
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.list import MDList,ImageLeftWidget,OneLineAvatarListItem,ImageRightWidget
from kivymd.uix.datatables import MDDataTable
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior,HoverBehavior,RectangularRippleBehavior
from kivymd.theming import ThemableBehavior
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager,RiseInTransition,FadeTransition
from kivymd.uix.card import MDCard
from kivy.uix.button import Button
from kivymd.uix.button import MDIconButton
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField

from kivy.core.text import FONT_BOLD, LabelBase
LabelBase.register(name='Calibri Light',fn_regular='C:\\Windows\\Fonts\\calibril.ttf')
LabelBase.register(name='Quicksand',fn_regular=r'C:\Users\thuan\AppData\Local\Microsoft\Windows\Fonts\Quicksand-VariableFont_wght.ttf')

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

configLocation = r"E:\My Coding Shits\Python Shits\OS Experiments\GUIExperiments\kivyMD\fileMigrator\configurations.json"
configData = json.load(open(configLocation))


screenProperties = """
#:import RiseInTransition kivy.uix.screenmanager.RiseInTransition
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
#:import FallOutTransition kivy.uix.screenmanager.FallOutTransition
#:import Window kivy.core.window
#:import MDDataTable kivymd.uix.datatables
ScreenManager:
    transition: FadeTransition()
    WelcomeScreen:
    FunctionScreen:
    allDirScreen:
    addDirScreen:
    changeDestScreen:
    startMigrateScreen:
    removeDirScreen:

<WelcomeScreen>
    name:'welcome'
    canvas.before:
        Rectangle:
            pos:self.pos
            size:self.size
            source: 'bg2.jpg'
    Image:
        source: 'folder.png'
        pos_hint:{'center_x':0.5,'center_y':0.65}
        size_hint:None,None
        width:90
        height:90
    
    MDLabel:
        text: "Files Migrator"
        font_style: "Caption"
        font_size: 50
        pos:(0,0)
        halign:'center'
        theme_text_color: 'Custom'
        text_color:(255/255,255/255,255/255,1)
    MDLabel:
        text:" V1.0 "
        font_style: "H3"
        font_size:30
        halign:'center'
        pos:(0,-60)
        theme_text_color: 'Custom'
        text_color:(255/255,255/255,255/255,1)
    


<MD3Card>
    id: root.cardId
    ripple_behavior: True
    ripple_duration_in_fast:.1
    padding: 16
    size_hint: None, None
    size: "220dp", "110dp"
    border_radius:20
    radius:[20]
    elevation:15
    md_bg_color: (86/255,72/255,139/255,0.2)

    RelativeLayout:
        size:root.size
        Image:
            source:root.imgsource
            allow_stretch: True
            keep_ratio: False
            size_hint_x:None
            size_hint_y:None
            width:60
            height:60
            pos:(0,10)

        BoxLayout
            size:(5,200)
            pos:(35,20)
            MDLabel:   
                text: root.funcText
                font_style: "Button"
                height:self.texture_size[1]
                halign:'center'
                text_size: self.width,None
                size_hint:1,None
                height: self.texture_size[1]
                font_size:18
                color:(1,1,1,1)
                
   
<FunctionScreen>
    name:'function'
    canvas.before:
        Rectangle:
            pos:self.pos
            size:self.size
            source: 'bg2.jpg'
    MDLabel:
        text:'Features'
        font_style:'H2'
        pos:(45,200)
        theme_text_color: 'Custom'
        text_color:(255/255,255/255,255/255,1)
        font_size:50
    
    ScrollView:
        pos_hint:{'center_x':0.56,'center_y':0.25}
        MDList:
            GridLayout:
                cols:3
                rows:2
                spacing:[80,50]
                MD3Card:
                    funcText: "All \\n Directories"
                    imgsource: "allDir.png"
                    cardId: 'allDirCard'
                MD3Card:
                    funcText: "Add \\n Directory"
                    imgsource: "plus.png"
                    cardId: 'addDirCard'
                MD3Card:
                    funcText: "Remove \\n Directory"
                    imgsource: "remove.png"
                    cardId: 'removeDirCard'
                MD3Card:
                    funcText: "Change \\n Destination"
                    imgsource: "destination.png"
                    cardId: 'changeDestCard'
                MD3Card:
                    funcText: "Start \\n Migration"
                    imgsource: "start.png"
                    cardId: 'startMigrateCard'
            
<menuButton>
    icon:"main-menu.png"
    size_hint:None,None
    pos_hint: {'center_x':0.93,'center_y':0.9}
    user_font_size: "35sp"
    ripple_duration_in_fast:.1
    ripple_scale:1
    ripple_alpha: .9
   

<allDirScreen>
    name:'allDir'
    canvas.before:
        Rectangle:
            pos:self.pos
            size:self.size
            source: 'bg2.jpg'
        Color: 
            rgba: 86/255,72/255,139/255,0.5
        RoundedRectangle:
            size:(820,350)
            pos:(42,55)
            radius: [(30, 30), (30, 30), (30, 30), (30, 30)]
    MDLabel:
        text:'All Directories'
        font_style:'H2'
        pos:(45,200)
        theme_text_color: 'Custom'
        text_color:(255/255,255/255,255/255,1)
        font_size:50
    menuButton:


<addDirScreen>
    name: 'addDir'
    canvas.before:
        Rectangle:
            pos:self.pos
            size:self.size
            source: 'bg2.jpg'
        Color: 
            rgba: 86/255,72/255,139/255,0.5
        RoundedRectangle:
            size:(770,80)
            pos:(72,240)
            radius: [(30, 30), (30, 30), (30, 30), (30, 30)]
    MDLabel:
        text:'Add directories'
        font_style:'H2'
        pos:(45,200)
        theme_text_color: 'Custom'
        text_color:(255/255,255/255,255/255,1)
        font_size:50
    menuButton:

    RelativeLayout:
        Label:
            text: "Please enter a valid directory"
            font_size: 27
            font_name: 'Calibri Light'
            pos_hint:{'center_x':0.26,'center_y':0.67}
            theme_text_color: 'Custom'
            text_color : (1,1,1,1)
        Image:
            source: 'folderLinked.png'
            size_hint_y:None
            width:60
            height:60
            pos_hint:{'center_x':0.13,'center_y':0.535}          
        TextInput:
            id:newDirField
            multiline: False
            pos_hint:{'center_x':0.55,'center_y':0.54}
            size_hint_x: None
            size_hint_y: None
            width: 650
            height: 50
            font_size: '30sp'
            font_style: 'H2'
            font_color:(1,1,1,1)
            background_color:0,0,0,0
            cursor_color:(1,1,1,1)
            foreground_color:(1,1,1,1)
            on_text_validate:
                root.add()
        MDFillRoundFlatIconButton:
            icon:"android"
            theme_icon_color:"Primary"
            text:"Continue"
            font_size:"25sp"
            size:(80,40)
            pos_hint:{'center_x':0.83,'center_y':0.36}
            on_release:
                root.add()



<changeDestScreen>
    name: "changeDest"
    canvas.before:
        Rectangle:
            pos:self.pos
            size:self.size
            source: 'bg2.jpg'
        Color: 
            rgba: 86/255,72/255,139/255,0.5
        RoundedRectangle:
            size:(770,80)
            pos:(72,240)
            radius: [(30, 30), (30, 30), (30, 30), (30, 30)]
    MDLabel:
        text:'Change Destination'
        font_style:'H2'
        pos:(45,200)
        theme_text_color: 'Custom'
        text_color:(255/255,255/255,255/255,1)
        font_size:50
    menuButton:
    RelativeLayout:
        Label:
            text: "Current destination directory"
            font_size: 27
            font_name: 'Calibri Light'
            pos_hint:{'center_x':0.26,'center_y':0.67}
            theme_text_color: 'Custom'
            text_color : (1,1,1,1)
        Image:
            source: 'dest.png'
            size_hint_y:None
            width:60
            height:60
            pos_hint:{'center_x':0.125,'center_y':0.535}          
        MDFillRoundFlatIconButton:
            icon:"android"
            text:"Update"
            font_size:"25sp"
            size:(80,40)
            pos_hint:{'center_x':0.83,'center_y':0.36}
            on_release:
                root.updateDest()
           
<startMigrateScreen>
    name:"startMigrate"
    canvas.before:
        Rectangle:
            pos:self.pos
            size:self.size
            source: 'bg2.jpg'
        Color: 
            rgba: 86/255,72/255,139/255,0.5
        RoundedRectangle:
            size:(770,260)
            pos:(70,40)
            radius: [(30, 30), (30, 30), (30, 30), (30, 30)] 
    MDLabel:
        text:'Migration'
        font_style:'H2'
        pos:(45,200)
        theme_text_color: 'Custom'
        text_color:(255/255,255/255,255/255,1)
        font_size:50
    Label:
        text:root.percentage
        font_name:"Calibri Light"
        font_size:40
        pos_hint:{'center_x':0.5,'center_y':0.74}
    MDProgressBar: 
        max:100
        size_hint:None,None
        width:600
        height:8
        value:root.progBarValue
        pos_hint:{'center_x':0.5,'center_y':0.69}
        color:1,1,1,1
    RelativeLayout:
        Label:
            text: "Files List"
            font_size: 28
            font_name: 'Calibri Light'
            pos_hint:{'center_x':0.14,'center_y':0.62}
            theme_text_color: 'Custom'
            text_color : (1,1,1,1)
    menuButton:

<removeDirScreen>
    name:"removeDir"
    canvas.before:
        Rectangle:
            pos:self.pos
            size:self.size
            source: 'bg2.jpg'
        Color: 
            rgba: 86/255,72/255,139/255,0.5
        
    MDLabel:
        text:'Remove Directories'
        font_style:'H2'
        pos:(45,200)
        theme_text_color: 'Custom'
        text_color:(255/255,255/255,255/255,1)
        font_size:50
 
    menuButton:


"""
"""    Objects (e.g. MDCard,MDList, MDButton...) ONLY     """
class MD3Card(MDCard, RoundedRectangularElevationBehavior,RectangularRippleBehavior):
    funcText = StringProperty()
    imgsource = StringProperty()
    #Sends the id to screenmanager, to help it switch between function pages (e.g. id='allDirCard' -> change to All Directories screen.)
    cardId = StringProperty() 

    def on_release(self,*args):
        Clock.schedule_once(self.changeScr,0.1)
    def changeScr(self,*args):
        #Use App.get_running_app to access the ScreenManager globally 
        # (applies for all widgets created, given that ScreenManager is the primary object returned in the App Class.)
        destScreen = str(self.cardId).replace("Card","") #Deletes 'Card' in cardId to get the name of the next screen (e.g. allDirCard -> allDir (screenName))
        App.get_running_app().root.current = destScreen

    

class menuButton(MDIconButton):
    def on_release(self,*args):
        Clock.schedule_once(self.returnMainScreen,0.1)
    def returnMainScreen(self,*args):
        App.get_running_app().root.current = 'function'

class notification(Label):
    def __init__ (self,promptText,iconVar,iconPos,textPos,duration,**kwargs):
        super().__init__(**kwargs)
        self.ico = Image(source=iconVar,size_hint=(None,None),width=60,height=60,
                            pos=iconPos)
        self.notif = Label(text=promptText,font_size=32,
                            font_name="Quicksand",pos=textPos)
        self.add_widget(self.notif) #Adds self.notif on screen whenever "notification" class is summoned.
        self.add_widget(self.ico)
        Clock.schedule_once(self.removeNotif,duration)
    def removeNotif(self,*args):
        self.remove_widget(self.notif)   
        self.remove_widget(self.ico)    
'''class migrationListItems(ImageLeftWidget,OneLineAvatarListItem):
    def __init__ (self,fileName,displayList,**kwargs):
        super(migrationListItems,self).__init__(**kwargs)
        image = ImageLeftWidget(source='file-sharing.png',size=(150,150))
        self.slot = OneLineAvatarListItem(text="[size=27][font=C:\\Windows\\Fonts\\Calibril.ttf]"+fileName+"[/font][/size]")
        self.slot.add_widget(image)
        self.slot.divider = 'Inset'
        self.slot.divider_color = [0,0,0,0]
        self.slot.theme_text_color = 'Custom'
        self.slot.text_color = [1,1,1,1]
        self.slot.font_style = 'H5'
        displayList.add_widget(self.slot)'''
        


########################---Screens ONLY---#######################

class WelcomeScreen(Screen):
    def on_enter(self,*args):
        Clock.schedule_once(self.nextScreen,2)
    def nextScreen(self,*args):
        self.manager.current = 'function'

class FunctionScreen(Screen):
    pass


class allDirScreen(Screen):
    def on_enter(self,*args):
        dirs = configData["sourceDirList"]
        self.scrollAll = ScrollView(size_hint=(None,None),size=(760,330),
                                pos_hint = {'center_x':0.49,'center_y':0.44},
                                always_overscroll=False,
                                bar_inactive_color = (0,0,0,0),bar_color=(1,1,1,1),
                                bar_width=3,
                                do_scroll_x=False)
        displayList = MDList(size_hint=(None,None),width=850)
        
        for eachText in dirs:
            image = ImageLeftWidget(source='slash.png',size=(150,150))
            slot = OneLineAvatarListItem(text="[size=27][font=C:\\Windows\\Fonts\\Calibril.ttf]"+eachText+"[/font][/size]")
            slot.add_widget(image)
            slot.divider = 'Inset'
            slot.divider_color = [0,0,0,0]
            slot.theme_text_color = 'Custom'
            slot.text_color = [1,1,1,1]
            slot.font_style = 'H5'
            
            #slot.add_widget(eachDir)
            displayList.add_widget(slot)

        self.scrollAll.add_widget(displayList)
        self.add_widget(self.scrollAll)

    def on_pre_leave(self,*args):
        self.remove_widget(self.scrollAll) #Remove and re_add the directory list on_enter, as a form of refreshing the list (if updated with new Dir)

class addDirScreen(Screen):
    def __init__ (self,**kwargs):
        super (addDirScreen,self).__init__(**kwargs)
        self.dirs = configData["sourceDirList"]    

    def add(self,*args):
        newDir = str(App.get_running_app().root.get_screen('addDir').ids.newDirField.text)
        if (os.path.isdir(newDir) == 0):
            notif = notification("Invalid input. Please try again!",'x-button2.png',(75,75),(320,58),2)
            self.add_widget(notif)
            return 0
        else:
            newDirJson = newDir.replace(os.sep,'\\')
            for directory in self.dirs:
                if directory == newDirJson:
                    notif = notification("Duplicated Directory found! Please try again.",'x-button2.png',(75,85),(420,68),2)
                    self.add_widget(notif)
                    return 0

            self.dirs.append(newDirJson)
            with open(configLocation,"w") as configFile:
                json.dump(configData,configFile)
            notif = notification("Directory successfully added!",'check-mark.png',(75,85),(300,68),2)
            self.add_widget(notif)
               
    
class changeDestScreen(Screen):
    def on_enter(self,*args):
        self.dest = configData["destPath"]
        self.inputDest = TextInput(font_size=30,pos=(160,245),
                          size_hint=(None,None),width=650,height=50,font_style='H2',
                          multiline=False,background_color=(0/255,0/255,0/255,0),
                          cursor_color=(1,1,1,1),foreground_color=(1,1,1,1),
                          pos_hint={'center_x':0.55,'center_y':0.54},
                          halign='left',cursor_blink=True,text=self.dest,
                          on_text_validate=self.updateDest)
        self.inputDest.line_color_focus=(1,1,1,1)
        self.add_widget(self.inputDest)
    def updateDest(self,*args):
        if (os.path.isdir(str(self.inputDest.text)) == 0):
            notif = notification("Invalid input. Please try again!",'x-button2.png',(75,75),(320,58),2)
            self.add_widget(notif)
            return 0
        else:
            newDestJson = str(self.inputDest.text).replace(os.sep,'\\')
            if self.dest == newDestJson:
                notif = notification("Similar destination inputted! Please try again.",'x-button2.png',(75,85),(420,68),2)
                self.add_widget(notif)
                return 0
            
            configData["destPath"] = newDestJson #Updates the old destination directory in the JSON file.
            with open(configLocation,"w") as configFile:
                json.dump(configData,configFile)
            notif = notification("Destination successfully changed!",'check-mark.png',(75,85),(330,68),1.5)
            self.add_widget(notif)
            Clock.schedule_once(self.returnHomeScreen,1)
        return 0
    def on_pre_leave(self,*args):
        self.remove_widget(self.inputDest)
    def returnHomeScreen(self,*args):
        App.get_running_app().root.current = 'function'
    pass

class startMigrateScreen(Screen):
    progBarValue = NumericProperty()
    percentage = StringProperty()     
    currentFileName = StringProperty()
    counter = 1
        
    def on_enter(self,*args):
        self.exePath = ""
        self.docsPath = ""
        self.zipsPath = ""
        self.audioPath = ""
        self.imagePath = ""
        self.othersPath = ""

        self.dirs = configData["sourceDirList"]
        self.dirsIndex = 0
        self.dirsLength = len(self.dirs)
        self.numberOfFiles = 0
        self.counter = 0
        for directory in self.dirs:
            for file in os.listdir(directory):
                if os.path.isfile(os.path.join(directory,file)) == True:
                    self.numberOfFiles += 1
        
        print("Total number of files: " + str(self.numberOfFiles))
  
        self.fileTypes = configData["fileTypes"]
        self.exeFormats = self.fileTypes[0]
        self.docsFormats = self.fileTypes[1]
        self.audioFormats = self.fileTypes[2]
        self.zipsFormats = self.fileTypes[3]
        self.imageFormats = self.fileTypes[4]
     
        self.percentage = str(0) + "%"

        self.scroll = ScrollView(size_hint=(None,None),size=(740,230),
                        pos_hint = {'center_x':0.49,'center_y':0.33},
                        bar_inactive_color = (0,0,0,0),bar_color=(1,1,1,1),
                        bar_width=3,
                        do_scroll_x=False,
                        always_overscroll=False)
        self.displayList = MDList(size_hint=(None,None),width=700)
        self.scroll.add_widget(self.displayList)
        self.add_widget(self.scroll)

        
        self.num = 0
        if len(self.dirs) != 0:
            self.checkDestPathExist()
    def checkDestPathExist(self,*args):
        self.dest = configData["destPath"]
        if os.path.isdir(self.dest) == True:
            self.trigger = 1
        else:
            os.mkdir(self.dest)
        self.checkSubFolder()
    def checkSubFolder(self,*args):
        self.folders = ["\\Audio", "\\Zips", "\\Executables", "\\Documents", "\\Images","\\Others"]
        for folder in self.folders:
            folderPath = self.dest + folder
            if os.path.isdir(folderPath) == False:
                os.mkdir(folderPath)             
        self.createDestForFileTypes()

    def createDestForFileTypes(self,*args):
        for category in self.folders:
            if category == "\\Executables":
                self.exePath = self.dest + category
            elif category == "\\Audio":
                self.audioPath = self.dest + category
            elif category == "\\Zips":
                self.zipsPath = self.dest + category
            elif category == "\\Documents":
                self.docsPath = self.dest + category
            elif category == "\\Images":
                self.imagePath = self.dest + category
            elif category == "\\Others":
                self.othersPath = self.dest + category
        self.directorySeekerForImages()
        
        
    
    '''The real migration part'''
    #Part 1: Moves images.
    def directorySeekerForImages(self,*args):
        #for eachDir in self.dirs: #First loop to pick out each source directories.
        self.currentDir = self.dirs[self.dirsIndex]
        print("Current directory: " + str(self.currentDir))
        self.imgTailIndex = 0
        self.imgFilesPerTailIndex = 0
        self.imageFormatsLength = len(self.imageFormats)
        self.imageMigratorPerImgType()

    def imageMigratorPerImgType(self,*args): #Second recursion loop to pick each format in 1 file type (e.g. Images have jpeg, png...)
        os.chdir(self.currentDir)
        #print('Current source directory: ' + str(os.getcwd()))
        #print('Current img tail index: ' + str(self.imgTailIndex))
        print("Current self.imgTailIndex = " + str(self.imgTailIndex))
        self.imgTailType = str(self.imageFormats[self.imgTailIndex]) #List of image file types (e.g. jpeg, jpg...)
        print('Current file type:' + self.imgTailType)
    
        self.imgFilesPerTailList = glob.glob(self.imgTailType) #List of images with same file types (e.g. png-only images)
        self.imgFilesPerTailListLength = len(self.imgFilesPerTailList)
        self.imageMigratorReal()
   
    def imageMigratorReal(self,*args):
        print("Still in the loop!")
        #os.chdir(self.currentDir)
        print("List: " + str(self.imgFilesPerTailList))
        try:   
            eachFileName = self.imgFilesPerTailList[self.imgFilesPerTailIndex]
            print("Current file in list: " + str(eachFileName))
            shutil.move(str(eachFileName),self.imagePath)
            self.counter = self.counter + 1
            self.progBarValue = int((self.counter/self.numberOfFiles)*100)
            
            self.percentage = str(self.progBarValue) + "%"
            print("Number of files: " + str(self.numberOfFiles))
            image = ImageLeftWidget(source='file-sharing.png',size=(150,150))
        
            
            self.slot = OneLineAvatarListItem(text="[size=27][font=C:\\Windows\\Fonts\\Calibril.ttf]"+eachFileName+"[/font][/size]")
            self.slot.add_widget(image)
            self.slot.divider = 'Inset'
            self.slot.divider_color = [0,0,0,0]
            self.slot.theme_text_color = 'Custom'
            self.slot.text_color = [1,1,1,1]
            self.slot.font_style = 'H5'
            self.displayList.add_widget(self.slot)
            self.scroll.scroll_to(self.slot,animate=False)   
            
        except:
            print("Fuck it :)))")
        if self.imgFilesPerTailIndex < self.imgFilesPerTailListLength - 1:
            Clock.schedule_once(self.imageMigratorReal,0.1)
            self.imgFilesPerTailIndex = self.imgFilesPerTailIndex + 1
        else:
            Clock.unschedule(self.imageMigratorReal)
            self.imgFilesPerTailIndex = 0 #Resets image list's index, to prevent list out of range.
            if self.imgTailIndex < self.imageFormatsLength-1:
                self.imgTailIndex = self.imgTailIndex + 1 #Changes to next image tail (e.g. after png comes jpeg)
                self.imageMigratorPerImgType()
            else: #Changes to the next source directory in the source directory list.
                if self.dirsIndex < self.dirsLength - 1: 
                    self.dirsIndex = self.dirsIndex + 1
                    self.directorySeekerForImages()
                else:
                    #Stops all operations on image migrator
                    Clock.unschedule(self.imageMigratorReal)
                    Clock.unschedule(self.imageMigratorPerImgType)
                    Clock.unschedule(self.directorySeekerForImages)
                    #Resets directory indexes before moving on to the next functions
                    self.dirsIndex = 0
                    self.directorySeekerForAudio()


        
     
    
    #Part 2: Moves audio
    def directorySeekerForAudio(self,*args):
        print("\n\n\n\n\n\n\n\n\n\n")
        print("This is the territory of Audio!")
        self.currentDir = self.dirs[self.dirsIndex]
        self.audioTailIndex = 0
        self.audioFilesPerTailIndex = 0
        self.audioFormatsLength = len(self.audioFormats)
        self.audioMigratorPerAudioType()
    def audioMigratorPerAudioType(self,*args):
        os.chdir(self.currentDir)
        self.audioTailType = str(self.audioFormats[self.audioTailIndex])

        self.audioFilesPerTailList = glob.glob(self.audioTailType)
        self.audioFilesPerTailListLength = len(self.audioFilesPerTailList)
        self.audioMigratorReal()
    def audioMigratorReal(self,*args):
        try:
            eachFile = self.audioFilesPerTailList[self.audioFilesPerTailIndex]
            print("Current audio file being moved: " + str(eachFile))
            shutil.move(str(eachFile),self.audioPath)
            self.counter = self.counter + 1
            
            print("self.counter in Audio: " + str(self.counter))
            self.progBarValue = int((self.counter/self.numberOfFiles)*100)
            print("progBarValue in Audio: " + str(self.progBarValue))
            self.percentage = str(self.progBarValue) + "%"

            image = ImageLeftWidget(source='file-sharing.png',size=(150,150))
            self.slot = OneLineAvatarListItem(text="[size=27][font=C:\\Windows\\Fonts\\Calibril.ttf]"+eachFile+"[/font][/size]")
            self.slot.add_widget(image)
            self.slot.divider = 'Inset'
            self.slot.divider_color = [0,0,0,0]
            self.slot.theme_text_color = 'Custom'
            self.slot.text_color = [1,1,1,1]
            self.slot.font_style = 'H5'
            self.displayList.add_widget(self.slot) 
            self.scroll.scroll_to(self.slot,animate=False)      
            

        except:
            print("Lmao")
        if self.audioFilesPerTailIndex < self.audioFilesPerTailListLength - 1:
            self.audioFilesPerTailIndex += 1
            Clock.schedule_once(self.audioMigratorReal,0.1)
        else:
            Clock.unschedule(self.audioMigratorReal)
            self.audioFilesPerTailIndex = 0
            if self.audioTailIndex < self.audioFormatsLength - 1:
                self.audioTailIndex += 1
                self.audioMigratorPerAudioType()
            else:
                if self.dirsIndex < self.dirsLength - 1:
                    self.dirsIndex = self.dirsIndex + 1
                    self.directorySeekerForAudio()
                else:
                    #Stops all operations on audio migrator
                    Clock.unschedule(self.audioMigratorReal)
                    Clock.unschedule(self.audioMigratorPerAudioType)
                    Clock.unschedule(self.directorySeekerForAudio)
                    self.dirsIndex = 0
                    self.directorySeekerForExecutables()
    
    
    #Part 3: Moves executable files
    def directorySeekerForExecutables(self,*args):
        print("\n\n\n\n\n\n\n\n\n\n")
        print("This is the territory of Executables!")
        self.currentDir = self.dirs[self.dirsIndex]
        self.exeTailIndex = 0
        self.exeFilesPerTailIndex = 0
        self.exeFormatsLength = len(self.exeFormats)
        self.exeMigratorPerExeType()
    def exeMigratorPerExeType(self,*args):
        os.chdir(self.currentDir)
        self.exeTailType = str(self.exeFormats[self.exeTailIndex])

        self.exeFilesPerTailList = glob.glob(self.exeTailType)
        self.exeFilesPerTailListLength = len(self.exeFilesPerTailList)
        self.exeMigratorReal()
    def exeMigratorReal(self,*args):
        try:
            eachFile = self.exeFilesPerTailList[self.exeFilesPerTailIndex]
            print("Current exe file being moved: " + str(eachFile))
            shutil.move(str(eachFile),self.exePath)
            self.counter = self.counter + 1
            
            print("self.counter in Exe: " + str(self.counter))
            self.progBarValue = int((self.counter/self.numberOfFiles)*100)
            print("progBarValue in Exe: " + str(self.progBarValue))
            self.percentage = str(self.progBarValue) + "%"

            image = ImageLeftWidget(source='file-sharing.png',size=(150,150))
            self.slot = OneLineAvatarListItem(text="[size=27][font=C:\\Windows\\Fonts\\Calibril.ttf]"+eachFile+"[/font][/size]")
            self.slot.add_widget(image)
            self.slot.divider = 'Inset'
            self.slot.divider_color = [0,0,0,0]
            self.slot.theme_text_color = 'Custom'
            self.slot.text_color = [1,1,1,1]
            self.slot.font_style = 'H5'
            self.displayList.add_widget(self.slot)       
            self.scroll.scroll_to(self.slot,animate=False)    

        except:
            print("Lmao")

        if self.exeFilesPerTailIndex < self.exeFilesPerTailListLength - 1:
            self.exeFilesPerTailIndex += 1
            Clock.schedule_once(self.exeMigratorReal,0.1)
        else:
            Clock.unschedule(self.exeMigratorReal)
            self.exeFilesPerTailIndex = 0
            if self.exeTailIndex < self.exeFormatsLength - 1:
                self.exeTailIndex += 1
                self.exeMigratorPerExeType()
            else:
                if self.dirsIndex < self.dirsLength - 1:
                    self.dirsIndex = self.dirsIndex + 1
                    self.directorySeekerForExecutables()
                else:
                    #Stops all operations on executables migrator
                    Clock.unschedule(self.exeMigratorReal)
                    Clock.unschedule(self.exeMigratorPerExeType)
                    Clock.unschedule(self.directorySeekerForExecutables)
                    self.dirsIndex = 0
                    self.directorySeekerForZips()

    #Part 4: Moves zip files
    def directorySeekerForZips(self,*args):
        print("\n\n\n\n\n\n\n\n\n\n")
        print("This is the territory of Zips!")
        self.currentDir = self.dirs[self.dirsIndex]
        self.zipTailIndex = 0
        self.zipFilesPerTailIndex = 0
        self.zipFormatsLength = len(self.zipsFormats)
        self.zipMigratorPerZipType()
    def zipMigratorPerZipType(self,*args):
        os.chdir(self.currentDir)
        self.zipTailType = str(self.zipsFormats[self.zipTailIndex])

        self.zipFilesPerTailList = glob.glob(self.zipTailType)
        self.zipFilesPerTailListLength = len(self.zipFilesPerTailList)
        self.zipMigratorReal()
    def zipMigratorReal(self,*args):
        try:
            eachFile = self.zipFilesPerTailList[self.zipFilesPerTailIndex]
            print("Current zip file being moved: " + str(eachFile))
            shutil.move(str(eachFile),self.exePath)
            self.counter = self.counter + 1
            
            print("self.counter in Exe: " + str(self.counter))
            self.progBarValue = int((self.counter/self.numberOfFiles)*100)
            print("progBarValue in Exe: " + str(self.progBarValue))
            self.percentage = str(self.progBarValue) + "%"

            image = ImageLeftWidget(source='file-sharing.png',size=(150,150))
            self.slot = OneLineAvatarListItem(text="[size=27][font=C:\\Windows\\Fonts\\Calibril.ttf]"+eachFile+"[/font][/size]")
            self.slot.add_widget(image)
            self.slot.divider = 'Inset'
            self.slot.divider_color = [0,0,0,0]
            self.slot.theme_text_color = 'Custom'
            self.slot.text_color = [1,1,1,1]
            self.slot.font_style = 'H5'
            self.displayList.add_widget(self.slot)      
            self.scroll.scroll_to(self.slot,animate=False)    

        except:
            print("Lmao")

        if self.zipFilesPerTailIndex < self.zipFilesPerTailListLength - 1:
            self.zipFilesPerTailIndex += 1
            Clock.schedule_once(self.zipMigratorReal,0.1)
        else:
            Clock.unschedule(self.zipMigratorReal)
            self.zipFilesPerTailIndex = 0
            if self.zipTailIndex < self.zipFormatsLength - 1:
                self.zipTailIndex += 1
                self.zipMigratorPerZipType()
            else:
                if self.dirsIndex < self.dirsLength - 1:
                    self.dirsIndex = self.dirsIndex + 1
                    self.directorySeekerForZips()
                else:
                    #Stops all operations on zips migrator
                    Clock.unschedule(self.zipMigratorReal)
                    Clock.unschedule(self.zipMigratorPerZipType)
                    Clock.unschedule(self.directorySeekerForZips)
                    self.dirsIndex = 0
                    self.directorySeekerForDocs()

    #Part 5: Moves docs files
    def directorySeekerForDocs(self,*args):
        print("\n\n\n\n\n\n\n\n\n\n")
        print("This is the territory of Docs!")
        self.currentDir = self.dirs[self.dirsIndex]
        self.docTailIndex = 0
        self.docFilesPerTailIndex = 0
        self.docFormatsLength = len(self.docsFormats)
        self.docMigratorPerDocType()

    def docMigratorPerDocType(self,*args):
        os.chdir(self.currentDir)
        self.docTailType = str(self.docsFormats[self.docTailIndex])
        self.docFilesPerTailList = glob.glob(self.docTailType)
        self.docFilesPerTailListLength = len(self.docFilesPerTailList)
        self.docMigratorReal()

    def docMigratorReal(self,*args):
        try:
            eachFile = self.docFilesPerTailList[self.docFilesPerTailIndex]
            print("Current doc file being moved: " + str(eachFile))
            shutil.move(str(eachFile),self.docsPath)
            self.counter = self.counter + 1
            
            print("self.counter in Doc: " + str(self.counter))
            self.progBarValue = int((self.counter/self.numberOfFiles)*100)
            print("progBarValue in Doc: " + str(self.progBarValue))
            self.percentage = str(self.progBarValue) + "%"

            image = ImageLeftWidget(source='file-sharing.png',size=(150,150))
            self.slot = OneLineAvatarListItem(text="[size=27][font=C:\\Windows\\Fonts\\Calibril.ttf]"+eachFile+"[/font][/size]")
            self.slot.add_widget(image)
            self.slot.divider = 'Inset'
            self.slot.divider_color = [0,0,0,0]
            self.slot.theme_text_color = 'Custom'
            self.slot.text_color = [1,1,1,1]
            self.slot.font_style = 'H5'
            self.displayList.add_widget(self.slot)        
            self.scroll.scroll_to(self.slot,animate=False)   

        except:
            print("Lmao")

        if self.docFilesPerTailIndex < self.docFilesPerTailListLength - 1:
            self.docFilesPerTailIndex += 1
            Clock.schedule_once(self.docMigratorReal,0.1)
        else:
            Clock.unschedule(self.docMigratorReal)
            self.docFilesPerTailIndex = 0
            if self.docTailIndex < self.docFormatsLength - 1:
                self.docTailIndex += 1
                self.docMigratorPerDocType()
            else:
                if self.dirsIndex < self.dirsLength - 1:
                    self.dirsIndex = self.dirsIndex + 1
                    self.directorySeekerForDocs()
                else:            
                    #Stops all operations on docs migrator
                    Clock.unschedule(self.docMigratorReal)
                    Clock.unschedule(self.docMigratorPerDocType)
                    Clock.unschedule(self.directorySeekerForDocs)
                    self.dirsIndex = 0
                    self.directorySeekerForOthers()
    
    
    #Part 6: Moves other file types (not belonging to any file types)
    def directorySeekerForOthers(self,*args):
        print("\n\n\n\n\n\n\n\n\n\n")
        print("This is the territory of Others!")
        self.currentDir = self.dirs[self.dirsIndex]
        print("Current major dir: " + str(self.currentDir))
        self.otherFilesListIndex = 0
        self.otherFilesListLength = 0
        self.othersFilesList = []
        for file in os.listdir(self.currentDir):
            if os.path.isfile(os.path.join(self.currentDir,file)) == True:
                
                self.otherFilesListLength +=1
                self.othersFilesList.append(file)
                print(file)
            
        print(self.othersFilesList)
        self.otherMigratorReal()


    def otherMigratorReal(self,*args):
        try:
            eachFileOnScreen = self.othersFilesList[self.otherFilesListIndex]
            eachFile = os.path.join(self.currentDir,eachFileOnScreen)
            print("Current other file being moved: " + str(self.othersFilesList[self.otherFilesListIndex]))
            shutil.move(eachFile,self.othersPath)
            self.counter = self.counter + 1
            
            print("self.counter in Others: " + str(self.counter))
            self.progBarValue = int((self.counter/self.numberOfFiles)*100)
            print("progBarValue in Others: " + str(self.progBarValue))
            self.percentage = str(self.progBarValue) + "%"

            image = ImageLeftWidget(source='file-sharing.png',size=(150,150))
            self.slot = OneLineAvatarListItem(text="[size=27][font=C:\\Windows\\Fonts\\Calibril.ttf]"+eachFileOnScreen+"[/font][/size]")
            self.slot.add_widget(image)
            self.slot.divider = 'Inset'
            self.slot.divider_color = [0,0,0,0]
            self.slot.theme_text_color = 'Custom'
            self.slot.text_color = [1,1,1,1]
            self.slot.font_style = 'H5'
            self.displayList.add_widget(self.slot)        
            self.scroll.scroll_to(self.slot,animate=False)   

        except:
            print("Lmao")

        if self.otherFilesListIndex < self.otherFilesListLength - 1:
            self.otherFilesListIndex += 1
            Clock.schedule_once(self.otherMigratorReal,0.1)
        else:
            Clock.unschedule(self.otherMigratorReal)
            self.otherFilesListIndex = 0
            if self.dirsIndex < self.dirsLength - 1:
                self.dirsIndex = self.dirsIndex + 1
                self.directorySeekerForOthers()
            else:            
                #Stops all operations on other files migrator
                Clock.unschedule(self.directorySeekerForOthers)
                Clock.unschedule(self.otherMigratorReal)
                self.dirsIndex = 0

    def on_pre_leave(self,*args):
        self.remove_widget(self.scroll)
        self.progBarValue = 0
        self.percentage = "0%"



class removeDirScreen(Screen):
    addToDeleteTrigger = 0
    removeDirList = []
    countTest = 1
        
    def on_enter(self,*args):
        self.dirs = configData["sourceDirList"]
        self.origDirsListForDataTable = [] #Contains all directories before delete
        displayNum=1

        #Formats json data into table data (with displayNum = No. and self.dirs[eachDirIndex] = Directory.)
        for eachDirIndex in range(0,len(self.dirs)):
            dispNumOnTable = "[size=24]" + str(displayNum) + "[/size]"
            dirsOnTable = "[size=24]" + str(self.dirs[eachDirIndex]) + "[/size]"
            eachData = [dispNumOnTable,dirsOnTable]
            self.origDirsListForDataTable.append(eachData)
            displayNum +=1      
        
        print("Length of origDirsList: " + str(len(self.origDirsListForDataTable)))

    
        self.table = MDDataTable(pos_hint={'center_x':0.5,'center_y':0.5},
                            size_hint=(0.88,0.58),
                            rows_num=200,
                            check=True,

                            column_data=[
                                ("[size=24]No.[/size]",dp(30)),
                                ("[size=24]Directory[/size]",dp(120))
                            ],
                            row_data=self.origDirsListForDataTable,
                            opacity=1,                      
                            background_color_cell = get_color_from_hex("#FF0000"),     
                            elevation=20)
        
        self.add_widget(self.table)
        self.button = MDFillRoundFlatIconButton(text='Remove',
                                            size_hint=(None,None),size=(80,40),
                                            pos_hint={'center_x':0.85,'center_y':0.14},
                                            font_size=25)
        self.button.bind(on_release=self.deleteCheckedItems)
        self.add_widget(self.button)


    def deleteCheckedItems(self,*args):
        print("Current count test: " + str(self.countTest))

        allToBeDeleted = self.table.get_row_checks() #Gets the list of checked items on the table.
        print("Current items in self.dirs:" + str(self.dirs))
        print("Items in allToBeDeleted:" + str(allToBeDeleted))

        for directory in allToBeDeleted:
            realDirectory = directory[1]
            realDirectory1 = realDirectory.replace("[size=24]","")
            realDirectory2 = realDirectory1.replace("[/size]","")
            print(realDirectory2)
            if realDirectory2 in self.dirs:
                print("I will be removed!")
                self.dirs.remove(realDirectory2)
        print("After removal list: " + str(self.dirs))
        with open(configLocation,"w") as configFile:
            json.dump(configData,configFile)
        
        
        #Reupdates the table data after delete.
        self.newDirsListForDataTable = [] #Contains all remaining directories after delete.
        displayNum = 1
        #Formats json data into table data (with displayNum = No. and self.dirs[eachDirIndex] = Directory.)
        for eachDirIndex in range(0,len(self.dirs)):
            dispNumOnTable = "[size=24]" + str(displayNum) + "[/size]"
            dirsOnTable = "[size=24]" + str(self.dirs[eachDirIndex]) + "[/size]"
            eachData = [dispNumOnTable,dirsOnTable]
            self.newDirsListForDataTable.append(eachData)
            displayNum +=1
        print("Post-processed list: " + str(self.newDirsListForDataTable))
        
        self.table.update_row_data(self.origDirsListForDataTable,self.newDirsListForDataTable)
        print(self.table.rows_num)
        self.origDirsListForDataTable = self.newDirsListForDataTable #Makes sure that the original list is up to date after delete.
        print("\n")
        self.countTest +=1 
        #App.get_running_app().root.current = 'function'

    def on_leave(self,*args):
        self.remove_widget(self.table) #Remove and re_add the directory list on_enter, as a form of refreshing the list (if updated with new Dir)
        self.remove_widget(self.button) #Prevents multiple clicks after exiting and reentering the removal screen.
        self.table.check = False
class migrator(MDApp):
    sm = ScreenManager()
    def build (self):
        screens = Builder.load_string(screenProperties)
        self.welcome = WelcomeScreen()
        self.sm.add_widget(self.welcome)

        self.func = FunctionScreen()
        self.sm.add_widget(self.func)

        self.allDir = allDirScreen()
        self.sm.add_widget(self.allDir)

        self.addDir = addDirScreen()
        self.sm.add_widget(self.addDir)

        self.changeDir = changeDestScreen()
        self.sm.add_widget(self.changeDir)
    
        self.startMig = startMigrateScreen()
        self.sm.add_widget(self.startMig)
        return screens


migrator().run()

