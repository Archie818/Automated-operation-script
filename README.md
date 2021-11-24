1. Install python3.4 or above, and configure environment variables
Tutorial: https://www.runoob.com/python3/python3-install.html
2. Install dependencies
Method: input in cmd (win+R enter cmd and press enter)
pip install pyperclip press enter
pip install xlrd press enter
pip install pyautogui==0.9.50 press enter
pip install opencv-python press enter
pip install pillow Enter
3. Save the screenshots of the icons and areas to be operated at each step in the png format of this folder (note that if there are multiple identical icons on the same screen, the upper left one will be found by default. Therefore, how to take screenshots and how large areas should be taken is a matter of knowledge. If the input box only cuts the blank part in the middle is definitely not enough, the purpose is "unique")
4. In sheet1 of cmd.xls, configure the instructions for each step. For example, the content corresponding to instruction type 1234 fills in the screenshot file name, the content corresponding to instruction 5 is the waiting time (in seconds), the content corresponding to instruction 6 is the distance of the scroll wheel , A positive number means roll up, a negative number means roll down
5. Save the file
6. Double-click waterRPA.py to open the program, press 1 to execute the instruction in excel once, and press 2 to repeat the execution indefinitely until the program is closed
7. If you can’t run after an error is reported, run vscode to see the content of the error. If it doesn’t work, you can contact WeChat blblwater
8. After starting the program, please minimize the program box, otherwise the area blocked by the program box will not be recognized and operated
9. If the mouse is occupied and cannot be stopped after the program starts because you have selected infinite repeat, please alt+F4~


If you want to develop and optimize by yourself, you can look at other usages of the pyautogui library https://blog.csdn.net/qingfengxd1/article/details/108270159