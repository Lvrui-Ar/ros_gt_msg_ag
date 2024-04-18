import rospy
from ros_gt_msg.msg import Lift_control
def Lift_Control(mode:int, data:int, clear_flag:int):
    control = Lift_control()
    control.mode = mode
    control.data = data
    control.clear_flag = clear_flag
    return control

#发布函数
def dopub(pub_lift, control):
    '''
    #指令发布成功
    #指令发布失败
    #间隔1秒发布一条指令
    '''
    du_x = rospy.Duration(1)
    try:
        pub_lift.publish(control)
        rospy.loginfo("指令发布成功")
    except Exception as e:
        rospy.logerr(f"指令发布失败：{str(e)}")
    
    rospy.sleep(du_x)

#升降台运动函数
def move_lift(pub, control,mode):
    '''
    1、间隔一秒发布一次命令，定义time变量
    2、发布对象，后台以Lift_control格式发布运动消息，定义变量pub
    3、运动消息对象，格式为(mode,data,clear_flag),定义变量control
    4、区分位置模式或者速度模式，定义变量mode
    '''
    dopub(pub,control)
    if control.mode == 0x01:
        mode = "位置模式"
        rospy.loginfo(f"升降台控制模式为{mode},位置是{control.data/10}mm")
    elif control.mode == 0x02:
        mode = "速度模式"
        rospy.loginfo(f"升降台控制模式为{mode},速度是{control.data}rpm")
    else:
        rospy.logerr(f"模式不正确，请输入正确模式")

    