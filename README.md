# Paging Simulator

The Paging Simulator is a main memory paging simulation tool developed for the Operating Systems course. It provides a comprehensive and graphical representation of how a paging system operates in a RAM.

## Technologies Used

The simulator is developed using Python and makes use of the following dependencies:

- Pygame
- NumPy

## Requirements

Before running the simulator, ensure that the following dependencies are installed on your machine:

- Python
- Pygame
- NumPy

## Screens of the Simulator

The simulator consists of four screens:

1. **Home**: This screen displays two buttons: "Start" and "Quit". Clicking on "Start" proceeds to the next screen.

2. **Parameter Selection**: On this screen, the user must select the system parameters, including:

   - Frame size (in words)
   - Operating system size (in words)
   - Process size (in words)
   - Number of frames in RAM

3. **Free Frame Selection**: On this screen, the user can select the available frames in RAM. A list of frames is displayed, and the user can mark them as free or occupied. Two lists are provided to visualize the free and occupied frames, respectively.

4. **Simulation**: The last screen displays four tables representing different aspects of the paging system:

   - Page table
   - Pages on the disk
   - Used frames in RAM
   - Memory addresses requested over time

## Running the Simulator

Follow these steps to run the simulator on your local machine:

1. Clone the project repository.
2. Install the required dependencies using the following commands:
   ```bash
   pip install pygame
   ```
   ```bash
   pip install numpy
   ```
3. From the terminal, navigate to the project's root directory.
4. Run the following command: `python main.py`
5. In the home screen, click on "Start".
6. On the parameter selection screen, choose the desired system parameters.
7. On the free frame selection screen, select the free frames.
8. Load a CSV file containing the memory addresses requested during the simulation. The first row should contain the address, and the second row should indicate whether it is a read or write request.
9. Select a file to save the logger outputs.
10. Finally, start the simulation on the fourth screen.

## Screenshots

Here are some screenshots from the Paging Simulator:

![Home Screen](https://github.com/LeoLizc/Paging_sistem_simulator/assets/74639893/e142dcaf-79da-4c23-a5fa-195c079c30e9)

![Parameter Selection Screen](https://github.com/LeoLizc/Paging_sistem_simulator/assets/74639893/788aebb0-38d4-4db7-b555-730f27c2ae7c)

![Free Frame Selection Screen](https://github.com/LeoLizc/Paging_sistem_simulator/assets/74639893/4e51ec7b-b65a-4753-a016-f82afe52b077)

![Simulation Screen](https://github.com/LeoLizc/Paging_sistem_simulator/assets/74639893/8a5500e5-e2a5-4d61-8f41-b3cb252bbf44)

## Credits

- Leonardo Lizcano
- Henry Caicedo
- Juan Julio San Juan
- Breynner Hurtado
