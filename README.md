# video-proc
HackDavis 2022. In the past movies and television have triggered mass seizures among viewers. Our tool helps people with epilepsy enjoy the same media. Users can upload videos with flashes and receive a modified file containing audio-based flash warnings to download and view safely. (Team: May Wynton, Kay Krachenfels, Omar Khan, Michelle Lu) 

## Inspiration
In the past movies and television have triggered mass seizures among viewers. We want to help solve that problem.

## What it does
Our tool helps people with epilepsy enjoy the same media. 

## How we built it
We began by taking a videofile and reducing its dimensionality. We extract individual frames convert those frames to grayscale take the average of regions of the screen reshaped the data into a 2D matrix where the rows are the regions of the screen, the columns are timesteps, and the data is grayscale. Then, we used threshold algorithms to detect where the flashes happen from these images. 

## Challenges we ran into
A lot of work needs to be done trying a lot of different models with a lot of different values. We have to test various models and inputs to get more accurate results.

## Accomplishments that we're proud of
-Reducing video data into a two-dimensional array.  
-Visualizing and understanding where flashing is happening (and being able to distinguish between different kinds of flashes)  
-Knowing which algorithms to use to optimize the model.

## What we learned
-Interacting with Python on the web  
-Pre-processing videos/data transformations  
-Beginning to understand how to segment images to make predictions

## What's next for Anomaly/Flash Detection Over Time Series
-Optimizing the model to have more accurate predictions  
-Sourcing a larger dataset  
-Using neural networks  
-Improving the user experience  

## Video demo of current progress [click image to watch video]:
[![Flash Detection Video](http://img.youtube.com/vi/bHZZutex_A0/0.jpg)](http://www.youtube.com/watch?v=bHZZutex_A0 "Anomaly/Flash Detection Over Time Series")
