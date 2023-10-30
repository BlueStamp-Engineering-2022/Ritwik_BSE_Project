# Facial Recognition Door Lock
This project creates a functional door lock which opens and closes based upon the guest present in front of the door. 

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Ritwik | Saint Francis High School | Computer Science | Incoming Junior

![Headstone Image](https://lh3.googleusercontent.com/pw/AM-JKLWpr7pPCQLDUqDiN9-NcsPHf-nBFKIOwLNO5tnhlps1uNwvSUM-O-VVlCm1BVA2gmbjrG3TcfVQu3OO06LVFoThpJlOyzsHBsDnk2S6oetTgsz5Q7ywEJeRpU2BF5OmQa9vyBLMukOW5TVKCQdiagY=s1624-no?authuser=0)
  
# Final Milestone
 My final milestone is to provide increased functionality to the door lock by adding a speaker. In order to do this, I soldered a speaker to the Arduino. I then coded an Arduino program through the Raspberry Pi monitor that outputted “Welcome!” when the lock opens; “Please step in front of the camera and ring the door again!” when there is a face present in the image, or “Access denied!” when there is an unrecognizable face in the picture. Through this code, I was able to complete my project of facial recognition door lock.

[![Final Milestone](https://i3.ytimg.com/vi/cp5kw2d6DTM/maxresdefault.jpg )](https://www.youtube.com/watch?v=cp5kw2d6DTM "Final Milestone")

# Second Milestone
My second milestone is the connection of the software to the hardware to produce a fully working facial recognition door lock. In order to accomplish this, I connected a push-button to the Arduino to allow for a signal to pass through. I then attached the small camera to the Arduino as well so that when the push-button sends a signal, the code in the Arduino can transfer this signal toward the camera and take a picture. In order for the face in the picture to be recognized, I downloaded several AWS services onto the Raspberry Pi, such as the DynamoDB (registers the incoming picture into a database) and the Rekognition software (compares the incoming picture with the pictures of the authorized users). After following the instructions and coding the connections between each AWS application and hardware component. The finished product was able to transfer a signal to the camera when the button is clicked; take a picture; transfer the new image to the database; compare the image with faces of the authorized users; and open the door lock if the person at the door was recognized, while closing the door if the person was not recognized. 

[![Second Milestone](https://i3.ytimg.com/vi/RRfHriVGMk8/maxresdefault.jpg)](https://www.youtube.com/watch?v=RRfHriVGMk8 "Second Milestone"){:target="_blank" rel="noopener"}
# First Milestone
  

My first milestone of the facial recognition door lock was to create all the fundamental hardware of the project. In order to create the physical pieces for the door lock I used a 3D printer. After screwing in the components together and attaching a servo motor to control the lock, I connected the motor with the Arduino using male to male wires. With Arduino fully functioning, I connected it to the Raspberry Pi which indirectly connected the Arduino to the monitor. At this point, I was able to write a simple program to turn the motor when I write “open” or “close” into the Raspberry Pi terminal. As a result, at the end I am able to manually control the door lock by typing in the two short commands into the monitor.

[![First Milestone](https://i3.ytimg.com/vi/uUYrQ2D1wDw/maxresdefault.jpg)](https://www.youtube.com/watch?v=uUYrQ2D1wDw "First Milestone"){:target="_blank" rel="noopener"}

# Starter Project

The purpose of the project is to control the brightness of the LED and the angle of the servo motor using the input which is given into the potentiometer. Initially in this project, I researched about using an arduino and a breadboard, as they are key components. Using what I learned, I created a fundamental hardware design using an LED, male-to-male wires, a servo motor, a breadboard, an arduino, and a potentiometer. Having the physical aspects of my project completed, I moved on to programming the arduino so the brightness of the LED, and the angle of the servo motor would correspond to the input given into the potentiometer. To accomplish this task, I had to download the arduino software which would allow me to manipulate any device connected to the arduino through code. Once it was downloaded, I learned the commands and format of the language (a combination of python and C++). Through trial and error, I successfully mapped the angle of the potentiometer to the brightness of the LED and the angle of the servo. For instance, if I turned the potentiometer halfway, the servo would turn 90 degrees of the 180 degrees possible while the LED would light up halfway to its full potential.

![Circuit Design](https://i.imgur.com/cbbJ1ec.png)

[![Starter Project](https://i3.ytimg.com/vi/dEDWUU-_8tA/maxresdefault.jpg)](https://youtu.be/dEDWUU-_8tA){:target="_blank" rel="noopener"}
