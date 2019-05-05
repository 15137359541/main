# ecoding:UTF-8
import socket


def main():

   ip = "127.0.0.1"  # 对方ip和端口
   port = 8888
   other_addr = (ip, port)
   byte = 1024
   udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

   while True:
       send_data = raw_input("输入要发送的信息:")
       udp_socket.sendto(send_data, other_addr)
       """输入数据为空退出,否则进入接收状态"""
       if send_data:
           recv_data, other_addr = udp_socket.recvfrom(byte)
           print("收到来自%s的消息: %s" % (other_addr, recv_data))
       else:
           break
   udp_socket.close()


if __name__ == '__main__':
   main()
