import socket
import thread as th
import sys
import os
from time import sleep
from random import randint
from subprocess import call

class Page:
    ''' This class will contain needed tools to manage page resource
        of a local machine
    '''
    def __init__(self,name,pageSize=10):
		  os.system("echo >> \"%s\""%name) # only linux
		  self.name = name
		  self.page = None
		  self.pageSize = pageSize# available lines in this page (memory)
		  self.openPage()		# it will open a local resource
		  self.putInitContent()	# it will generate initial content into page

    def __del__(self):
        self.closePage()

    def openPage(self):
        ''' it will open resource file '''
        self.page = open(self.name,'r+')
        return 'Done!'

    def closePage(self):
        ''' it will close resource file '''
        self.page.close()
        return 'Done!'

    def generLineContent(self):
        ''' it will generate a line content page '''
        numbers = ['1','2','3','4','5','6','7','8','9','0']
        lineSize = 81; line = ''
        for char in range(0,lineSize): line += numbers[randint(0,len(numbers)-1)]
        return line

    def putInitContent(self):
        ''' it will put initial content into page '''
        for line in range(0,self.pageSize-1): self.page.write(self.generLineContent()+'\n')
        self.page.flush()
        return 'Done!'

    def write(self,content):
        ''' it will write resource file '''
        self.page.seek(0)
        self.page.write(content)
        self.page.flush()
        return 'Done!'

    def read(self):
        ''' it will read resource file '''
        self.closePage()
        self.openPage()
        content = ''
        for line in self.page: content += line
        return content

class Menu:
    ''' defining machine Menu, it will let to interact with user '''
    def __init__(self):
        self.ownerName = None
        self.purpose = None

    def getOwnerName(self):
        ''' it will get ownerName attribute '''
        return self.ownerName

    def getPurpose(self):
        ''' it will get purpose attribute '''
        return self.purpose

    def showMenu(self,pagesInfo):
        ''' it will print menu and get data from user '''
        validPurposes = ['w','r']; ownersNames = []
        for ownerName in pagesInfo: ownersNames.append(ownerName)
        while 1:
            print ""
            for ownerName in ownersNames:
                ownerName, pageName, pageSize, page = pagesInfo[ownerName]
                print "Owner name = %s | Page name = %s | Page size = %s"%(ownerName,pageName,pageSize)
            else:
                print "Type 'Exit' if you want it"
                self.ownerName = raw_input("\nGive me desired owner name of the page: ")
                if self.ownerName == 'Exit': self.ownerName = None; self.purpose = None; break
                if not self.ownerName in ownersNames: print "Owner name typed does not exist!"; continue
                self.purpose = raw_input("Give me desired purpose (w/r): ")
                if not self.purpose in validPurposes: print "'(w/r)' are the valid purposes only!"; continue
            print ""
            break
        return 'Done!'

class Machines:
    ''' simulating a machine (client/server) that belong to a distribuited system
        it will share internal memory (file) with others external machines
    '''
    def __init__(self,ip='',port=5005,externIp=['localhost']*3,externPorts=[5006,5007,5008]):
        if not isinstance(externIp,list): print "The sequence of ips must be a list!"; sys.exit()
        if not isinstance(externPorts,list): print "The sequence of ports must be a list!"; sys.exit()
        if not len(externIp) == len(externPorts): print "There must be the same amount of ip as ports!"; sys.exit()
        self.sock = None            # this server socket
        self.ip = ip                # this server ip
        self.port = port            # this server port
        self.externIp = externIp    # ips external machines
        self.externPorts = externPorts # ports external machines
        self.externMachines = {}    # it will store external machines sockets
        self.buffer = 2048          # channel size
        self.isBeingAccessedPage = {}# it will store synchronization variables
        self.pagesInfo = {}         # it will store pages info ['owner machine name','name page','page size','page object']
        self.notReadyAllExternMachines = len(externPorts)# it will report if all external machines already know about this server page size
        self.thisOwnerPage = os.path.basename(__file__) # this source file name (name.py)
        pageName = self.thisOwnerPage+' page.txt'# own page name
        page = Page(pageName,10)    # it will be the page of this machine (resource)
        self.logPageInfo(self.thisOwnerPage,pageName,10,page)# it will log own page
        self.isBeingAccessedPage[self.thisOwnerPage] = False# it will log own page status
        self.menu = Menu()          # it will build user menu
        self.setSeverSock()         # it will set up this server socket

    def __del__(self):
        self.closeServer()          # it will close this server socket
        self.disconnect()           # it will disconnect with external machines

    # ----- server section -----
    def closeServer(self):
        ''' it will close socket server'''
        self.sock.close()
        return 'Done!'

    def logPageInfo(self,owner,pageName,pageSize,page):
        ''' it will log page info '''
        self.pagesInfo[owner] = [owner,pageName,pageSize,page]
        return 'Done!'

    def setSeverSock(self):
        ''' it will set up server socket '''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip,self.port))
        self.sock.listen(len(self.externPorts))
        return 'Done!'

    def listenRequest(self,sock,addr):
        ''' it will listen request from external process '''
        while 1:
            data = sock.recv(self.buffer)
            if not data: break
            info = 'None'
            request, text, ownerPage, pageStatus = data.split('|')
            if request == 'getPageInfo':
                ownerName, pageName, pageSize, page = self.pagesInfo[self.thisOwnerPage]
                info = ownerName+'|'+pageName+'|'+str(pageSize)
                self.notReadyAllExternMachines -= 1
            elif request == 'notifyAccessedPage':
                pageStatus = bool(pageStatus)
                self.isBeingAccessedPage[ownerPage] = pageStatus
                info = 'ok'
            elif request == 'upgradePage':
                ownerName, pageName, pageSize, page = self.pagesInfo[ownerPage]
                info = page.write(text)
            elif request == 'readyToDisconnect': info = 'ok'; self.notReadyAllExternMachines -= 1
            sock.send(info)
        sock.close()
        return 'Done!'

    def setChannelConection(self):
        ''' it will let set up channel connection with external machines '''
        while 1:
            Psock, Padd = self.sock.accept()
            th.start_new_thread(self.listenRequest,(Psock,Padd[0]))
        return 'Done!'

    # -----  client section -----
    def disconnect(self):
        ''' it will let to disconnect with external machines '''
        for port in self.externPorts:
            try: self.externMachines[port].close()
            except: continue
        return 'Done!'

    def connect(self):
        ''' will let to connect with external machines '''
        for port in self.externPorts:
            ip = self.externIp.pop(0)
            sock = socket.socket()
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            connected = False
            while not connected:
                try: sock.connect((ip, port))
                except: sleep(1); continue
                connected = True
            self.externMachines[port] = sock
        return 'Done!'

    def notifyAllExternMachines(self,requestType,text,ownerPage,pageStatus):
        ''' it will notify to external machines about a purpose inside requestType parameter '''
        for port in self.externPorts:
            self.externMachines[port].send(requestType+'|'+text+'|'+ownerPage+'|'+pageStatus)
            self.externMachines[port].recv(self.buffer)
        return 'Done!'

    def getPagesInfo(self):
        ''' it will get pages info of external machines '''
        for port in self.externPorts:
            self.externMachines[port].send("getPageInfo|None|None|None")
            infoPage = self.externMachines[port].recv(self.buffer)
            ownerName, pageName, pageSize = infoPage.split('|')
            pageName = '(copy) '+pageName
            page = Page(pageName,int(pageSize))
            self.logPageInfo(ownerName,pageName,pageSize,page)
            self.isBeingAccessedPage[ownerName] = False
        while self.notReadyAllExternMachines: sleep(1)
        self.notReadyAllExternMachines = len(self.externPorts)
        return 'Done!'

    def openEditor(self,pageName):
        ''' it will launch an editor '''
        popularEditors = ['gedit','geany','mousepad','notepad','nano','vim','atom']
        while popularEditors:
            editor = popularEditors.pop(0)
            try: call([editor,pageName])
            except OSError: continue
            raw_input("press enter key!")
            break
        return 'Done!'

    def loadUserText(self,page,pageSize):
        ''' it will load user text from file '''
        userText = page.read()
        userTextLen = len(userText.split('\n'))
        if userTextLen > pageSize: userText = ''
        return userText

    def getUserText(self,page,pageName,pageSize):
        ''' it will get user text and load it into memory '''
        userText = ''
        while not userText:
            print "Text must be greater than 0 lines! and lower or equal than %s lines"%pageSize
            self.openEditor(pageName)
            userText = self.loadUserText(page,pageSize)
        return userText

    def interact(self,ownerName,purpose):
        ''' it will interact with user and externals machines '''
        if not self.isBeingAccessedPage[ownerName]:
            self.notifyAllExternMachines('notifyAccessedPage','None',ownerName,'True')
            ownerName,pageName,pageSize,page = self.pagesInfo[ownerName]
            if purpose == 'w':
                userText = self.getUserText(page,pageName,pageSize)
                print userText
                self.notifyAllExternMachines('upgradePage',userText,ownerName,'None')
            elif purpose == 'r': print page.read()
            self.notifyAllExternMachines('notifyAccessedPage','None',ownerName,'')
        else: print "\nRequested owner page is being used by another process\nTry again more late..."

    def main(self):
        ''' main method will get the program control '''
        while 1:
            self.menu.showMenu(self.pagesInfo)
            ownerName = self.menu.getOwnerName()
            purpose = self.menu.getPurpose()
            if not ownerName: break
            self.interact(ownerName,purpose)
        self.notifyAllExternMachines('readyToDisconnect','None','None','None')
        print "Waiting for externals machines complete their tasks!"
        while self.notReadyAllExternMachines: sleep(1)
        return 'Done!'

if __name__ == "__main__":
    # ---- behaving of server -----
    machine1 = Machines('',5000,[],[])
    th.start_new_thread(machine1.setChannelConection,())

    # ---- behaving of client -----
    machine1.connect()
    machine1.getPagesInfo()
    machine1.main()
