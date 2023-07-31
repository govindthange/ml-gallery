import React, { useState } from 'react';
import './App.css';
import Tags from './features/entity-tags/components/Tags';

const API_URL = '/api/detect-entities'; // Adjust the URL to match your server

function App() {
  const SAMPLE_TEXT = "ICICI Direct has buy call on Torrent Pharmaceuticals with a target price of Rs 2010.5. The current market price of Torrent Pharmaceuticals is Rs 1775.9. Time period given by analyst is a year when Torrent Pharmaceuticals price can reach defined target";
  const [inputText, setInputText] = useState(SAMPLE_TEXT);
  const [taggedEntities, setTaggedEntities] = useState([]);

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const handleSubmit = async (e) => {
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
      setTaggedEntities(responseObj.data);
    } catch (error) {
      console.error('Error processing text:', error);
    }
  };

  return (
    <div className="App">
      <h1>NLP for NER Training</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={inputText}
          onChange={handleInputChange}
          placeholder="Enter recommendation..."
        />
        <br/>
        <button type="submit">Process</button>
      </form>
      <div>
        <Tags entities={taggedEntities} />
      </div>
    </div>
  );
}

export default App;
