import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import Header from './componentes/Header';
import  TaskList from './componentes/TaskList';
<style>
  @import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@100&family=Lilita+One&family=Oswald&display=swap');
</style>


const tasks1 =["df"];


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
<>

  <Header/>
  <TaskList tasks={tasks1}/>
  {/* <TaskList tasks={tasks3}/> */}

</>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
