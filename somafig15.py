from Tkinter import *
from Tkconstants import *
import  os, tkFileDialog, tkMessageBox
import Image
import ImageTk
import StringIO
import base64
import subprocess
from shutil import rmtree


cube2str = \
"""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
p+r+Gx11qLGF/0j2AAAAAElFTkSuQmCC
"""

cube2 = Image.open(StringIO.StringIO(base64.b64decode(cube2str)))

class Svgfig:
    def __init__(self,name="somafig",rows=6,cols=2,lays=3):
        self.name =  name
        self.svgname = name + ".svg"
        self.items = []
        self.rows = rows
        self.cols = cols
        self.lays = lays
        self.curid = 1200
        self.width = ((rows + cols + 2.5) * 20)
        self.height = ((rows + cols + 2.5) * 25)
        return

    def add(self,item):
            self.items.append(item)

    def strarray(self):
        tmp = ["""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <!-- Created with SOMA Cube Figure Maker -->
    <svg
       xmlns:svg="http://www.w3.org/2000/svg"
       xmlns="http://www.w3.org/2000/svg"
       version="1.0"
       width=\"""" +  str(self.width) + """"
       height=\"""" + str(self.height) + """"
       id="svg1961">
      <defs id="defs2776" />
      <g transform="translate(""" + str(self.rows * 15) + """,-60)">
         """]
        for item in self.items: tmp += item.strarray()
        tmp += [" \n</g>\n</svg>\n"]
        return tmp

    def write_svg(self,filename=None):
        if filename:
            self.svgname = filename
        else:
            self.svgname = self.name 
        file = open(self.svgname,'w')
        file.writelines(self.strarray())
        file.close()
        return


class Cube:
    def __init__(self,row=1,col=1,lay=1):
        self.row = row
        self.col = col
        self.lay = lay
        self.id = 0
        return

    def strarray(self):
        dx = self.col * 20 - ((self.row - 1) * 20)
        dy = (self.row * 20) + (self.col * 14) + (self.lay * 20) - ((self.row - 1) * 6)
        tmp = '<g transform="translate(' + str(dx) + ',' + str(dy+50) + ')" '
        tmp += """
    id="g2286">
    <rect
       width="24.385448"
       height="19.975428"
       x="0.03503795"
       y="13.865141"
       transform="matrix(0.8191531,0.5735749,0,1,0,0)"
       style="fill:#b3b3b3;fill-opacity:1;stroke:#000000;stroke-width:0.227295;stroke-opacity:1"
       id="rect1975" />
    <rect
       width="24.385448"
       height="19.975428"
       x="24.560686"
       y="42.074257"
       transform="matrix(0.8191531,-0.5735749,0,1,0,0)"
       style="fill:#4d4d4d;fill-opacity:1;stroke:#000000;stroke-width:0.227295;stroke-opacity:1"
       id="rect1977" />
    <rect
       width="24.18391"
       height="24.18391"
       x="-36.625439"
       y="-12.00878"
       transform="matrix(-0.8200648,-0.5722706,0.8200648,-0.5722706,0,0)"
       style="fill:#e6e6e6;fill-opacity:1;stroke:#000000;stroke-width:0.22404556;stroke-opacity:1"
       id="rect1979" />
  </g>"""
        return tmp




class Figure:
    "A SomaCube Figure"
    def __init__(self, rows=0, cols=0, lays=0, title="empty"):
            self.rows = rows
            self.cols = cols
            self.lays = lays
            self.title = title
            self.fmap = {}
            self.img = ''
            self.cubes = 0
            

    def load(self,figfile):

        solfile = open ( figfile, 'r' )
        self.fmap.clear()
        self.cubes = 0
        rows = 0
        lays = -1
        cols = 0
        layernum = []
        infile =  solfile.readlines()
        rows = len(infile) -1
        title = infile[0].strip('.,;:|/\ ').strip('\n')
        for r in range(0,rows):
                tmpline = infile[r+1].strip().replace('.','-').replace('/','|')
                if tmpline[0] == '|':
                    tmpline = tmpline[1:]
                if tmpline[-1] == '|':
                    tmpline = tmpline[:-1]
                tmprows = tmpline.split('|')
                for l in range(0,len(tmprows)):
                    for c in range(0,len(tmprows[l])):
                        if tmprows[l][c] != '-':
                            self.fmap[(r,l,c)] = '0'
                            self.cubes += 1
                        else:
                            self.fmap[(r,l,c)] = '-'

        lays = len(tmprows)
        cols = len(tmprows[0])

        solfile.close()
        self.rows = rows 
        self.cols = cols
        self.lays = lays 
        self.title = title
        self.makeimg()


    def newfig(self):
        self.rows = 3 
        self.cols = 3
        self.lays = 3
        self.title = "cube"
        self.fmap.clear()
        self.cubes = 27

        for r in range(0,3):
          for c in range(0,3):
              for l in range(0,3):
                  self.fmap[(r,l,c)] = '0'
        self.makeimg()

        
    def makeimg(self):

        mimg = Image.new("RGBA", (300, 300), "#D4D8E7")
        ly = 20
        dx = 20
        dy = 15
        pd = 14
        sh = 10
        dh = 7

        
        r,g,b,ach = cube2.convert("RGBA").split()

        if self.cols > self.rows:
            spy = pd + (self.rows * dh) + ((self.cols - self.rows -1)*dh) + (self.lays * sh)
        else:
            spy = pd + (self.cols * dh) + ((self.rows - self.cols -1)*dh) + (self.lays * sh)
        spx = pd + (self.rows * dx) 

        for row in range(0,self.rows):
            for lay in range(0,self.lays):
                for col in range(0,self.cols):
                    nx = (col * dx) - (row * dx)
                    ny = (col * dy) + (row * dy) - ((lay) * ly)
                    if self.fmap[(row,lay,col)] != "-":
                        mimg.paste(cube2,(nx+spx,ny+spy),ach)

        self.img = mimg
        

    def write_fig(self,type='f',fname=None):
        if type == 'f':
            ch = '|'
            ext = '.fig'
        else:
            ch = '/'
            ext = '.bcs'
            
        if not fname:
            fname = self.title.strip('\n')
        tmpfig = fname + '\n'
        for r in range(0,self.rows):
            tmpfig += ch
            for l in range(0,self.lays):
                for c in range(0,self.cols):
                    tmpfig += self.fmap[(r,l,c)]
                tmpfig += ch
            tmpfig += '\n'
        file = open(fname + ext,'w')
        file.writelines(tmpfig)
        file.close()


def window(tk):
    #global cube 

    myContainer1 = Frame(tk) 
    myContainer1.pack()

    nclr = "#D4D0C8"
    bclr = "#7BA8C3"
    dict = {}
    layers = {}
    cubs = IntVar()
    fnametx = StringVar()

    winfig = Figure()

    top_frame = Frame(myContainer1) 
    top_frame.pack(side=TOP,
        fill=BOTH, 
        expand=YES,
        )  

    menu_frame = Frame(top_frame, background="#D4D0C8",
        borderwidth=5,  relief=GROOVE,
        height=50, 
        width=450, 
        )

    left_frame = Frame(top_frame, background="#F9F5D0",
        borderwidth=5,  relief=RIDGE,
        height=300, 
        width=150, 
        )

    menu_frame.pack(
        fill=BOTH
        )

    left_frame.pack(side=LEFT,
        fill=BOTH, 
        expand=YES,
        )

    right_frame = Frame(top_frame, background="#7BA8C3",
        borderwidth=5,  relief=RIDGE,
        width=300,
        )
    right_frame.pack(side=RIGHT,
        fill=BOTH, 
        expand=YES,
        ) 

    bot_frame = Frame(myContainer1, background="#D4D0C8",
        borderwidth=5,  relief=RIDGE,
        height=150
        )
    bot_frame.pack(
        fill=BOTH
        ) 

    canvas=Canvas(right_frame,bg ='#D4D8E7', width=310,height=310)
    canvas.pack()


    def winshowcube():
        winfig.makeimg()
        tmpimg = ImageTk.PhotoImage(winfig.img)
        canvas.image = tmpimg
        canvas.create_image(int(tmpimg.width()/2),int(tmpimg.height()/2),image=tmpimg)
        

    def flip(rc):
        if winfig.fmap[rc] == '-':
            winfig.fmap[rc] = '0'
            dict[rc].configure(bg=bclr)
            winfig.cubes += 1
        else:
            winfig.fmap[rc] = '-'
            dict[rc].configure(bg=nclr)
            winfig.cubes += -1
        rt = ''
        cubs.set(winfig.cubes)
        winshowcube()
        
    def winmakegrid():
        for key,but in dict.items():
            but.destroy()

        dict.clear()
        
        col = 0
        row = 1

        layers.clear()

        for l in range(0,winfig.lays):
            layers[l] = Frame(bot_frame, padx=7, pady=6)
            layers[l].grid(row = 1, column = l)
            for r in range(0,winfig.rows):
                for c in range(0,winfig.cols):
                    action = lambda x =(r,l,c): flip(x)
                    if winfig.fmap[(r,l,c)] != "-":
                        dict[(r,l,c)] = Button(layers[l], text=' ', padx=6, bg=bclr, command=action) 
                        winfig.fmap[(r,l,c)] = '0'
                    else:
                        dict[(r,l,c)] = Button(layers[l], text=' ', padx=6, bg=nclr, command=action) 
                    dict[(r,l,c)].grid(row = row, column = c + l + (l * winfig.cols) )
                    col += 1
                row += 1
                col = 0
            row = 1
        

    def winloadfig(fname):

        nclr = "#D4D0C8"
        bclr = "#7BA8C3"

        if fname:
            winfig.load(fname)
        else:
            winfig.newfig()

        cubs.set(winfig.cubes)
        winshowcube()
        winmakegrid()

    winloadfig(None)
    
    rows = winfig.rows
    cols = winfig.cols
    lays = winfig.lays


    def loadfig():
        n = tkFileDialog.askopenfilename(master=root,
                       title='Select Figure to Load',
                       filetypes=[('SomaCube Figures','*.fig'),
                                  ('All Files','*.*')])  #a courtesy to users
        if n:
            folder, file = os.path.split(n)
            winloadfig(folder+'/'+file)
            fnametx.set(file.split(".")[0])
            return file,folder
        else:
            return None, ''
        rowsc.set(winfig.rows)
        colsc.set(winfig.cols)
        laysc.set(winfig.lays)
        

    def quitbutton():
        if tkMessageBox.askyesno("Quit", "Do you really wish to quit?"):
            root.destroy()

    def savefig():
        n = fnametx.get()
        print "writing fig: ", n
        winfig.write_fig(type='f',fname=n)
        savebcs()
        savepng()
        savesvg()
        savesol()

    def savebcs():
        n = fnametx.get()
        print "writing BCS: ", n
        winfig.write_fig(type='b',fname=n)

    def savepng():
        n = fnametx.get()
        print "writing PNG: ", n
        winfig.img.save(n + ".png")

    def savesvg():
        n = fnametx.get()
        print "writing SVG: ", n
        fig = Svgfig(n.strip(),winfig.rows,winfig.cols,winfig.lays)

        for lay in range(0,winfig.lays):
            for row in range(0,winfig.rows):
                 for col in range(0,winfig.cols):
                    c = winfig.fmap[(row,lay,col)]
                    if c <> '-':
                        fig.add(Cube(row,col,(lays - lay)))
        fig.write_svg(n + ".svg")

    def savesol():
        fig = fnametx.get()
        print "writing SOL: ", fig
        figfilename = fig + ".sol"
        if os.path.isfile(figfilename):
            os.remove(figfilename)
        sol = subprocess.Popen(["BCSolve.exe", "-f" + fig + ".bcs"], stdout=subprocess.PIPE)
        sol_file = open(figfilename, "w")
        sol_file.write("===== " + fig + " =====\n")
        figsol = sol.communicate()[0].replace("\r",'')
        figsol = figsol.replace("6","$")
        figsol = figsol.replace("5","6")
        figsol = figsol.replace("$","5")
        figsol = figsol.replace("/","|")
        sol_file.write(figsol)
        sol_file.close()


    def addrow():
        r = winfig.rows
        winfig.rows += 1
        for l in range(0,winfig.lays):
            for c in range(0,winfig.cols):
                winfig.fmap[(r,l,c)] = '-'
        winmakegrid()

    def delrow():
        r = winfig.rows - 1
        for l in range(0,winfig.lays):
            for c in range(0,winfig.cols):
                if winfig.fmap[(r,l,c)] != '-':
                    winfig.cubes += -1
                del winfig.fmap[(r,l,c)]
        winfig.rows += -1
        winshowcube()
        winmakegrid()
        cubs.set(winfig.cubes)

    def addcol():
        c = winfig.cols
        winfig.cols += 1
        for l in range(0,winfig.lays):
            for r in range(0,winfig.rows):
                winfig.fmap[(r,l,c)] = '-'
        winmakegrid()
       
    def delcol():
        c = winfig.cols - 1
        for l in range(0,winfig.lays):
            for r in range(0,winfig.rows):
                if winfig.fmap[(r,l,c)] != '-':
                    winfig.cubes += -1
                del winfig.fmap[(r,l,c)]
        winfig.cols += -1
        winshowcube()
        winmakegrid()
        cubs.set(winfig.cubes)

    def addlay():
        l = winfig.lays
        winfig.lays += 1
        for r in range(0,winfig.rows):
            for c in range(0,winfig.cols):
                winfig.fmap[(r,l,c)] = '-'
        winmakegrid()

    def dellay():
        l = winfig.lays - 1
        for r in range(0,winfig.rows):
            for c in range(0,winfig.cols):
                if winfig.fmap[(r,l,c)] != '-':
                    winfig.cubes += -1
                del winfig.fmap[(r,l,c)]
        winfig.lays += -1
        winshowcube()
        winmakegrid()
        cubs.set(winfig.cubes)

    titleL = Label(menu_frame, text="Title: ").grid(row=1, column=1, padx=2)
    fnametx.set(winfig.title)
    fnametxt = Entry(menu_frame,textvariable=fnametx).grid(row=1, column=2, padx=2)
    cubnumL = Label(menu_frame, text="Cubes: ").grid(row=1, column=3, padx=2)
    cubsL = Label(menu_frame, textvariable=cubs).grid(row=1, column=4, padx=2)

    septxt = "--------------"   
    button2=Button(left_frame, fg ="black",text="Save FIG",activebackground="#7BA8C3", width=14,command=savefig).grid(row=1, column=1, padx=3, pady=2)
    #button3=Button(left_frame, fg ="black",text="Save BCS",activebackground="#7BA8C3", width=14,command=savebcs).grid(row=2, column=1, padx=3, pady=2)
    button4=Button(left_frame, fg ="black",text="Load FIG",activebackground="#7BA8C3", width=14,command=loadfig).grid(row=2, column=1, padx=3, pady=2)
    sep01 = Label(left_frame, text=septxt, bg="#F9F5D0").grid(row=3, column=1, padx=2)

    #button5=Button(left_frame, fg ="black",text="Save PNG",activebackground="#7BA8C3", width=14,command=savepng).grid(row=4, column=1, padx=3, pady=2)
    #button6=Button(left_frame, fg ="black",text="Save SVG",activebackground="#7BA8C3", width=14,command=savesvg).grid(row=5, column=1, padx=3, pady=2)
    button7=Button(left_frame, fg ="black",text="Row +",activebackground="#7BA8C3", width=14,command=addrow).grid(row=6, column=1, padx=3, pady=2)
    button8=Button(left_frame, fg ="black",text="Row -",activebackground="#7BA8C3", width=14,command=delrow).grid(row=7, column=1, padx=3, pady=2)
    button9=Button(left_frame, fg ="black",text="Col +",activebackground="#7BA8C3", width=14,command=addcol).grid(row=8, column=1, padx=3, pady=2)
    button10=Button(left_frame, fg ="black",text="Col -",activebackground="#7BA8C3", width=14,command=delcol).grid(row=9, column=1, padx=3, pady=2)
    button11=Button(left_frame, fg ="black",text="Lay +",activebackground="#7BA8C3", width=14,command=addlay).grid(row=10, column=1, padx=3, pady=2)
    button12=Button(left_frame, fg ="black",text="Lay -",activebackground="#7BA8C3", width=14,command=dellay).grid(row=11, column=1, padx=3, pady=2)
    sep02 = Label(left_frame, text=septxt, bg="#F9F5D0").grid(row=12, column=1, padx=2)

    button=Button(left_frame, fg ="red",text=" ~EXIT~ ",activebackground='red', width=14,command=quitbutton).grid(row=13, column=1, padx=3, pady=10)



root = Tk()
root.title("SomaCube Figure Maker")
window(root)
root.mainloop()
        
