/*
 * lis3dsh.h
 *
 *  Created on: 25-Mar-2026
 *      Author: sunbeam
 */

#ifndef INC_LIS3DSH_H_
#define INC_LIS3DSH_H_

#include "main.h"

#define ACCEL_CR4		0x20
#define ACCEL_STATUS	0x27
#define ACCEL_XL		0x28
#define ACCEL_XH		0x29
#define ACCEL_YL		0x2A
#define ACCEL_YH		0x2B
#define ACCEL_ZL		0x2C
#define ACCEL_ZH		0x2D

#define ACCEL_CR4_XEN		(1 << 0)
#define ACCEL_CR4_YEN		(1 << 1)
#define ACCEL_CR4_ZEN		(1 << 2)
#define ACCEL_CR4_ODR_Pos	4

#define ACCEL_CR4_ODR_25HZ	(0x4 << ACCEL_CR4_ODR_Pos)

#define ACCEL_STATUS_XDA	(1 << 0)
#define ACCEL_STATUS_YDA	(1 << 1)
#define ACCEL_STATUS_ZDA	(1 << 2)
#define ACCEL_STATUS_XYZDA	(1 << 3)

typedef struct AccelReading {
	int16_t x, y, z;
}AccelRead_t;

void accel_init(void);
AccelRead_t accel_get_xyz(void);

void accel_write(uint8_t int_addr, uint8_t data[], uint8_t size);
void accel_read(uint8_t int_addr, uint8_t data[], uint8_t size);


#endif /* INC_LIS3DSH_H_ */
