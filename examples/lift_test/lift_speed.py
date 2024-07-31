import rospy
from ros_gt_msg.msg import Lift_control
from src.package import Controlfunc_Lift

if __name__ == '__main__':
    rospy.init_node('lift_control_node_speed')
    pub = rospy.Publisher('lift_speed',Lift_control,queue_size=20)

    # # 测试例子1：转速超过25RPM正常范围，出现的现象。根据此例子可以进一步观察是否可以通过转速超过固定值，会产生什么风险，该例子不能直接在车上测试
    # '''
    # 1。创建测试对象
    # 2。给一个低于25RMP的值
    # 3.给一个高于25RMP的值
    # '''
    # control_low = Controlfunc_Lift.Lift_control(mode=2,data=10,clear_flag=0)
    # control_high = Controlfunc_Lift.Lift_control(mode=2,data=30,clear_flag=0)

    # Controlfunc_Lift.move_lift(pub=pub,control=control_low,mode="速度模式")
    # rospy.sleep(10)
    # Controlfunc_Lift.move_lift(pub=pub,control=control_high,mode="速度模式")
    # rospy.sleep(1)

    # # 测试例子2：正常转速内,让转速模式下能停下来，除了手动急停，可以通过发送停止运动的指令或者让转速清零
    # '''
    # 1.创建一个转速模式下的运动对象消息
    # 2.创建一条停止运动的消息命令:原理是让速度清零
    # '''
    # control_move = Controlfunc_Lift.Lift_control(mode=2,data=15,clear_flag=0)
    # control_stop = Controlfunc_Lift.Lift_control(mode=2,data=0,clear_flag=0)
    # # n=10
    # # while n>0:
    # #     Controlfunc_Lift.move_lift(pub=pub,control=control_move,mode="速度模式")
    # #     n=n-1
    # Controlfunc_Lift.move_lift(pub=pub,control=control_move,mode="速度模式")  # 第一条命令会丢失
    # try:
    #     rospy.sleep(10)
    #     pub.publish(control_stop)
    #     rospy.loginfo("已经发送停止运动指令")
    # except Exception as e:
    #     rospy.logerr(f"停止运动指令发送失败：{str(e)}")


    # 测试例子3：测试驱动器故障标志位生效（即为1）时，升降台的状态信息会发生什么变化
    control_clear_normal = Controlfunc_Lift.Lift_control(2,24,1)
    control_clear_abnormal = Controlfunc_Lift.Lift_control(2,26,1)
    Controlfunc_Lift.move_lift(pub, control_clear_normal,"速度模式")
    rospy.sleep(5)
    Controlfunc_Lift.move_lift(pub, control_clear_abnormal,"速度模式")


