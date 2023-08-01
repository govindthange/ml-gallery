import React, { useState } from 'react';
import './App.css';
import InputForm from './features/entity-tags/components/InputForm';
import Tags from './features/entity-tags/components/Tags';
import TaggedText from './features/entity-tags/components/TaggedText';

const API_URL = '/api/detect-entities';

function App() {
  const SAMPLE_TEXT = "ICICI Direct has buy call on Infosys with a target price of Rs 1335.8 . The current market price of Infosys is Rs 1325.5 . Time period given by analyst is Intra Day when Infosys price can reach defined target. ICICI Direct recommended to keep stop loss at Rs 1308.7";
  const [inputText, setInputText] = useState(SAMPLE_TEXT);
  const [data, setData] = useState([]);

  const onInputChange = (e) => {
    setInputText(e.target.value);
  };

  const onSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }),
      });
      const responseObj = await response.json();
      setData(responseObj.data);
    } catch (error) {
      console.error('Error processing text:', error);
    }
  };

  return (
    <div className="App">
      <h1>NLP for NER Training</h1>
      <InputForm
        inputText={inputText}
        onInputChange={onInputChange}
        onSubmit={onSubmit}
      />
      <TaggedText text={inputText} entities={data} />
      <Tags entities={data} />
    </div>
  );
}

export default App;
