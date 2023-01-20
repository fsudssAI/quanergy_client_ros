from launch_ros.actions import Node
import os #  (ZYblend 01/20/2023)

from ament_index_python.packages import get_package_share_directory #  (ZYblend 01/20/2023)

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    host = LaunchConfiguration('host')
    ns = LaunchConfiguration('ns')
    topic = LaunchConfiguration('topic')
    frame = LaunchConfiguration('frame')
    
    # get directory of setting file (ZYblend 01/20/2023)
    setting_path = os.path.join(
        get_package_share_directory('quanergy_client_ros'),
        'settings/client.xml'
    )

    host_arg = DeclareLaunchArgument(
        name='host',
        description='Host name or IP of the sensor.'
    )

    ns_arg = DeclareLaunchArgument(
        name='ns',
        default_value='quanergy',
        description='Namespace for the node.'
    )

    topic_arg = DeclareLaunchArgument(
        name='topic',
        default_value='points',
        description='ROS topic for publishing the point cloud.'
    )

    frame_arg = DeclareLaunchArgument(
        name='frame',
        default_value=ns,
        description='Frame name inserted in the point cloud.'
    )

    client_node = Node(
        package='quanergy_client_ros',
        namespace=ns,
        executable='client_node',
        name='client_node',
        output='screen',
        arguments=[
                "--host", host,
                "--settings", setting_path,  # (ZYblend 01/20/2023)
                "--topic", topic,
                "--frame", frame
        ]
    )

    return LaunchDescription([
        host_arg,
        ns_arg,
        topic_arg,
        frame_arg,
        client_node
    ])