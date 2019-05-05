# ecoding:UTF-8

import socket


def main():
    ip = ""
    port = 8888
    own_addr = (ip, port)  # 接收方端口信息
    byte = 1024
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(own_addr)  # 绑定端口信息
    while True:
        recv_data, other_addr = udp_socket.recvfrom(byte)
        print("收到来自%s的消息: %s" % (other_addr, recv_data))
        send_data = raw_input("输入要发送的信息:")
        udp_socket.sendto(send_data, other_addr)
        """输入数据为空退出"""
        if send_data:
            pass
        else:
            break
    udp_socket.close()  # 关闭socket

if __name__ == '__main__':
    main()
