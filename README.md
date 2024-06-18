## Backend Services for Academic Query Management Transformation Project

Welcome to the graphical interface for our exciting academic query management transformation project by integrating LLM and the OpenAI API into an Academic Assistant! In this interface, we have developed a solution that uses advanced natural language processing technologies to enhance academic information search and management.

Currently, artificial intelligence (AI) has made impressive progress. One notable development is the emergence of Large Language Models (LLMs), capable of generating and interpreting natural language data. Among these models have gained widespread attention for their remarkable text generation capabilities and improved user interface. Academic institutions face challenges in accessing vast amounts of information efficiently. This problem is compounded by the increasing amount of academic documents, the dispersion of information in different repositories, and the time and resources required to search and filter this information, representing a significant workload for professors and students. To address the issue, this paper proposes an AI-powered assistant integrated with LLMs and a software system based on a microservices architecture. The Assistant offers clear and contextually relevant answers, making academic information retrieval processes more efficient. This article proposes an AI-powered assistant, covering integration aspects of both AI and software models. Moreover,  it uses intelligent assistants to manage academic information, serving as a model for future implementations.

For a detailed exposition of the project's framework, methodologies, and results, please refer to our comprehensive document available on GitHub. This document provides an in-depth look at the underlying technologies, implementation strategies, and performance evaluations that underscore the success of our project.

To explore further details, consult the [Research paper](docs/Academic_Query_Assistant.pdf).

### Interface Highlights
- AI-Powered Academic Assistant:** Our interface includes an AI-powered academic assistant that helps users efficiently find relevant academic information. This simplifies the process of searching and managing academic documents.
LLM and OpenAI API integration:** We have integrated the Long Term Language Model (LLM) along with the OpenAI API to improve the academic assistant's understanding and responsiveness. This enables more accurate and contextually relevant responses to user queries.
Efficient Query Management:** The interface provides intuitive tools for managing academic queries, allowing users to perform advanced searches, organize their searches, and easily access relevant documents.

### Interface Usage Instructions
1. **Clone the Repository:** Start by cloning the interface repository on your local machine using the following command:
2. 
```bash
git clone https://github.com/xr-lab-ucacue/Academic-Assistant.git
```

2. **Install Dependencies:** Once the repository has been cloned, navigate to the project directory and run the following command to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

3. **Configure the Python Environment:** Make sure you have Python v3.11.4 installed and pip properly configured on your system. Add the Python path if necessary.

4. **Install Specific Libraries:**
   - To install Streamlit v1.18.1, execute:
     ```bash
     pip install streamlit==1.18.1
     ```
   - To install the OpenAI library, run:
     ```bash
     pip install openai
     ```
   - If an error related to "altair" occurs, install version 4.0 specifically with the following command:
   - 
     ```bash
     pip install altair==4.0
     ```

5. **Run the Application:** Use the following command to run the interface in your browser:

```bash
streamlit run app.py
```

6. **Access the Interface:** Open your web browser and navigate to http://localhost:8501 to access the graphical interface. Use the academic assistant to query and manage academic information efficiently.


## Project Preview
### Home Screen
![interfaz vacia](https://github.com/xr-lab-ucacue/Academic-Assistant/assets/73256134/e08d84fe-4a0f-4b82-a2c4-cf3865b4068b)
In this view users are presented with the input field for the queries they wish to make and a button to send the queries. The interface was created using the Streamlit framework.

### Display of the assistant's response
![FinalDiagram](https://github.com/xr-lab-ucacue/Academic-Assistant/assets/73256134/2b5e65e4-97ac-4dd6-bf64-22ddd60fb70f)


This interface will simplify the management of academic queries and improve the user experience when interacting with academic documents! If you have any questions or suggestions, please do not hesitate to contact us.



Team Developers:

Pedro Alvarez
Sebastian Quevedo
