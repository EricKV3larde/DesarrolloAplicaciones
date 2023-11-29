// Importando paquetes y archivos necesarios para trabajar las rutas
var express = require('express');
var bodyParser = require('body-parser');
var Product = require('../models/products');
var router = express.Router();

// Configurando el Parser
router.use(bodyParser.urlencoded({ extended: true }));
router.use(bodyParser.json());
router.use(function (req, res, next) {
    console.log("request");
    next();
});

// Métodos para manejar Base de Datos MongoDB llamada node-crud
router.route('/products')
    .post(async function (req, res) {
        try {
            var product = new Product();
            product.name = req.body.name;
            product.amount = req.body.amount;
            product.description = req.body.description;

            await product.save();
            res.json({ message: "Producto registrado con éxito" });
        } catch (error) {
            res.status(500).send("Error en el servicio" + error);
        }
    })
    .get(async function (req, res) {
        try {
            var products = await Product.find({}, 'name amount description'); // Solo selecciona los campos que quieres mostrar
            res.json(products);
        } catch (error) {
            res.status(500).send("Error en el servicio" + error);
        }
    });

module.exports = router;
