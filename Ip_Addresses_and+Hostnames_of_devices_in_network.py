def get_all_hostnames(rang):
    import socket
    hostanames_and_ips = []
    myhostname = socket.gethostname()
    ipaddfirst = socket.gethostbyname(myhostname)
    print(ipaddfirst)
    numofdots = 3
    ip = "0.0.0.0"

    for i in range(len(ipaddfirst)):

        if ipaddfirst[i]=='.':

            numofdots-=1

            if numofdots ==0:
                ip = ipaddfirst[:i+1]





    for num in range(1, rang):
        ipaddress= ip + str(num)


        try:


            name = socket.gethostbyaddr(ipaddress)
            

            hostanames_and_ips.append(name)
        except:
            pass
    return hostanames_and_ips

print(get_all_hostnames(20))