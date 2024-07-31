import rospy
from ros_gt_msg.msg import gt_control

def handle_mode(control, direction_text):
    """
    处理不同的控制模式，以减少冗余。
    
    参数:
    - control: 控制对象，包含模式和速度信息。
    - direction_text: 行进方向的文字描述。
    
    返回值:
    无
    """
    # 根据控制模式，确定当前是轮速设置模式还是线速设置模式
    mode = "轮速设置模式" if control.mode == 0x01 else "线速设置模式" 
    #<value_if_true> if <condition> else <value_if_false>

    # 根据模式选择相应的速度信息
    speed = abs(control.x) if control.mode == 0x01 else abs(control.y)
    
    # 当控制模式为0x01且x轴和y轴速度不同时，记录原地动作
    if (control.x + control.y)!=0 and control.mode == 0x01:
        rospy.loginfo(f"向{direction_text}行进，mode为{mode},speed为{speed}mm/s")
    # 当速度不为0时，记录行进动作
    elif speed != 0:
        rospy.loginfo(f"原地{direction_text}，mode为{mode}")
    # 当速度为0时，记录静止动作
    else:
        rospy.loginfo(f"原地静止，mode为{mode},speed为0mm/s")

def GTControl(mode, x, y, stop):
    """
    创建一个控制消息。

    参数:
    - mode: 控制模式，默认为1。
    - x: 控制消息中的x坐标，默认为0。
    - y: 控制消息中的y坐标，默认为0。
    - stop: 是否停止的标志，默认为1（停止）。

    返回值:
    - control: 创建的控制消息对象。
    """

    # 初始化控制消息对象
    control = gt_control()
    # 设置控制模式
    control.mode = mode
    # 设置x坐标
    control.x = x
    # 设置y坐标
    control.y = y
    # 设置停止标志
    control.stop = stop
    return control

def dopub(pub, control):
    """
    发布控制消息并处理异常。

    :param pub: 发布者对象，用于发布消息。
    :param control: 控制消息，需要被发布的消息内容。
    :return: 无返回值。
    """
    try:
        rospy.loginfo("指令发布成功。")
        pub.publish(control)  # 发布控制消息
    except Exception as e:
        rospy.logerr(f"指令发布失败:{str(e)}")  # 记录发布的异常信息
    # du_x = rospy.Duration(1)
    rospy.sleep(1)

def move(time, direction, pub, control, speed):
    """
    根据给定的方向和时间移动机器人。
    
    参数:
    - time: 移动持续的时间，单位为个数，每个单位时间执行一次移动操作
    - direction: 移动的方向，可选值包括"forward"、"backward"、"left"、"right"、"rotation"
    - pub: 用于发布移动命令的publisher对象
    - control: 包含移动控制信息的对象，如速度和方向等
    - speed: 移动速度，未在函数内使用，可能用于未来的扩展
    
    返回值:
    - 无
    """
    try:
        # 定义方向与对应移动信息的映射
        directions_map = {
            "forward": ("前", control.x),
            "backward": ("后", -control.x),
            "left": ("左", control.y),
            "right": ("右", -control.y),
            "rotation": ("旋转", None),
            "static": ("静止", 0),
        }
        direction_text, value = directions_map[direction]
    except KeyError as e:
        # 处理无效方向的错误
        rospy.logerr(f"无效的方向: {direction}. 错误: {str(e)}")
        return
    
    # 循环执行移动操作
    for _ in range(time):
        dopub(pub, control)  # 发布移动命令
        # 根据控制模式处理移动模式
        if control.mode == 0x01:
            handle_mode(control, direction_text)
        elif control.mode == 0x02:
            # 处理线速设置模式下的转向信息
            if control.y != 0 and control.x != 0:
                rospy.loginfo(f"向{direction_text}转移动，mode为线速设置模式，角速度为{abs(control.y/1000)}rad/s")
            else:
                handle_mode(control, direction_text)