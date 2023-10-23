# Spiral Movement in Blender using Flask API

## Description

This experiment demonstrates how to control the position of an object in Blender (in this case, a Cube) using a Flask API server. The objective is to make the Cube move in a spiral trajectory on the XY plane, with the trajectory being calculated by the Flask server and the Cube in Blender fetching its updated position periodically.

## Requirements

- **Blender**: Version used during development: 2.9x.
- **Python**: Version used during development: 3.8+.
- **Flask**: Install via pip with the command `pip install Flask`.

## Setup and Usage

1. **Setting up the Flask server**:

   - Clone this repository or copy the Flask server code.
   - Run the Flask server with the command:
     ```
     python server_filename.py
     ```

   Once running, the server will be available at `http://localhost:5000/position`.

2. **Setup in Blender**:

   - Open Blender and import the Python script.
   - Execute the script within Blender. This will start Blender continuously polling the Flask server to get the updated position of the Cube.

3. **Spiral Movement**:

   - With the server running and the script in Blender activated, the Cube will start moving in a spiral trajectory on the XY plane.

## How It Works

1. **Spiral Calculation**:
   - We use the Archimedean spiral to calculate the Cube's trajectory.
   - With each request to the Flask server, it calculates the next position in the trajectory and returns the coordinates to Blender.

2. **Blender-Flask Communication**:
   - Blender polls the Flask server periodically. Upon receiving a new position, it moves the Cube to that new position.

## Limitations and Future Improvements

- Currently, the movement is restricted to the XY plane. We could extend this to 3D.
- We're using `polling` to fetch updates. A WebSocket-based approach might be more efficient.

## Contributions

Contributions are welcome! Be it to enhance the movement, optimize the code, or introduce new features.

## License

This project is licensed under the MIT license.
