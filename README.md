# SayurBox Technical Test
This repository is for my technical test for SayurBox.

## Prerequisites
---
- Python 3.8
- Anaconda 4.9.2

### Create a new conda environment
1. Clone this repository<br>
<code>git clone https://github.com/archeltaneka/sayurbox-technical-test.git</code><br>
and change the directory into the repository you just cloned<br>
<code>cd sayurbox-technical-test</code>

2. Open your Anaconda Prompt and create the environment from the `environment.yml` file:<br>
<code>conda env create --file=environment.yml</code><br>
Make sure that you are inside the repository while creating the environment from the .yml file

3. Let Anaconda finish the whole installation process. Once finished, activate the environment:<br>
<code>conda activate data-science</code>

4. (optional) Open jupyter notebook to view the notebooks and other python scripts.<br> Type <code>jupyter notebook</code> in your Anaconda Prompt and press Enter.


## Data Scientist (Platform)
---
### 'Programming' Task
1. Open Command Prompt/Terminal/Anaconda Prompt and make sure you already set the PATH variable for `python`. This is important to run the script.

2. Change directory to the repository and type<br>
<code>python programming.py</code>

3. You will get an initial input for the length of the input array (k). After you are done, press enter.

4. Next, you will enter a number that will fill in the input array. According to the number you input on step 3, the system will continue to ask for a user prompt k times.

5. Finally, the system will ask the user to display n most frequent numbers.

6. To view the unit test case, please view `programming_unit_test.py`

<b>Note: For 'SQL' and 'Pandas DataFrame' task, please refer to `platform.ipynb`.

## Data Science - Take Home Test
---
Open up Jupyter Notebook and open `data-science.ipynb`