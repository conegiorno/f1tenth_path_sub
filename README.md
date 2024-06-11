# f1tenth_path_sub
ROS2 Package used to measure path of AWSIM F1Tenth vehicle and write it to *.csv* file. Package include python scripts usefull to plot recorded paths and error relative to reference trajectory.

# Usage:
Build package by:
```bash
colcon build --symlink-install
```
And then source to:
```bash
source install/setup.bash
```

To record your vehicle path in terminal use:
```bash
ros2 run f1tenth_path_sub path_to_csv
```
You can plot your path or path error by running python scripts *plot_path.py* and *error_graph.py*.

## Example graphs:
