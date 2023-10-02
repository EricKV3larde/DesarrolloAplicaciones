// ProgressBar.js
import React from 'react';
import './ProgressBar.css'; 
const ProgressBar = ({ totalTasks, completedTasks }) => {
  const progress = totalTasks === 0 ? 0 : (completedTasks / totalTasks) * 100;

  return (
    <div className="progress-bar">
      <div
        className="progress-bar-inner"
        style={{ width: `${progress}%` }}
      ></div>
      <div className="progress-text">{`${Math.round(progress)}%`}</div>
    </div>
  );
};

export default ProgressBar;


