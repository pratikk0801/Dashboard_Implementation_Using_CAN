/*
 * accel.c
 *
 *  Created on: 05-Apr-2026
 *      Author: suhas
 */

#include"accel.h"
#include"main.h"

extern SPI_HandleTypeDef hspi1;

#define SPI_CS_ENABLE()	HAL_GPIO_WritePin(GPIOE, GPIO_PIN_3, GPIO_PIN_RESET)
#define SPI_CS_DISABLE() HAL_GPIO_WritePin(GPIOE, GPIO_PIN_3, GPIO_PIN_SET)

void accel_write(uint8_t intr_add,uint8_t data[],uint8_t size)
{
	SPI_CS_ENABLE();
	intr_add &= ~(1<<7);
	HAL_SPI_Transmit(&hspi1, &intr_add,1,HAL_MAX_DELAY);
	HAL_SPI_Transmit(&hspi1, data, size, HAL_MAX_DELAY);
	SPI_CS_DISABLE();
}

void accel_read(uint8_t intr_add,uint8_t data[],uint8_t size)
{
	SPI_CS_ENABLE();
	intr_add |= (1<<7);
	HAL_SPI_Transmit(&hspi1,&intr_add,1,HAL_MAX_DELAY);
	HAL_SPI_Receive(&hspi1,data,size,HAL_MAX_DELAY);
	SPI_CS_DISABLE();
}

void accel_init(void)
{
	uint8_t data=ACCEL_CTRL_25HZ | ACCEL_CTRL_XEN | ACCEL_CTRL_YEN | ACCEL_CTRL_ZEN;
	accel_read(ACCEL_CTRL_REG4,&data,1);

}

Accelget_t getxyz(void)
{
	uint8_t status;
	do{
		accel_read(ACCEL_STATUS,&status,1);
	}while((status & ACCEL_STATUS_ZYXDA)==0);

	Accelget_t val;
	uint8_t data[6]={0};
	accel_read(ACCEL_OUT_X_L,data,6);
	val.x=((uint16_t)data[1]<<8) | data[0];
	val.y=((uint16_t)data[3]<<8) | data[2];
	val.z=((uint16_t)data[5]<<8) | data[4];

	return val;
}

