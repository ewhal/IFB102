#!/usr/bin/python
import lcd
import mpd
def main():
    # Main program block

    # Initialise display
    lcd_init()
    ## Connect to mpd client ###
    client = mpd.MPDClient()
    client.connect("localhost", 6600)

    ## Get current song info ###
    curSongInfo = client.currentsong()
    songTitle = curSongInfo['file']

    # Send some right justified text
    lcd_byte(LCD_LINE_1, LCD_CMD)
    lcd_string("Now Playing: ", 1)
    str_pad = " " * 16  
    songTitle = str_pad + songTitle 
    for i in range (0, len(songTitle)):  
        lcd_byte(LCD_LINE_2, LCD_CMD)  
        lcd_text = songTitle[i:(i+15)]  
        lcd_string(lcd_text,1)  
        time.sleep(0.4)  
    lcd_byte(LCD_LINE_2, LCD_CMD)  
    lcd_string(str_pad,1)  

if __name__ == '__main__':
    main()

