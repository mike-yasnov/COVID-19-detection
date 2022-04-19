# Covid-19 detection 
Simple detection of Covid-19 using ensemble models.

Results:
Metrics   | Result
--------  | ---------
Accuracy  | 0.9014
Precision | 0.9449
Recall    | 0.7584
F1-score  | 0.8116
Roc-auc   | 0.7584

## Data 
The data were obtained using the voltammetry method on eGaIn electrodes. The data is written in a table in the .сsv format 


# Determination of the stage of development of the disease (lung damage)
For this, ensemble models were also taken.
The data were supplemented by the content of trace elements in the patient's blood.

There were three classes: mild, moderate, and severe lung injury.

Results:
Metrics   | Result
--------  | ---------
Accuracy  | 1.0000
Precision | 1.0000
Recall    | 1.0000
F1-score  | 1.0000
Roc-auc   | 1.0000

To run the interface, unpack the models.zip archive into the folder models/ 