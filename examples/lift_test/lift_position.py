import rospy
from ros_gt_msg.msg import Lift_control
from src.package import Controlfunc_Lift

if __name__ == '__main__':
    rospy.init_node('lift_control_node_position')
    pub = rospy.Publisher('/lift_position',Lift_control,queue_size=20)

    # 测试例子1：参考hight值零点的位置（假设是绝对零点位置）
    '''
    1.创建发布消息，将hight(即速度模式下的data值)调为0
    2.发布消息，并在后台反馈
    '''
    control_zeroH = Controlfunc_Lift.Lift_control(mode=1,data=0,clear_flag=0)
    Controlfunc_Lift.move_lift(pub=pub,control=control_zeroH,mode="位置模式")

    # # 测试例子2：hight值正负与升降台运动上下的关系
    # control_up = Controlfunc_Lift.Lift_control(mode=1,data=1000,clear_flag=0)
    # control_down = Controlfunc_Lift.Lift_control(mode=1,data=-1000,clear_flag=0)
    # Controlfunc_Lift.move_lift(pub=pub,control=control_up,mode="位置模式")
    # rospy.sleep(5)
    # Controlfunc_Lift.move_lift(pub=pub,control=control_down,mode="位置模式")
    # rospy.sleep(5)

    # # 测试例子3：master主动Pub发送控制命令给升降台，这个通过话题来查看
    # # 

    # # 测试例子4：测试hight值与给定位置的倍速关系
    # control_hight_low = Controlfunc_Lift.Lift_control(mode=1,data=100,clear_flag=0)
    # Controlfunc_Lift.move_lift(pub=pub,control=control_hight_low,mode="位置模式")
    # rospy.sleep(10)
    # control_hight_medium = Controlfunc_Lift.Lift_control(mode=1,data=1000,clear_flag=0)
    # Controlfunc_Lift.move_lift(pub=pub,control=control_hight_medium,mode="位置模式")
    # rospy.sleep(10)
    # control_hight_high = Controlfunc_Lift.Lift_control(mode=1,data=2000,clear_flag=0)
    # Controlfunc_Lift.move_lift(pub=pub,control=control_hight_high,mode="位置模式")


