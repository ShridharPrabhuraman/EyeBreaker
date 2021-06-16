# EyeBreaker

## To Contribute
- Clone the Dev Branch (No need to fork) (git clone
- Make changes in your local machine
- 
## Trainer.py | Obtaining Training Data
- Present in 'trainer/trainer.py'
- To execute
    - Check dependencies and install if required
    - run | python trainer.py arg ; where arg == facing / not
    - if arg == facing:
        - user is recording images when he is facing the monitor(s)
        - a sub-folder with timestamp is created in the 'facing' folder
        - images captured at 1 FPS are stored, numbered serially.
    - else:
        - user is recording images when he is NOT facing the monitor(s)
        - a sub-folder with timestamp is created in the 'not_facing' folder
        - images captured at 1 FPS are stored, numbered serially.

    - at any moment, while the control is on the frame (click on the frame window), press 'q' to quit.
