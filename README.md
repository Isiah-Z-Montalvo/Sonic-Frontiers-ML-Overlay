# Sonic-Frontiers-ML-Overlay
This is a project that will obtain a custom image dataset from Sonic Frontiers to train a convolution neural network in recognizing different triggers involving all of the requirements for 100%ing the game such as collecting chaos emeralds, completing cyberspace stages, and catching all unique fish within Big's fishing space. Once the model is trained on this data, it will be used to run predictions by watching the players screen, taking screenshots periodically, then using these screenshots to conduct predictions on the current collectible. This will then trigger the OBS overlay to display or disappear depending on the scenario. This will allow a fun and automatic way to track collectibles for 100% speedruns. 

# Collecting the Dataset (Completed)
To collect the training data, I wrote a simple script (frontiersScreenshotter.py within the repository) to take a screenshot every second of Sonic Frontiers footage found on YouTube. These are all 1333x800 pixel screenshots, bigger than the standard size for training data which should make up for less overall images for each label. 

# Pre-processing the images for input (Not yet implemented)

# Building the Convulutional Neural Network (Not yet implemented)

# Training the Model (Not yet implemented)

# Validating the Model (Not yet implemented)

# Deploying the Model using Flask (Not yet implemented)

# OBS and Overlay Triggers (Not yet implemented)