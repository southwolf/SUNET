 
/**
 * @file server.h
 * @author kymowind@gmail.com
 * @date 2016/10/17 10:08:00
 * @brief 
 *  
 **/




#ifndef  __SERVER_H_
#define  __SERVER_H_
#include <stdio.h>
#include <iostream>
#include <vector>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/epoll.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include "select.h"
#include "event.h"
#include <fcntl.h>
#include "define.h"

namespace sub_framework {

enum {
    SELECT = 0,
    EPOLL
};


class SubServer {
   
SINGLETN(Server);

private:
    struct sockaddr_in _svr_addr;
    int _svr_fd;
    std::vector<int> _clt_sock_vec;
    SubEvent* _event;

public:
    void _run();
    void _init_sock(int port);
    void _init_evt(int evt_type);

    static int _on_read(int clt_fd);
    static int _on_accept(int svr_fd);
    static void _set_nonblocking(int sock_fd);

};
}

#endif 
