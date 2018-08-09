import Tkinter as tk
import ttk
import threading

def je_anagram(alfa,beta):
	return sorted(alfa.lower()) == sorted(beta.lower())
	
def je_ok(alfa,beta):
	if len(beta) != len(alfa)+1:
		return False
	if len(set(beta)-set(alfa)) == 1:
		if je_anagram(alfa, "".join(letter for letter in beta if letter in alfa)):
			return True
	return False

def najdi_plus1(trenutno, seznam, lines):
	if trenutno in seznam:
		return {}
	for word in lines:
		if je_ok(trenutno, word):
			if trenutno not in seznam:
				seznam[trenutno] = []
			seznam[trenutno].append(word)
	else:
		if trenutno not in seznam:
			seznam[trenutno] = [""]
	return seznam

class App(tk.Frame):
	def __init__(self, *args,**kwargs):
		tk.Frame.__init__(self, *args,**kwargs)
		self.word = ""
		self.lines = open('besede.txt').read().splitlines()
		self.nodes = dict()
		self.thread_stop = False
		#frame = tk.Frame(master)

		self.tree_frame = tk.Frame(self)
		self.btn_frame = tk.Frame(self)

		self.edit = tk.Entry(self.btn_frame)
		self.button_lazy = tk.Button(self.btn_frame, text="Nalozi", command=self.btn_load_lazy, padx=5)
		self.button_stop = tk.Button(self.btn_frame, text="Stop", command=self.btn_stop, padx=5)
		self.button_all = tk.Button(self.btn_frame, text="Nalozi vse", command=self.btn_load_all, padx=5)

		self.tree = ttk.Treeview(self.tree_frame)
		ysb = ttk.Scrollbar(self.tree_frame, orient='vertical', command=self.tree.yview)
		self.tree.configure(yscroll=ysb.set)
		self.tree.heading('#0', text='Anagram+1')
		self.tree.pack(side=tk.LEFT,fill=tk.BOTH,expand=tk.YES)
		ysb.pack(side=tk.RIGHT,fill=tk.Y)

		self.lbl_frame = tk.Frame(self)
		self.lbl_status = tk.Label(self.lbl_frame, text="...")
		self.lbl_status.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)

		self.edit.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)
		self.button_stop.pack(side=tk.RIGHT)
		self.button_all.pack(side=tk.RIGHT)
		self.button_lazy.pack(side=tk.RIGHT)
		
		
		self.btn_frame.grid(row=0,column=0,sticky=tk.W+tk.N)
		self.tree_frame.grid(row=1,column=0,sticky=tk.W+tk.S+tk.E+tk.N)
		self.lbl_frame.grid(row=2,column=0, sticky=tk.W+tk.E)

		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=1)

		self.tree.bind('<<TreeviewOpen>>', self.open_node)
		self.tree.bind('<<TreeviewSelect>>', self.select_node)

	def select_node(self,event):
		node = self.tree.focus()
		text = ""
		temp_node = node
		while self.tree.parent(temp_node) != '':
			text= text+ " "+self.tree.item(temp_node,option="text")
			temp_node=self.tree.parent(temp_node)
		text = text + " " + self.word
		self.lbl_status.config(text=text)

	def btn_load_lazy(self,*args):
		self.word = self.edit.get()
		self.tree.delete(*self.tree.get_children())
		self.nodes={}
		if self.word:
			self.insert_node('', self.word, self.word)
			self.lbl_status.config(text="Beseda pripravljena!")
			for node in self.nodes:
				if self.nodes[node] == self.word:
					self.expand(node)
					if self.tree.item(node,'open') == 0:
							self.tree.item(node,open=True)
					break

	def btn_load_all(self,*args):
		self.btn_load_lazy()
		self.thread = threading.Thread(target=self.load_all)
		self.thread_stop = False
		self.thread.start()
		self.lbl_status.config(text="Nalaganje....")

	def btn_stop(self,*args):
		self.thread_stop = True
		self.thread.join()
		self.lbl_status.config(text="Avtomatsko nalaganje prekinjeno!")

	def load_all(self):
		while True:
			temp = {}
			temp.update(self.nodes)
			for node in temp:
				if self.thread_stop:
					return
				self.expand(node)
				if self.tree.item(node,'open') == 0:
					self.tree.item(node,open=True)
			if len(temp) == len(self.nodes):
				break

	def insert_node(self, parent, text, abspath):
		node = self.tree.insert(parent, 'end', text=text, open=False)
		self.nodes[node] = abspath
		self.tree.insert(node, 'end')

	def open_node(self, event):
		node = self.tree.focus()
		self.expand(node)

	def expand(self, node):
		abspath = self.nodes.pop(node, None)
		if abspath:
			self.tree.delete(self.tree.get_children(node))
			seznam = {}
			najdi_plus1(abspath, seznam, self.lines)
			for p in seznam[abspath]:
				if p != "":
					self.insert_node(node, p, p)


if __name__ == '__main__':
	root = tk.Tk()
	app = App(root)
	app.pack(side="top", fill="both", expand=True)
	root.wm_geometry("500x500")
	root.winfo_toplevel().title("Anagram+1")
	root.mainloop() 
