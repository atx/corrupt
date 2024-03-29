/*
 * Copyright (c) 2021 Josef Gajdusek
 *
 * SPDX-License-Identifier: MIT
 */

#include <kernel.h>
#include <device.h>
#include <init.h>
#include <drivers/pinmux.h>
#include <sys/sys_io.h>

#include <pinmux/stm32/pinmux_stm32.h>

static const struct pin_config pinconf[] = {
#ifdef CONFIG_USB_DC_STM32
	{STM32_PIN_PB14, STM32F4_PINMUX_FUNC_PB14_OTG_HS_DM},
	{STM32_PIN_PB15, STM32F4_PINMUX_FUNC_PB15_OTG_HS_DP},
#endif /* CONFIG_USB_DC_STM32 */
};

static int pinmux_stm32_init(const struct device *port)
{
	ARG_UNUSED(port);

	stm32_setup_pins(pinconf, ARRAY_SIZE(pinconf));

	return 0;
}

SYS_INIT(pinmux_stm32_init, PRE_KERNEL_1,
		CONFIG_PINMUX_STM32_DEVICE_INITIALIZATION_PRIORITY);
