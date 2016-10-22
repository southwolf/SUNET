 
/**
 * @file define.h
 * @author wangxiaofeng04(com@baidu.com)
 * @date 2016/10/17 10:06:03
 * @brief 
 *  
 **/




#ifndef  __DEFINE_H_
#define  __DEFINE_H_

#define SINGLETN(_class) \
    private: \
        static Sub##_class* _sub_##_class##_instance;\
        Sub##_class() {} \
    public: \
        static Sub##_class* _get_instance() { \
            if (NULL == _sub_##_class##_instance) { \
                _sub_##_class##_instance = new Sub##_class();\
            } \
            return _sub_##_class##_instance; \
        } 

#define INIT_SINGLE(_class) \
    Sub##_class* Sub##_class::_sub_##_class##_instance = NULL; 


#endif  //__DEFINE_H_

/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */