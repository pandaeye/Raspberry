#include <bcm2835.h>
#include <stdio.h>
#define PIN 18
#define IO bcm2835_gpio_lev(PIN)

unsigned char get_signal();