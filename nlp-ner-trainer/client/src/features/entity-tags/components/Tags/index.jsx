import React from 'react';
import './index.css';

const TableComponent = ({ entities }) => {
  return (
    <div className="table-container">
      <table>
        <thead>
          <tr>
            <th>Tagged Labels</th>
            <th>Important Words</th>
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
