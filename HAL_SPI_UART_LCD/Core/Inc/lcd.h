/*
 * lcd.h
 *
 *  Created on: 05-Apr-2026
 *      Author: suhas
 */

#ifndef INC_LCD_H_
#define INC_LCD_H_


#include"main.h"

#define BV(n) (1<<(n))

#define LCD_SLAVE_ADDRESS 0x27<<1

#define LCD_RS   0
#define LCD_RW   1
#define LCD_EN   2
#define LCD_BL   3
#define LCD_DB4  4
#define LCD_DB5  5
#define LCD_DB6  6
#define LCD_DB7  7

#define LCD_CMD  0
#define LCD_DATA 1

#define LCD_CLEAR  0x01
#define LCD_ENTRY_MODE_SET 0x06
#define LCD_DISPLAY_ON_OFF 0x0C
#define LCD_FUCTION_SET    0x28
#define LCD_LINE1    0x80
#define LCD_LINE2    0xC0

void lcd_init(void);
void lcd_write_nibble(uint8_t rs,uint8_t val);
void lcd_write_byte(uint8_t rs,uint8_t val);
void lcd_puts(uint8_t line ,char str[]);
void lcd_scroll(void);


#endif /* INC_LCD_H_ */
