#本文件测试车体一次的执行时间具体为几秒

import rospy
from ros_gt_msg.msg import gt_control
from package import Controlfunc_gt


if __name__ == "__main__":
    rospy.init_node("/pub_command1")
    pub = rospy.Publisher("/time_1s", gt_control, queue_size=20)
    #当发送消息频率大于本地序列化速度，来不及发送的就会到达queuesize,设置了quesize就默认是异步的，否则就是同步
    rospy.INFO("创建发布节点成功")

    du_x = rospy.Duration(1)-1
    # 一次车体运动命令的时间
    mode1_forward = Controlfunc_gt.GTControl(1,100,100,0)
    while True:
        Controlfunc_gt.move(1,"forward",pub,mode1_forward,mode1_forward.x)
        rospy.sleep(du_x) #间接控制时间测定

    # mode1_backward = Controlfunc_gt.GTControl(1,100,-100,0)
    # Controlfunc_gt.move(1,"backward",pub,mode1_forward,mode1_backward.x)




