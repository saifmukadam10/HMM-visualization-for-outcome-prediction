A Hidden Markov Model (HMM) is a statistical model used to describe the evolution of observable events that are influenced by internal "hidden" states.
•	Hidden States: In this experiment, these are the actual temperature categories (e.g., 0: Cold, 1: Mild, 2: Hot) that we want the model to infer.
•	Observations: The external data points (like humidity or pressure) that are visible.
•	Transition Probabilities: The probability of moving from one hidden state to another (e.g., the likelihood of a "Hot" day following a "Mild" day).
•	Emission Probabilities: The probability of an observation being generated from a specific hidden state.
4. Pseudo Code
BEGIN
    1. LOAD dataset containing temperature observations and actual labels.
    2. PREPROCESS data:
        a. Map labels to integers (0: Cold, 1: Mild, 2: Hot).
        b. Normalize or reshape observation features.
    3. INITIALIZE Hidden Markov Model (e.g., GaussianHMM).
    4. TRAIN the model using the observation sequence.
    5. PREDICT the hidden states (hidden_states) using the trained model.
    6. EXTRACT actual states (hidden_states_actual) for comparison.
    7. VISUALIZE:
        a. Define a mapping dictionary for labels.
        b. Plot the first 200 points of 'Actual' vs 'Predicted' states.
        c. Label axes, title, and add a legend.
    8. DISPLAY the plot.
END

5. Outcome
The model successfully generated a sequence of predicted states. The visualization demonstrates the following:
•	The Actual Temperature States (blue circles) show frequent fluctuations between "Mild" and "Hot" states.
•	The Predicted Temperature States (orange crosses) track the general trend but appear more stabilized in the "Hot" state in the provided sample.
•	The mapping was correctly applied to the Y-axis, displaying "Cold," "Mild," and "Hot" instead of raw integers.


The Weather Dataset is a time-series data set with per-hour information about the weather conditions at a particular location. It records Temperature, Dew Point Temperature, Relative Humidity, Wind Speed, Visibility, Pressure, and Conditions.

This data is available as a CSV file. We have analysed this data using the Pandas library.

