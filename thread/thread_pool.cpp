 
/**
 * @file src/thread_pool.cpp
 * @author kymowind@gmail.com
 * @date 2016/10/08 17:13:22
 * @brief 
 *  
 **/

#include "thread_pool.h"
#include "task_handler.h"

namespace sub_framework {
    

SubThreadPool* SubThreadPool::_sub_thread_pool_instance = NULL;

SubThreadPool::SubThreadPool() {
    _stoped = false;
    _threads_cnt = 0;
}

SubThreadPool::~SubThreadPool() {
    
}

void SubThreadPool::_init() {
    _threads_cnt = SubConfig::_get_instance()->_get_thread_cnt();
    std::cout << "thread cnt:" << _threads_cnt << std::endl;
}

void SubThreadPool::_set_thread_cnt(int thread_cnt) {
    if (_threads.size() != 0) {
        std::cout << "Thread Pool is running!Set thread count is not allowed!" << std::endl;
        return ;
    }
    _threads_cnt = thread_cnt;
    std::cout << "threads cnt:" << _threads_cnt << std::endl;
}

int SubThreadPool::_start() {
    if (_threads.size() != 0 || _threads_cnt < 1) {
        std::cout << "start failed!" << _threads.size() << "," << _threads_cnt << std::endl;
        return 0;
    }
    for (int i = 0; i < _threads_cnt; i++) {
        SubThreadHandler* sub_task_handler = new SubTaskHandler();
        SubThread* sub_thread = new SubThread(sub_task_handler, (void*)&i);
        sub_thread->_start();
        _threads.push_back(sub_thread);
    }
    return 1;
}

}





















/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
