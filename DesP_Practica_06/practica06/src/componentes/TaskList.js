// TaskList.js
import React, { useState } from 'react';
import TaskItem from './TaskItem';
import ProgressBar from './ProgressBar';
import './TaskList.css';

const TaskList = () => {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState('');
  const [completedTasks, setCompletedTasks] = useState([]);

  const handleTaskChange = taskId => {
    const updatedTasks = [...completedTasks];
    const index = updatedTasks.indexOf(taskId);

    if (index === -1) {
      updatedTasks.push(taskId);
    } else {
      updatedTasks.splice(index, 1);
    }

    setCompletedTasks(updatedTasks);
    console.log('Tareas Completadas:', updatedTasks);
    console.log('Todas las Tareas:', tasks);
  };

  const handleNewTaskChange = e => {
    setNewTask(e.target.value);
  };

  const handleAddTask = () => {
    if (newTask.trim() !== '') {
      const newTaskObject = {
        id: tasks.length + 1, // puedes usar un método más robusto para generar IDs
        text: newTask.trim(),
      };

      setTasks([...tasks, newTaskObject]);
      setNewTask('');
    }
  };
  const handleKeyDown = e => {
    if (e.key === 'Enter') {
      handleAddTask();
    }
  };
  const handleDeleteTask = taskId => {
    const updatedTasks = tasks.filter(task => task.id !== taskId);
    const updatedCompletedTasks = completedTasks.filter(id => id !== taskId);
  
    setTasks(updatedTasks);
    setCompletedTasks(updatedCompletedTasks);
  };
  
  return (
    <div>
        <ProgressBar 
            totalTasks={tasks.length} 
            completedTasks={completedTasks.length} 
        />
        <div>
        <div className="task-input-container">

        <input 
            type="text" 
            className="task-input"
            value={newTask} 
            onChange={handleNewTaskChange} 
            onKeyDown={handleKeyDown}
            placeholder="Escribe aquí tus tareas"
        />
        </div>
      </div>
      <ul>
        {tasks.map(task => (
          <TaskItem
            key={task.id}
            task={task}
            isChecked={completedTasks.includes(task.id)}
            onTaskChange={handleTaskChange}
            onDeleteTask={handleDeleteTask}
          />
        ))}
      </ul>

    </div>
  );
};

export default TaskList;