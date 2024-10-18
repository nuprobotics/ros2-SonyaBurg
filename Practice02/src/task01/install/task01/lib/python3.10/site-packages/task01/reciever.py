import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class reciever(Node) :
	def __init__(self) :
	   super(reciever, self).__init__('simple_node')
	   timer_period = 1
	   self.timer = self.create_timer(timer_period, self.timer_callback)
	   self.subscriber = self.create_subscription(String, 'spgc/sender', self.subscriber_callback, qos_profile=10)
	def subscriber_callback(self, msg):
	   self.get_logger().info(f"Recieved: {msg.data}")

	def timer_callback(self) :
	   self.get_logger().info("Hello world!")

def main () :
   rclpy.init()
   node = reciever()
   rclpy.spin(node)
   rclpy.shutdown()

if __name__ == '__main__':
   main()
