from setuptools import setup

package_name = 'my_pypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dev',
    maintainer_email='hoangduyprop@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = my_pypkg.my_first_node:main",
            "robot_news_station = my_pypkg.robot_news_station:main",
            "smartphone = my_pypkg.smartphone:main",
            "add_two_ints_server = my_pypkg.add_two_ints_server:main",
            "add_two_ints_clients_no_oop = my_pypkg.add_two_ints_clients_no_oop:main",
            "add_two_ints_clients = my_pypkg.add_two_ints_clients:main",
            "number_publisher = my_pypkg.number_publisher:main",
            "number_counter = my_pypkg.number_counter:main",
            "hw_status_publisher = my_pypkg.hw_status_publisher:main",
            "led_panel = my_pypkg.led_panel:main",
            "battery = my_pypkg.battery:main"
        ],
    },
)
