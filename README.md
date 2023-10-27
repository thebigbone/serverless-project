**Overview of Your Prototype's Task:**

The prototype combines Azure Functions and Flask. Azure Functions receive HTTP requests, and Flask serves as the backend to process these requests. The primary task is to count the occurrences of a specific word in a given text provided through the Azure Functions-triggered HTTP endpoint.

**Brief Explanation of How Your Prototype Works:**

- Azure Functions receive HTTP requests from users.
- These requests contain text and specific words as parameters.
- Azure Functions forward these parameters to the Flask application.
- The Flask application processes the parameters, counts the occurrences of specific words in the text, and returns the result as an HTTP response to Azure Functions.
- Azure Functions send this response back to the user.

**Specific Azure Service Used and Its Role:**

Azure Functions play a pivotal role in this prototype. They serve as the entry point for HTTP requests, extracting parameters and forwarding them to the Flask backend. Azure Functions then send back the Flask application's response to the user. The Flask application itself is hosted within Azure Functions.

**Challenges Encountered and How You Overcame Them (if applicable):**

Encountered some problems with the function app when I tried to integrate it with Flask. But I was easily able to solve it.

**Sharing Prototype's Source Code and Setup Instructions:**

- You can check the source code here: https://github.com/thebigbone/serverless-project
- The site with flask backend is here: https://az.hcrypt.net
- The azure function link is here: https://test938103.azurewebsites.net/api/httptrigger1/?text=hello&specific_words=hello

replace `hello` with your text and specific words

If you want to setup then first add the azure extension in vscode. Afterwards create a local workspace and then it will ask you for templates, just skip that. Keep python as the runtime and then create.

Copy paste the `function.py` and then click deploy from the workspace section.

**Share the source code of your Azure Function and the Flask application within it.**

It's here: https://github.com/thebigbone/serverless-project
