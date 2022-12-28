#!/usr/bin/python1.7
#coding=utf-8
import marshal,os,sys,time

os.system("clear")
print ("\033[1;92mJangan Lupa Subscribe Channel Youtube Tutorial Termux")
os.system("xdg-open https://youtube.com/@TutorialTermux")
os.system("clear")
aleju = ("""\033[1;92m
╔╦╗┌─┐┬─┐┌─┐┬ ┬┌─┐┬
║║║├─┤├┬┘└─┐├─┤├─┤│
╩ ╩┴ ┴┴└─└─┘┴ ┴┴ ┴┴─┘
Creator : Demias Syihab Aldino
Youtube : Tutorial Termux
Github : https://github.com/maskprivate1457/
Whatsapp : 0895320372281\n""")
def aleeju():
        try:
                print (aleju)
                print ('\33[31m[-] Contoh > /sdcard/file.py')
                file = input ('[-] File Kamu : ')
                fileopen = open(file).read()
                a = compile(fileopen, 'dg', 'exec')
                m = marshal.dumps(a)
                s = repr(m)
                b = ('import marshal\nexec(marshal.loads(' + s +'))')
                c = file.replace('.py', '.py')
                d = open(c, 'w')
                d.write(b)
                d.close()
                print ('[-] Berhasil > ',c)
                time.sleep(1)
                aq = input ('[-] Ingin encrypt lagi? [Y/N]')
                if aq =="":
                        print ('Command not found !')
                        os.sys.exit()
                elif aq =="y" or aq =="Y":
                        aleeju()
                else:
                        if aq =="n" or aq =="N":
                                print ('> Terimakasih anjeng ;v\n')
                        else:
                                print ('Command not found !')
                                os.sys.exit()
        except IOError:
                print ('File Tidak Ditemukan ! ')
                time.sleep(1)
                aleeju()

if __name__=='__main__':
        aleeju()
