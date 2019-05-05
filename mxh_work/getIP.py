# ecoding:UTF-8
# import socket
# import platform
# import logging
# #获取本机电脑名
# myname = socket.getfqdn(socket.gethostname(  ))
# #获取本机ip
# myaddr = socket.gethostbyname(myname)
# print myname
# print myaddr
#
#
#
# # ouput system type and version info
# print("platform.machine()=%s", platform.machine())
# print("platform.node()=%s", platform.node())
# print("platform.platform()=%s", platform.platform())
# print("platform.processor()=%s", platform.processor())
# print("platform.python_build()=%s", platform.python_build())
# print("platform.python_compiler()=%s", platform.python_compiler())
# print("platform.python_branch()=%s", platform.python_branch())
# print("platform.python_implementation()=%s", platform.python_implementation())
# print("platform.python_revision()=%s", platform.python_revision())
# print("platform.python_version()=%s", platform.python_version())
# print("platform.python_version_tuple()=%s", platform.python_version_tuple())
# print("platform.release()=%s", platform.release())
# print("platform.system()=%s", platform.system())
# # print("platform.system_alias()=%s", platform.system_alias())
# print("platform.version()=%s", platform.version())
# print("platform.uname()=%s", platform.uname())

import socket
import platform

def getip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('www.baidu.com', 0))
        ip = s.getsockname()[0]
    except:
        ip = "x.x.x.x"
    finally:
        s.close()
    return ip
def IpMain():
    ip_address = "0.0.0.0"
    sysstr = platform.system()
    if sysstr == "Windows":
        ip_address = socket.gethostbyname(socket.gethostname())
        return "Windows @ " + ip_address
    elif sysstr == "Linux":
        ip_address = getip()
        return "Linux @ " + ip_address
    elif sysstr == "Darwin":
        ip_address = socket.gethostbyname(socket.gethostname())
        return "Mac @ " + ip_address
    else:
        return "Other System @ some ip"
if __name__ == "__main__":
    IpMain()