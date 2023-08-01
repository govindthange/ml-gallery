import React from 'react';
import './index.css';

const InputForm = ({ inputText, onInputChange, onSubmit }) => {
  return (
    <form className="input-form" onSubmit={onSubmit}>
      <textarea
        value={inputText}
        onChange={onInputChange}
        placeholder="Enter recommendation..."
      />
      <br />
      <button type="submit">Process</button>
    </form>
  );
};

export default InputForm;
