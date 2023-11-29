// TaskItem.js
import React, { useState } from 'react';
import "./TaskItem.css";
const TaskItem = ({ task, onTaskChange, onDeleteTask }) => {
  const [isChecked, setIsChecked] = useState(false);

  const handleCheckboxChange = () => {
    setIsChecked(!isChecked);
    onTaskChange(task.id);
  };

  return (
    <li className="task-item">
      <input
        type="checkbox"
        id={task.id}
        checked={isChecked}
        onChange={handleCheckboxChange}
      />
      <label>{task.text}</label>
      <button onClick={() => onDeleteTask(task.id)}>X</button>
    </li>
  );
};

export default TaskItem;
