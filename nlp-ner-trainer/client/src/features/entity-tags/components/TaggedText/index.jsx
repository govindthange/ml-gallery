import React from 'react';
import './index.css';

const TaggedText = ({ text, entities }) => {
  const taggedText = [];
  const words = text.split(' ');

  let currentIndex = 0;
  for (let i = 0; i < words.length; i++) {
    let matchedEntity = null;
    for (let j = 0; j < entities.length; j++) {
      const entity = entities[j];
      const entityWords = entity.text.split(' ');

      if (entityWords.length + i <= words.length) {
        const joinedWords = words.slice(i, i + entityWords.length).join(' ');
        if (entity.text.toLowerCase() === joinedWords.toLowerCase()) {
          matchedEntity = entity;
          break;
        }
      }
    }

    if (matchedEntity) {
      const wordGroup = words.slice(i, i + matchedEntity.text.split(' ').length).join(' ');
      taggedText.push(
        <span
          key={currentIndex}
          className={`highlighted-text ${matchedEntity.label.toLowerCase()}`}
          title={matchedEntity.label}
        >
          {wordGroup}{' '}
          {matchedEntity.label && (
            <sup className={`label-sup ${matchedEntity.label.toLowerCase()}`}>{matchedEntity.label}</sup>
          )}
        </span>
      );
      i += matchedEntity.text.split(' ').length - 1;
    } else {
      taggedText.push(
        <span key={currentIndex} className="non-highlighted-text">
          {words[i]}{' '}
        </span>
      );
    }

    currentIndex++;
  }

  return (
    <div className='tagged-text'>
      <h1>Tagged Text</h1>
      <p>{taggedText}</p>
    </div>
  );
};

export default TaggedText;
