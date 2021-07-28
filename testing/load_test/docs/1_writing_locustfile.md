### User class
- `wait_time`  
  How long use should wait between tasks.  

  Own wait time possible.  
  ```python
  class MyUser(User):
    last_wait_time = 0

    def wait_time(self):
      self.last_wait_time += 1
      return self.last_wait_time
  ```

- `weight`  
  If you more than one user and you wish to stimulate one type of user more.  

  ```python
  class WebUser(User):
    weight = 3
    ...
  ```  

  `locust -f locust_file.py WebUser MobileUser`


- `environment` - attribute.  
  `self.environment.runner.quit()`  
  Will stop the node it's running on, master or worker.

- `on_start` AND `on_stop` methods.  


### Tasks

- `tasks` attribute.  
  tasks are either python callable or a TaskSet class

  ```python
  def my_task(user):
    pass

  def MyUser(User):
    tasks = [my_task]   # Picked randomly
    tasks = {my_task: 3, another_task: 1}  # Picked randomly, but as per weight.
  ```


- `tags`  
  `@tags('tag1')`  

  You can be picky about what tasks will be executed during the running.
  Using the `--tags` and `--exclude-tags` arguments.


### Events
- `test_start` and `test_stop`  
  ```python
  from locust import events

  @events.test_start.add_listener
  def on_test_start(environment, **kwargs):
    print("A new test is starting")

  @events.test_stop.add_listener
  def on_test_stop(environment, **kwargs):
    print("A new test is ending")
  ```

  When running distributed, it will only be running on master node.


- `init`  
  At the beginning of each locust process (master, worker).  
  ```python
  from locust import events
  from locust.runners import MasterRunner

  @events.init.add_listener
  def on_locust_init(environment, **kwargs):
      if isinstance(environment.runner, MasterRunner):
          print("I'm on master node")
      else:
          print("I'm on a worker or standalone node")
  ```


### HttpUser
Mostly used User. It adds a `client` attribute which is used to make
HTTP request.


- **Validating Response**  
  ```python
  with self.client.get("/", catch_response=True) as response:
    if response.text != "Success":
      response.failure("Got wrong response")
    elif response.elapsed.total_seconds() > 0.5:
      response.failure("Request took too long")
  ```

- **Grouping Requests**  
  by passing name attribure on self.client call.


### TaskSets
To structure tests of hierarchial web sites/systems.






























