const express = require('express');
const cors = require('cors');

const app = express();
app.use(express.json())
app.use(express.urlencoded({ extended: true }));
app.use(cors())

app.get('/', (req, res) => {
    res.send('Express server is running');
});

app.listen('3001', () => { })
