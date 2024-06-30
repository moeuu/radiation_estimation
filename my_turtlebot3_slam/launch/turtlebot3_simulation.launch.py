from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('my_turtlebot3_slam'),
                'launch', 'turtlebot3_gazebo.launch.py')]),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('my_turtlebot3_slam'),
                'launch', 'turtlebot3_slam.launch.py')]),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('my_turtlebot3_slam'),
                'launch', 'turtlebot3_rviz.launch.py')]),
        ),
    ])