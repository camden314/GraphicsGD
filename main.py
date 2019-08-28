#!/usr/bin/python
string = """<?xml version='1.0' encoding='utf-8'?>
<interface>
  <object class="tk.Toplevel" id="mainwindow">
    <child>
      <object class="ttk.Labelframe" id="TopFrame">
        <property name="height">200</property>
        <property name="relief">sunken</property>
        <property name="takefocus">false</property>
        <property name="text" translatable="yes">GraphicsGD</property>
        <property name="width">200</property>
        <layout>
          <property name="column">0</property>
          <property name="propagate">True</property>
          <property name="row">0</property>
        </layout>
        <child>
          <object class="ttk.Label" id="SizeLabel">
            <property name="text" translatable="yes">Size: </property>
            <layout>
              <property name="column">0</property>
              <property name="propagate">True</property>
              <property name="row">0</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Scale" id="SizeScale">
            <property name="command">test</property>
            <property name="from_">0</property>
            <property name="length">170</property>
            <property name="orient">horizontal</property>
            <property name="to">1</property>
            <property name="value">1</property>
            <property name="variable">int:num</property>
            <layout>
              <property name="column">1</property>
              <property name="propagate">True</property>
              <property name="row">0</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Label" id="LevelNameLavel">
            <property name="text" translatable="yes">Level Name: </property>
            <layout>
              <property name="column">0</property>
              <property name="propagate">True</property>
              <property name="row">1</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Entry" id="LevelNameInput">
            <property name="font">{Didot} 15 {bold}</property>
            <layout>
              <property name="column">1</property>
              <property name="propagate">True</property>
              <property name="row">1</property>
              <property name="sticky">n</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Label" id="UsernameLabel">
            <property name="text" translatable="yes">Username: </property>
            <layout>
              <property name="column">0</property>
              <property name="propagate">True</property>
              <property name="row">2</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Entry" id="UsernameInput">
            <property name="font">{Didot} 15 {bold}</property>
            <layout>
              <property name="column">1</property>
              <property name="propagate">True</property>
              <property name="row">2</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Label" id="PasswordLabel">
            <property name="text" translatable="yes">Password:</property>
            <layout>
              <property name="column">0</property>
              <property name="propagate">True</property>
              <property name="row">3</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Entry" id="PasswordInput">
            <property name="font">{Didot} 15 {bold}</property>
            <property name="show">•</property>
            <layout>
              <property name="column">1</property>
              <property name="propagate">True</property>
              <property name="row">3</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Button" id="SubmitButton">
            <property name="command">dostuff</property>
            <property name="text" translatable="yes">Create Level</property>
            <layout>
              <property name="column">0</property>
              <property name="columnspan">1</property>
              <property name="padx">10</property>
              <property name="propagate">True</property>
              <property name="row">6</property>
              <property name="sticky">w</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Label" id="LevelIDLabel">
            <property name="text" translatable="yes">LevelID:</property>
            <layout>
              <property name="column">1</property>
              <property name="padx">0</property>
              <property name="propagate">True</property>
              <property name="row">6</property>
              <property name="sticky">w</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Entry" id="LevelID">
            <property name="justify">center</property>
            <property name="width">18</property>
            <layout>
              <property name="column">1</property>
              <property name="padx">70</property>
              <property name="propagate">True</property>
              <property name="row">6</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Label" id="Credits">
            <property name="font">{Trebuchet MS} 10 {}</property>
            <property name="text" translatable="yes">GUI Layout inspired by: Glitchy4</property>
            <layout>
              <property name="column">2</property>
              <property name="propagate">True</property>
              <property name="row">10</property>
              <property name="sticky">w</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Label" id="ScaleValue">
            <property name="text" translatable="yes">1.0
</property>
            <layout>
              <property name="column">1</property>
              <property name="propagate">True</property>
              <property name="row">0</property>
              <property name="rowspan">2</property>
              <property name="sticky">ne</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Button" id="SvgPathChoose">
            <property name="command">choosesvg</property>
            <property name="text" translatable="yes">Choose Svg</property>
            <layout>
              <property name="column">0</property>
              <property name="columnspan">4</property>
              <property name="padx">10</property>
              <property name="pady">15</property>
              <property name="propagate">True</property>
              <property name="row">4</property>
              <property name="sticky">w</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Label" id="PathLabel">
            <property name="text" translatable="yes">Path: </property>
            <layout>
              <property name="column">1</property>
              <property name="padx">16</property>
              <property name="propagate">True</property>
              <property name="row">4</property>
              <property name="sticky">w</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Entry" id="PathInput">
            <property name="justify">center</property>
            <property name="width">10</property>
            <layout>
              <property name="column">1</property>
              <property name="columnspan">2</property>
              <property name="ipadx">35.5</property>
              <property name="padx">70</property>
              <property name="propagate">True</property>
              <property name="row">4</property>
              <property name="sticky">w</property>
            </layout>
          </object>
        </child>
      </object>
    </child>
  </object>
</interface>
"""
# File: toplevelminimal.py
import os
try:
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import filedialog
except:
    import Tkinter as tk
    import tkMessageBox as messagebox
    from tkFileDialog import filedialog
import pygubu
import graphicsgd

class GraphicsGDRoot(pygubu.TkApplication):
    def _create_ui(self):
        self.builder = builder = pygubu.Builder()
        self.filename = ''
        #2: Load an ui file
        builder.add_from_string(string)
        self.mainwindow = builder.get_object('TopFrame', self.master)
        self.builder.connect_callbacks(self)
    def dostuff(self):
        scale = 1.0/self.builder.get_object('SizeScale').get()
        username = self.builder.get_object('UsernameInput').get()
        password = self.builder.get_object('PasswordInput').get()
        lname = self.builder.get_object('LevelNameInput').get()
        path = self.filename
        id = None
        try:
            id = graphicsgd.uploadSvg(path,scale,lname,username,password)
        except:
            messagebox.showerror('GraphicsGD Error','An error occured')
        else:
            t = self.builder.get_object('LevelID')
            t.delete(0,'end')
            t.insert(0,str(id))
            print(str(id))
    def test(self,v):
        self.builder.get_object('ScaleValue').configure(text = str(round(float(v),2)).ljust(4,'0'))
    def choosesvg(self):
        filename = filedialog.askopenfilename(filetypes = (("Graphics files", "*.svg"),("All files", "*.*") ))
        if filename: 
            self.filename = filename
            print('yee')
            path = self.builder.get_object('PathInput')
            path.delete(0,'end')
            path.insert(0,filename)
if __name__ == '__main__':
    root = tk.Tk()
    app = GraphicsGDRoot(root)
    app.run()