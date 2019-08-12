# copy_clipboard-v1.0

This is a support programm for the Windows file or text copying system. This programm helps in increasing your productivity by saving your previous 10 copied items let it be a file/folder/text etc. and let you acess these saved items through simple and eassily accessible shortcut kyes. To provide refference for your last 10 copied items the console shows them with their respective indexing.

copy_clipboard cheet sheet ( shortcut keys ):

    ctrl + c  -----  copies the text
    shift + x  -----  copies the files and folders
    ctrl + v + int( 1 - 9) -----  pastes the copied item at the respective index
  
Modules required are:
    pyautogui    installation---->    pip install pyautogui
    pynput       installation---->    pip install pynput
    
setting up the programm.
    
press shift and right click on a file or folder and take a screen shot and crop the image for only "copy as path" in the right click       dropdown box and save the cropped image in the folder of copy_clipboard programm. Save al least 4 such images there with the names:
    
    Screenshot (6).png
    Screenshot (7).png
    Screenshot (8).png
    Screenshot (9).png
    
    DELETE the existing .png file in the folder (these are for example).
    
And the programm is ready for use.
