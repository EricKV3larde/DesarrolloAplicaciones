// models/todo.js
const mongoose = require('mongoose');

const TodoSchema = new mongoose.Schema({
    task: String,
    completed: Boolean,
});

const Todo = mongoose.model('Todo', TodoSchema);

module.exports = Todo;
