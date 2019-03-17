
qytang_dict = {'公司':
                   {'乾颐堂':
                        {'部门':
                             [{'部门名': 'python',
                               '师资': ['秦柯', '教主'],
                               '课程':['python基础',
                                     'python网络编程 第一部分 经典协议',
                                     'python网络编程 第二部分 HTTP协议',
                                     'python网络编程 第三部分 自动化运维']
                               }
                              ]
                         }
                    }
               }


if __name__ == '__main__':
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(qytang_dict)

