import tkinter as tk
import sys

#the prupose of this mini project was to learn and demonstrate usage of a GUI in python (tkinter)

class RPN_Calculator(): #a simple calculator using reverse polish notation. 
	args = []

	def clr(self):
		self.args = []

	def add(self, arg1, arg2):
		return arg1 + arg2

	def sub(self, arg1, arg2):
		return arg1 - arg2

	def mult(self, arg1, arg2):
		return arg1 * arg2

	def div(self, arg1, arg2):
		return arg1 / arg2

	def parse(self, args):
		try:
			op = args[-1]

			if len(args) <= 3:
				if op == "+":
					ans = self.add(int(args[0]), int(args[1]))
					return ans
					self.clr()
				elif op == "-":
					ans = self.sub(int(args[0]), int(args[1]))
					return ans
					self.clr()
				elif op == "*":
					ans = self.mult(int(args[0]), int(args[1]))
					return ans
					self.clr()
				elif op == "/":
					ans = self.div(int(args[0]), int(args[1]))
					return ans
					self.clr()
				else:
					return str("I'm sparticus")

			else:
				return str("only 3 args pls")

		except:
			with Exception as e:
				print(e)


class Interface(tk.Frame):	#this the basic graphic user interface built using tk
	calc = RPN_Calculator()

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.var = tk.StringVar()
		self.var.set("hej")
		self.display()
		self.buttons()

	def display(self):
		self.lbl = tk.Label(textvariable = self.var)
		self.lbl.pack(side = "top")

	def click(self, arg):
		operators = ['+', '-', '*', '/']
		operands = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
		if arg in operands or arg in operators:
			self.calc.args.append(arg)
			self.var.set(arg)

		elif arg == '=':
			ans = self.calc.parse(self.calc.args)
			self.var.set(ans)

		elif arg == 'C':
			self.calc.args = []

	def buttons(self):
		self.one = tk.Button(self, text = "1", command = lambda: self.click(1))
		self.one.grid(column = 1, row = 1)

		self.two = tk.Button(self, text = "2", command = lambda: self.click(2))
		self.two.grid(column = 2, row = 1)

		self.three = tk.Button(self, text = "3", command = lambda: self.click(3))
		self.three.grid(column = 3, row = 1)

		self.four = tk.Button(self, text = "4", command = lambda: self.click(4))
		self.four.grid(column = 1, row = 2)

		self.five = tk.Button(self, text = "5", command = lambda: self.click(5))
		self.five.grid(column = 2, row = 2)

		self.six = tk.Button(self, text = "6", command = lambda: self.click(6))
		self.six.grid(column = 3, row = 2)

		self.seven = tk.Button(self, text = "7", command = lambda: self.click(7))
		self.seven.grid(column = 1, row = 3)

		self.eight = tk.Button(self, text = "8", command = lambda: self.click(8))
		self.eight.grid(column = 2, row = 3)

		self.nine = tk.Button(self, text = "9", command = lambda: self.click(9))
		self.nine.grid(column = 3, row = 3)

		self.zero = tk.Button(self, text = "0", command = lambda: self.click(0))
		self.zero.grid(column = 2, row = 4)

		self.plus = tk.Button(self, text = "+", command = lambda: self.click('+'))
		self.plus.grid(column = 4, row = 1)

		self.minus = tk.Button(self, text = "-", command = lambda: self.click('-'))
		self.minus.grid(column = 4, row = 2)

		self.mult = tk.Button(self, text = "*", command = lambda: self.click('*'))
		self.mult.grid(column = 4, row = 3)

		self.div = tk.Button(self, text = "/", command = lambda: self.click('/'))
		self.div.grid(column = 4, row = 4)

		self.equals = tk.Button(self, text = "=", command = lambda: self.click('='))
		self.equals.grid(column = 4, row = 5)

		self.clear = tk.Button(self, text = "C", command = lambda: self.click('C'))
		self.clear.grid(column = 3, row = 4)

		self.quit = tk.Button(self, text ="QUIT", fg="red", command = self.master.destroy)
		self.quit.grid(column = 4, row = 6)

root = tk.Tk()
app = Interface(master=root)
app.mainloop()