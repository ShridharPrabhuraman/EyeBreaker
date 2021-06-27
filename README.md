# EyeBreaker
#### _Because your eyes needs it_

In a survey by OnePoll, it was discovered that an average person spends 17 hours and 9 minutes everyday on screen, out of that around 5 hours on a computer/laptop screen time. That\'s a total of 44 years of a person\'s life that is spent watching a display.

This is a serious issue that could lead to variety of eye diseases like Eye fatigue, Dry and irritated eyes, Loss of focus flexibility, Nearsightedness, Retinal damage.
Some of these damages to a person could be permanent, others; very costly to treat. We believe that by a simple set of regular on-screen-off-screen break patterns can help rest the eyes and recover from constant eye screen damages.

That is why, we are introducing EyeBreaker, a simple yet an amazingly helpful tool that will notify you to take breaks at regular interval from your computer/laptop screen so that your eyes can maintain a better long-term health.

The tool uses your device\'s camera/webcam to track your face direction using Machine Learning (Tensorflow) to determine if you are watching the screen or not. If you are not watching the screen or not present in front of the computer, then it considers it as your break period.

### Run this Tool
To run this tool you need to install some python libraries. It would be prefered if you create a new python environment to avoid any version clashes with your system's global libraries.

Python Virtual Environment Reference: https://docs.python.org/3/library/venv.html

Next step is to install all the packages to your environment. After you have sourced your environment with the command:
```
source <venv>/bin/activate
```
You need to install all the libraries that are mentioned in requirements.txt using the command (Pip):
```
pip install -r requirements.txt
```
After all the libraries have been successfully installed you can run your program by running the main.py file:
```
python main.py
```

Then the tool's UI window will successfuly open up (Shown in the screenshots below).
Some of the customization that you can do:
 - Focus Time: How much time you can focus on-screen without taking a break. Default 1200 seconds (20 Minutes).
 - Break Period: Number of seconds you want to take break. Default 60 seconds (1 Minute).
 - Checking Period: At what intervals should the camera check if you are on-screen or off-screen. Default 45 seconds.

When you start using the tool, it will capture snapshots using your camera/webcam at regular interval based on the checking period variable, and will determine if you are watching the screen or taking a break. When you should be taking break after (Focus Time) minutes of screen time, there will be a sound played for you to notify the start and end of the break period.

We have minimized the usage of Memory that this program consumes and with the checking period you can control the usage of how often the camera captures and determines your screentime, thus saving battery consumption.

### UI Screenshots
![Screen Shot 2021-06-27 at 2 49 22 PM](https://user-images.githubusercontent.com/15246084/123539543-ef30a000-d757-11eb-88ac-3c4e8c52f14a.png)
![Screen Shot 2021-06-27 at 2 49 38 PM](https://user-images.githubusercontent.com/15246084/123539548-f35cbd80-d757-11eb-8460-c5d44d2d96df.png)
![Screen Shot 2021-06-27 at 2 49 49 PM](https://user-images.githubusercontent.com/15246084/123539552-f5bf1780-d757-11eb-9d8a-34a68d9c066a.png)


###### Please Note: This application is developed based on open source research and surveys. No Medical Proof has been granted by usage of this application.
