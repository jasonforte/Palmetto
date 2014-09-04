'''
Created on 04 Sep 2014

SimpleApp for the Palmetto Project

This file is aimed at setting up GUI components to help debug the operation of the Palmetto
Vein Scanner

@version: 1.0
@author: Jason Forte <design@dustio.com>
'''


''' Test the availability of the wxPython module'''
try:
    import wx
except ImportError as err:
    print("The wxPython module is required to run this program", err)

''' Create a simple wx app with one frame '''
class SimpleApp(wx.Frame):
    def __init__(self, parent, id, title):
        # Call to parent class
        wx.Frame.__init__(self, parent, id, title)
        
        # useful to store the parent
        self.parent = parent
        
        # separate the logic and the GUI construction
        self.initialise()
    
    def initialise(self):
        self.Show(True)



''' Intiate the class in main'''
if __name__ == '__main__':
    # it's important to instanciate the App class
    app = wx.App()
    
    # frame is an instance of the frame with
    # no parent (because it is the highest element)
    # -1 = wx will chose own identifier
    # title - window title
    frame = SimpleApp(None, -1, "First App")
    
    # initiate main loop
    app.MainLoop()