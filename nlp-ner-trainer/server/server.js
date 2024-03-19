const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { PythonShell } = require('python-shell'); // Assuming you have installed the "@tbergq/spacy-py" package

const app = express();
app.use(bodyParser.json());
app.use(cors());

const nlpModelPath = './model/nlp-ner-stck-recmndtns.pkl';

// Function to process text and return tagged entities
function processText(text) {
  console.log("Inside processText(%d)", text.length);
  return new Promise((resolve, reject) => {
    const options = {
      mode: 'text',
      pythonOptions: ['-u'], // get print results in real-time
      scriptPath: './', // the path to the python script
      args: [nlpModelPath, text],
    };

    // Create a PythonShell instance with the options
    const pyShell = new PythonShell('nlp-processor.py', options);

    // Event handler for Python script output
    pyShell.on('message', (message) => {
      console.log('Python script output:', message);
      resolve(JSON.parse(message));
    });

    // Event handler for script end (completion or error)
    pyShell.end((err, code, signal) => {
      if (err) {
        console.error('Error processing text:', err);
        reject(err);
      } else {
        // Parse the JSON result from the Python script
        try {
          resolve(pyShell.messages);
        } catch (parseError) {
          console.error('Error parsing entities:', parseError);
          reject(parseError);
        }
      }
    });
  });
}

// API endpoint to process text
app.post('/api/detect-entities', async (req, res) => {
  const { text } = req.body;
  try {
    const entities = await processText(text);
    res.json({ status: 200, message: "Successful NER processing", data: entities});
  } catch (error) {
    console.error('Error processing text:', error);
    res.status(500).json({ error: 'Error processing text' });
  }
});

// API endpoint to process text
app.get('/ping', async (req, res) => {
  const { text } = req.body;
  try {
    res.json({ status: 200, message: "Successful ping test" });
  } catch (error) {
    console.error('Error processing text:', error);
    res.status(500).json({ error: 'Error processing text' });
  }
});

console.log("listen")
const PORT = 5000; // TODO: Make this configurable!
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
