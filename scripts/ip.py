#!/usr/bin/python
#import
import lcd
import time
import subprocess
def main():
    # Main program block

    # Initialise display
    lcd_init()
    ip = subprocess.check_output('hostname -I', shell=True).decode('utf-8')


    # Send some right justified text
    lcd_byte(LCD_LINE_1, LCD_CMD)
    lcd_string(ip, 1)



if __name__ == '__main__':
    main()

