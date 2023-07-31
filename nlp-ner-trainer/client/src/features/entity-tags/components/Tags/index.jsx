import React from 'react';
import './index.css';

const TableComponent = ({ entities }) => {
  return (
    <div className="table-container">
      <h2>Tagged Entities</h2>
      <table>
        <thead>
          <tr>
            <th>Label</th>
            <th>Text</th>
          </tr>
        </thead>
        <tbody>
          {entities && entities.map((entity, index) => (
            <tr key={index}>
              <td>{entity.label}</td>
              <td>{entity.text}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TableComponent;
