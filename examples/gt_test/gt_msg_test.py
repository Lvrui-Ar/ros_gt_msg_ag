# 本文件测试gt_motion.msg的参数意思
import rospy
from ros_gt_msg.msg import gt_control
from src.package import Controlfunc_gt


if __name__ == "__main__":
    rospy.init_node("/pub_command1")
    pub = rospy.Publisher("/time_1s", gt_control, queue_size=20)
    #当发送消息频率大于本地序列化速度，来不及发送的就会到达queuesize,设置了quesize就默认是异步的，否则就是同步
    rospy.INFO("创建发布节点成功")

    mode2_forward = Controlfunc_gt.GTControl(2,100,500,0)
    Controlfunc_gt.move(5,"forward",pub,mode2_forward,mode2_forward.y)
    rospy.INFO(f"Vx:{int()}")


#线速度反馈、底盘状态
# int16   Vx   #线速度：mm/s
# float32 Vz   #线速反馈的角速度：0.001rad/s
# int16   power  #power:底盘电压,单位0.1v
# uint8   robot_data
# uint8   robot_contr_mode  #控制状态  0x00：空闲状态; 0x01：遥控器模式;0x02:上位机模式;0x05:升降台模式; 0xFF: 错误状态
# int16   temp_l  #左驱动器温度
# #int16  temp_r
# uint16  driver_err_L #左驱动器状态：16种值，Bit15:保留
# uint16  driver_err_R #右驱动器状态：16种值，Bit15:保留
# uint16  driver_init_L #左驱动器电流：0.1A
# uint16  driver_init_R #右驱动器电流：0.1A
# int16   Current_L #左电机状态：16种状态
# int16   Current_R #右电机状态：16种状态
# int16   Current_max_L #电机状态：电流最大值_左？单位0.1A
# int16   Current_max_R #电机状态：电流最大值_右？