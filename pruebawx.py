import wx

app = wx.App(clearSigInt=True)
frame = wx.Frame(parent=None, title="Programación Avanzada")
panel = wx.Panel(parent=frame)
text = wx.StaticText(parent=panel, label="Hello, from wxPython!!", pos = (40,40))
frame.Show()
app.MainLoop()