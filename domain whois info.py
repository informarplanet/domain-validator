import whois
from domainvalid import is_registered

domain_name="facebook.com"
if is_registered(domain_name):
    whois_info= whois . whois ( domain_name )
    domain_name=whois_info.domain_name
    nameservers=whois_info.name_servers

    serverlist=list(set([nameserver.lower()  for nameserver in nameservers]))

    finalserverslist=','.join(serverlist)

    update_date=whois_info.updated_date
    creatation_date=whois_info.creation_date
    expire_date=whois_info.expiration_date

    if type(domain_name)==list:
        if len(domain_name)>0:
            print (f'[++] Showing result for Domain: {whois_info.domain_name[0]}\n========================================'  )
    else:
        print (f'[++] Showing result for Domain: {domain_name}\n========================================')
    
    print (f"[++] WHOIS server:", whois_info.whois_server)
    print (f"[++] Registrar:" , whois_info.registrar)
    #creatation date
    if type(creatation_date)==list:
        if (len(creatation_date))>0:
            print(f"[++] Creatation Date:",creatation_date[-1])
    else:
        print (f"[++] Creation Date:" , creatation_date)    
    
    # update Date
    if type(update_date)==list:
        if (len(update_date))>0:
            print(f"[++] Updated Date:",update_date[-1])
    else:
        print (f"[++] Updated Date:" ,update_date)
    #expire date
    if type(expire_date)==list:
        if (len(expire_date))>0:
            print(f"[++] Expire Date:",expire_date[-1])
    else:
        print (f"[++] Registry Expiry Date:" , expire_date)
    
    print (f"[++] Name Servers:" , finalserverslist)
    print (f"[++] Registrant Organization" , whois_info.org)
    print (f"[++] Registrant State/Province:" , whois_info.state)
    print (f"[++] Registrant Country:" , whois_info.country)
    print (f"[++] Admin Organization:" , whois_info.org)
    print (f"[++] Admin Street_Name:" , whois_info.address)
    print (f"[++] Admin City:" , whois_info.city)
    print (f"[++] Admin Country:" , whois_info.country)
    print (f"[++] Postal Code:" , whois_info.registrant_postal_code)
    print (f"[++] Email:" ,whois_info.emails )
 
