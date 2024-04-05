# Inventory Management System with ESP8266 Integration

This project is an Inventory Management System integrated with an ESP8266 microcontroller, allowing users to control and monitor inventory items remotely. The system utilizes a web interface for managing inventory items and an Adafruit NeoPixel LED strip to visually represent item locations within the inventory.

## Features
- **Web-Based Inventory Management**: Users can add, view, edit, and delete inventory items through a modern web interface.
- **Real-Time Inventory Visualization**: The status of each inventory item is visually represented by an LED on the NeoPixel strip, providing users with real-time feedback on item availability and location.
- **ESP8266 Integration**: The ESP8266 microcontroller handles LED control based on user interactions with the web interface, ensuring seamless synchronization between the inventory system and physical inventory storage.
- **Responsive Design**: The web interface is designed using Bootstrap, ensuring compatibility across various devices and screen sizes.

## Installation
To run the Inventory Management System, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/your-username/inventory-management.git
```

2. Navigate to the project directory:
```bash
cd inventory-management
```

3. Install required Python packages:
```bash
pip install -r requirements.txt
```

4. Create supper user:
```bash
python manage.py createsuperuser
```
This will be your login credentials

5. Upload the Arduino sketch to the ESP8266 microcontroller.
File name 'ESP8266_NeoPixel_WebController.ino'

6. Start the Django server:
```bash
python manage.py runserver
```

7. Access the web interface by navigating to http://localhost:8000 in your web browser.

# Usage
- Add new inventory items by clicking the "Add Item" button and filling out the required information.
- View and manage existing inventory items from the main dashboard.
- Click on an item to view detailed information, edit its properties, or delete it.
- Interact with the NeoPixel LED strip by controlling the LEDs corresponding to each inventory item.
