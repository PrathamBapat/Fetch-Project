# Fetch Offer Recommender

A tool that allows users to intelligently search for offers via text input from the user.

## Dataset
The files provided by Fetch are stored in the `Data` directory of the project.

## How to Run The Code

Follow these steps to run the code:

1. **Download the project folder.**

2. **Navigate to the project folder.**

    Open your terminal/command line, then change to the project directory using the `cd` command. 

    ```bash
    cd path/to/your/project/folder/
    ```

3. **Install the required packages.**

    You can install the necessary packages using pip. This command reads from the `requirements.txt` file and installs all necessary packages.

    ```bash
    pip install --upgrade -r requirements.txt
    ```

4. **Run the model creation script.**

    Use Python to run the `create_models.py` script.

    ```bash
    python create_models.py
    ```

5. **Run the prediction script.**

    Use Streamlit to run the `offer_predict.py` script. This will start a local web server and open the user interface in your web browser.

    ```bash
    streamlit run offer_predict.py
    ```

Please ensure you have Python installed on your system before running these commands.

## Snapshot of Output

Here is a snapshot of the expected output in the browser:

![Output Snapshot](IMG/pic.png)

---


