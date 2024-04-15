# Title
Sketchbook

## Repository
https://github.com/SPRG14/sketchbook.git

## Description
Sketchbook is a simple yet powerful program that allows the user to unleash their creativity by sketching digitally. With multiple drawing tools and a customizable canvas, users can create artworks from doodles and sketches to detailed pieces. 

## Features
- Ability to draw around the canvas with the mouse
	- Using the pygame.draw.line method to draw lines on the position of the mouse when it is clicked. The mouse properties are checked with event.type pygame.MOUSEBUTTONDOWN/MOUSEBUTTONUP to know if the mouse is being clicked or not.
- You can clear the canvas by pressing 'c' on the keyboard
	- The canvas is filled with white when the 'c' key is pressed
- Multiple brush and background colors 
	- When the 1-5 keys on the keyboard are pressed, a different brush color is gotten for each, and when the 6-0 keys are pressed, a different background color is gotten.

## Challenges
- Learning to check the mouse position for where the lines are being drawn
- Being able to draw only when the mouse is down, and not when it is up.

## Outcomes
Ideal Outcome:
- A drawing program with multiple customzability options and functions that allow to make both simple and more complex sketches.

Minimal Viable Outcome:
- An app with the ability to draw outlines and sketches

## Milestones

- Week 1
  1. Make drawing possible with mouse
  2. Clear screen with 'c'

- Week 2
  1. Multiple drawing colors
  2. Multiple background colors

- Week 3 (Final)
  1. Optimize
