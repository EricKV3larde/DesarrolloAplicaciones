// routes/todoRoutes.js
const express = require('express');
const router = express.Router();
const Todo = require('../models/todos.js');
const mongoose = require('mongoose');

// Endpoint para obtener todos los todos
router.get('/', async (req, res) => {
    try {
        const todos = await Todo.find({}, 'task completed');
        res.json(todos);
    } catch (error) {
        res.status(500).send("Error en el servicio" + error);
    }
});

// Endpoint para agregar un nuevo todo
router.post('/', async (req, res) => {
    try {
        const newTodo = new Todo({
            task: req.body.task,
            completed: false,
        });

        await newTodo.save();
        res.json({ message: "Todo agregado con éxito" });
    } catch (error) {
        res.status(500).send("Error en el servicio" + error);
    }
});

// Endpoint para actualizar un todo usando PUT
router.put('/:id', async (req, res) => {
    try {
        const updatedTodo = await Todo.findByIdAndUpdate(
            req.params.id,
            { $set: { completed: req.body.completed } },
            { new: true }
        );

        res.json(updatedTodo);
    } catch (error) {
        res.status(500).send("Error en el servicio" + error);
    }
});

// Endpoint para eliminar un todo usando DELETE
// ...

router.delete('/:id', async (req, res) => {
    try {
        const isValidObjectId = mongoose.Types.ObjectId.isValid(req.params.id);

        if (!isValidObjectId) {
            return res.status(400).json({ message: 'ID no válido' });
        }

        const removedTodo = await Todo.findOneAndDelete({ _id: req.params.id });

        if (!removedTodo) {
            return res.status(404).json({ message: 'Todo no encontrado' });
        }

        res.json({ message: "Todo eliminado con éxito" });
    } catch (error) {
        res.status(500).send("Error en el servicio" + error);
    }
});


module.exports = router;
