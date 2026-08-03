/*
 * accel.h
 *
 *  Created on: 05-Apr-2026
 *      Author: suhas
 */

#ifndef INC_ACCEL_H_
#define INC_ACCEL_H_

#include<stdint.h>

#define ACCEL_CTRL_REG4  0x20
#define ACCEL_STATUS     0x27
#define ACCEL_OUT_X_L    0x28
#define ACCEL_OUT_X_H    0x29
#define ACCEL_OUT_Y_L    0x2A
#define ACCEL_OUT_Y_H    0x2B
#define ACCEL_OUT_Z_L    0x2C
#define ACCEL_OUT_Z_H    0x2D

#define ACCEL_CTRL_XEN   (1<<0)
#define ACCEL_CTRL_YEN   (1<<1)
#define ACCEL_CTRL_ZEN   (1<<2)
#define ACCEL_ODR0       (1<<4)

#define ACCEL_CTRL_25HZ  (0x4 << 4)

#define ACCEL_STATUS_XDA (1<<0)
#define ACCEL_STATUS_YDA (1<<1)
#define ACCEL_STATUS_ZDA (1<<2)
#define ACCEL_STATUS_ZYXDA (1<<3)

void accel_write(uint8_t intr_add,uint8_t data[],uint8_t size);
void accel_read(uint8_t intr_add,uint8_t data[],uint8_t size);
void accel_init(void);

typedef struct accel_read{
	uint8_t x,y,z;
}Accelget_t;

Accelget_t getxyz(void);

#endif /* INC_ACCEL_H_ */
