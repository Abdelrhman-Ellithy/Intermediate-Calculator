# 🧮 Intermediate Calculator

**A calculator project built using the STM32F103C8T6 microcontroller (ARM Cortex M3).**

---

## 📚 Project Overview

This project features an intermediate-level calculator implemented on the STM32F103C8T6 microcontroller, leveraging ARM Cortex M3 capabilities. It demonstrates the use of GPIO, timers, and peripherals such as keypads and LCDs.

---

## 🗂️ Project Structure

Here's an overview of the project structure and key files:

```
├── .settings
│   ├── language.settings.xml
│   ├── org.eclipse.cdt.core.prefs
│   └── org.eclipse.core.resources.prefs
│
├── ARM Calc
│   ├── Project Backups
│   ├── New Project.pdsprj
│   └── New Project.pdsprj.ABDELRHMAN-LAPT.lenovo.workspace
│
├── Inc
│   ├── HAL
│   │   ├── Keypad
│   │   │   ├── Keypad_Config.h
│   │   │   ├── Keypad_Private.h
│   │   │   └── Keypad_interface.h
│   │   │
│   │   ├── LCD
│   │   │   ├── CLCD_config.h
│   │   │   ├── CLCD_extrachar.h
│   │   │   ├── CLCD_interface.h
│   │   │   └── CLCD_private.h
│   │
│   ├── LIB
│   │   ├── BIT_MATH.h
│   │   ├── BIT_OPERATIONS.h
│   │   ├── STD_TYPES.h
│   │   ├── Types.h
│   │   ├── ellithy_delay.h
│   │   └── stm32f103c8t6.h
│   │
│   ├── MCAL
│   │   ├── GPIO
│   │   │   ├── GPIO_Config.h
│   │   │   ├── GPIO_interface.h
│   │   │   └── GPIO_private.h
│   │   │
│   │   ├── PORT
│   │   │   ├── PORT_config.h
│   │   │   ├── PORT_interface.h
│   │   │   └── PORT_private.h
│   │   │
│   │   ├── RCC
│   │   │   ├── RCC_config.h
│   │   │   ├── RCC_interface.h
│   │   │   └── RCC_private.h
│   │   │
│   │   ├── SYSTICK
│   │   │   ├── SysTicK_private.h
│   │   │   ├── SysTick_Interface.h
│   │   │   └── Systick_Config.h
│   │   │
│   │   ├── TIMER1
│   │   │   ├── TIMER1_config.h
│   │   │   ├── TIMER1_interface.h
│   │   │   └── TIMER1_private.h
│   │   │
│   │   └── UART
│   │       ├── UART_Config.h
│   │       ├── UART_interface.h
│   │       └── UART_private.h
│   │
│   ├── Startup
│   │   ├── startup_stm32f103c8tx.d
│   │   ├── startup_stm32f103c8tx.o
│   │   └── subdir.mk
│   │
│   ├── Task_3_IntermediateCalc.elf
│   ├── Task_3_IntermediateCalc.list
│   ├── Task_3_IntermediateCalc.map
│   ├── makefile
│   ├── objects.list
│   ├── objects.mk
│   └── sources.mk
│
├── Src
│   ├── HAL
│   │   ├── Button_progaram.c
│   │   ├── Buzzer_Program.c
│   │   ├── CLCD_program.c
│   │   ├── DCMOTOR_program.c
│   │   ├── Keypad_Program.c
│   │   └── LED_Program.c
│   │
│   ├── MCAL
│   │   ├── GPIO_program.c
│   │   └── RCC_program.c
│   │
│   ├── ellithy_dalay.c
│   ├── main.c
│   ├── syscalls.c
│   └── sysmem.c
│
├── Startup
│   └── startup_stm32f103c8tx.s
│
├── .cproject
├── .project
├── LICENSE
├── README.md
└── STM32F103C8TX_FLASH.ld
```

---

## 📝 Key Features

- **🔢 Calculator Logic:** Intermediate-level arithmetic functions.
- **📟 LCD Display:** Output displayed on an LCD screen.
- **⌨️ Keypad Support:** Input via a 4x4 matrix keypad.
- **⚙️ STM32F103C8T6:** Based on ARM Cortex M3 microcontroller.
- **⏱️ Timers:** Integration with SYSTICK and TIMER peripherals.
- **🔧 Modular Design:** Organized HAL and MCAL layers for flexibility.

---

## 🛠️ Dependencies

- **Toolchain:** ARM GCC Compiler
- **Debugger:** ST-Link Debugger
---

## 🚀 Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Abdelrhman-Ellithy/Intermediate-Calculator.git
   ```
2. **Open the Project in Eclipse.**
3. **Build the Project:**
   - Use the `makefile` for building the project.
4. **Flash the Binary:**
   - Use ST-Link to flash `Task_3_IntermediateCalc.elf` onto the STM32 board.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).


## 💬 Contact

- **Author:** Abdelrhman Ellithy
