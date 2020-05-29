import tkinter as tk# 导入 Tkinter 库
import time
import asyncio
import threading
import tkinter.messagebox
 
class Form:
  def __init__(self):
    self.root=tk.Tk()
    self.root.geometry('500x300')
    self.root.title('窗体程序') #设置窗口标题
 
    self.button=tk.Button(self.root,text="开始计算",command=self.change_form_state)
    self.label=tk.Label(master=self.root,text="等待计算结果")
 
    self.button.pack()
    self.label.pack()
 
    self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    self.root.mainloop()
  def on_closing(self):
    # self.new_loop.close()
    # self.t.destroy()
    self.root.destroy()
    asyncio
  async def calculate(self):
    ll=[1,2,3,4,5]
    for i in ll:
      self.label["text"]=i
      await asyncio.sleep(3)
    await asyncio.sleep(3)
    self.label["text"]=300
    return self
 
  def get_loop(self,loop):
    self.loop=loop
    asyncio.set_event_loop(self.loop)
    self.loop.run_forever()
  def change_form_state(self):
    coroutine1 = self.calculate()
    self.new_loop = asyncio.new_event_loop()            #在当前线程下创建时间循环，（未启用），在start_loop里面启动它
    self.t = threading.Thread(target=self.get_loop,args=(self.new_loop,))  #通过当前线程开启新的线程去启动事件循环
    self.t.start()
 
    asyncio.run_coroutine_threadsafe(coroutine1,self.new_loop) #这几个是关键，代表在新线程中事件循环不断“游走”执行
 
 
if __name__=='__main__':
  form=Form()