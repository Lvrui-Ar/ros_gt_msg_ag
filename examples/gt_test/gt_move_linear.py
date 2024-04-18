import rospy
from ros_gt_msg.msg import gt_control
from package import Controlfunc_gt

'''
本文件针对车体的模式2：线速模式，进行测试
测试例程1： 测试角速度的正反与运动方向的对应关系

'''

if __name__ == "__main__":
    rospy.init_node("pub_command1_linear")
    pub = rospy.Publisher("/gt_move_linear", gt_control, queue_size=20)
    #当发送消息频率大于本地序列化速度，来不及发送的就会到达queuesize,设置了quesize就默认是异步的，否则就是同步
    rospy.loginfo("创建发布节点成功")
    
    # 测试例子1：测试角速度为正，线速度为正的情况，车子逆时针还是顺时针运动？（逆时针是左转，顺时针是右转，不跟线速度正负有关系）
    linear_move_left = Controlfunc_gt.GTControl(2,200,500,0)
    Controlfunc_gt.move(10,"left",pub,linear_move_left,linear_move_left.x)

    linear_move_right = Controlfunc_gt.GTControl(2,200,-500,0)
    Controlfunc_gt.move(10,"right",pub,linear_move_right,linear_move_right.x)

    # 测试例子2：测试线速度值为0,角速度值不为0的运动情况
    linear_test_nospeed = Controlfunc_gt.GTControl(2,0,500,0)
    n = 10
    while n>0:
        Controlfunc_gt.dopub(pub,linear_test_nospeed)
        n=n-1

    # 测试例子3：测试线速度值为0,角速度值为0的运动情况
    linear_test_norad = Controlfunc_gt.GTControl(2,0,0,1)
    n = 10
    while n>0:
        Controlfunc_gt.dopub(pub,linear_test_norad)
        n=n-1

    # # 测试例子4：测试急停标志stop对运动的影响
    linear_test_stop = Controlfunc_gt.GTControl(2,200,500,1)
    n = 10
    while n>0:
        Controlfunc_gt.dopub(pub,linear_test_stop)
        n=n-1
