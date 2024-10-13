DoS Attack Script
====================
Description
-----------
This script simulates a Denial of Service (DoS) attack by sending a continuous stream of GET requests to a specified URL. It is intended for educational purposes only, such as testing and understanding how DoS attacks work in a controlled environment. Do not use this script against any system without explicit permission.

Features
----------
Multithreading: The script spawns multiple threads (100 by default) to send requests concurrently, simulating a higher load.
Error Handling: Captures and displays any errors encountered during the request process.
Status Code Reporting: Logs the HTTP status codes received from the server for monitoring purposes.
