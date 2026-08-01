/*
 * lis3dsh.c
 *
 *  Created on: 25-Mar-2026
 *      Author: Sunbeam
 */

#include "lis3dsh.h"

extern SPI_HandleTypeDef hspi1;

#define SPI_CS_ENABLE()	HAL_GPIO_WritePin(GPIOE, GPIO_PIN_3, GPIO_PIN_RESET)
#define SPI_CS_DISABLE() HAL_GPIO_WritePin(GPIOE, GPIO_PIN_3, GPIO_PIN_SET)

void accel_write(uint8_t int_addr, uint8_t data[], uint8_t size) {
	// enable slave (chip select)
	SPI_CS_ENABLE();
	// write internal address
	int_addr &= ~(1 << 7);	// MSB=0 for write
	HAL_SPI_Transmit(&hspi1, &int_addr, 1, HAL_MAX_DELAY);
	// write data byte(s)
	HAL_SPI_Transmit(&hspi1, data, size, HAL_MAX_DELAY);
	// disable slave (child de-select)
	SPI_CS_DISABLE();
}

void accel_read(uint8_t int_addr, uint8_t data[], uint8_t size) {
	// enable slave (chip select)
	SPI_CS_ENABLE();
	// write internal address
	int_addr |= (1 << 7);	// MSB=1 for read
	HAL_SPI_Transmit(&hspi1, &int_addr, 1, HAL_MAX_DELAY);
	// read data bytes
	HAL_SPI_Receive(&hspi1, data, size, HAL_MAX_DELAY);
	// disable slave (chip de-select)
	SPI_CS_DISABLE();
}

void accel_init(void) {
	// config CR4 -- ODR=25Hz, Enable X, Y, Z axes
	uint8_t data = ACCEL_CR4_ODR_25HZ | ACCEL_CR4_XEN | ACCEL_CR4_YEN | ACCEL_CR4_ZEN;
	accel_write(ACCEL_CR4, &data, 1);
}

AccelRead_t accel_get_xyz(void) {
	// wait for new data to be avail -- poll status regr
	uint8_t status;
	do {
		accel_read(ACCEL_STATUS, &status, 1);
	}while((status & ACCEL_STATUS_XYZDA) == 0);
	// read x, y, z axes readings and store in AccelRead_t struct
	AccelRead_t val;
	uint8_t data[6] = { 0 };
	accel_read(ACCEL_XL, data, 6);
	val.x = ((uint16_t)data[1] << 8) | data[0];// XL->data[0], XH->data[1]
	val.y = ((uint16_t)data[3] << 8) | data[2];// YL->data[2], YH->data[3]
	val.z = ((uint16_t)data[5] << 8) | data[4];// ZL->data[4], ZH->data[5]
	// return accel readings
	return val;
}





