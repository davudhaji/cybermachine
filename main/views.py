from django.shortcuts import render,HttpResponse
import hashlib
import base64
# Create your views here.


def index(request):

    return render(request,"index.html")


def md5(request):
    #hashlib.md5()

    if request.POST:
        txt=request.POST["md5"]
        hashf = hashlib.md5(txt.encode("UTF-8")).hexdigest()
        print(hashf)
        content = {
        "md5":"1",
        "sifre":hashf,
        }

        return render(request,"md5.html",content)



    content = {
        "md5":"1"
    }

    return render(request,"md5.html",content)


def Base645(request):
    if request.POST:
        try:
            if request.POST["base641"]:
                txt = request.POST["base641"]
                
                sifre = base64.b64decode(txt)
                sifre = sifre.decode("utf-8")
                content = {
                "base64":"1",
                "sifre":sifre
                }
                return render(request,"base64.html",content)
        except:
            try:
                txt = request.POST["base64"]
                txt = txt.encode("utf-8")
                sifre = base64.b64encode(txt)
                sifre = sifre.decode("utf-8")
                content = {
                "base64":"1",
                "sifre":sifre
                }
                return render(request,"base64.html",content)
            except:
                pass

    content = {
        "base64":"1"
    }
    return render(request,"base64.html",content)


def ceaser(request):

    if request.POST:
        print(request.POST)
        try:
            if request.POST["acar1"]:
                txt = request.POST["ceaser"]
                acar = request.POST["acar1"]
                acar = int(acar)
                word =''
                for i in range(len(txt)):
                    print(ord(txt[i])+acar,i)
                    if 0>(ord(txt[i])-acar):
                        word += chr(ord(txt[i])-acar+122)
                    else:
                        word += chr(ord(txt[i])-acar)
                        print(word)
                print(word)
                content = {
                    "ceaser":"1",
                    "sifre":word,
                }
                return render(request,"ceaser.html",content)
            
                
        except:
                txt = request.POST["ceaser"]
                acar = request.POST["acar"]
                acar = int(acar)
                word =''
                
                for i in range(len(txt)):
                    print(ord(txt[i])+acar,i)
                    if 122<(ord(txt[i])+acar):
                        word += chr(ord(txt[i])+acar-122)
                    else:
                        word += chr(ord(txt[i])+acar)
                        print(word)
                print(word)
                content = {
                    "ceaser":"1",
                    "sifre":word,
                }
                return render(request,"ceaser.html",content)





    content = {
        "ceaser":"1"
    }
    return render(request,"ceaser.html",content)

def mtc(request):

    if request.POST:
        txt = request.POST["mtc"]
        sifre = txt[::-1] 
        content = {
        "mtc":"1",
        "sifre":sifre,
        }
        return render(request,"mtc.html",content)
    content = {
        "mtc":"1"
    }
    return render(request,"mtc.html",content)


