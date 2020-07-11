Training a convolutional neural network based on the Xception model to play Touhou 6: The Embodiment of Scarlet Devil.

Everything besides testing the model was done on Arch Linux. Initially I was going to avoid using Windows 10 altogether but having
to deal with Wine and Xorg at the same time proved to be too stressful so I moved the testing portion of the model there.

----
The model outputs a prediction based on each frame, taking raw pixel data as input. Trained on 9 epochs with imagenet weights (due to hardware limitations :C)
on 5 different datasets - Samples from the first 5 stages on easy difficulty (24k, 100k, 160k) - all of them performed horribly 
(weirdly enough the 24k model did better than the 160k one so I decided to simply cut down on the variety of the data) -> 
The current model is trained
only on the first stage on normal difficulty with 109k samples and is the best performing model yet.
## Code overview:
- collect_data - Methods used for collecting the data (Linux focused but most of the stuff except the screen grabber should work on Win10).
- process_data - Methods used for processing the collected data (balancing, cleaning, combining, etc.).
- test_model - Testing the model, done on Win10.
- train_model - Xception, as well as everything else needed to train a model on it.

----

If for some reason you want to test the models -

[109k samples on the first stage (About 3-4 hours of collecting data?)](https://mega.nz/file/tJFlnA6Q#cwMlKk_r8BsGU5fiUXQt58pu_2Y2lFlNbVrhS6BkCPg)

[160k samples on 5 stages (4-5 hours of collecting data)](https://mega.nz/file/cEUHGCQD#MbKRk03kk0L9txxDuSY4RnkQ-LX15hHclKzdVuG34GE)
