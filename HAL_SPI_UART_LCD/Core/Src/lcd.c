/*
 * lcd.c
 *
 *  Created on: 05-Apr-2026
 *      Author: suhas
 */

#include"lcd.h"
extern I2C_HandleTypeDef hi2c1;
void lcd_init()
{
	HAL_Delay(20);
	lcd_write_nibble(LCD_CMD,0x03);
	HAL_Delay(5);
	lcd_write_nibble(LCD_CMD,0x03);
	HAL_Delay(1);
	lcd_write_nibble(LCD_CMD,0x03);
	HAL_Delay(1);
	lcd_write_nibble(LCD_CMD,0x03);

	lcd_write_byte(LCD_CMD,LCD_FUCTION_SET);
	lcd_write_byte(LCD_CMD,LCD_DISPLAY_ON_OFF);
	lcd_write_byte(LCD_CMD,LCD_ENTRY_MODE_SET);
	lcd_write_byte(LCD_CMD,LCD_CLEAR);

}

void lcd_write_nibble(uint8_t rs,uint8_t val)
{
	uint8_t rs_flag=(rs==LCD_DATA)?BV(LCD_RS):0;
	uint8_t data= val<<LCD_DB4 | rs_flag | BV(LCD_BL) | BV(LCD_EN);
	HAL_I2C_Master_Transmit(&hi2c1, LCD_SLAVE_ADDRESS, &data,1,HAL_MAX_DELAY);
	data=val<<LCD_DB4 | rs_flag | BV(LCD_BL);
	HAL_I2C_Master_Transmit(&hi2c1, LCD_SLAVE_ADDRESS, &data,1,HAL_MAX_DELAY);
}

void lcd_write_byte(uint8_t rs,uint8_t val)
{
	uint8_t high,low;
	high=val>>4;
	low=val&0x0F;
	lcd_write_nibble(rs,high);
	lcd_write_nibble(rs,low);
}

void lcd_puts(uint8_t line,char str[])
{
	lcd_write_byte(LCD_CMD, line);
	for(int i=0;str[i]!='\0';i++)
	{
		lcd_write_byte(LCD_DATA,str[i]);
	}
}

void lcd_scroll()
{
	lcd_write_byte(LCD_CMD,0x18);
}
