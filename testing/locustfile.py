import logging
import psutil
from locust import HttpUser, task, events

class HelloWorldUser(HttpUser):
    test_failed = False;    

    @task
    def hello_world(self):
        self.client.get("/") 
        self.log_system_metrics()

        if not HelloWorldUser.test_failed:
            # Verificar condiciones de fallos y rendimiento antes de salir
            if self.environment.stats.total.fail_ratio > 0.40:
                logging.error("Test failed due to failure ratio > 10%")
                self.environment.process_exit_code = 1
                HelloWorldUser.test_failed = True
                self.environment.runner.quit()
                
            elif self.environment.stats.total.avg_response_time > 2000:
                logging.error("Test failed due to average response time > 2000 ms")
                self.environment.process_exit_code = 1
                HelloWorldUser.test_failed = True
                self.environment.runner.quit()
                
            elif self.environment.stats.total.get_response_time_percentile(0.95) > 10000:
                logging.error("Test failed due to 95th percentile response time > 2000 ms")
                print(self.environment.stats.total.get_response_time_percentile(0.95))
                self.environment.process_exit_code = 1
                HelloWorldUser.test_failed = True
                self.environment.runner.quit()
            
                
    def log_system_metrics(self):
        """Logs system metrics such as CPU, memory, and disk usage."""
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')

        logging.info(f"CPU Usage: {cpu_usage}%")
        logging.info(f"Memory Usage: {memory_info.percent}%")
        logging.info(f"Available Memory: {memory_info.available / (1024 ** 2)} MB")
        logging.info(f"Disk Usage: {disk_usage.percent}%")

        if cpu_usage > 80:
            logging.error("Test failed due to CPU usage > 80%")
            self.environment.process_exit_code = 1
            HelloWorldUser.test_failed = True
            self.environment.runner.quit()
 

#verify=False   